Introduction
------------

Peon works for you while you are developing.

It runs any command you tell it and execute the command when some file that matches a pattern is changed.


Installing
----------

Just install using::

    python setup.py install

Using
-----

By default Peon looks for changes in python files *(\*.py)* and if no command is specified, it run *nosetests*.

Peon will keep running that command whenever a file changes.

For example, take the following directory tree as example::

    .
    |-- Makefile
    |-- peon
    |   |-- __init__.py
    |   |-- peon.py
    |   |-- stop.png
    |   `-- tick.png
    |-- setup.py
    `-- tests
        |-- base.py
        |-- checksum_spec.py
        |-- something_has_changed_spec.py

If I want Peon watches for changes in all my "\*.py" files and run "make" when something changes, I could do simply::
    
    $ peon make # run make in the current dir, looking for changes in *.py files


It is possible to specify the directory to watch (-d or --directory option)::

    $ peon make -d peon

    
It is possible to tell peon what is your pattern too, through -p or --patern option::
    
    $ peon make -p '*.png' -d peon
