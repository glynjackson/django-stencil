======================================================
Fabric Tasks
======================================================


Django Stencil comes with a powerful yet flexible set of fabric tasks.


    - fab local setupwizard
        - Creates configuration and connection settings to AWS for first time use.
          Adds the new host to the hostfile for production environment.

     - fab production instance
        - Creates a new EC2 instance form a blank AMI image. Instance will be setup based on your server template.

    - fab production serversetup
        - Runs and configures server software and services i.e. Gunicorn, Supervisor and Nginx.

    - fab production deploy
        - Pulls the latest commit from the master branch locally and zips up a release. deploys files to server,
          collects the static files, syncs the db and restarts services.

    - fab production update
        - Updates/Installs OS site packages.

    - fab production requirements
        - Runs the pip installs all requirements.txt command

    - fab production static
        - Runs the collectstatic command.

    - fab production sync
        - Runs syncdb or migration tasks against a database.

    - fab production reboot
        - Reboots a EC2 instance.2

    - fab production createsuperuser
        - Creates a new superuser against a database.


These fabric tasks have been design to allow flexibility using Django Stancil's environment templates which define the server environment such tasks are run against.

Environment templates allow any of the available fabric tasks to be run against a predefined AMI on Amazon. Each template can be written for a particular Linux distro and server set-up.

Out-of-the-box Django Stencil’s includes one environment template (Ubuntu14)  which can be run against a blank AMI running Ubuntu 14. However, its easy to add your own template.
