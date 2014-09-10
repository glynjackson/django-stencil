==========================
django-stencil
==========================

Django Stencil is a boilerplate template for Django 1.7+ running Python 3.4.1
It has been build from our experience in deploying rapid applications in AWS. It draws on
the methodologies used on projects with both Samsung and HTC.

This project is a work in progress and still in development. It is intended for use with Django 1.7+ or above.

=============
Documentation
=============

Documentation can be found at http://django-stencil.readthedocs.org/

======================================================
Starting your project
======================================================

Create your Python environment::

    $ virtualenv env
    $ source env/bin/activate

If you are multiple version of Python you will need to install your virtualenv with Python 3.4.1::

    $ virtualenv -p python3 env

Install Django::

    $ pip install django

To create a new django-stencil base project, run the following command::

    $ django-admin.py startproject --template=https://github.com/glynjackson/django-stencil/zipball/master project_name

Where ``project_name`` is the name of the project you'd like to create.


Installing requirements
------------------------

You can install basic project requirements by running::

    pip3 install -r requirements.txt
