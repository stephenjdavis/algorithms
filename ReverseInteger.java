class ReverseInteger {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            // Pop the last digit in the 10's place.
            int pop = x % 10;
            // Update the power of 10 we are working with.
            x /= 10;
            // Check for an positive integer that is larger than 32-bit bits.
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) {
                return 0;
            }
            // Check for an negative integer that is larger than 32-bit bits.
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) {
                return 0;
            }
            // Replacing the power of 10 we remove each time and add the popper number.
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
