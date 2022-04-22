#!/usr/bin/env sh

set -e

coverage erase
coverage run manage.py test
coverage report
