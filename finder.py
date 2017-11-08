
from storage import Storage

class SearchHelper(object):

  def __init__(self, hostName, port, tags=None):
    self._storage = Storage(hostName, port)
    if tags is not None:
      self.analyze( tags )


  def search(self, tags):
    response = self._storage.search( tags )
    _format = "Total hits : {hits.totals}"
    _format = "{}"
    return response


