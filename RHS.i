%module RHS
%{
#include "RHS.h"
%}


class RHS{
public:
  bool nonZeroRHS(int testVarID);
  void addTerm(LinearTermPtr rhsTerm);
  void addTerm(VarPtr v);
  LinearTermPtr linearTerm();
  LinearTermPtr linearTermCopy();
  
  %extend {
    RHS(){
     return  RHS(false);
    }
    //find out how to extend an exisiting class with a new constructor that calls an existing constructor.
  }

};
