Setting up Virtual environment:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
Installing Django extensions:
```
pip install django-extensions
```
(Can find the documentation here: https://github.com/django-extensions/django-extensions/tree/master/)

Installing PostgreSQL:
```
brew install postgresql
# to run the postgres server locally
postgres -D /usr/local/var/postgres
```
You will now have the server running in the foreground with logs being displayed in STDOUT. In another shell, open up the `psql` shell:
```
psql -d postgres
```
And then create the local users:
```
CREATE DATABASE dradle;
CREATE USER admin WITH PASSWORD 'admin';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```
You will notice that each of these actions outputs a log line in the server output shell.

Next you need to apply the django migrations to update your database:
```
# from within the dradle directory
python manage.py makemigrations
python manage.py migrate
```
For reference on how to set up django with a postgres backend, visit https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04. Keep in mind that `brew` does not create the `postgres` user when it installs, so you must do that manually (which was already handled above).

Now you are ready to run your django server:
Running the server
```
python manage.py runserver <PORT>
# the server is now running at localhost on <PORT>
```
