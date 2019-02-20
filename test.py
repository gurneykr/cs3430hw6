from const import const
from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot, make_e_expr, make_ln, make_absv
from tof import tof
from deriv import deriv
from hw06_s19 import percent_retention_model, plant_growth_model, plot_retention
import unittest
import math

class Assign01UnitTests(unittest.TestCase):

    def test_01(self):

        print("****Unit Test 01********")
        eq = percent_retention_model(make_const(0.5), make_const(15.0))
        assert not eq is None
        print("rt: ",eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: (100.0-15.0)*math.e**(-0.5*t)+15
        #print(gt(1))
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err
        print("Unit Test 01: pass")
        plot_retention(make_const(0.5), make_const(15.0), make_const(0.0), make_const(30.0))



    if __name__ == "__main__":
        unittest.main()