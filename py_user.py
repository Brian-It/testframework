#!/usr/bin/env python

import argparse

# session.py --html_report Upstream-staging-report cfg_a,cases_list_a cfg_b,cases_list_b

# def session_file(filename):
#     tests = []
#     try:
#         with open(filename) as f:
#             for line in f:
#                 test = line.strip("\n ")
#                 if not test or test.startswith("#"):
#                     continue
#                 if test in tests:
#                     raise ArgumentTypeError("duplicate test: %s" % test)
#                 if not os.path.isfile(test):
#                     raise ArgumentTypeError("file not found: %s" % test)
#                 tests.append(test)
#     except IOError:
#         raise ArgumentTypeError("Invalid session file")
#
#     if not tests:
#         raise ArgumentTypeError("Empty session file")
#
#     #return filename, tests

# def cfg_file(filename):
#     """chect a configuration file"""
#
#     config = ConfigObj(filename, file_error=True)
#     print "ConfigObjError, IOError, e:"
#     print """ArgumentTypeError('Could not read "%s": %s' % (filename, e))"""


# def check_session_list(name):
#     """Read a argument and return it as parsed object"""
#     session_list = name.strip().split()
#     for session in session_list:
#         list_task = session.split(",")
#         if list_task[0]:
#             cfg_file(list_task[0])
#         else:
#             print "%s check fail in session %s" % (list_task[0], session)
#
#         session_file(list_task[1])

def check_session_list(name):
    print "check_session_list %s" % name
    return name

def do_session_test(args):
    print args
    print "doing session test..."

def mail_address(mail_addr_list):
    """Return a mail list"""
    if mail_addr_list:
        mail_addr_list = mail_addr_list.replace(" ", "")
        if "," in mail_addr_list:
            mail_addr_list = mail_addr_list.replace(",", ";")
        mail_addr_list = mail_addr_list.split(";")
        for mail_addr in mail_addr_list:
            if len(mail_addr.split("@")) != 2:
                raise ArgumentTypeError("Invalid mail address: %s" % mail_addr)
        return mail_addr_list
    else:
        raise ArgumentTypeError("mail address is not specified")


parser = argparse.ArgumentParser(description='Session script for upstream test')
parser.add_argument("--html_report", help="Set the html report name", default="default")
parser.add_argument("--mail_to", type=mail_address,
        default=None,
        help="Send out html report by email, multiple receivers should be separated by ',' or ';'")

parser.add_argument("session_list", nargs="+", help="Add session list", type=check_session_list)

parser.set_defaults(func=do_session_test)
args = parser.parse_args()

print args
args.func(args)
