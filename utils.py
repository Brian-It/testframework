import os
import sys


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
