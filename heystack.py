
import utils
import audio_utils
from analyze import Analyze
from finder import SearchHelper

def search(args):
	sh = SearchHelper()
	res = sh.search( args.keywords )
	print( "search : {}".format(res) )

def analyze(args):
	_analyze = Analyze( )

	# args.input_dir is actually of dict type with keys like "mp3", "wav" etc and values like list of files
	normalized_wav_chunks = audio_utils.normalizeAudioData( args.input_dir )
	l,s = _analyze.analyze( normalized_wav_chunks )

	print( "{} items labelled and {} items were stored in DB".format(l,s) )


if __name__ == '__main__':

  args = utils.parseArgs()
	analyze(args)
	#search(args)

