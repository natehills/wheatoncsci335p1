from FunctionXNYNTest import *
from FunctionDivTests import *
from FunctionAddTests import *
from FunctionSubTests import *
from FunctionMulTests import *
import unittest

testSuite = unittest.makeSuite(FunctionXNYNTest)
testSuite.addTest(unittest.makeSuite(FunctionDivTests))
testSuite.addTest(unittest.makeSuite(FunctionAddTests))
testSuite.addTest(unittest.makeSuite(FunctionSubTests))
testSuite.addTest(unittest.makeSuite(FunctionMulTests))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
