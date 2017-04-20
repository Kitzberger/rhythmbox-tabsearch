# Tabsearch

A plugin for [Rhythmbox](https://wiki.gnome.org/Apps/Rhythmbox) to load tabs for currently playing songs.

## Features

* Supports these tab sites:
  * [AZChords](https://www.azchords.com/) (currently broken)
  * [e-chords](http://www.e-chords.com/)
  * [GuitareTab](http://www.guitaretab.com/)
  * [ultimateGuitar](https://www.ultimate-guitar.com/)
  * [lacuerda](http://lacuerda.net/)
* Stores tabs locally, allows editing too

## Requirements / compatibility

* rhythmbox 3.3
* python 3.x
* python-lxml

## Installation

```
git clone git@github.com:Kitzberger/rhythmbox-tabsearch.git
cd rhythmbox-tabsearch
make
```

## Debugging

Start rhythmbox in debug mode filtering "tabsearch" lines:

```
rhythmbox -D tabsearch
```
