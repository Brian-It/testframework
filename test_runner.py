
class TestRunner(object):
    def __init__(self, cfg):
        self.cfg = cfg
        print 'do TestRunner __init__...'
        super(TestRunner, self).__init__()

    def run(self):
        print 'do TestRunner run...'
        try:
            teststack = TestStack()
            teststack.make_all()
        except Exception, e:
            teststack.make_clean()


class TestStack(list):

    def do(self, act_fun, recover_fun=None, act_args=None, recover_args=None):
        if act_fun:
            try:
                act_fun(*act_args)
            except Exception, e:
                print e
                raise
        if recover_fun:
            self.append((recover_fun, recover_args))

    def recover_env(self):
        while self:
            fun, args = self.pop()
            if not fun:
                continue
            try:
                fun(*args)
            except Exception, e:
                print "Calling %s failed,error:%s" % (fun.__name__, e)


    def make_all(self):
        # task 1
        self.do(None)
        # task 2
        self.do(None)

    def make_clean(self):
        self.recover_env()





