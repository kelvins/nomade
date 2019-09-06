<p align="center">
  <img src="https://github.com/kelvins/nomade/blob/master/artwork/logo.svg" alt="Nomade Logo" title="Nomade Logo" width="250" height="150" />
</p>

![Release Alpha](https://img.shields.io/badge/Release-alpha-orange.svg?style=flat-square)
[![Python Version 3.7](https://img.shields.io/badge/Python-3.7-green.svg?style=flat-square)](https://www.python.org/downloads/release/python-370/)
[![Code Style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![License Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square)](https://github.com/kelvins/nomade/blob/master/LICENSE)

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
│   ├── template.py
│   └── migrations
└── .nomade.yml
```

Define **Nomade** settings in the `.nomade.yml` file.

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
