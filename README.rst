Python Mnemonicode
==================

|build-status| |coverage|

A python library for encoding binary data as a sequence of english words.

Based on, and compatible with http://web.archive.org/web/20101031205747/http://www.tothink.com/mnemonic/


Installation
------------

Recommended method is to use the version from `pypi`_

.. code:: bash

    $ pip install mnemonicode

Please note that this library supports python 3 only.


Usage
-----

Python mnemonicode exposes four functions: `mnformat` and `mnparse` for handling conversions to and from formatted strings, and `mnencode` and `mndecode` for working with lower level lists of tuples of words.


String encoding
~~~~~~~~~~~~~~~

Encode a byte array as a sequence of grouped words, formatted as a single string:

.. code:: python

    >>> mnformat(b"cucumber")
    'paris-pearl-ultra--gentle-press-total';

Decode a mnemonicode string into a byte array:

.. code:: python

    >>> mnparse('scoop-limit-recycle--ferrari-album')
    b'tomato'

Both functions allow specifying the word and group separator.  It is safe for the word separator to match part of the group separator, but not the other way round.  Word and group separators that overlap with word in the dictionary should obviously be avoided.

An example using custom separators:

.. code:: python

    >>> mnemonicode.mnformat(
    ...     b'apricot', group_separator=', uhhh, ', word_separator=', um, '
    ... )
    'arctic, um, dilemma, um, single, uhhh, presto, um, mask, um, jet'


Tuple encoding
~~~~~~~~~~~~~~

Encode a bytes object as an iterator of tuples of words:

.. code:: python

    >>> list(mnencode(b"avocado"))
    [('bicycle', 'visible', 'robert'), ('cloud', 'unicorn', 'jet')]

Decode an iterator of tuples of words to get a byte array:

.. code:: python

    >>> mndecode([('turtle', 'special', 'recycle'), ('ferrari', 'album')])
    b'potato'


Links
-----

- Source code: https://github.com/bwhmather/python-mnemonicode
- Issue tracker: https://github.com/bwhmather/python-mnemonicode/issues
- Continuous integration: https://travis-ci.org/bwhmather/python-mnemonicode
- PyPI: https://pypi.python.org/pypi/mnemonicode


License
-------

The project is licensed under the BSD license.  See `LICENSE`_ for details.


.. |build-status| image:: https://travis-ci.org/bwhmather/python-mnemonicode.png?branch=develop
    :target: https://travis-ci.org/bwhmather/python-mnemonicode
    :alt: Build Status
.. |coverage| image:: https://coveralls.io/repos/bwhmather/python-mnemonicode/badge.png?branch=develop
    :target: https://coveralls.io/r/bwhmather/python-mnemonicode?branch=develop
    :alt: Coverage
.. _pypi: https://pypi.python.org/pypi/mnemonicode
.. _LICENSE: ./LICENSE
