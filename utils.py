
import os
import argparse

def parseArgs(_argsi=None):

# python haystack.py analyze --input_dir /code/dir
# python haystack.py search --keywords up down left

	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input_dir" ,type=parseInputDir, help="Path of the dir where audio files are present")
	parser.add_argument("-s", "--search", help="The keywords to be searched for", nargs='*')
	parser.add_argument("-m", "--model", default="models/frozengraph_heystack.pb", help="Model used to analyse the input file")
	parser.add_argument("-l", "--labels", default="models/labels.txt", help="Labels to be analysed")
	parser.add_argument("-d", "--db_host", default="127.0.0.1", help="DB hostname")
	parser.add_argument("-p", "--port", default=9200, help="DB port no.")

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
