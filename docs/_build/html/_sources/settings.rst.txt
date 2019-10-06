Settings
========

**Nomade** can be customized by defining the following settings in the ``pyproject.toml`` file.

Description
-----------

- **migrations**: Path to the migrations folder.
- **template**: Path to the template file.
- **connection-string**: String to connect to the database. The connection string can also be set by an environment variable (``CONNECTION_STRING``).
- **date-format**: Date format (follows the `Python date format <https://docs.python.org/3/library/datetime.html>`_).
- **name-format**: Name format (options are: ``date``, ``time``, ``id`` and ``slug``).

Example
-------

::

    [tool.nomade]
    migrations = "nomade/migrations"
    template = "nomade/template.py.j2"
    connection-string = "sqlite:///nomade.db"
    date-format = "%d/%m/%Y"
    name-format = "{date}_{time}_{id}_{slug}"
