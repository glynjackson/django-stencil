======================================================
Starting your project
======================================================

Create your Python environment::

    $ virtualenv env
    $ source env/bin/activate

If you are multiple version of Python you will need to install your virtualenv with Python 3.4::

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
