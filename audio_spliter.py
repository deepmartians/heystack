import sys
import os
import errno

class AudioChunk:
  def __init__(self, name, data):
    self.name = name
    self.data = data

class FilePersister:
  def __init__(self, fileName, isPersist, min_silence_len="", silence_thresh=""):
    self.__isPersist = isPersist
    self.__baseName = os.path.splitext(os.path.basename(fileName))[0]
    self.__dirName='chunks_{}_{}_{}'.format(self.__baseName,min_silence_len, abs(silence_thresh))
    self.__min_silence_len = min_silence_len
    self.__silence_thresh = silence_thresh
    if self.__isPersist:
      self.__mkdir(self.__dirName)

  def save(self, chunk, chunk_id):
    if self.__isPersist:
      fileName = "{0}/{1}_chunk_{2:03d}.wav".format(self.__dirName, self.__baseName, chunk_id)
      chunk.export(fileName, format="wav")

  def __mkdir(self, dirPath):
    try:
      print 'creating dir {}'.format(dirPath)
      os.makedirs(dirPath)
    except OSError as exc:  # Python >2.5
      if exc.errno == errno.EEXIST and os.path.isdir(dirPath):
        pass
      else:
        raise

def getAudioChunks( wavFiles, min_silence_len = 800, silence_thresh=-16, isPersist=False ):
  chunks = []
  for wavFile in wavFiles:
    filePersister = None
    if isPersist:
      filePersister = FilePersister(wavFile, isPersist, min_silence_len, silence_thresh)
    with open(wavFile, 'rb') as wf:
      chunks.append(AudioChunk(wavFile, wf.read()))
  return chunks

if __name__ == '__main__':
  if len(sys.argv) <= 1: 
    print 'Usage: audio_splitter.py <wav_file_path>'
    sys.exit(1)
  getAudioChunks(sys.argv[1:], isPersist = True)
