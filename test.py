from const import const
from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot, make_e_expr, make_ln, make_absv
from tof import tof
from deriv import deriv

from hw05 import solve_pdeq, solve_pdeq_with_init_cond, \
    find_growth_model, radioactive_decay, c14_carbon_dating, demand_elasticity, is_demand_elastic, expected_rev_dir
import unittest
import math

class Assign01UnitTests(unittest.TestCase):

    def test_01(self):
        #solve y' = y => 1.0*(2.71828182846^(1.0*(t^1.0))))
        print("****Unit Test 01********")
        eq = solve_pdeq(make_const(1.0), make_const(1.0))
        assert not eq is None
        print(eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: math.e**t
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err
        print("Unit Test 01: pass")

    def test_02(self):
        #solve 4y' = 1/3y
        print("****Unit Test 02********")
        eq = solve_pdeq(make_const(4.0), make_const(1.0/3.0))
        assert not eq is None
        print(eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: math.e**((1.0/12.0)*t)
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err
        print("Unit Test 02: pass")

    def test_03(self):
        # solve y'=3y y(0) =1
        print("****Unit Test 03********")
        eq = solve_pdeq_with_init_cond(make_const(1.0), make_const(3.0))
        assert not eq is None
        print(eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: math.e ** (3.0*t)
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err
        print("Unit Test 03: pass")

    def test_04(self):
        print("****Unit Test 04********")
        eq = find_growth_model(make_const(20000.0), make_const(2.0), make_const(80000.0))
        print(eq)
        eqf = tof(eq)
        print("After 12 hours: ",eqf(0.5))
        assert not eqf is None
        err = 0.0001
        gt = lambda t: 20000 * math.e ** (0.6931471805599453*t)
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err
        print("Unit Test 04: pass")

    def test_05(self):
        print("****Unit Test 05********")
        eq = radioactive_decay(make_const(0.021), make_const(8.0), make_const(10.0))
        print(eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: 8 * math.e ** (-0.021*t)
        assert abs(gt(10.0) - eqf(0)) <= err
        print("Unit Test 05: pass")

    def test_06(self):
        print("****Unit Test 06********")
        years = c14_carbon_dating(make_const(0.583))
        print(years)

    def test_07(self):
        print("****Unit Test 07********")
        p = make_plus(make_quot(make_const(18000.0), make_pwr('p', 1.0)), make_const(-1500.0))
        q = demand_elasticity(p, make_const(6.0))
        #q = is_demand_elastic(p, make_const(6.0))
        print(q)

    def test_08(self):
        print("****Unit Test 07********")
        p = make_plus(make_quot(make_const(18000.0), make_pwr('p', 1.0)), make_const(-1500.0))
        return expected_rev_dir(p, make_const(6.0), const(-1.0))

    if __name__ == "__main__":
        unittest.main()