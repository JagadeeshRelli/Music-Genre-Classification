
def predict_genn(meta1):
    import pickle
    import os
    import numpy as np
    from django.conf import settings
    path = os.path.join("C:/Users/jagad/Desktop/mgctemp/predictor/models", 'models.p')
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)

    svmp = data['svmp']
    meta1=np.round(meta1, decimals =3)
    # norma = data['norma']
    # lgn = data['lgn']
    scaler=data['stx']
    temp_flist=np.array(meta1)
    #temp_flist=temp_flist.reshape(1,-1)
    x = scaler.transform([temp_flist])
    predx = svmp.predict_proba(x)
    
    jagadlist=['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']
    ixx=predx.tolist()
    ixxx=ixx[0]
    dictt={}
    for i in range(0,len(jagadlist)):
        dictt[jagadlist[i]]=ixxx[i]

    dicttsort={k: v for k, v in sorted(dictt.items(), key=lambda item: item[1])}
    # print(list(dicttsort.keys())[-1])
    # print(list(dicttsort.keys())[-2])
    aa=list(dicttsort.keys())[-1]
    bb=list(dicttsort.keys())[-2]
    # l=dict((k,v) for k,v in dicttsort.items() if v>=0.65)
    # print(l)
    # if(len(l)):
    #     dicttsortx={k: v for k, v in sorted(l.items(), key=lambda item: item[1], reverse=True)}
    #     templ=[]
    #     for i in dicttsortx.keys():
    #         templ.append(i)
    # elif(len(l)==0):
    #     templ=[]
    #     templ.append(list(dicttsort.keys())[-1])
    #     templ.append(list(dicttsort.keys())[-2])
    # templstr=str(templ)
    # templstr=templstr[1:-1]
    # templstr=templstr.replace("'"," ")
    
    templ=[aa,bb]
    templstr=str(templ)
    templstr=templstr[1:-1]
    templstr=templstr.replace("'"," ")


    #pred=str(pred[0])
    return(templstr)

