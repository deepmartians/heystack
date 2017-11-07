import sys
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def mkdir_p(path):
	try:
		os.makedirs(path)
	except OSError as exc:  # Python >2.5
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else:
			raise

def getAudioChunks( wavFiles ):
	for wavFile in wavFiles:
		print 'Loading wav file {} ...'.format(wavFile)
		sound_file = AudioSegment.from_wav(wavFile)

		min_silence_len = 250
		silence_thresh = -16
		print 'splitting audio with sil_len: {} and threshold: {} ...'.format(min_silence_len, silence_thresh)
		audio_chunks = split_on_silence(sound_file, 
				# must be silent for at least half a second
				min_silence_len=min_silence_len,

				# consider it silent if quieter than -16 dBFS
				silence_thresh=silence_thresh
		)

		print '{} audio chunks found...'.format(len(audio_chunks))

		fileBaseName = os.path.splitext(os.path.basename(wavFile))[0]
		dirName='{}_{}_{}'.format(fileBaseName, min_silence_len, abs(silence_thresh))
		print 'Exporting chunks to {}'.format(fileBaseName)
		mkdir_p(dirName)
		for i, chunk in enumerate(audio_chunks):
			out_file = ".//{0}//{1}_chunk_{2}.wav".format(dirName, fileBaseName,i)
			#if not i % 50:
				#print "exporting {} chunk: {} ".format(i, out_file)
			chunk.export(out_file, format="wav")

				print 'Export complete.'
				print 
