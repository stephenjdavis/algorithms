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
            # We set a mid point by adding the left and right point index values and dividing by 2.
            # We must round this number because we need a whole number for our index.
            mp = round((lp + rp) / 2);

            # If the value at the midpoint is what we are looking for, return that value.
            if (arr[mp] == f):
                return f;

            # If our mid point is less than the sought value, move the left position one position
            # to the right of the mid point.
            if (arr[mp] < f):
                lp = mp + 1;

            # If our midpoint is greater than the sought value, move the right position one position
            # to the left of the midpoint.
            if (arr[mp] > f):
                rp = mp - 1;
            
            i += 1

# Test method
if __name__ == '__main__':
    unittest.main()
