# newspaper-agency

Django project for tracking Redactors, assigned to Newspapers.
So you will always know, who were the publishers of each Newspaper.


[Newspaper agency project deployed to Render](https://newspaper-agency-de9j.onrender.com)

# Installation

Python3 must be already installed

```shell
git clone https://github.com/anton-chumak-main/newspaper-agency.git
cd newspaper-agency
python3 -m venv venv
source venv/bin/activate

set DJANGO_DEBUG=<False to run in DEBUG=False or True for DEBUG=True>
set SECRET_KEY=<your SECRET_KEY>
set DATABASE_URL=<your DATABASE_URL>

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
 - You can use the following superuser (or create another user one yourself):
    - Login: user
    - Password: User12345

## Feature

* Authentication functionality for Redactor/User
* Tracking Redactors, assigned to Newspapers or topical articles
* Powerful admin panel for advanced managing
