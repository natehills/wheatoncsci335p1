from LinearTerm import *
import LinearTerm
import Function
import Var
import VarFactory
import unittest

class LinearTermTest(unittest.TestCase):
  """Test LinearTerm methods"""
  def testLinearTerm(self):
    lt = LinearTerm.LinearTerm()
    # checks if linearTerm is empty
    self.assertEqual(lt.rank(), -1)
    # write code to make VarPtr with VarType "test"
    varFact = VarFactory.VarFactory()
    test1 = varFact.fieldVar("x")
    test2 = varFact.fieldVar("y")
    self.assertEqual(test1.termType(), 'FIELD')


    #add overloads
    ltp = test1 + test2
    eval = ltp.evaluate( #var + var
    #add more stuff...
    test3 = varFact.fieldVar("2x")
    ltp2 = ltp + test3
    eval = ltp2.evaluate( #LinearTerm + Var
    #add more stuff...
    test4 = varFact.fieldVar("2y")
    ltp2 = test3 + test4
    ltp3 = ltp + ltp2
    eval = ltp3.evaluate( #LinearTerm + LinearTerm
    #add more stuff...
    ltp = test3 + ltp2
    eval = ltp.evaluate( #Var + LinearTerm
    #add more stuff...



    #Mul overloads
    funPtr = Function.Function_xn(2)
    ltp = funPtr * test3
    eval = ltp.eval(  #Function * Var
    #add more stuff...
    ltp = test3 * funPtr
    eval = ltp.eval(   #Var * Function
    #add more stuff...
    ltp = test3 * 2.0
    eval = ltp.eval(   #Var * Double
    #add more stuff...
    ltp = 2.0 * test3
    eval = ltp.eval(   # Double * Var
    #add more stuff...

    # dont know what to do with vector doubles

    ltp = test3 + test4
    ltp2 = funPtr * ltp
    eval = ltp2.eval(   # Function * LinearTerm


    #Div overloads
    ltp = test3 / 2.0
    eval = ltp.eval(   # Var / Double
    ltp = test3 / funPtr
    eval = ltp.eval(   # Var / function
    

    # Sub overloads
    ltp = test3 - test4
    eval = ltp.eval(  # Var - Var
    ltp = - test3
    eval = ltp.eval(  # - Var
    ltp2 = -ltp
    eval = ltp2.eval(  # - LinearTerm
    ltp = test3 + test4
    ltp2 = ltp - test3
    eval = ltp2.evaluate( # LinearTerm - Var
    ltp2 = ltp - test4
    eval = ltp2.evaluate( #Var - LinearTerm
    ltp2 = test1 + test2
    ltp3 = ltp - ltp2
    eval = ltp3.evaluate( #LinearTerm - LinearTerm







    
