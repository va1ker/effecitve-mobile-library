# Library managment system

Test case for effective mobile

## Requirements

- [Python 3.10^](https://www.python.org/downloads/)

## Installation

```bash
git clone 
```

```bash
cd effective-mobile-library
```

```bash
python3 main.py
```

## Usage
Use `help` command to see all avaliable commands.

List of commands:

- exit: stop programm
- help: list of commands
- get_all: get all books
- find: find book by it's title, year or name
- add: add book 
- update: update book status by it's ID
- delete: delete book by it's ID

## About project
I've been wanting to try something like this for a while—creating an app with base classes. It's been such a cool experience, and I'm really glad I gave it a shot! <3

I tried to build an app with a structure kinda similar to Django, starting by creating a base model and inheriting it to make a book model. I also set up commands, which are basically like views in Django. I even attempted to make a mini Django-like ORM, so interacting with the models would be smoother. The goal was to make CRUD operations universal, so every model could work with them without needing to redefine those methods in each model. 🚀

All in all, it’s been a fun challenge! 😎

## About tests

I'm turning this in on the deadline day 'cause I spotted the job posting on HH last minute, so I didn't have time to write tests 😅.

Instead, I'll briefly explain how I'd approach them. Using OOP, I'd write test classes for each CRUD operation, relying on assert to validate outcomes. I'd also check edge cases like empty input, invalid data, or nonexistent IDs to make sure everything behaves as expected. The idea is to keep it simple but solid enough to cover the basics. 🚀





