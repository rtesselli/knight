from setuptools import setup, find_packages
import pathlib
import os.path
import codecs

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


def read(rel_path):
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delimiter = '"' if '"' in line else "'"
            return line.split(delimiter)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def read_requirements(path):
    with open(path, 'r') as file:
        return file.readlines()


setup(
    name='knight',
    version=get_version('knight/__init__.py'),
    description='Knight shortest path',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',  # TODO
    author='Riccardo Tesselli',
    author_email='riccardo.tesselli@gmail.com',
    packages=find_packages(include=['knight', 'knight.*']),
    python_requires='>=3.9',
    install_requires=read_requirements('requirements.txt'),
    extras_require={  # Optional
        'test': read_requirements('requirements_test.txt'),
    }
)
