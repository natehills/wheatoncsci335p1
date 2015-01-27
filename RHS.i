module RHS
%{
#include "RHS.h"
%}


class RHS{
public:
  RHS(false);
  bool nonZeroRHS(int testVarID);
  void addTerm(LinearTermPtr rhsTerm);
  void addTerm(VarPtr v);
  LinearTermPtr linearTerm();
  LinearTermPtr linearTermCopy();
}
