from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from predictor.predictt import predict_genn
from .apps import PredictorConfig
from .forms import DocumentForm
from .models import Document
from .Metadata import getmetadata
import warnings
from .predictt import predict_genn
from django.contrib import messages
import librosa
warnings.simplefilter('ignore')

class IndexView(ListView):
    template_name= 'music/index.html'
    def get_queryset(self):
        return True

def model_form_upload(request):

    documents = Document.objects.all()
    if request.method == 'POST':
        if len(request.FILES) == 0:
            messages.error(request,'Upload a file')
            return redirect("predictor:index")

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploadfile = request.FILES['document']
            print(uploadfile.name)
            print(uploadfile.size)
            if not uploadfile.name.endswith('.wav'):
                messages.error(request,'Only .wav file type is allowed')
                return redirect("predictor:index")
        
            yy,sr = librosa.load(uploadfile, sr = 22050)
            meta = getmetadata(yy)
            
            # genre = predict_gen(meta)
            # print(genre)

            # context = {'genre':genre}
            # return render(request,'music/result.html',context)

                      
            genre = predict_genn(meta)
            print(genre)

            context = {'genre':genre}
            return render(request,'music/result.html',context)

    else:
        form = DocumentForm()

    return render(request,'music/result.html',{'documents':documents,'form':form})




















# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
# from django.views.generic import ListView
# from .apps import PredictorConfig
# from .forms import DocumentForm
# from .models import Document
# from .Metadata import getmetadata
# import warnings
# from .predict import predict_gen
# from django.contrib import messages
# import librosa
# warnings.simplefilter('ignore')
# import os


# class IndexView(ListView):
#     template_name= 'music/index.html'
#     def get_queryset(self):
#         return True

# def model_form_upload(request):

#     documents = Document.objects.all()
#     if request.method == 'POST':
#         if len(request.FILES) == 0:
#             messages.error(request,'Upload a file')
#             return redirect("predictor:index")

#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploadfile = request.FILES['document']
#             print(uploadfile.name)
#             print(uploadfile.size)
#             # if not uploadfile.name.endswith('.wav'):
#             #     messages.error(request,'Only .wav file type is allowed')
#             #     return redirect("predictor:index")
#             import subprocess
#             tempfile=os.path.join('C:/Users/jagad/Desktop/',uploadfile.name)
#             print(tempfile)
#             subprocess.call(['ffmpeg', '-i',tempfile,'C:/Users/jagad/Downloads/temp.wav'])
#             from pydub import AudioSegment
#             ii=AudioSegment.from_wav("C:/Users/jagad/Downloads/temp.wav")
#             ii=ii[0:30000]
#             tempp=ii.export('C:/Users/jagad/Downloads/temp.wav', format="wav")
#             #print(tempp)
#             temppfile="C:/Users/jagad/Downloads/temp.wav"
#             yy,sr = librosa.load(temppfile, sr = 22050)
#             meta = getmetadata(yy)
            
#             genre = predict_gen(meta)
#             print(genre)

#             context = {'genre':genre}
#             return render(request,'music/result.html',context)

#     else:
#         form = DocumentForm()

#     return render(request,'music/result.html',{'documents':documents,'form':form})