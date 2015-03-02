==========================
django-stencil
==========================

Django Stencil is a boilerplate template for Django 1.7+ running Python 3.4.1
It has been build from our experience in deploying rapid applications in AWS. It draws on
the methodologies used on projects with both Samsung and HTC.

This project is a work in progress and still in development. It is intended for use with Django 1.7+ or above.

Documentation
=============

Documentation can be found at http://django-stencil.readthedocs.org/


Starting your project
=====================

Create your Python environment::

    $ virtualenv env
    $ source env/bin/activate

If you are running multiple version of Python you will need to install your virtualenv with Python 3.4.1::

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

Local Environment Setup
=======================

When the codebase is deployed using Fabric, the environment is automatically detected based on the server type staging/production.
However, running a local version of the API requires you to set these environment variables yourself.

The fastest way is to create a file ``.env``
in the root directory (in the same folder as ``manage.py``) then add your variables to it.
You can get started by coping the settings from ``aws_fabric/config/vars_staging.env``,
and override as required.

If you required different settings you don't have to set a ``.env`` file.
Because settings use standard environment variables you can either ``export var=xyz`` in shell or create a
``.ssh`` script for each environment yourself i.e.``source yourvars.sh``



List of Fabric Commands
=======================

There are a number of convenient Fabric scrips available to facilitate code deployment and other server tasks.

**Note:** Local environment must be configured correctly to run Fabric tasks *(see local environment setup)*.


* ``fab staging/production instance`` - Creates an EC2 instance from an AMI and configures it based on template.
    * Creates new EC2 instance.
    * Updates OS.
    * Builds essential packages.
    * Deploy cloud API form release branch.
    * Installs API requirements.
    * Server Setup, Gunicorn, Nginx and ports.
    * Celery Setup.
    * Restarts all services.

* ``fab staging/production deploy`` - Deploys API codebase.
    * Deploy API form master(staging)/release branch. Creates a release zip.
    * Updates environment variables.
    * Restarts all services.

* ``fab staging/production celery_setup`` - Updates **Supervisor** and **Celery** processes from ``celery.conf``
    * Deploy engine form release branch.
    * Updates each Celery worker start process.
    * Restarts Supervisor and Celery worker on the server.

* ``fab staging/production environment_vars`` - Sets or Updates system environment variables.
* ``fab staging/production reload`` - Restarts services.
* ``fab staging/production update`` - Update OS site packages.
* ``fab staging/production requirements`` - Runs ``pip install`` requirements.txt.
* ``fab staging/production serversetup`` - Runs all the build server tasks.
* ``fab staging/production create_swap`` - Creates Swap Memory
