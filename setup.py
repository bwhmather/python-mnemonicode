from setuptools import setup, find_packages


setup(
    name='mnemonicode',
    url='https://github.com/bwhmather/python-mnemonicode',
    version='1.4.3',
    author='Ben Mather',
    author_email='bwhmather@bwhmather.com',
    maintainer='',
    license='BSD',
    description=(
        "A library for encoding binary data as a sequence of english words"
    ),
    long_description=__doc__,
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
