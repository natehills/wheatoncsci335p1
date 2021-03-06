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
            fp, pathname, description = imp.find_module('_RHS', [dirname(__file__)])
        except ImportError:
            import _RHS
            return _RHS
        if fp is not None:
            try:
                _mod = imp.load_module('_RHS', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _RHS = swig_import_helper()
    del swig_import_helper
else:
    import _RHS
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


class RHS(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RHS, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RHS, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def nonZeroRHS(self, *args): return _RHS.RHS_nonZeroRHS(self, *args)
    def addTerm(self, *args): return _RHS.RHS_addTerm(self, *args)
    def linearTerm(self): return _RHS.RHS_linearTerm(self)
    def linearTermCopy(self): return _RHS.RHS_linearTermCopy(self)
    __swig_getmethods__["rhs"] = lambda x: _RHS.RHS_rhs
    if _newclass:rhs = staticmethod(_RHS.RHS_rhs)
    __swig_destroy__ = _RHS.delete_RHS
    __del__ = lambda self : None;
RHS_swigregister = _RHS.RHS_swigregister
RHS_swigregister(RHS)

def RHS_rhs():
  return _RHS.RHS_rhs()
RHS_rhs = _RHS.RHS_rhs

class RHSPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RHSPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RHSPtr, name)
    __repr__ = _swig_repr
    def __deref__(self): return _RHS.RHSPtr___deref__(self)
    def __init__(self): 
        this = _RHS.new_RHSPtr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RHS.delete_RHSPtr
    __del__ = lambda self : None;
    def nonZeroRHS(self, *args): return _RHS.RHSPtr_nonZeroRHS(self, *args)
    def addTerm(self, *args): return _RHS.RHSPtr_addTerm(self, *args)
    def linearTerm(self): return _RHS.RHSPtr_linearTerm(self)
    def linearTermCopy(self): return _RHS.RHSPtr_linearTermCopy(self)
    def rhs(self): return _RHS.RHSPtr_rhs(self)
RHSPtr_swigregister = _RHS.RHSPtr_swigregister
RHSPtr_swigregister(RHSPtr)

# This file is compatible with both classic and new-style classes.


