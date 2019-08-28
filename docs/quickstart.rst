Quick Start
===========

Here you can find a quick tutorial with basic ``Nomade`` commands.

virtualenv
----------

We recommend the use of a virtual environment to run develop any Python project. You can create a virtual environment using ``virtualenv`` tool, for example:

    $ pip install virtualenv
    
    $ virtualenv venv
    
    $ source venv/bin/activate

Installation
------------

With the virtual environment created and activated you are ready to go. Go ahead and install ``Nomade`` with:

    $ pip install nomade

Basic commands
--------------

Initialize a ``Nomade`` project with:

    $ nomade init

Set the settings in the `.nomade.yml` file.

Then, create your first migration:

    $ nomade migrate "My first migration"

Then apply the migration to the database:

    $ nomade upgrade head

These are the basic ``Nomade`` commands, to discover more features please read the :doc:`Commands <commands>` section or run the following command:

    $ nomade --help
