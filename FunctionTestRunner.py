from FunctionXNYNTest import *
import unittest

testSuite = unittest.makeSuite(FunctionXNYNTest)

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
