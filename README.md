# robotframework-jsonvalidator

Robot Framework library for JSON validating based on JSONSchema, JSONPath, JSONSelect.

## Additional Information

- [Json Schema](http://json-schema.org/)
- [Jsonschema generator](http://www.jsonschema.net/)
- [JSONPath by Stefan Goessner](http://goessner.net/articles/JsonPath/)
- [JSONPath Tester](http://jsonpath.curiousconcept.com/)
- [JSONSelect](http://jsonselect.org/)
- [JSONSelect Tester](http://jsonselect.curiousconcept.com/)

## Dependencies

- [jsonschema](https://pypi.python.org/pypi/jsonschema)
- [jsonpath-rw-ext](https://pypi.python.org/pypi/jsonpath-rw-ext)
- [objectpath](https://pypi.python.org/pypi/objectpath/)
- [pyjsonselect](https://pypi.python.org/pypi/pyjsonselect)

## Documentation

See keyword documentation for JsonValidator library on [GitHub](https://github.com/peterservice-rnd/robotframework-jsonvalidator/tree/master/docs).

## Example

*json_example.json*
```
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
```

Robot Framework test case:

```robot
*** Settings ***
Library    JsonValidator
Library    OperatingSystem

*** Test Cases ***
Check Element
    ${json_example}=    OperatingSystem.Get File   ${CURDIR}${/}json_example.json
    Element should exist    ${json_example}    .author:contains("Evelyn Waugh")
```

## License

Apache License 2.0
