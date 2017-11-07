
import utils
#import audio_utils
from analyze import Analyze
from finder import SearchHelper

def search(args):
	sh = SearchHelper()

	tags = args.keywords[0] if len(args.keywords) == 1 else args.keywords
	res = sh.search( tags )

	print( "search : {}".format(res) )

def analyze(args):
	_analyze = Analyze( )

	normalized_wav_chunks = audio_utils.normalizeAudioData( args.input_dir )
	l,s = _analyze.analyze( normalized_wav_chunks )

	print( "{} items labelled and {} items were stored in DB".format(l,s) )


if __name__ == '__main__':

  args = utils.parseArgs()

  if args.input_dir is not None:
		analyze(args)

  if args.keywords is not None:
		search(args)

  if args.input_dir is None and args.keywords is None:
		print "Nothing to do"
