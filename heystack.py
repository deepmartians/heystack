
import pprint
import json

import utils
import audio_spliter
from analyze import Analyze
from finder import SearchHelper

pp = pprint.PrettyPrinter(indent=4)

def search(args):
  sh = SearchHelper()

  tags = args.keywords[0] if len(args.keywords) == 1 else args.keywords
  res = sh.search( tags )

  print res["hits"]["total"], " match found"
  for a in  res["hits"]["hits"]:
    print "\t", a["_source"]["name"]


def analyze(args):
  _analyze = Analyze( )
  print "input files", args.input_dir["wav"]

  normalized_wav_chunks = audio_spliter.getAudioChunks( args.input_dir["wav"] )
  print "length", len(normalized_wav_chunks)
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
