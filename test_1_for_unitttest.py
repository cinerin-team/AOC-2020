from unittest import TestCase

import for_unitttest_1


class Test(TestCase):

    def test_read_to_array_int(self):
        test_object = for_unitttest_1.read_to_array_int("src_files/1test.txt")
        self.assertTrue(isinstance(test_object, list))
        self.assertIsInstance(test_object, list)
        self.assertEqual(len(test_object), 6)
        self.assertEqual(test_object, [1721, 979, 366, 299, 675, 1456])

    def test_part1(self):
        test_object = for_unitttest_1.part1(for_unitttest_1.read_to_array_int("src_files/1test.txt"))
        expected_value = 514579
        self.assertEqual(test_object, expected_value)

    def test_part2(self):
        test_object = for_unitttest_1.part2(for_unitttest_1.read_to_array_int("src_files/1test.txt"))
        expected_value = 241861950
        self.assertEqual(test_object, expected_value)
