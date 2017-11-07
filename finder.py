
from storage import Storage

class SearchHelper(object):

	def __init__(self, tags=None):
		self._storage = Storage()
		if tags is not None:
			self.analyze( tags )


	def search(self, tags):
		response = self.storage.search( tags )
		return response


