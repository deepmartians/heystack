
from elasticsearch import Elasticsearch 

class Storage(object):

	_index_name = "heystack_voice_call_index"
	_doc_type = "voice_call_type"

	def __init__(self):
		self._db = Elasticsearch()
		self.__createIndex()


	def store(self, data):
		try:
			response = self._db.index( index=Storage._index_name, doc_type=Storage._doc_type, body=data )
			print( "data {result} in version {_version}".format(**response) )
			return response
		except Exception as e:
			print( "wrong input provided {}".format(_input_data) )
			print( "exception : {}".format(e) )
		return None


	def search(self, tags):
		query = self.__frameSearchQueryBody(tags)
		if query is not None:
			response = self._db.indices.search( index=Storage._index_name, doc_type=Storage._doc_type, body=query )
			return response
		else:
			print "wrong query"


	def __createIndex(self):
		self._db.indices.create( index=Storage._index_name, ignore=400 )


	def __frameSearchQueryBody(self, tags):
		_body = None
		if type(tags) = str:
			_body = self.__frameSimpleSearchQueryBody( tags )
		else type(tags) = list:
			_body = self.__frameSearchQueryBodyForList( tags )\
		return _body


	def __frameSearchQueryBodyForList(self, tags):
		_body = {
			"query" : {
				"match" : {
					"tags" : " ".join(tags)
					}
				}
			}
		return _body


	def __frameSimpleSearchQueryBody(self, tags):
		_body = {
			"query" : {
				"match" : {
					"tags" : tags
					}
				}
			}
		return _body


	def __getUniqueIdDataUsingBasicSearch(self, key_value_pair):
		body = {
			"query" : {
				"match" : key_value_pair
				}
			}
		response = self._db.indices.search( index=Storage._index_name, doc_type=Storage._doc_type, body=query )
		total_rows = response["hits"]["total"]
		if total_rows == 0:
			return None, None
		elif total_rows == 1:
			for res in response["hits"]["hits"]:
				return res["_id"], res["_source"]
		else:
			raise Exception("More than 1 value found for criteria : {}".format(key_value_pair) )


