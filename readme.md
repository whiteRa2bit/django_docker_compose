# Django Docker-compose application

## Introduction
Django Docker-compose sample application with pytest tests, that allows storing study materials.

## Features

- Get list of items
- Get item
- Add item
- Delete item
- Update item

A detailed description of those features can be found at [docs](docs/readme.md)

## Structure

`src` folder contains two subfolders:
  - `server`, subfloder with server code and Dockerfile
  - `tests`, subfolder with tests (pytest) and Dockerfile

In `docs` you can find a detailed API description

### Getting Started

Install Docker and docker-compose, if not already.
Instructions for an installation can be found there: https://docs.docker.com/compose/install/.

To build the server and tests:
```bash
$ cd src
$ docker-compose build
```

To run the server and tests:
```bash
$ docker-compose up -d server
$ docker-compose run pytest -vs
```

After tests successfully passed you can down docker-compose until the next run.
```bash
$ docker-compose down
```

One-liner for comands listed above:
```bash
$ docker-compose build && docker-compose up -d server && docker-compose run pytest && docker-compose down
```
