# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Christopher Lenz
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

"""Thin abstraction layer over the different available modules for decoding
and encoding JSON data.

This module currently supports the following JSON modules:
 - ``simplejson``: http://code.google.com/p/simplejson/
 - ``cjson``: http://pypi.python.org/pypi/python-cjson
 - ``json``: This is the version of ``simplejson`` that is bundled with the
   Python standard library since version 2.6
   (see http://docs.python.org/library/json.html)

The default behavior is to use ``simplejson`` if installed, and otherwise
fallback to the standard library module. To explicitly tell CouchDB-Python
which module to use, invoke the `use()` function with the module name::

    from couchdb import json
    json.use('cjson')

In addition to choosing one of the above modules, you can also configure
CouchDB-Python to use custom decoding and encoding functions::

    from couchdb import json
    json.use(decode=my_decode, encode=my_encode)

"""

__all__ = ['decode', 'encode']

json = __import__('json', {}, {})
decode = lambda string, loads=json.loads: loads(string)
encode = lambda obj, dumps=json.dumps: \
         dumps(obj, allow_nan=False, ensure_ascii=True)
