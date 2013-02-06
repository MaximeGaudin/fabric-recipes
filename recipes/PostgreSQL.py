#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = u'Maxime Gaudin'

from fabric.api import sudo, task


@task
def install():
    sudo('apt-get install postgresql postgresql-server-dev-9.1')


@task
def create_db(db_name):
    sudo('createdb -E utf-8 {0}'.format(db_name), warn_only=True,
         user='postgres')
