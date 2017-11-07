
import os
import argparse

def parseArgs(_argsi=None):

# python haystack.py analyze --input_dir /code/dir
# python haystack.py search --keywords up down left

	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input_dir" ,type=parseInputDir, help="Path of the dir where audio files are present")
	parser.add_argument("-k", "--keywords", help="The keywords to be searched for", nargs='*')

	return parser.parse_args()


def parseInputDir(dir_path):
	_mp3=[]
	_wav=[]
	for f in os.listdir(dir_path):
		ff = os.path.abspath( os.path.join(dir_path,f) )
		if os.path.isfile(ff) :
			if f.endswith(".mp3"):
				_mp3.append(ff)
			if f.endswith(".wav"):
				_wav.append(ff)
	inputdict = {'mp3' : _mp3, 'wav' : _wav}
	#print inputdict
	return inputdict

if __name__ == "__main__":
	parseInputDir("/home/disha/code")
