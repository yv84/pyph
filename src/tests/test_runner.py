# http://stackoverflow.com/questions/1732438/run-all-unit-test-in-python-directory
# python3 -m tests.test_runner

import unittest

testmodules = [
    'tests.integrate_tests.test1',
    'tests.unit_tests.test_l2',
    'tests.unit_tests.utest',
    ]

suite = unittest.TestSuite()

for t in testmodules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
