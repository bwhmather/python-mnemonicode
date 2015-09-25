Python Mnemonicode
==================

|build-status| |coverage|

A python library for encoding binary data as a sequence of english words.

Based on, and compatible with http://web.archive.org/web/20101031205747/http://www.tothink.com/mnemonic/


Installation
------------

Recommended method is to use the version from `pypi`_

.. code::

    pip install mnemonicode


Usage
-----

Encode

.. code::

    import mnemonicode as mn
    with open(infile, 'rb') as f:
        data = f.read()
    
    output = mn.mnformat(data)
    with open(outfile, 'w') as f:
        f.write(output)

Decode

.. code::

    import mnemonicode as mn
    with open(infile, 'r') as f:
        data = f.read()
    
    output = mn.mnparse(data)
    with open(outfile, 'wb') as f:
        f.write(output)


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
