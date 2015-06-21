#!/usr/bin/env python
#tests file

from domain import*
import unittest

class MathFunctionTest (unittest.TestCase):

    def test_emptyConstructor(self):
        mf = MathFunction()
        actionName = mf.applyAction()
        self.assertEqual(actionName, "calcul")

    def test_ConstructorWithLambda(self):
        mf2 = MathFunction(lambda x: x*x)
        result = mf2.execute(5)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()

raw_input() 
