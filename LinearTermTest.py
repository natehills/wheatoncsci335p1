from LinearTerm import *
import LinearTerm
import Function
import Var
import VarFactory
import Mesh
import MeshFactory
import unittest

class LinearTermTest(unittest.TestCase):
  """Test LinearTerm methods"""
  def testLinearTerm(self):
    lt = LinearTerm.LinearTerm()
    # checks if linearTerm is empty
    self.assertEqual(lt.rank(), -1)
    varFact = VarFactory.VarFactory()
    test1 = varFact.fieldVar("x")
    test2 = varFact.fieldVar("y")

    test3 = varFact.fieldVar("2x")
    test4 = varFact.fieldVar("2y")
    ltp = test1 + test2
    str = ' x +  y'
    self.assertEqual(str, ltp.displayString())
    self.assertEqual(ltp.rank(),0)
    bool = (ltp.termType() == Var.FIELD)
    self.assertTrue(bool)
    #self.assertEqual(ltp.termType(), Var.FIELD)

    varFunctions = LinearTerm.map_int_FunctionPtr({test1.ID(): Function.Function_xn(1), test2.ID(): Function.Function_yn(1), test3.ID(): Function.Function_xn(1) * 2, test4.ID(): Function.Function_yn(1) * 2})
    varID = (test1.ID(), test2.ID())

    #add overloads
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    self.assertEqual(ltp.varIDs(), varID) # tests varIDs()
    #var + var (x+y)
    ltp2 = ltp + test3
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 4.0)
    #LinearTerm + Var (x + y + 2x)
    ltp2 = test3 + test4
    ltp3 = ltp + ltp2
    eval = ltp3.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 6.0)
    #LinearTerm + LinearTerm (x + y + 2x + 2y)
    ltp = test3 + ltp2
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 6.0)
    #Var + LinearTerm (2x + 2x + 2y)


    #Mul overloads
    funPtr = Function.Function_xn(2)
    ltp = funPtr * test3
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(3,1), 54.0)
    #Function * Var 2x*x^2
    ltp = test3 * funPtr
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(2,1), 16.0)
    #Var * Function 2x*x^2
    ltp = test3 * 2.0
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 4.0)
    #Var * Double   2x * 2
    ltp = 2.0 * test3
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 4.0)
    # Double * Var   2x * 2

    doubV = [1.0, 1.0]
    ltp = test1 * doubV
    self.assertEqual(ltp.rank(),1)
    eval = ltp.evaluate(varFunctions) #gives vector-valued function
    x = eval.x()
    y = eval.y()
    self.assertEqual(x.evaluate(2,1), 2.0)
    self.assertEqual(x.evaluate(5,3), 5.0)
    ltp = doubV * test1
    eval = ltp.evaluate(varFunctions)
    x = eval.x()
    y = eval.y()
    self.assertEqual(x.evaluate(2,1), 2.0)
    self.assertEqual(x.evaluate(4,3), 4.0)

    ltp = test3 + test4
    ltp2 = funPtr * ltp
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(2,4), 48.0)
    # Function * LinearTerm  x^2 * (2x + 2y)


    #Div overloads
    ltp = test3 / 2.0
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,0), 1.0)
    # Var / Double  2x/2
    ltp = test3 / funPtr
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,0), 2.0)
    # Var / function  2x/(x^2)
    

    # Sub overloads
    ltp = test3 - test4
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(4,1), 6.0)
    # Var - Var 2x - 2y
    ltp = - test3
    eval = ltp.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), -2.0)
    # - Var  -2x
    ltp2 = -ltp
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    # - LinearTerm  -(-2x)
    ltp = test3 + test4
    ltp2 = ltp - test3
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    # LinearTerm - Var   (2x + 2y) - 2x
    ltp2 = test4 - ltp
    eval = ltp2.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), -2.0)
    #Var - LinearTerm    2y - (2x + 2y)
    ltp2 = test1 + test2
    ltp3 = ltp - ltp2
    eval = ltp3.evaluate(varFunctions)
    self.assertEqual(eval.evaluate(1,1), 2.0)
    #LinearTerm - LinearTerm  (2x + 2y)-(x+y)







    
