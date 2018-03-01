robotframework-jsonvalidator
============================

|Build Status|

Short Description
-----------------

`Robot Framework`_ library for JSON validation based on JSONSchema,
JSONPath, JSONSelect.

Additional Information
----------------------

-  `Json Schema`_
-  `Jsonschema generator`_
-  `JSONPath by Stefan Goessner`_
-  `JSONPath Tester`_
-  `JSONSelect`_
-  `JSONSelect Tester`_

Installation
------------

Install the library from PyPI using pip:

::

    pip install robotframework-jsonvalidator

Dependencies
------------

-  `jsonschema`_
-  `jsonpath-rw-ext`_
-  `objectpath`_
-  `pyjsonselect`_

Documentation
-------------

See keyword documentation for JsonValidator library on `GitHub`_.

Example
-------

*json_example.json*

::

    {
      "store": {
        "book": [
          {
            "category": "reference",
            "author": "Nigel Rees",
            "title": "Sayings of the Century",
            "price": 8.95
          },
          {
            "category": "fiction",
            "author": "Evelyn Waugh",
            "title": "Sword of Honour",
            "price": 12.99
          },
          {
            "category": "fiction",
            "author": "Herman Melville",
            "title": "Moby Dick",
            "isbn": "0-553-21311-3",
            "price": 8.99
          },
          {
            "category": "fiction",
            "author": "J. R. R. Tolkien",
            "title": "The Lord of the Rings",
            "isbn": "0-395-19395-8",
            "price": 22.99
          }
        ],
        "bicycle": {
          "color": "red",
          "price": 19.95
        }
      }
    }

Robot Framework test case:

.. code:: robotframework

    *** Settings ***
    Library    JsonValidator
    Library    OperatingSystem

    *** Test Cases ***
    Check Element
        ${json_example}=    OperatingSystem.Get File   ${CURDIR}${/}json_example.json
        Element should exist    ${json_example}    .author:contains("Evelyn Waugh")

License
-------

Apache License 2.0

.. _Robot Framework: http://www.robotframework.org
.. _Json Schema: http://json-schema.org/
.. _Jsonschema generator: http://www.jsonschema.net/
.. _JSONPath by Stefan Goessner: http://goessner.net/articles/JsonPath/
.. _JSONPath Tester: http://jsonpath.curiousconcept.com/
.. _JSONSelect: http://jsonselect.org/
.. _JSONSelect Tester: http://jsonselect.curiousconcept.com/
.. _jsonschema: https://pypi.python.org/pypi/jsonschema
.. _jsonpath-rw-ext: https://pypi.python.org/pypi/jsonpath-rw-ext
.. _objectpath: https://pypi.python.org/pypi/objectpath/
.. _pyjsonselect: https://pypi.python.org/pypi/pyjsonselect
.. _GitHub: https://github.com/peterservice-rnd/robotframework-jsonvalidator/tree/master/docs

.. |Build Status| image:: https://travis-ci.org/peterservice-rnd/robotframework-jsonvalidator.svg?branch=master
   :target: https://travis-ci.org/peterservice-rnd/robotframework-jsonvalidator
