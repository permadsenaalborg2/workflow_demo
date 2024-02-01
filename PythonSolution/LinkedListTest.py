import unittest
from LinkedList import LinkedList
from LinkedList import Element


class TestElement(unittest.TestCase):

    def setUp(self):
        print("Running test ...")

    def tearDown(self):
        print("Done!")

    def test_constructor_elemString(self):
        el = Element('Per')
        self.assertIsNotNone(el)

    def test_constructor_elemInteger(self):
        el = Element(37)
        self.assertIsNotNone(el)

    def test_compare(self):

        # test that 465 is greater than 37
        el1 = Element(37)
        el2 = Element(465)
        self.assertFalse(el1.is_greater(el2))
        self.assertTrue(el2.is_greater(el1))

        # test that Hund is greater than Abe
        el1 = Element('Abe')
        el2 = Element('Hund')
        self.assertFalse(el1.is_greater(el2))
        self.assertTrue(el2.is_greater(el1))

        # test that Hund is greater than 37
        el1 = Element(37)
        el2 = Element('Hund')
        self.assertFalse(el1.is_greater(el2))
        self.assertTrue(el2.is_greater(el1))


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        print("Running test ...")

    def tearDown(self):
        print("Done!")

    def test_constructor_list(self):
        ll = LinkedList()
        self.assertIsNotNone(ll)

    def test_addToEmpty(self):
        ll = LinkedList()
        self.assertEqual(ll.count(), 0)
        ll.add_first(37)
        self.assertIsNotNone(ll)
        self.assertEqual(ll.count(), 1)

    def test_addToNonEmpty(self):
        ll = LinkedList()
        self.assertEqual(ll.count(), 0)
        ll.add_first(37)
        ll.add_first(65)
        self.assertIsNotNone(ll)
        self.assertEqual(ll.count(), 2)

    def test_addMany(self):
        ll = LinkedList()
        for t in range(1000):
            ll.add_first(t)
        self.assertEqual(ll.count(), 1000)

    def test_removeFromEmpty(self):
        """Test that calling remove_first on an empty list do not crash"""
        ll = LinkedList()
        ll.remove_first()
        self.assertIsNotNone(ll)

    def test_removeNonEmpty(self):
        ll = LinkedList()
        ll.add_first(37)
        ll.remove_first()
        self.assertIsNotNone(ll)

    def test_basis(self):
        ll = LinkedList()

        ll.add_first(86)
        ll.add_first(90)
        ll.add_first(34)
        ll.add_first(67)
        ll.add_first(46)
        self.assertEqual(ll.count(), 5)

    def test_sort(self):
        val1 = 67
        val2 = 334
        val3 = 23

        ll = LinkedList()
        ll.add_first(val1)
        ll.add_first(val2)
        ll.add_first(val3)
        self.assertEqual(ll.count(), 3)
        self.assertEqual(ll.get_first(), val3)

        ll.sort()
        self.assertEqual(ll.count(), 3)
        self.assertEqual(ll.get_first(), val3)
        ll.remove_first()
        self.assertEqual(ll.get_first(), val1)
        ll.remove_first()
        self.assertEqual(ll.get_first(), val2)
        ll.remove_first()
        self.assertIsNone(ll.get_first())

    def test_sortEmpty(self):
        ll = LinkedList()
        ll.sort()
        self.assertIsNotNone(ll)

    def test_sort_mixed_types(self):
        val1 = 67
        val2 = 'Per'
        val3 = 23

        ll = LinkedList()
        ll.add_first(val1)
        ll.add_first(val2)
        ll.add_first(val3)
        self.assertEqual(ll.count(), 3)
        self.assertEqual(ll.get_first(), val3)

        ll.sort()
        self.assertEqual(ll.count(), 3)
        self.assertEqual(ll.get_first(), val3)
        ll.remove_first()
        self.assertEqual(ll.get_first(), val1)
        ll.remove_first()
        self.assertEqual(ll.get_first(), val2)
        ll.remove_first()
        self.assertIsNone(ll.get_first())

    def test_remove_one(self):
        ll = LinkedList()
        self.assertEqual(ll.count(), 0)
        ll.add_first("Per")
        self.assertEqual(ll.count(), 1)
        self.assertEqual(ll.get_first(), "Per")
        ll.remove_first()
        self.assertEqual(ll.count(), 0)
        self.assertTrue(ll.get_first() is None)

    def test_remove_three(self):
        ll = LinkedList()
        self.assertEqual(ll.count(), 0)
        ll.add_first(34)
        ll.add_first(67)
        ll.add_first(456)
        self.assertEqual(ll.count(), 3)
        self.assertEqual(ll.get_first(), 456)
        ll.remove_first()
        self.assertEqual(ll.count(), 2)
        self.assertEqual(ll.get_first(), 67)
        ll.remove_first()
        self.assertEqual(ll.count(), 1)
        self.assertEqual(ll.get_first(), 34)
        ll.remove_first()
        self.assertEqual(ll.count(), 0)
        self.assertTrue(ll.get_first() is None)
        ll.remove_first()
        self.assertEqual(ll.count(), 0)
        self.assertTrue(ll.get_first() is None)


if __name__ == '__main__':
    unittest.main()
