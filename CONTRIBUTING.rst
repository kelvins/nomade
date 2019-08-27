===========================
How to contribute to Nomade
===========================

Thanks for considering contributing to Nomade.

Reporting issues
================

When reporting an issue please make sure to include the following information:

- Describe the issue in detail.

- Provide a reproducible example of the issue.

- Include the Python version where the issue happened.

- Include the Nomade version where the issue happened.

Submitting patches
==================

- Include tests if your patch is supposed to solve a bug, and explain clearly
  under which circumstances the bug happens. Make sure the test fails without
  your patch.

- Follow `PEP8 <http://legacy.python.org/dev/peps/pep-0008/>`_ style guide.
  Please use `make isort` to sort imports and `make black` to format the code 
  using `black <https://github.com/psf/black>`_. 

- For notable changes (e.g. bug fixes, new features) please add the changes 
  to the ``CHANGELOG.rst``.

Setting up the environment
--------------------------

You can use `virtualenv <https://github.com/pypa/virtualenv>`_ 
or any other virtual environment tool you like.

Using ``virtualenv``::

    virtualenv venv
    source venv/bin/activate

This project uses `Poetry <https://github.com/sdispater/poetry>`_ to manage 
dependencies. After activating the virtual environment install the 
dependencies with::

    poetry install

Running the testsuite
---------------------

With the environment activated and the dependencies installed we can now run 
the tests with::

    make runtests

It will run the tests using ``pytest``.

To make sure the code is well formatted we can use the following command::

    make codecheck

It will run ``flake8`` and ``black`` to check the code.

