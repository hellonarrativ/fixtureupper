from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.utils import iteritems

from unittest import TestCase

from fixtureupper.register import UpperRegister

class TestModelFixtureUpper(TestCase):
    def setUp(self):
        self.ModelFixtureUpper = UpperRegister('Model')

    def test_sorted_by_generated_order(self):
        self.ModelFixtureUpper.generated_field_order = ['a', 'z', 'c', 'b', 'd']
        m_fu = self.ModelFixtureUpper()
        result = [v for k, v in m_fu.sorted_by_generated_order({
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'z': 7,
        })]
        self.assertEqual(result[:5], [1, 7, 3, 2, 4])