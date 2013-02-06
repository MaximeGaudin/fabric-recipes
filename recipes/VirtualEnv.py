#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = u'Maxime Gaudin'

from fabric.api import sudo, run, cd, prefix, task

from contextlib import contextmanager as _contextmanager
import os


@task
def install():
    sudo('pip install --upgrade virtualenv')


@task
def create(path):
    if run('which virtualenv') == '':
        install()

    venv = os.path.join(path, 'venv')
    run('virtualenv --distribute {0}'.format(venv))

    return venv


@_contextmanager
def activate(venv):
    with cd(os.path.join(venv, '..')):
        with prefix('source {0}/bin/activate'.format(venv)):
            yield
