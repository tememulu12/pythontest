import unittest
from survey import AnonymousSurvey


class TestAnonymusSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = "Jaki jest Twój native język?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('angielski')
        self.assertIn('angielski', my_survey.responses)

    def test_store_three_response(self):
        question = "Jaki jest Twój native język?"
        my_survey = AnonymousSurvey(question)
        responses = ['polski', 'angielski', 'niemiecki']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)