from FunctionTest import *
import unittest

testSuite = unittest.makeSuite(FunctionTest)

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
