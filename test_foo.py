import time
from unittest import TestCase

import foo


class TestFoo(TestCase):
    def test_generate_numbers_one_to_100(self):
        self.assertEqual(list(range(1, 100)), foo.generate_numbers_one_to_100())

    def test_generate_numbers_one_to_100_except_multiples_of_5(self):
        generated_numbers = foo.generate_numbers_one_to_100_except_multiples_of_5()
        self.assertEqual(len(generated_numbers), 81)
        self.assertEqual(generated_numbers[:5], [1, 2, 3, 4, 6])

    def test_speed_of_generation(self):
        start = time.time()
        for iteration_count in range(500000):
            foo.generate_numbers_one_to_100_except_multiples_of_5()
        end = time.time()
        self.assertLess(end - start, 8)
