import doctest
import unittest
import prime

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(prime))
    tests.addTests(doctest.DocFileSuite('prime.md'))
    return tests
    
if __name__ == '__main__':
    unittest.main()

    """
    Ran 1 test in 7.792s

    OK"""