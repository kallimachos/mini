# Mini collection specification

An application for recording a collection of miniature figures from different
systems and companies. Local clients sync with the remote server through a
web-based REST API.

## Language

* Python 3.4
* Python 2.7 compatible if possible

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

* SQLite

## View

* CLI - argparse
* GUI - tkinter
* Web - HTML, CSS, mobile-friendly
* Android

## Controller

* mini object
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
* paint object
  - Name
  - Colour
  - Company
  - Notes
  - methods: add, edit, delete
* book object
  - Title
  - Army
  - Edition
  - Year
  - Notes
  - methods: add, edit, delete
* Load/Download DB
* Sync local DB with remote
* Add/edit list of companies, systems, armies, unit types, etc.
* Upload images
* Search
* Reports
* Save DB/reports as spreadsheets
* Print
* Authentication
