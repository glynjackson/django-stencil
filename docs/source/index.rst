=====
Django Stencil Template
=====

-----------------------------------
What is Django Stencil?
-----------------------------------

Django Stencil is a boilerplate template for Django 1.7+ running Python 3.4.1
It has been build from our experience in deploying rapid applications and draws on
the methodologies used on projects with both Samsung and HTC.

.. attention::
    Everyone has there own way of structuring a project and Django Stencil will not meet everyones requirements.
    The template is very much based on our own opinions and experiences.

It has been designed to deploy on Amazon Web Services and includes some useful tools/tasks to aid with this, such as:

* AWS deployment
* ELB ``ALLOWED_HOSTS`` fix

If you are not planning on deploying on AWS then the template is still
very useful and provides a very good foundation to get you up and running fast.

First steps
===========
.. toctree::
    :maxdepth: 1

    getting_started/getting_started


AWS Deployment
===============

.. toctree::
    :maxdepth: 1

    aws/tasks
    aws/allowed_hosts