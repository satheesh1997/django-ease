========
Overview
========
The decore package should be installed properly in the current python environment to import and use it inside a Django app.


Supported versions
******************
The following python versions are currently supported by this package

* 3.6
* 3.7
* 3.8

The below are the Django versions that are currently supported by this package

* 2.2
* 3.3

Package installation
**********************
**decore** package can be installed from the PyPi server directly into any of the supported python environments using,

.. code-block:: console

   $ pip install django-easy

Once the above command is completed you can check if the package is installed properly using,

.. code-block:: console

   $ python -m "import decore"

the above command should give the below exception in your python shell

.. code-block:: python

   django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

if you get ModuleNotFoundError, this means that django_easy is not installed properly in your environment.