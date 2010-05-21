from scripttest import TestFileEnvironment
import sys
import os


here = os.path.abspath(os.path.dirname(__file__))
package_dir = os.path.dirname(here)
peon_src_dir = os.path.join(package_dir, 'peon')
TEST_OUTPUT_DIR = os.path.join(here, 'test-output')

sys.path.insert(0, peon_src_dir)


class EnvironmentUnderTest(object):

    def __init__(self):
        self.reset()

    def reset(self):
        environ = os.environ.copy()
        environ.update({'PATH': os.path.join(TEST_OUTPUT_DIR, 'bin',
                                             os.pathsep, environ['PATH'])})
        self._env = TestFileEnvironment(environ=environ)
        self._env.run(sys.executable, '-m', 'virtualenv',
                                            '--no-site-packages',
                                            self._env.base_path)
        self._env.run('python setup.py install', cwd=package_dir)

    def run(self, *args, **kw):
        return self._env.run(*args, **kw)

    def mkdir(self, path):
        return os.mkdir(os.path.join(self._env.base_path, path))

    def writefile(self, *args, **kw):
        return self._env.writefile(*args, **kw)

env = EnvironmentUnderTest()
