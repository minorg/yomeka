import csv
import os.path
import shutil
import sys
from pprint import pformat

try:
    __import__('thryft')
    raise RuntimeError('thryft should not be on the PYTHONPATH already')
except ImportError:
    pass

MY_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR_PATH = os.path.abspath(os.path.join(MY_DIR_PATH, '..', '..'))
THRYFT_ROOT_DIR_PATH = os.path.abspath(os.path.join(ROOT_DIR_PATH, '..', 'thryft'))
assert os.path.isdir(THRYFT_ROOT_DIR_PATH), THRYFT_ROOT_DIR_PATH
sys.path.insert(0, os.path.join(THRYFT_ROOT_DIR_PATH, 'compiler', 'src'))

# Generate from thrift
import thryft.main
from thryft.generators.py.py_generator import PyGenerator
from thryft.generators.lint.lint_generator import LintGenerator


class Main(thryft.main.Main):
    def __init__(self, **kwds):
        thryft.main.Main.__init__(
            self,
            include_dir_paths=(
                os.path.join(ROOT_DIR_PATH, 'thrift', 'src'),
            ),
            **kwds
        )

    def _clean(self):
        for dir_path in (
             os.path.join(ROOT_DIR_PATH, 'py', 'src', 'yomeka', 'api'),
        ):
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)

    def _compile(self):
        self._clean()

        thrift_src_root_dir_path = os.path.join(ROOT_DIR_PATH, 'thrift', 'src')

        for thrift_subdir_name in ('api',):
            thrift_src_dir_path = os.path.join(thrift_src_root_dir_path, 'yomeka', thrift_subdir_name)
            if not os.path.isdir(thrift_src_dir_path):
                continue

            for thrift_file_path in self._get_thrift_file_paths(thrift_src_dir_path):
                thrift_file_name = os.path.split(thrift_file_path)[1]
                thrift_file_base_name = os.path.splitext(thrift_file_name)[0]

                compile_kwds = {
                    'document_root_dir_path': thrift_src_root_dir_path,
                    'thrift_file_path': thrift_file_path
                }

                self._compile_thrift_file(
                    generator=LintGenerator(),
                    **compile_kwds
                )

                self._compile_thrift_file(
                    generator=PyGenerator(),
                    out=os.path.join(ROOT_DIR_PATH, 'py', 'src'),
                    **compile_kwds
                )

assert __name__ == '__main__'
Main.main()
