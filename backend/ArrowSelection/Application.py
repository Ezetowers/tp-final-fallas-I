import sys, logging, time, random
import web
import json
from intellect.Intellect import Intellect
from MyIntellect import MyIntellect
from Question import Question
from Arrow_Model import Arrow_Model
from Model import Model


class Application(object):
	def __init__(self):
		# Load the rules 
		self._myIntellect = MyIntellect() 
		self._myIntellect.learn(
			self._myIntellect.local_file_uri('./rulesets/secondRuleSet.policy'))

	def GET(self):
		# Habilitate the cross-domain communication
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Credentials', 'true')

		# Receive the data from the browser and create 
		# the objects used by the policies
		user_data = web.input()
		self._model = Model()

		self._myIntellect.initialize()

		self.set_length( user_data )
		self.set_height( user_data )
		self.set_poundage( user_data )
		self.set_temperature( user_data )
		self.set_target_distance( user_data )

		self._question = Question()
		self._arrow_model = Arrow_Model()

		self._myIntellect.learn( self._model )
		self._myIntellect.reason()

		self._question.number = self._model.question
		self._arrow_model.value = self._model.arrow_model

		# Send the results to the browser on a json
		json_map = { 'question' : self._question.number,
					 'model' : self._arrow_model.get_model_name() } 
		return json.dumps( json_map )


	def set_length(self, user_data):
		try:
			self._model.arm_length = int(user_data.longitud)
		except AttributeError:
			logging.getLogger( 'ArrowSelection' ).error( '[APPLICATION] Arm_Length does not exists' )

	def set_height(self, user_data):
		try:
			self._model.height = int(user_data.altura)
		except AttributeError:
			logging.getLogger( 'ArrowSelection' ).error( '[APPLICATION] Height does not exists' )

	def set_poundage(self, user_data):
		try:
			self._model.poundage = int(user_data.libraje) 
		except AttributeError:
			logging.getLogger( 'ArrowSelection' ).error( '[APPLICATION] Poundage does not exists' )


	def set_temperature(self, user_data):
		try:
			self._model.temperature = int(user_data.temperatura)
		except AttributeError:
			logging.getLogger( 'ArrowSelection' ).error( '[APPLICATION] Temperature does not exists' )


	def set_target_distance(self, user_data):
		try:
			self._model.target_distance = int(user_data.distancia)
		except AttributeError:
			logging.getLogger( 'ArrowSelection' ).error( '[APPLICATION] Target Distance does not exists' )

