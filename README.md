# About

Monkeybrains is an api server for the [Monkeys app](https://github.com/janet/monkeys)

# To start development locally

1. Clone this repo `git clone git@github.com:janet/monkeybrains.git`
1. Run nginx @ localhost:8080 (instructions below)
1. Run api server @ localhost:5000 (instructions below)
1. Create and seed database (instructions below)
1. Run frontend server (instructions @ [Monkeys app](https://github.com/janet/monkeys))
1. Monkeys frontend app connected to Monkeybrains api server @ localhost:8080

## Nginx (osx)

1. Install nginx [Coderwall link](https://coderwall.com/p/dgwwuq/installing-nginx-in-mac-os-x-maverick-with-homebrew) for more info on nginx

        $ brew install nginx

2. Use nginx config from this repo

        $ rm /usr/local/etc/nginx/nginx.conf
        $ ln -s `pwd`/nginx.conf /usr/local/etc/nginx/nginx.conf

3. Start nginx proxy server @ localhost:8080

        $ sudo nginx

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

    $ (monkeybrains_env) cd api
    $ (monkeybrains_env) pytest

## Database
Create local postgres database @ postgresql://localhost/monkeys (first time only)

    $ createdb monkeys

Add dummy data to database - can be re-run to reset database

    $ (monkeybrains_env) python seed_database.py
