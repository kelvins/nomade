<p align="center">
  <img src="https://github.com/kelvins/nomade/blob/master/artwork/logo.svg" alt="Nomade Logo" title="Nomade Logo" width="300" height="169" />
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
│   ├── template.py
│   └── migrations
└── .nomade.yml
```

Set the settings in the `.nomade.yml` file.

Then, create your first migration:

```bash
$ nomade migrate "My first migration"
```

Then apply the migration to the database:

```bash
$ nomade upgrade head
```

To discover more Nomade features please read the documentation or run:

```bash
$ nomade --help
```

## Documentation

Comming soon

## How to Contribute

- Check for open issues or open a fresh one to start a discussion around a feature idea or a bug.
- Become more familiar with the project by reading the [Contributor's Guide](CONTRIBUTING.rst).
