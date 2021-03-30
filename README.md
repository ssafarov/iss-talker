# ISSTalker

Author: Sergei Safarov <inbox@sergeysafarov.com>

Repo: (https://github.com/ssafarov/iss-talker)

## Introduction

This app is making api requests to the open-notify.org and get some information about ISS

## Prerequisites

* [python](https://www.python.org/)

## Running the Application

    python main.py <command line arguments>

### Allowable arguments
    * loc - [python main.py loc] -- output ISS location
    * people - [python main.py people] -- output current ISS crew onboard
    * pass <lat> <long> - [python main.py pass 45 -80] -- show nearest ISS passes over specific coordinates  


## Testing

    python -m unittest tests/test_main.py


