## Sukko lake


### Description

>https://sukkolake-production.up.railway.app/

Freelance project.
One page application about sukko-lake tour. It is possible to sign up for a tour online.

Also admin possible add reviews and slides to carousel from admin-panel.

### Installation

1. Clone repo: ``$ git clone https://github.com/seeu359/sukko-lake.git``
2. Go to the directory with code: ``$ cd sukko-lake``
3. Set the dependencies:
   1. If you're using poetry, run command: ``$ make p_install``
   2. Else: ``$ make install``
---
### Main dependencies

| Library | Version |
|--------|--------|
| python | 3.10   |
 | django | 4.1.4  | 
 | gunicorn | 20.1.0 | 
 | psycopg2 | 2.9.5 |
|whitenoise | 6.2.0 |

---
### Environment Variables 

SECRET_KEY - Django secret key 

DATABASE_URL - Database url

DEBUG - True or False

MAIL_TOKEN - Mail token or password for sending alert email while client put application

SENDER_EMAIL - Email address which the letters will come

RECEIVER_EMAIL - Admin email address

There are all variables in env.example file.
