<p align="center">
  <img src="https://github.com/kelvins/nomade/blob/master/docs/logo.svg" alt="Nomade Logo" title="Nomade Logo" width="300" height="169" />
</p>

> Python Migration Manager for Humans :camel:

## Feature Support

- Manage your database migrations regardless of the ORM.
- Support for SQLite
- Support for MySQL (comming soon)
- Support for PostgreSQL (comming soon)

## Installation

Use [pip](https://pip.pypa.io/en/stable/installing/) to install Nomade:

```bash
pip install nomade
```

## Quick Start

Initialize a Nomade project with:

```bash
nomade init
```

It will create the migrations folder, the migration template and the nomade YAML file.

Configure the `.nomade.yml` file by setting the database connection string.

To create a new migration use:

```bash
nomade migrate "Create table XYZ"
```

Manually edit the migration as you like and upgrade your database with:

```bash
nomade upgrade
```

If needed you can downgrade to a previous version with:

```bash
nomade downgrade
```

To check your current database migration or to check the migration history use the following commands:

```bash
nomade current
nomade history
```

## Documentation

Comming soon

## How to Contribute

Comming soon

