# Mini collection specification

An application for recording a collection of miniature figures from different
systems and companies. Local clients sync with the remote server through a
web-based REST API.

## Language

* Python 3.4

## Testing, logging, and configuration

* tox
* pytest
* flake8
* logging
* configparser

## Version control and CI

* GitHub
* Travis

## Documentation

* Swagger API docs
* Markdown docs

## Hosting

* Rackspace public cloud
* Bottle framework

## Model

* model.py
* collection.sqlite

## View

* cli.py - argparse
* gui.py - tkinter
* web.py - HTML, CSS, mobile-friendly
* Android

## Controller

* controller.py
* REST API (bottle)

### record object
* mini
  - Name
  - Army
  - Unit type (e.g. hero, core, etc.)
  - System
  - Company
  - Quantity
  - Status (painted, unpainted, sprue, bitz, NIB)
  - Notes
  - Image of model
  - methods: add, edit, delete
* paint
  - Name
  - Colour
  - Company
  - Notes
  - methods: add, edit, delete
* book
  - Title
  - Army
  - Edition
  - Year
  - Company
  - Notes
  - methods: add, edit, delete
* game (aka board games)
  - Title
  - Company
  - Number of players
  - Time to play
  - Age range
  - methods: add, edit, delete

### Features
* Load/Download DB
* Sync local DB with remote
* Add/edit list of companies, systems, armies, unit types, etc.
* Upload images
* Search
* Reports
* Save DB/reports as spreadsheets
* Print
* Authentication
