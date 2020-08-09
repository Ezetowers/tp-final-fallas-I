from intellect.Intellect import Intellect
from intellect.Intellect import Callable

class MyIntellect(Intellect):
	def initialize(self):
		self._actual_flux = 0
		self._question_selected = 0
		self._arrow_model_selected = 0
		self._flux_array = ['Flux1', 'Flux2', 'Flux3', 'Flux4']

	@Callable
	def arrow_model_selected(self, value):
		self._arrow_model_selected = value

	@Callable
	def question_selected(self, value):
		self._question_selected = value

	def get_arrow_model_selected(self):
		return self._arrow_model_selected

	def get_question_select(self):
		return self._question_selected

	def get_next_flux(self):
		flux = self._flux_array[ self._actual_flux ]
		self._actual_flux = self._actual_flux + 1
		return flux

	def reason_not_finished(self):
		return self._question_selected == 0 and self._arrow_model_selected == 0