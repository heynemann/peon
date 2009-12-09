Introduction
------------

Peon works for you while you are developing.

Installing
----------

Just install using:::
    python setup.py install

Using
-----

To use Peon, go to the folder where you want to keep running your tests and type:::
    peon make unit

(assuming your build command is make unit)

If you don't specify any commands Peon will assume you want "nosetests" as its command.

Peon will keep running that command whenever a file changes.
