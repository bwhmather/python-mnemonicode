import os
from setuptools import setup, find_packages

_readme_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'README.rst',
)
with open(_readme_path, encoding='utf-8') as _readme_file:
    _readme = _readme_file.read()


setup(
    name='mnemonicode',
    url='https://github.com/bwhmather/python-mnemonicode',
    version='1.4.4',
    author='Ben Mather',
    author_email='bwhmather@bwhmather.com',
    maintainer='',
    license='BSD',
    description=(
        "A library for encoding binary data as a sequence of english words"
    ),
    long_description=_readme,
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
    ],
    packages=find_packages(),
    package_data={
        '': ['*.pyi', 'py.typed'],
    },
    entry_points={
        'console_scripts': [
            'mnencode=mnemonicode:_mnencode_main',
            'mndecode=mnemonicode:_mndecode_main',
        ],
    },
    test_suite='mnemonicode.tests.suite',
)
