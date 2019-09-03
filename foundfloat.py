import unittest

class TestFoundFloat(unittest.TestCase):

    # Check that we find the correct float value parameter.
    def test_found_float_equal(self):
        self.assertEqual(found_float(5.5, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]), 5.5)

    # Check that we are finding the correct value when the whole number matches but not the decimal.
    def test_found_float_not_equal_decimal(self):
        self.assertNotEqual(found_float(5.5, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]), 5.6)

    # Check that we are not converting a float to an integer in our method.
    def test_found_float_not_equal_whole(self):
        self.assertNotEqual(found_float(5, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]), 5.0)


def found_float(f, arr):
        ''' Parameter f is the float value we are looking for. Parameter arr is our array of floats.'''
        # Left point starts at zero.
        lp = 0;

        # Right point starts at the end position.
        rp = len(arr);
        
        for i in range(rp):
            mp = round((lp + rp) / 2);

            if (arr[mp] == f):
                return f;

            if (arr[mp] < f):
                lp = mp + 1;

            if (arr[mp] > f):
                rp = mp - 1;
            
            i += 1

# Test method
if __name__ == '__main__':
    unittest.main()
