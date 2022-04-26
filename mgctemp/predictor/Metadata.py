#creating a function to perform feature extraction on the given audio file

def getmetadata(y):
  import librosa
  import numpy as np
  feature_list=[]
  sr=22050
  zcr = librosa.feature.zero_crossing_rate(y)[0]
  feature_list.append(np.mean(zcr))
  feature_list.append(np.std(zcr))

  
  spectral_centroids = librosa.feature.spectral_centroid(y, sr=sr)[0]
  feature_list.append(np.mean(spectral_centroids))
  feature_list.append(np.std(spectral_centroids))

  
  spectral_rolloff = librosa.feature.spectral_rolloff(y, sr=sr)[0]
  feature_list.append(np.mean(spectral_rolloff))
  feature_list.append(np.std(spectral_rolloff))

  mfccs = librosa.feature.mfcc(y, sr=sr)
  feature_list.extend(np.mean(mfccs, axis=1))
  feature_list.extend(np.std(mfccs, axis=1))

  
  
  return feature_list




# def getmetadata(filename):
#     import librosa
#     import numpy as np


#     y, sr = librosa.load(filename)
#     #fetching tempo

#     onset_env = librosa.onset.onset_strength(y, sr)
#     tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

#     #fetching beats

#     y_harmonic, y_percussive = librosa.effects.hpss(y)
#     tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,sr=sr)

#     #chroma_stft

#     chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)

#     #rmse

#     rmse = librosa.feature.rms(y=y)

#     #fetching spectral centroid

#     spec_centroid = librosa.feature.spectral_centroid(y, sr=sr)[0]

#     #spectral bandwidth

#     spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)

#     #fetching spectral rolloff

#     spec_rolloff = librosa.feature.spectral_rolloff(y+0.01, sr=sr)[0]

#     #zero crossing rate

#     zero_crossing = librosa.feature.zero_crossing_rate(y)

#     #mfcc

#     mfcc = librosa.feature.mfcc(y=y, sr=sr)

#     #metadata dictionary

#     metadata_dict = {'tempo':tempo,'chroma_stft':np.mean(chroma_stft),'rmse':np.mean(rmse),
#                      'spectral_centroid':np.mean(spec_centroid),'spectral_bandwidth':np.mean(spec_bw), 
#                      'rolloff':np.mean(spec_rolloff), 'zero_crossing_rates':np.mean(zero_crossing)}

#     for i in range(1,21):
#         metadata_dict.update({'mfcc'+str(i):np.mean(mfcc[i-1])})

#     return list(metadata_dict.values())



