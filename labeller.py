
import tensorflow as tf

class Labeller(object):

	def __init__(self, graph_file, label_file, input_name=None, output_name=None, how_many_labels=None ):
		""" 
				graph_file : graph file
				lable_file : label file. Assumtion : labels order should be in sync with confusion matrix order
				input_name, output_name, how_many_labels are needed for searching in trained graph
		"""
		self.__graph_file = graph_file
		self.__label_file = label_file
		self.__input_name = input_name
		self.__output_name = output_name
		self.__how_many_labels = how_many_labels
		self.__initialize()


	def __initialize(self):
		"""Loads the model and labels, and sets other required values"""
		self.__loadGraph()
		self.__loadLabels()

		if self.__input_name is None:
			self.__input_name = 'wav_data:0'

		if self.__output_name is None:
			self.__output_name = 'labels_softmax:0'

		if self.__how_many_labels is None:
			self.__how_many_labels = 1

		self.__tf_session = tf.Session()
		self.__session_tensor = self.__tf_session.graph.get_tensor_by_name( self._output_name )


	def __loadGraph(self):
		"""Unpersists graph from file as default graph."""
		with tf.gfile.FastGFile(self.__graph_file, 'rb') as f:
			graph_def = tf.GraphDef()
			graph_def.ParseFromString( f.read() )
			tf.import_graph_def (graph_def, name='' )


	def __loadLabels(self):
		"""Read in labels, one label per line."""
		self.__readble_labels = [ line.rstrip() for line in tf.gfile.GFile( self.__label_file ) ]


	def getPredictedLabelForWavFile(self, a_wav_file_raw_data):
		"""Runs the wave form of audio data through the graph and return the predictions."""

			_input = { self.__input_name : a_wav_file_raw_data }

			# Getting predictions values
			predictions, = self.__tf_session.run( self._session_tensor, _input )

			# Sort to show labels in order of confidence
			top_k = predictions.argsort()[-self.__how_many_labels:][::-1]

			# preparing output
			data_to_return = [ ( self.__readble_labels[i], predictions[i] ) for i in top_k ]

			return data_to_return

