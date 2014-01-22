import unittest
from BrainTest import BrainTest
from JudgeTest import JudgeTest
from BoardTest import BoardTest

suite1 = unittest.TestLoader().loadTestsFromTestCase(BrainTest)
suite2 = unittest.TestLoader().loadTestsFromTestCase(JudgeTest)
suite3 = unittest.TestLoader().loadTestsFromTestCase(BoardTest)

tests = [suite1, suite2, suite3]
alltests = unittest.TestSuite(tests)
unittest.TextTestRunner(verbosity=2).run(alltests)
