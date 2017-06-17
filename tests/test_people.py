#!/usr/bin/env python

""" Unit tests for my classes """

import unittest

from employees import people as P

class TestPeopleMethods(unittest.TestCase):

    def setUp(self):
        self.worker = P.Worker('Abraham Aardvark', 'Engineer', 40000)
        self.manager = P.Manager('Molly Midge', 100000)

    def test_empty_department(self):
        team = P.Department()
        self.assertEqual(team.headCount(), 0)

    def test_grow_department(self):
        team = P.Department(self.worker)
        team.addMember(self.manager)
        self.assertEqual(team.headCount(), 2)

    @unittest.skip('TBD')
    def test_nothing(self):
        self.fail('To be fixed')

    def test_pay_rise(self):
        pass


if __name__ == '__main__':
    #unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPeopleMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
