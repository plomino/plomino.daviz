Introduction
============

plomino.daviz offers services and utilities to get Plomino-base information from
Daviz more easily.

Features
========

Only one feature for now:

* overrides the eea.app.visualization ExternalData utility so query string parameters are passed to the called url.

Installation
============

Edit your ``buildout.cfg`` file and add the following in the ``eggs`` section::

    eggs =
         ...
         plomino.daviz

Then you have to run ``buildout`` to realize your configuration::

    bin/buildout -N

Credits
=======

Authors
-------

* Eric BREHAULT <eric.brehault@makina-corpus.org>

Companies
---------
|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_


.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
