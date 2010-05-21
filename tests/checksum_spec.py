import os
import unittest
from base import env, TEST_OUTPUT_DIR
from peon import checkSumRecursive
from should_dsl import *


class ChecksumSpec(unittest.TestCase):

    def setUp(self):
        env.reset()

    def should_find_python_files_in_dir(self):
        env.writefile('lol.py', 'lol')
        first_checksum = checkSumRecursive(TEST_OUTPUT_DIR)
        env.writefile('lol.py', 'lol\nlol again')
        second_checksum = checkSumRecursive(TEST_OUTPUT_DIR)

        first_checksum |should_be.less_than| second_checksum

    def should_find_python_files_in_subdirs(self):
        env.mkdir('foo')
        env.mkdir('foo/bar')
        foo_path = os.path.join(TEST_OUTPUT_DIR, 'foo')
        env.writefile('foo/bar/lol.py', 'lol')
        first_checksum = checkSumRecursive(foo_path)
        env.writefile('foo/bar/lol.py', 'lol\nlol again')
        second_checksum = checkSumRecursive(foo_path)

        first_checksum |should_be.less_than| second_checksum

    def should_find_files_by_pattern_matching(self):
        env.writefile('lol.foo', 'lol')
        first_checksum = checkSumRecursive(TEST_OUTPUT_DIR, pattern='*.foo')
        env.writefile('lol.foo', 'lol\nlol again')
        second_checksum = checkSumRecursive(TEST_OUTPUT_DIR, pattern='*.foo')

        first_checksum |should_be.less_than| second_checksum

    def should_find_files_by_relative_paths(self):
        env.writefile('lol.foo', 'lol')
        first_checksum = checkSumRecursive('tests/test-output', pattern='*.foo')
        env.writefile('lol.foo', 'lol\nlol again')
        second_checksum = checkSumRecursive(TEST_OUTPUT_DIR, pattern='*.foo')

