# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Solution', [dirname(__file__)])
        except ImportError:
            import _Solution
            return _Solution
        if fp is not None:
            try:
                _mod = imp.load_module('_Solution', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Solution = swig_import_helper()
    del swig_import_helper
else:
    import _Solution
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Solution.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _Solution.SwigPyIterator_value(self)
    def incr(self, n=1): return _Solution.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _Solution.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _Solution.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _Solution.SwigPyIterator_equal(self, *args)
    def copy(self): return _Solution.SwigPyIterator_copy(self)
    def next(self): return _Solution.SwigPyIterator_next(self)
    def __next__(self): return _Solution.SwigPyIterator___next__(self)
    def previous(self): return _Solution.SwigPyIterator_previous(self)
    def advance(self, *args): return _Solution.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _Solution.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _Solution.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _Solution.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _Solution.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _Solution.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _Solution.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _Solution.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class SetInt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SetInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SetInt, name)
    __repr__ = _swig_repr
    def iterator(self): return _Solution.SetInt_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _Solution.SetInt___nonzero__(self)
    def __bool__(self): return _Solution.SetInt___bool__(self)
    def __len__(self): return _Solution.SetInt___len__(self)
    def append(self, *args): return _Solution.SetInt_append(self, *args)
    def __contains__(self, *args): return _Solution.SetInt___contains__(self, *args)
    def __getitem__(self, *args): return _Solution.SetInt___getitem__(self, *args)
    def add(self, *args): return _Solution.SetInt_add(self, *args)
    def discard(self, *args): return _Solution.SetInt_discard(self, *args)
    def __init__(self, *args): 
        this = _Solution.new_SetInt(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _Solution.SetInt_empty(self)
    def size(self): return _Solution.SetInt_size(self)
    def clear(self): return _Solution.SetInt_clear(self)
    def swap(self, *args): return _Solution.SetInt_swap(self, *args)
    def count(self, *args): return _Solution.SetInt_count(self, *args)
    def begin(self): return _Solution.SetInt_begin(self)
    def end(self): return _Solution.SetInt_end(self)
    def rbegin(self): return _Solution.SetInt_rbegin(self)
    def rend(self): return _Solution.SetInt_rend(self)
    def erase(self, *args): return _Solution.SetInt_erase(self, *args)
    def find(self, *args): return _Solution.SetInt_find(self, *args)
    def lower_bound(self, *args): return _Solution.SetInt_lower_bound(self, *args)
    def upper_bound(self, *args): return _Solution.SetInt_upper_bound(self, *args)
    def equal_range(self, *args): return _Solution.SetInt_equal_range(self, *args)
    def insert(self, *args): return _Solution.SetInt_insert(self, *args)
    __swig_destroy__ = _Solution.delete_SetInt
    __del__ = lambda self : None;
SetInt_swigregister = _Solution.SetInt_swigregister
SetInt_swigregister(SetInt)

class MapIntToFunction(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MapIntToFunction, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MapIntToFunction, name)
    __repr__ = _swig_repr
    def iterator(self): return _Solution.MapIntToFunction_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _Solution.MapIntToFunction___nonzero__(self)
    def __bool__(self): return _Solution.MapIntToFunction___bool__(self)
    def __len__(self): return _Solution.MapIntToFunction___len__(self)
    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args): return _Solution.MapIntToFunction___getitem__(self, *args)
    def __delitem__(self, *args): return _Solution.MapIntToFunction___delitem__(self, *args)
    def has_key(self, *args): return _Solution.MapIntToFunction_has_key(self, *args)
    def keys(self): return _Solution.MapIntToFunction_keys(self)
    def values(self): return _Solution.MapIntToFunction_values(self)
    def items(self): return _Solution.MapIntToFunction_items(self)
    def __contains__(self, *args): return _Solution.MapIntToFunction___contains__(self, *args)
    def key_iterator(self): return _Solution.MapIntToFunction_key_iterator(self)
    def value_iterator(self): return _Solution.MapIntToFunction_value_iterator(self)
    def __setitem__(self, *args): return _Solution.MapIntToFunction___setitem__(self, *args)
    def asdict(self): return _Solution.MapIntToFunction_asdict(self)
    def __init__(self, *args): 
        this = _Solution.new_MapIntToFunction(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _Solution.MapIntToFunction_empty(self)
    def size(self): return _Solution.MapIntToFunction_size(self)
    def clear(self): return _Solution.MapIntToFunction_clear(self)
    def swap(self, *args): return _Solution.MapIntToFunction_swap(self, *args)
    def get_allocator(self): return _Solution.MapIntToFunction_get_allocator(self)
    def begin(self): return _Solution.MapIntToFunction_begin(self)
    def end(self): return _Solution.MapIntToFunction_end(self)
    def rbegin(self): return _Solution.MapIntToFunction_rbegin(self)
    def rend(self): return _Solution.MapIntToFunction_rend(self)
    def count(self, *args): return _Solution.MapIntToFunction_count(self, *args)
    def erase(self, *args): return _Solution.MapIntToFunction_erase(self, *args)
    def find(self, *args): return _Solution.MapIntToFunction_find(self, *args)
    def lower_bound(self, *args): return _Solution.MapIntToFunction_lower_bound(self, *args)
    def upper_bound(self, *args): return _Solution.MapIntToFunction_upper_bound(self, *args)
    __swig_destroy__ = _Solution.delete_MapIntToFunction
    __del__ = lambda self : None;
MapIntToFunction_swigregister = _Solution.MapIntToFunction_swigregister
MapIntToFunction_swigregister(MapIntToFunction)

class Solution(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solution, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Solution, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Solution.new_Solution(*args)
        try: self.this.append(this)
        except: self.this = this
    def solve(self): return _Solution.Solution_solve(self)
    def addSolution(self, *args): return _Solution.Solution_addSolution(self, *args)
    def clear(self): return _Solution.Solution_clear(self)
    def cubatureEnrichmentDegree(self): return _Solution.Solution_cubatureEnrichmentDegree(self)
    def setCubatureEnrichmentDegree(self, *args): return _Solution.Solution_setCubatureEnrichmentDegree(self, *args)
    def L2NormOfSolution(self, *args): return _Solution.Solution_L2NormOfSolution(self, *args)
    def projectOntoMesh(self, *args): return _Solution.Solution_projectOntoMesh(self, *args)
    def energyErrorTotal(self): return _Solution.Solution_energyErrorTotal(self)
    def setWriteMatrixToFile(self, *args): return _Solution.Solution_setWriteMatrixToFile(self, *args)
    def setWriteMatrixToMatrixMarketFile(self, *args): return _Solution.Solution_setWriteMatrixToMatrixMarketFile(self, *args)
    def setWriteRHSToMatrixMarketFile(self, *args): return _Solution.Solution_setWriteRHSToMatrixMarketFile(self, *args)
    def mesh(self): return _Solution.Solution_mesh(self)
    def bc(self): return _Solution.Solution_bc(self)
    def rhs(self): return _Solution.Solution_rhs(self)
    def ip(self): return _Solution.Solution_ip(self)
    def setBC(self, *args): return _Solution.Solution_setBC(self, *args)
    def setRHS(self, *args): return _Solution.Solution_setRHS(self, *args)
    def setIP(self, *args): return _Solution.Solution_setIP(self, *args)
    def save(self, *args): return _Solution.Solution_save(self, *args)
    __swig_getmethods__["load"] = lambda x: _Solution.Solution_load
    if _newclass:load = staticmethod(_Solution.Solution_load)
    def saveToHDF5(self, *args): return _Solution.Solution_saveToHDF5(self, *args)
    def loadFromHDF5(self, *args): return _Solution.Solution_loadFromHDF5(self, *args)
    def setUseCondensedSolve(self, *args): return _Solution.Solution_setUseCondensedSolve(self, *args)
    __swig_getmethods__["solution"] = lambda x: _Solution.Solution_solution
    if _newclass:solution = staticmethod(_Solution.Solution_solution)
    __swig_destroy__ = _Solution.delete_Solution
    __del__ = lambda self : None;
Solution_swigregister = _Solution.Solution_swigregister
Solution_swigregister(Solution)

def Solution_load(*args):
  return _Solution.Solution_load(*args)
Solution_load = _Solution.Solution_load

def Solution_solution(*args):
  return _Solution.Solution_solution(*args)
Solution_solution = _Solution.Solution_solution

class SolutionPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SolutionPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SolutionPtr, name)
    __repr__ = _swig_repr
    def __deref__(self): return _Solution.SolutionPtr___deref__(self)
    def __init__(self): 
        this = _Solution.new_SolutionPtr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Solution.delete_SolutionPtr
    __del__ = lambda self : None;
    def solve(self): return _Solution.SolutionPtr_solve(self)
    def addSolution(self, *args): return _Solution.SolutionPtr_addSolution(self, *args)
    def clear(self): return _Solution.SolutionPtr_clear(self)
    def cubatureEnrichmentDegree(self): return _Solution.SolutionPtr_cubatureEnrichmentDegree(self)
    def setCubatureEnrichmentDegree(self, *args): return _Solution.SolutionPtr_setCubatureEnrichmentDegree(self, *args)
    def L2NormOfSolution(self, *args): return _Solution.SolutionPtr_L2NormOfSolution(self, *args)
    def projectOntoMesh(self, *args): return _Solution.SolutionPtr_projectOntoMesh(self, *args)
    def energyErrorTotal(self): return _Solution.SolutionPtr_energyErrorTotal(self)
    def setWriteMatrixToFile(self, *args): return _Solution.SolutionPtr_setWriteMatrixToFile(self, *args)
    def setWriteMatrixToMatrixMarketFile(self, *args): return _Solution.SolutionPtr_setWriteMatrixToMatrixMarketFile(self, *args)
    def setWriteRHSToMatrixMarketFile(self, *args): return _Solution.SolutionPtr_setWriteRHSToMatrixMarketFile(self, *args)
    def mesh(self): return _Solution.SolutionPtr_mesh(self)
    def bc(self): return _Solution.SolutionPtr_bc(self)
    def rhs(self): return _Solution.SolutionPtr_rhs(self)
    def ip(self): return _Solution.SolutionPtr_ip(self)
    def setBC(self, *args): return _Solution.SolutionPtr_setBC(self, *args)
    def setRHS(self, *args): return _Solution.SolutionPtr_setRHS(self, *args)
    def setIP(self, *args): return _Solution.SolutionPtr_setIP(self, *args)
    def save(self, *args): return _Solution.SolutionPtr_save(self, *args)
    def load(self, *args): return _Solution.SolutionPtr_load(self, *args)
    def saveToHDF5(self, *args): return _Solution.SolutionPtr_saveToHDF5(self, *args)
    def loadFromHDF5(self, *args): return _Solution.SolutionPtr_loadFromHDF5(self, *args)
    def setUseCondensedSolve(self, *args): return _Solution.SolutionPtr_setUseCondensedSolve(self, *args)
    def solution(self, *args): return _Solution.SolutionPtr_solution(self, *args)
SolutionPtr_swigregister = _Solution.SolutionPtr_swigregister
SolutionPtr_swigregister(SolutionPtr)

# This file is compatible with both classic and new-style classes.


