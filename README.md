# To start development

## Api Server
First time only, create python 3 virtualenv and install requirements and app

    $ virtualenv -p python3 monkeybrains_env
    $ source monkeybrains_env/bin/activate
    $ (monkeybrains_env) pip install -r requirements.txt
    $ (monkeybrains_env) pip install --editable .

Run server @ http://localhost:5000/

    $ source monkeybrains_env/bin/activate
    $ (monkeybrains_env) python api/runserver.py

Run tests

    $ (monkeybrains_env) pytest

## Database
Create local postgres database @ postgresql://localhost/monkeys (first time only)

    $ createdb monkeys

Add dummy data to database - can be re-run to reset database

    $ (monkeybrains_env) python seed_database.py


## Gotchas

**Issue:**

CORS error when using google chrome in development

    Fetch API cannot load http://localhost:5000/student_class_schedule. No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost:3000' is therefore not allowed access. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.

**Solution:**

Download chrome extension Allow-Control-Allow-Origin:* and enable it when developing
