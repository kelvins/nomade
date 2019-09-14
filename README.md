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

Nomade is a simple migration manager tool that aims to be easy to integrate with any ORM.

## Installation

Use [pip](https://pip.pypa.io/en/stable/installing/) to install Nomade:

```bash
$ pip install nomade
```

## Quick Start

Initialize a Nomade project:

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

Define **Nomade** settings in the `pyproject.toml` file.

Then, create your first migration:

```bash
$ nomade migrate "My first migration"
```

Implement the `upgrade` and `downgrade` functions in the migration file.

Then apply the migration to the database:

```bash
$ nomade upgrade head
```

To discover more **Nomade** features please read the documentation or run:

```bash
$ nomade --help
```

## How to Contribute

- Check for open issues or open a fresh one to start a discussion around a feature idea or a bug.
- Become more familiar with the project by reading the [Contributor's Guide](CONTRIBUTING.rst).
