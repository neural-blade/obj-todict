# Object To Dictionary

`obj-todict` is a simple utility to recursively convert objects to dictionaries. This can be particularly useful for serializing complex nested objects into JSON-compatible dictionaries.

## Features

- Recursively converts objects, including nested lists and dictionaries, into dictionaries.
- Handles custom objects by converting their `__dict__` attributes.

## Installation

You can install the package using pip:

```bash
pip install obj-todict
```

# Usage

Here's a quick example to get you started:

```python
from obj_todict import todict

class Example:
    def __init__(self, name, value):
        self.name = name
        self.value = value

example = Example('example', [1, 2, {'key': 'value'}])
print(todict(example))
```

# License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/neural-blade/obj-todict/tree/main?tab=MIT-1-ov-file#MIT-1-ov-file) file for more details.
