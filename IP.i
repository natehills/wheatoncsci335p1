%module IP
%{
#include "IP.h"
%}


class IP{
public:
  IP();
  void AddTerm(LinearTermPtr a);
  void AddTerm(VarPtr v);
  LinearTermPtr(VarPtr v);
}
