Enterprise Information Systems Patterns Examples
================================================

This project aims at presenting examples on how to use EIS Patterns framework.
Currently an ultra-simple Bank System is in development.

Setup
-----

Pre-setup (on Ubuntu)::

    $ apt-get install python-setuptools
    $ easy_install pip


Install dependencies (if needed) and run all specs (depending on your
environment, you'll need to call with sudo)::

    $ make


Run only unit specs::

    $ make unit


Run only acceptance specs::

    $ make acceptance

