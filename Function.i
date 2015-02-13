%module Function
%{
#include "Function.h"
#include "Mesh.h"
%}

%include "std_string.i"
%include "std_vector.i"
%include "Solution.i"

namespace std {
  %template(DoubleVector) vector<double>;
}


%nodefaultctor Function;  // Disable the default constructor for class Function

class Function {
public:
  std::string displayString();
  double evaluate(double x);
  double evaluate(double x, double y);
  double evaluate(double x, double y, double z);
  
  virtual FunctionPtr x(); 
  virtual FunctionPtr y();

  // member functions for taking derivatives:
  virtual FunctionPtr dx();
  virtual FunctionPtr dy();
  
  virtual FunctionPtr div();
  virtual FunctionPtr grad();

  int rank();
  double l2norm(MeshPtr mesh, int cubatureDegreeEnrichment = 0);
  
  // static methods:
  static double evaluate(FunctionPtr f, double x, double y); 
  
  static FunctionPtr xn(int n=1); // NOTE: important to have "FunctionPtr" here exactly as below; "Teuchos::RCP<Function>", though equivalent in C++, is not equivalent for SWIG
  static FunctionPtr yn(int n=1);
  static FunctionPtr composedFunction( FunctionPtr f, FunctionPtr arg_g);
  static FunctionPtr constant(double value);
  static FunctionPtr constant(vector<double> &value);
  static FunctionPtr vectorize(FunctionPtr f1, FunctionPtr f2);
  static FunctionPtr normal();
  static FunctionPtr solution(VarPtr var, SolutionPtr soln);

  // SWIG/Python extensions:
  %extend {
    std::string __str__() {
      return self->displayString();
    }
  }
};

//FunctionPtr operator*(double weight, FunctionPtr f);

class FunctionPtr {
public:
  Function* operator->();

  %extend {
    FunctionPtr __add__(FunctionPtr f2) {
      return *self + f2;
    }
    FunctionPtr __add__(double value) {
      return *self + value;
    }
    FunctionPtr __radd__(double value) {
      return *self + value;
    }
    FunctionPtr __mul__(double value) {
      return *self * value;
    }
    FunctionPtr __rmul__(double value) {
      return *self * value;
    }
    FunctionPtr __mul__(FunctionPtr f2) {
      return *self *  f2;
    }
    FunctionPtr __mul__(vector<double> weight) {
      return *self *  weight;
    }
    FunctionPtr __rmul__(vector<double> weight) {
      return *self * weight;
    }
    FunctionPtr __div__(FunctionPtr scalarDivision) {
      return *self / scalarDivision;
    }
    FunctionPtr __div__(double divisor) {
      return *self / divisor;
    }
    FunctionPtr __rdiv__(double divisor) {
      return divisor / *self;
    }
    FunctionPtr __sub__(FunctionPtr f2) {
      return *self - f2;
    }
    FunctionPtr __sub__(double value) {
      return *self - value;
    }
    FunctionPtr __rsub__(double value) {
      return value - *self;
    }
    FunctionPtr __neg__() {
      return - *self;
    }

    LinearTermPtr __mul__(VarPtr v) {
      return *self * v;
    }

    LinearTermPtr __rmul__(VarPtr v) {
      return *self * v;
    }

  }
};
