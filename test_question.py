from unittest import TestCase
from question import Question, listQuestions, searchQuestions, viewQuestion
from textwrap import dedent
data = [{
    "option_1": "A",
    "option_2": "B",
    "mature": True,
    "votes_1": 0,
    "votes_2": 100
}, {
    "option_1": "123456789 123456789 123456789 123456789 123456789",
    "option_2": "123456789 123456789 123456789 123456789 123456789",
    "mature": False,
    "votes_1": 0,
    "votes_2": 0
}]

questions = [Question(**item) for item in data]

class TestQuestionMethods(TestCase):

    def test_repl(self):
        question = Question(option_1="ABC", option_2="DEF", mature=True)
        expected = """\
            Would you rather...
             1) ABC?
             2) DEF?
             
            This question has not been answered
            For mature audiences only
            Option 1 has 0 (0.0%) votes and Option 2 has 0 (0.0%) votes
            """
        self.assertEqual(question.__repl__(), dedent(expected))

    def test_contains(self):
        question = Question(option_1="ABC", option_2="DEF")
        self.assertEqual("A" in question, True)
