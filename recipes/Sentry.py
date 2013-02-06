#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = u'Maxime Gaudin'

from fabric.api import run, task
from fabric.contrib.files import exists

from recipes import VirtualEnv, PostgreSQL


@task
def install(path):
    PostgreSQL.install()

    if not exists(path):
        run('mkdir {0}'.format(path))

    venv = VirtualEnv.create(path)
    with VirtualEnv.activate(venv):
        run('pip install sentry')
        run('pip install psycopg2')

        if exists('./sentry.conf.py'):
            run('rm ./sentry.conf.py')

        run('sentry init ./sentry.conf.py')

        PostgreSQL.create_db('sentry')

        run('sentry --config=./sentry.conf.py upgrade')
        run('sentry --config=./sentry.conf.py createsuperuser --username={0}'.format(run('whoami')))
        run('sentry --config=./sentry.conf.py repair --owner={0}'.format(run('whoami')))
