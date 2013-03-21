android-lapse-sync
==================

A small python app to sync time lapse photos on my Android phone with Dropbox.

I received a bonsai tree for my birthday and thought it'd be cool to get some time lapse photos of as it grows.  Using [SL4A](https://code.google.com/p/android-scripting/), I wrote this python app to transfer the photos that the time lapse application was taking to my Dropbox account.

The OAuth client key & secret as well as the local directory is stored in a (non-committed) config.ini file in the same directory.

I'm using the official [Dropbox Python SDK](https://www.dropbox.com/developers/core/sdk), but had to make a change to the rest module becausd the Python interpreter that SL4A used didn't have pkg_resources from [setuptools](https://pypi.python.org/pypi/setuptools).
