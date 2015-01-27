%module LinearTerm
%{
#include "LinearTerm.h"
%}

%include "std_string.i"

class LinearTerm{
public:
  void LinearTerm();
  const set<int> & varIDs();
  VarType termType();
  FunctionPtr evaluate(map< int, FunctionPtr> &varFunctions);
  int Rank();
  string displayString();

}

class LinerTermPtr{
public:
  LinearTerm* operator->();

  %extend {
    LinearTermPtr __add__(LinearTermPtr a){
      return *self + a;
    }

    LinearTermPtr __add__(VarPtr v){
      return *self + v;
    }

    LinearTermPtr __radd__(VarPtr v){
      return *self + v;
    }

    LinearTermPtr __rmul__(FunctionPtr f) {
      return *self * f;
    }

    LinearTermPtr __sub__() { 
      return - *self;
    }

    LinearTermPtr __sub__(VarPtr v) { 
      return *self - v;
    }

    LinearTermPtr __rsub__(VarPtr v) { 
      return v - *self;
    }

    LinearTermPtr __sub__(LinearTermPtr a) { 
      return *self - a;
    }

  }
}
    //for FunctionPtr and VarPtr without linear term
    //add in the Function and Var .i files
    //VarPtr and double




