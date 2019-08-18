<p align="center">
  <img src="https://github.com/kelvins/nomade/blob/master/docs/logo.png" alt="Nomade Logo" title="Nomade Logo" />
</p>

> Python Migration Manager for Humans :camel:

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

To check your current database migration or to check the migration history use the following commands:

```bash
nomade current
nomade history
```

