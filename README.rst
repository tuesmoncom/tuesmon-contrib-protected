=======================
tuesmon-contrib-protected
=======================

This package implements an alternative storage system for tuesmon.

This is a part of the system. To run it also needs:

- nginx with specific configuration

- and tuesmon-protected service as the backend to validate requests.


.. code::

    #########################################
    ## Media Static settings
    #########################################

    MEDIA_URL = "https://media-domain.example.com/"
    MEDIA_ROOT = "/path/to/media"
    DEFAULT_FILE_STORAGE = "tuesmon_contrib_protected.storage.ProtectedFileSystemStorage"


Vendoring
=========

How to update vendored libraries.

.. code::

   pip install -t tuesmon_contrib_protected/_vendor -r tuesmon_contrib_protected/_vendor/vendor.txt --no-compile --no-deps
   rm -rf tuesmon_contrib_protected/_vendor/*.dist-info
