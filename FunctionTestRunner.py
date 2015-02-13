from FunctionXNYNTest import *
from FunctionTestInstance import *
from FunctionDivTests import *
from FunctionAddTests import *
from FunctionSubTests import *
from FunctionMulTests import *
from IPTest import *

from LinearTermTest import *

from RHSTest import *

import unittest

testSuite = unittest.makeSuite(FunctionXNYNTest)
testSuite.addTest(unittest.makeSuite(FunctionTestInstance))
testSuite.addTest(unittest.makeSuite(FunctionDivTests))
testSuite.addTest(unittest.makeSuite(FunctionAddTests))
testSuite.addTest(unittest.makeSuite(FunctionSubTests))
testSuite.addTest(unittest.makeSuite(FunctionMulTests))
testSuite.addTest(unittest.makeSuite(IPTest))
testSuite.addTest(unittest.makeSuite(LinearTermTest))
testSuite.addTest(unittest.makeSuite(RHSTest))


testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
