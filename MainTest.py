import unittest

from HRM_LOGIN_INVALID import MyLoginTestCase2
from HRM_LOGIN import MyLoginTestCase1
from PIM_ADD_01 import MyPIMTestCase1
from PIM_EDIT_02 import MyPIMTestCase2
from PIM_DELETE_03 import MyPIMTestCase3

tc1 = unittest.TestLoader().loadTestsFromTestCase(MyLoginTestCase1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(MyLoginTestCase2)

tc3 = unittest.TestLoader().loadTestsFromTestCase(MyPIMTestCase1)
tc4 = unittest.TestLoader().loadTestsFromTestCase(MyPIMTestCase2)
tc5 = unittest.TestLoader().loadTestsFromTestCase(MyPIMTestCase3)


Login_Test = unittest.TestSuite([tc1,tc2])

Pim_Test = unittest.TestSuite([tc3,tc4,tc5])

unittest.TextTestRunner().run(Login_Test)
unittest.TextTestRunner().run(Pim_Test)



