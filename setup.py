import os
import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def read_requirements(filename):
    """Open a requirements file and return list of its lines."""
    contents = read_file(filename).strip('\n')
    return contents.split('\n') if contents else []


def read_file(filename):
    """Open and a file, read it and return its contents."""
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()


def get_metadata(init_file):
    """Read metadata from a given file and return a dictionary of them"""
    return dict(re.findall("__([a-z]+)__ = '([^']+)'", init_file))


class PyTest(TestCommand):

    """Command to run unit tests after in-place build."""

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '-sv',
            '--pep8',
            '--flakes',
            '--cov', 'kore',
            '--cov-report', 'term-missing',
        ]
        self.test_suite = True

    def run_tests(self):
        # Importing here, `cause outside the eggs aren't loaded.
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


init_path = os.path.join('kore', '__init__.py')
init_py = read_file(init_path)
metadata = get_metadata(init_py)


entry_points = """\
[kore.configs]
dict = kore.configs.dict:DictConfig
env = kore.configs.env:EnvConfig
"""


setup(
    name='kore',
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    packages=find_packages(include=('kore*',)),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=read_requirements('requirements.txt'),
    tests_require=read_requirements('requirements_dev.txt'),
    entry_points=entry_points,
    cmdclass={'test': PyTest},
    zip_safe=False,
)
