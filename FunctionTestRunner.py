from FunctionXNYNTest import *
from FunctionTestInstance import *
import unittest

testSuite = unittest.makeSuite(FunctionXNYNTest)
testSuite.addTest(unittest.makeSuite(FunctionTestInstance))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
