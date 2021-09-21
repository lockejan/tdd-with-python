#Provisioning a new site

## Reqired packages:

- nginx
- Python 3.6
- virtualenv + pip
- Git
- pwgen
- Systemd

## Nginx Virtual Host Config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder Structure:

Assume we have a user account at /home/username

DOMAIN
├── db.sqlite3
├── deploy_tools
├── functional_tests
├── geckodriver.log
├── lists
├── manage.py
├── requirements.txt
├── static
├── superlists
└── venv
