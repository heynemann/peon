import os
import unittest
from base import env, TEST_OUTPUT_DIR
from peon import something_has_changed
from should_dsl import *


class CheckIfSomethingHasChanged(unittest.TestCase):

    def setUp(self):
        env.reset()

    def should_be_true_if_there_are_changes_and_false_if_not(self):
        before = something_has_changed(TEST_OUTPUT_DIR)
        env.writefile('lol.py', 'lol')
        after = something_has_changed(TEST_OUTPUT_DIR)
        after |should_be| True
        before |should_be| False

