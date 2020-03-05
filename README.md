ntbk
====

*ntbk* is a command line note taking tool. Everything is stored as plain text,
and matching is fuzzy.

Quick Start
-----------

- edit

This command:
```
$ python ntbk.py edit "New Note"
```
will open up $EDITOR and allow you to write a note titled "New Note". If a
similarly titled note already exists, *ntbk* will open that for editing
instead.

- ls

This command:
```
$ python ntbk.py ls
```

Yields:
```
[0] First Note
[1] Second Note
[2] Keeping Notes
[3] Plans for world domination
[4] Papers to read
```

- search

This command:
```
$ python ntbk.py ls papers -n 1
```

Yields:
```
[0] Papers to read
```

- cat

This command:
```
$ python ntbk.py cat "first note"
```

Yields:
```
First Note
==========

Hello, world!
```

TODO
----

- [ ] delete notes

Inspiration
-----------

- [jrnl](https://github.com/jrnl-org/jrnl)
- [Notational Velocity](http://notational.net/)