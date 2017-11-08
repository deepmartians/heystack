import sys
import os

from labeller import Labeller
from storage import Storage

class Analyze(object):
  def __init__(self, hostName, port, modelPath, labelsPath):
    self._labeller = Labeller( modelPath, labelsPath)
    self._storage = Storage(hostName, port)

  def analyze(self, normalized_wav_chunks):
    no_labelled = self.__label( normalized_wav_chunks )
    no_stored = self.__store()
    return no_labelled, no_stored


  def __label(self, normalized_wav_chunks):
    self.labels = {}

    for wav_chunk in normalized_wav_chunks:
      label = self._labeller.analyze( wav_chunk.data )
      self.labels.setdefault(wav_chunk.name, []).append(label)

    return len( normalized_wav_chunks) 


  def __store(self):
    for k,v in self.labels.iteritems():
      #print k,v
      data = { "name" : k, "tags" : " ".join(v) }
      print '{}: {}'.format(os.path.basename(k), v)
      self._storage.store( data )

    return len( self.labels.keys() )

