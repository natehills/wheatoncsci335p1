%module LinearTerm
%{
#include "LinearTerm.h"
%}

%include "std_string.i"
%include "std_map.i"
%include "std_set.i"
%include "Var.i"

namespace std {
%template(map_int_FunctionPtr) map<int, FunctionPtr>;
}

namespace std {
%template(set_int) set<int>;
}

using namespace Camellia;

class LinearTerm {
public:
  LinearTerm();
  const std::set<int> & varIDs();
  VarType termType();
  FunctionPtr evaluate(std::map< int, FunctionPtr> &varFunctions);
  int rank();
  string displayString();

 };

class LinearTermPtr{
public:
  LinearTerm* operator->();
 
  %extend {
    LinearTermPtr __add__(LinearTermPtr a){
      return *self + a;
    }

    LinearTermPtr __add__(VarPtr v){
      return *self + v;
    }

    /**LinearTermPtr __radd__(VarPtr v){
      return *self + v;
    }
    **/
    LinearTermPtr __rmul__(FunctionPtr f) {
      return f * *self ;
    }

    LinearTermPtr __neg__() { 
      return - *self;
    }

    LinearTermPtr __sub__(VarPtr v) { 
      return *self - v;
    }
    /**
    LinearTermPtr __rsub__(VarPtr v) { 
      return v - *self;
    }
    **/
    LinearTermPtr __sub__(LinearTermPtr a) { 
      return *self - a;
    }

  }

};
    //for FunctionPtr and VarPtr without linear term
    //add in the Function and Var .i files
    //VarPtr and double




