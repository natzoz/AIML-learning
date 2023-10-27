from unittest import TestCase
from neural_in_class import *


class Test(TestCase):
    def test_high_logistic_function(self):
        self.assertTrue(logistic(10) > 0.9)

    def test_low_logistic_function(self):
        self.assertTrue(logistic(-10) < 0.1)

    def test_medium_logistic_function(self):
        self.assertAlmostEquals(0.5, logistic(0))
