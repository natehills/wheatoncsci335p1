from FunctionXNYNTest import *
from FunctionTestInstance import *
from FunctionDivTests import *
from FunctionAddTests import *
from FunctionSubTests import *
from FunctionMulTests import *
from IPTest import *
<<<<<<< HEAD
from LinearTermTest import *
=======
from RHSTest import *
>>>>>>> 9854e3e0065a282f50afd7fa2a67021daf2a8021
import unittest

testSuite = unittest.makeSuite(FunctionXNYNTest)
testSuite.addTest(unittest.makeSuite(FunctionTestInstance))
testSuite.addTest(unittest.makeSuite(FunctionDivTests))
testSuite.addTest(unittest.makeSuite(FunctionAddTests))
testSuite.addTest(unittest.makeSuite(FunctionSubTests))
testSuite.addTest(unittest.makeSuite(FunctionMulTests))
testSuite.addTest(unittest.makeSuite(IPTest))
<<<<<<< HEAD
testSuite.addTest(unittest.makeSuite(LinearTermTest))
=======
testSuite.addTest(unittest.makeSuite(RHSTest))

>>>>>>> 9854e3e0065a282f50afd7fa2a67021daf2a8021

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
