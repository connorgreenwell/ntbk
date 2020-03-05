ntbk
====

*ntbk* is a command line note taking tool. Everything is stored as plain text, and matching is fuzzy.

Quick Start
-----------

- ls

    $ python ntbk.py ls

    [0] First Note
    [1] Second Note
    [2] Keeping Notes
    [3] Plans for world domination
    [4] Papers to read

- search

    $ python ntbk.py ls papers -n 1

    [0] Papers to read

- cat

    $ python ntbk.py cat "first note"

    First Note
    ==========
    
    Hello, world!

TODO
----

- [ ] delete notes

Inspiration
-----------

- [jrnl](https://github.com/jrnl-org/jrnl)
- [Notational Velocity](http://notational.net/)