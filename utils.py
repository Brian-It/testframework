import os
import sys

if hasattr(sys, '_getframe'): currentframe = lambda: sys._getframe(3)
_srcfile = os.path.normcase(currentframe.__code__.co_filename)


def getCaller():
    if _srcfile:
        # IronPython doesn't track Python frames, so findCaller raises an
        # exception on some versions of IronPython. We trap it here so that
        # IronPython can use logging.
        try:
            fn, lno, func = findCaller()
        except ValueError:
            fn, lno, func = "(unknown file)", 0, "(unknown function)"
    else:
        fn, lno, func = "(unknown file)", 0, "(unknown function)"
    return fn, lno, func


def findCaller():
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    f = currentframe()
    # On some versions of IronPython, currentframe() returns None if
    # IronPython isn't run with -X:Frames.
    if f is not None:
        f = f.f_back
    rv = "(unknown file)", 0, "(unknown function)"
    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename == _srcfile:
            f = f.f_back
            continue
        rv = (co.co_filename, f.f_lineno, co.co_name)
        break
    return rv


def currentframe():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_back


def print_caller(func):
    def wrapper(*args, **kwargs):
        import sys
        f = sys._getframe()
        # f = currentframe()
        pathname = f.f_back.f_code.co_filename
        filename = os.path.basename(pathname)
        module = os.path.splitext(filename)[0]
        # func_name = f.f_back.f_code.co_name
        func_name = func.func_name
        lineno = f.f_back.f_lineno
        if kwargs:
            print "%s:%s  %-10s\targs%s %s" % (filename, lineno, func_name, args, kwargs)
        else:
            print "%s:%s  %-10s\targs%s" % (filename, lineno, func_name, args)
        # print '######################################'
        # print 'caller filename is ',pathname
        # print 'caller func is ', func_name
        # print 'caller lineno is',lineno
        # print 'the passed args is',args,kwargs
        # print '######################################'
        func(*args, **kwargs)
    return wrapper

