import sys
import os
from test_runner import TestRunner

cur_dir = os.getcwd()
print cur_dir

print sys.path
if cur_dir not in sys.path:
    sys.path.insert(0, cur_dir)

test_module = __import__('my_test')
print type(test_module)
test_class = type('runner', (TestRunner, test_module.Test), {})
print type(test_class)
cfg = None
test = test_class(cfg)
test.run()
