#Provisioning a new site

## Reqired packages:

- nginx
- Python 3.7
- virtualenv + pip
- Git
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

## Local Development

Vagrant needs to be installed.

Invoking `vagrant up` inside `${Project_Dir}/deploy_tools` will bring up a headless ubuntu machine.

Ansible will provision the project and setup the missing parts. 
Afterwards the project is reachable via the configured domain.

Before accessing it altering `/etc/hosts/` is probably necessary.
