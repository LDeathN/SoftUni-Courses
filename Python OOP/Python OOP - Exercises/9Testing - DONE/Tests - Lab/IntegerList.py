class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):

    def test_constructor_with_valid_integers(self):
        integers = [1, 2, 3, 4]
        integer_list = IntegerList(*integers)
        self.assertEqual(integer_list.get_data(), integers)

    def test_constructor_with_non_integer_raises_value_error(self):
        numbers = IntegerList(1, 2, "three", 4)
        self.assertEqual(numbers.get_data(), [1, 2, 4])

    def test_constructor_with_no_arguments(self):
        integer_list = IntegerList()
        self.assertEqual(integer_list.get_data(), [])

    def test_add_operation_with_integer(self):
        integer_list = IntegerList(1, 2, 3)
        result = integer_list.add(4)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_add_operation_with_non_integer_raises_value_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as context:
            integer_list.add("four")
        expected_message = "Element is not Integer"
        self.assertEqual(str(context.exception), expected_message)

    def test_remove_index_operation_with_valid_index(self):
        integer_list = IntegerList(1, 2, 3, 4)
        result = integer_list.remove_index(1)
        self.assertEqual(result, 2)
        self.assertEqual(integer_list.get_data(), [1, 3, 4])

    def test_remove_index_operation_with_out_of_range_index_raises_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError) as context:
            integer_list.remove_index(10)
        expected_message = "Index is out of range"
        self.assertEqual(str(context.exception), expected_message)

    def test_get_operation_with_valid_index(self):
        integer_list = IntegerList(1, 2, 3, 4)
        result = integer_list.get(2)
        self.assertEqual(result, 3)

    def test_get_operation_with_out_of_range_index_raises_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError) as context:
            integer_list.get(10)
        expected_message = "Index is out of range"
        self.assertEqual(str(context.exception), expected_message)

    def test_insert_operation_with_valid_index_and_integer_element(self):
        integer_list = IntegerList(1, 2, 3)
        integer_list.insert(1, 4)
        self.assertEqual(integer_list.get_data(), [1, 4, 2, 3])

    def test_insert_operation_with_out_of_range_index_raises_index_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as context:
            integer_list.insert(5, 7)
        expected_message = "Index is out of range"
        self.assertEqual(str(context.exception), expected_message)

    def test_insert_operation_with_non_integer_element_raises_value_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as context:
            integer_list.insert(1, 3.5)
        expected_message = "Element is not Integer"
        self.assertEqual(str(context.exception), expected_message)

    def test_get_biggest_method(self):
        numbers = IntegerList(3, 5, -2, 10, 8)
        result = numbers.get_biggest()
        self.assertEqual(result, 10)

    def test_get_index_operation_with_valid_element(self):
        integer_list = IntegerList(1, 2, 3, 4)
        result = integer_list.get_index(3)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()



