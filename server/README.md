# Server for Bio AI project

This is the Flask server for the Bio AI project.

## Quickstart

`python -m flask run`

## Setup

``` virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python -m flask run
```

## Run the App
### Linux

`python -m flask run`
`FLASK_ENV=development flask run`
`FLASK_ENV=development FLASK_DEBUG=1 python -m flask run`

### Windows

Create environment:
`py -m venv venv`

Activate environment:
`.\venv\Scripts\activate`
Install dependencies
`pip install -r ./requirements.txt`

Run app (in Powershell):
`$env:FLASK_APP = "__init__"; $env:FLASK_ENV = "development";  flask run`

https://www.raffaelechiatto.com/modificare-permessi-di-esecuzione-di-script-in-powershell/
