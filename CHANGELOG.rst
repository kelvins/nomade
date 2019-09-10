Changelog
=========

All notable changes to this project are documented here.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

It basically follows the following approach to define versions (**MAJOR.MINOR.PATCH**):

- **MAJOR** for incompatible API changes.
- **MINOR** for new functionalities that are backward compatible.
- **PATCH** for backward compatible bug fixes.

[Unreleased] [0.0.1] - 2019-09-09
------------

Added
+++++

- Use `Poetry` to manage dependencies.
- Use `bumpversion` to automate semantic versioning.
- Add command line interface (CLI) commands:

  - `init`: initialize a Nomade project.
  - `version`: show package version.
  - `migrate`: create a new migration.
  - `upgrade`: upgrade to a new migration version.
  - `downgrade`: downgrade to a previous migration version.
  - `history`: show migrations history.
  - `current`: show the current migration.

- Support for `SQLite`, `MySQL` and `PostgreSQL`.
- Use `isort`, `black` and `flake8` to format and check the source code.
