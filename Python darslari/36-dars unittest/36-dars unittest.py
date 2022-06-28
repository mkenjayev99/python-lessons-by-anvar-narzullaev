import unittest


# from simple1 import max_num, min_num
# class NumTest(unittest.TestCase):    
#     def testMaxNum(self):
#         self.assertEqual(max_num(4, 5, -3), -3)
#         self.assertEqual(max_num(951, -951, 0), 952)

#     def testMinimum(self):
#         self.assertAlmostEqual(min_num(21, 54, -54), -54)
#         self.assertAlmostEqual(min_num(65, 0, 7), 0)

# unittest.main()


# from simple2 import capLetter
# class txtTest(unittest.TestCase):
#     def testTxt(self):
#         self.assertEqual(capLetter(['ali', 'vali', 'salim']), ['Ali', 'Vali', 'karim'])

# unittest.main()


# from simple2 import bite_even
# class EvenNumTest(unittest.TestCase): # Alhamdulillah
#     def test_even_num(self): # Be careful when you write a func name. in unittest mode, func name begins always with 'test' !!!
#         self.assertEqual(bite_even([2, 5, 8, 6, 4, 9, 32, 21, 45, 78]), [7, 1, 3, 10, 11, 12, 13, 14, 15])
#         self.assertEqual(bite_even([4, 6, 5, 8, 9, 7, 3]), [4, 6, 8])

# unittest.main()


# from fibonaci import fibonaci
# class FibonaciTest(unittest.TestCase):
#     def test_fibo(self):
#         self.assertTrue(fibonaci(13))
#         self.assertTrue(fibonaci(55))
#         self.assertFalse(fibonaci(54))
#         self.assertFalse(fibonaci(15))
        
# unittest.main()