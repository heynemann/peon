import os
import unittest
from base import env, TEST_OUTPUT_DIR
from peon import something_has_changed
from should_dsl import *


class CheckIfSomethingHasChanged(unittest.TestCase):

    def setUp(self):
        env.reset()

    def should_be_true_if_there_are_changes_and_false_if_not(self):
        before = something_has_changed(TEST_OUTPUT_DIR, '*.py')
        env.writefile('dummy.py', 'dummy')
        after = something_has_changed(TEST_OUTPUT_DIR, '*.py')
        after |should_be| True
        before |should_be| False

    def should_be_possible_to_pass_patterns(self):
        before = something_has_changed(TEST_OUTPUT_DIR, pattern='*.ext')
        env.writefile('myfile.ext', 'my text')
        after = something_has_changed(TEST_OUTPUT_DIR, pattern='*.ext')
        after |should_be| True
        before |should_be| False

