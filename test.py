from const import const
from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot, make_e_expr, make_ln, make_absv
from tof import tof
from deriv import deriv
from hw06_s19 import percent_retention_model, plant_growth_model, plot_retention, spread_of_disease_model, plot_spread_of_disease
import unittest
import math

class Assign01UnitTests(unittest.TestCase):

    # def test_01(self):
    #
    #     print("****Unit Test 01********")
    #     eq = percent_retention_model(make_const(0.5), make_const(15.0))
    #     assert not eq is None
    #     print("rt: ",eq)
    #     eqf = tof(eq)
    #     assert not eqf is None
    #     err = 0.0001
    #     gt = lambda t: (100.0-15.0)*math.e**(-0.5*t)+15
    #     #print(gt(1))
    #     for t in range(100):
    #         assert abs(gt(t) - eqf(t)) <= err
    #     print("Unit Test 01: pass")
    #     plot_retention(make_const(0.5), make_const(15.0), make_const(0.0), make_const(30.0))

    def test_02(self):
        print("****Unit Test 02********")
        #p, t0, p0, t1, p1
        eq = spread_of_disease_model(make_const(500000), make_const(0.0), make_const(200.0), make_const(1.0), make_const(500.0))
        assert not eq is None
        print("eq: ", eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 100.0
        gt = lambda t: 500000/(1+(2499*math.e**(-500000*.000001832701472148934*t)))
        print(gt(1), eqf(1))
        plot_spread_of_disease(make_const(500000), make_const(0.0), make_const(200.0), make_const(1.0),
                               make_const(500.0), make_const(0.0), make_const(7.0))

        for t in range(100):
            print("t[",t,"] ",abs(gt(t) - eqf(t)) )
            assert abs(gt(t) - eqf(t)) <= err
        print("Unit Test 02: pass")

    if __name__ == "__main__":
        unittest.main()