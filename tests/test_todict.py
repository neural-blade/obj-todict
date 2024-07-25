import unittest
from src.obj_todict import todict


class TestToDict(unittest.TestCase):

    def test_dict(self):
        input_data = {'a': 1, 'b': {'c': 2}}
        expected_output = {'a': 1, 'b': {'c': 2}}
        self.assertEqual(todict(input_data), expected_output)

    def test_list(self):
        input_data = [1, {'a': 2}, [3, 4]]
        expected_output = [1, {'a': 2}, [3, 4]]
        self.assertEqual(todict(input_data), expected_output)

    def test_tuple(self):
        input_data = (1, {'a': 2}, (3, 4))
        expected_output = [1, {'a': 2}, [3, 4]]
        self.assertEqual(todict(input_data), expected_output)

    def test_set(self):
        input_data = {1, 2, 3}
        expected_output = [1, 2, 3]
        result = todict(input_data)
        self.assertCountEqual(result, expected_output)

    def test_object(self):
        class Test:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        obj = Test(1, {'a': 2})
        expected_output = {'x': 1, 'y': {'a': 2}}
        self.assertEqual(todict(obj), expected_output)

    def test_nested_structures(self):
        class Nested:
            def __init__(self, name, values):
                self.name = name
                self.values = values

        class Container:
            def __init__(self, items):
                self.items = items

        nested_obj = Nested('example', [1, {'key': 'value'}, (2, 3)])
        container = Container([nested_obj, {'another_key': 4}])

        expected_output = {
            'items': [
                {'name': 'example', 'values': [1, {'key': 'value'}, [2, 3]]},
                {'another_key': 4}
            ]
        }
        self.assertEqual(todict(container), expected_output)

    def test_non_recursive(self):
        self.assertEqual(todict(1), 1)
        self.assertEqual(todict("string"), "string")
        self.assertEqual(todict(3.14), 3.14)
        self.assertEqual(todict(None), None)


if __name__ == '__main__':
    unittest.main()
