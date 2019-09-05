Commands
========

Here you can find a description of all ``Nomade`` commands:

Version
-------

Show the ``Nomade`` version.

Usage:

    $ nomade version

Init
----

Initialize a ``Nomade`` project.

Usage:

    $ nomade init

Migrate
-------

Create a new ``Nomade`` migration.

Usage:

    $ nomade migrate "My First Migration"

Upgrade
-------

Upgrade database version.

Usage:

    $ nomade upgrade head

    $ nomade upgrade 1

Downgrade
---------

Downgrade database version.

Usage:

    $ nomade downgrade tail

    $ nomade downgrade 1

History
-------

Show migration history.

Usage:

    $ nomade history

Current
-------

Show the current migration applied in the database.

Usage:

    $ nomade current

Help
----

Show ``Nomade`` helper.

Usage:

    $ nomade --help
