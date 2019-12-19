#!/usr/bin/env python

"""
Author: Olga Joloud
File: product_tests.py
Purpose: Entrypoint for selenium automation
"""
import unittest
from unittests.test_sign_in import TestSignIn 

def main():

    test_loader=unittest.TestLoader()
    test_suites = [
            test_loader.loadTestsFromTestCase(TestSignIn)
            ]
    test_runner = unittest.TextTestRunner(verbosity=2)
    for test_suite in test_suites:
        test_runner.run(test_suite)
if __name__=='__main__':
    main()
