
import pprint
import json

import utils
import audio_spliter
from analyze import Analyze
from finder import SearchHelper

pp = pprint.PrettyPrinter(indent=4)

def search(args):
  sh = SearchHelper(args.db_host, args.port)

  tags = args.search[0] if len(args.search) == 1 else args.search
  res = sh.search( tags )

  print res["hits"]["total"], " match found"
  for a in  res["hits"]["hits"]:
    print "\t", a["_source"]["name"]


def analyze(args):
  _analyze = Analyze(args.db_host, args.port, args.model, args.labels )
  print "{} input wave files detected.".format(len(args.input_dir["wav"]))

  audio_chunks = audio_spliter.getAudioChunks( args.input_dir["wav"] )
  analyse_count, saved_count = _analyze.analyze( audio_chunks )

  print( "{} words identified across {} audio files".format(saved_count, analyse_count) )


if __name__ == '__main__':

  args = utils.parseArgs()

  if args.input_dir is not None:
    analyze(args)

  if args.search is not None:
    search(args)

  if args.input_dir is None and args.search is None:
    print "unknown arguments"
