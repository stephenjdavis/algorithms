import unittest
import sys


class TestRevereString(unittest.TestCase):

    # Check that the return string appears in the correct reverse order.
    def test_is_equal(self):
        self.assertEqual(reverse_string('abcdefg'), 'gfedcba')

    # Check that the returned string appears is not in the correct reverse order.
    def test_is_not_equal(self):
        self.assertIsNot(reverse_string('abcdefg'), 'abcdefg')

    # Check that the return string ignores upper and lower case..
    def test_upper_case(self):
        self.assertEqual(reverse_string('abcDeFg'), 'gfedcba')
    
    # Check that number strings are correctly treated as strings within the function.
    def test_numbers_as_strings(self):
        self.assertEqual(reverse_string('123456'), '654321')


def reverse_string(string_a): 
    '''We already know that we can trust the string from the caller, so we don't
    need to do any checking for a non-zero-terminated string.'''
    # Convert the string into a list of characters so that we can use an index.
    str_lower = string_a.lower()
    x = list(str_lower)
    # Create an index variable for the first character item.
    start = 0
    #Create an index variable for the last character item.
    end = len(x) - 1
    
    # Swap items at the start and end positions until we meet in the middle, meaning all character items have been swapped.
    while start < end: 
        # Create a temporary variable to store the start value which will eventually replace the end value. 
        temp = x[start]
        # Replace the start value with the end value.
        x[start] = x[end] 
        # Replace the end value with the item value previously at the start.
        x[end] = temp 
        # Move forward one character position in the list.
        start += 1
        # Move backward one character position in the list.
        end -= 1

    # Convert the list back into a string, now in reversed order.
    result = ''
    for i in x:
        result += i

    print(result)
    return result

# Test method
if __name__ == '__main__':
    unittest.main()
        