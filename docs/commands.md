# Commands

Here you can find a description of all **Nomade** commands:

## Version

Show the `Nomade` version.

Usage:

```bash
$ nomade version
```

## Init

Initialize a `Nomade` project.

Usage:

```bash
$ nomade init
```

## Migrate

Create a new `Nomade` migration.

Usage:

```bash
$ nomade migrate "My First Migration"
```

## Upgrade

Upgrade database version.

Usage:

```bash
$ nomade upgrade head
$ nomade upgrade 1
```

## Downgrade

Downgrade database version.

Usage:

```bash
$ nomade downgrade tail
$ nomade downgrade 1
```

## History

Show migration history.

Usage:

```bash
$ nomade history
```

## Current

Show the current migration applied in the database.

Usage:

```bash
$ nomade current
```

## Help

Show `Nomade` helper.

Usage:

```bash
$ nomade --help
```

## Stamp

Stamp a specific migration to the database.

**Note**: this command will not run any migration, it will only save the migration ID in the database.

Usage:

```bash
$ nomade stamp u19jh2h1
```
