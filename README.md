<p align="center">
    <img src="https://github.com/kelvins/nomade/blob/master/artwork/logo.svg" alt="Nomade Logo" title="Nomade Logo" width="250" height="150" />
</p>

<p align="center">
    <a href="https://travis-ci.org/kelvins/nomade" alt="Build Status">
        <img src="https://travis-ci.org/kelvins/nomade.svg?branch=master" />
    </a>
    <a href="https://coveralls.io/github/kelvins/nomade?branch=master" alt="Coverage Status">
        <img src="https://coveralls.io/repos/github/kelvins/nomade/badge.svg?branch=master" />
    </a>
    <a href="https://pypi.org/project/nomade/" alt="PyPI Version">
        <img src="https://img.shields.io/pypi/v/nomade.svg" />
    </a>
    <a href="https://www.python.org/downloads/release/python-370/" alt="Python Version">
        <img src="https://img.shields.io/badge/python-3.7-blue.svg" />
    </a>
    <a href="https://github.com/psf/black" alt="Code Style">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" />
    </a>
    <a href="https://github.com/kelvins/nomade/blob/master/LICENSE" alt="License">
        <img src="https://img.shields.io/badge/license-apache%202.0-blue.svg" />
    </a>
</p>

> Python Migration Manager for Humans :camel:

Nomade is a simple migration manager tool that aims to be easy to integrate with any ORM (e.g. [SQLAlchemy](https://www.sqlalchemy.org/), [Peewee](http://docs.peewee-orm.com/en/latest/), [Pony](https://ponyorm.org/)) and database (e.g. [SQLite](https://www.sqlite.org/index.html), [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/)). It is basically a command-line interface (CLI) tool that manages migrations (Python files) by applying changes to the database schema and storing the current migration ID.

This tool was inspired by [alembic](https://alembic.sqlalchemy.org/en/latest/) (if you are using SQLAlchemy as ORM you should consider using alembic).

> **Note**: this project is still under development so you may find bugs. If you find any bug, feel free to contribute by creating an issue and/or submitting a PR to fix it.

## Installation

Use [pip](https://pip.pypa.io/en/stable/installing/) to install Nomade:

```bash
$ pip install nomade
```

## Quick Start

Initialize a **Nomade** project:

```bash
$ nomade init
```

It will create the following project structure:

```
.
├── nomade
│   ├── template.py.j2
│   └── migrations
└── pyproject.toml
```

Define **Nomade** settings in the `pyproject.toml` file, for example:

```toml
[tool.nomade]
migrations = "nomade/migrations"
template = "nomade/template.py.j2"
connection-string = "sqlite:///nomade.db"
date-format = "%d/%m/%Y"
name-format = "{date}_{time}_{id}_{slug}"
```

Then, create your first migration:

```bash
$ nomade migrate "Create first table"
```

Implement the `upgrade` and `downgrade` functions in the migration file.

Then apply the migration to the database:

```bash
$ nomade upgrade head
```

To discover more **Nomade** features please read the documentation or call for help:

```
$ nomade --help

Usage: nomade [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  current    Show the current migration.
  downgrade  Downgrade migrations.
  history    Show migrations history.
  init       Init a Nomade project.
  migrate    Create a new migration.
  stamp      Stamp a specific migration to the database.
  upgrade    Upgrade migrations.
  version    Show Nomade version.
```

## How to Contribute

- Check for open issues or open a fresh one to start a discussion around a feature idea or a bug.
- Become more familiar with the project by reading the [Contributor's Guide](CONTRIBUTING.rst).
