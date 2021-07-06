from HashTable import HashArray, Element
import unittest


class MyTestCase(unittest.TestCase):
    def test_hash_table(self):
        arr = HashArray(size=13)
        arr.insert(Element(1, "one"))
        arr.insert(Element(2, "two"))
        arr.insert(Element(3, "three"))
        arr.insert(Element(4, "four"))
        arr.insert(Element(5, "five"))
        arr.insert(Element(18, "eighteen"))
        arr.insert(Element(31, "thirty one"))
        arr.insert(Element(8, "eight"))
        arr.insert(Element(9, "nine"))
        arr.insert(Element(10, "ten"))
        arr.insert(Element(11, "eleven"))
        arr.insert(Element(12, "twelve"))
        arr.insert(Element(13, "thirteen"))
        with self.assertRaises(ValueError):
            arr.insert(Element(14, "fourteen"))
        self.assertEqual(arr.search(5), 'five')
        self.assertEqual(arr.search(14), None)
        arr.insert(Element(5, "new_five"))
        self.assertEqual(arr.search(5), 'new_five')
        arr.remove(5)
        self.assertEqual(arr.search(5), None)
        arr.insert(Element("test", "A"))
        self.assertEqual(arr.search("test"), "A")


if __name__ == '__main__':
    unittest.main()
