Changelog
=========

All notable changes to this project are documented here.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

It basically follows the following approach to define versions (**MAJOR.MINOR.PATCH**):

- **MAJOR** for incompatible API changes.
- **MINOR** for new functionalities that are backward compatible.
- **PATCH** for backward compatible bug fixes.

[Unreleased]
------------

[1.0.0] - 2019-10-05
--------------------

Added
+++++

- Add the ``stamp`` command to save a migration ID in the database without applying any migration.
- Configure Travis CI and Coveralls to track the code quality (code format and coverage).
- Add a way to provide the connection string through an environment variable (``CONNECTION_STRING``).

Changed
+++++++

- Change settings file from ``.nomade.yml`` to ``pyproject.toml``.
- Makes configuration variables more verbose.
- Change migration template from ``template.py`` to ``template.py.j2`` (Jinja2).

Security
++++++++

- Use ``bandit`` to search for common security issues.

[0.0.1] - 2019-09-09
--------------------

Added
+++++

- Use ``Poetry`` to manage dependencies.
- Use ``bumpversion`` to automate semantic versioning.
- Add command line interface (CLI) commands:

  - ``init``: initialize a Nomade project.
  - ``version``: show package version.
  - ``migrate``: create a new migration.
  - ``upgrade``: upgrade to a new migration version.
  - ``downgrade``: downgrade to a previous migration version.
  - ``history``: show migrations history.
  - ``current``: show the current migration.

- Support for ``SQLite``, ``MySQL`` and ``PostgreSQL``.
- Use ``isort``, ``black`` and ``flake8`` to format and check the source code.
