import sys

from labeller import Labeller
from storage import Storage

class Analyze(object):

  def __init__(self, normalized_wav_chunks=None):
    self._labeller = Labeller( "models/frozengraph_heystack.pb", "models/labels.txt" )
    self._storage = Storage()
    if normalized_wav_chunks is not None:
      self.analyze( normalized_wav_chunks )


  def analyze(self, normalized_wav_chunks):
    no_labelled = self.__label( normalized_wav_chunks )
    no_stored = self.__store()
    return no_labelled, no_stored


  def __label(self, normalized_wav_chunks):
    self.labelled_wav_chunks = {}

    for wav_chunk in normalized_wav_chunks:
      predicted_label = self._labeller.getPredictedLabelForWavFile( wav_chunk.data )
      if wav_chunk.name not in self.labelled_wav_chunks.keys():
        self.labelled_wav_chunks.update( { wav_chunk.name : [] } )
      self.labelled_wav_chunks[ wav_chunk.name ].append( predicted_label )

    return len( normalized_wav_chunks) 


  def __store(self):
    for k,v in self.labelled_wav_chunks.iteritems():
      #print k,v
      data = { "name" : k, "tags" : " ".join(v) }
      self._storage.store( data )

    return len( self.labelled_wav_chunks.keys() )

