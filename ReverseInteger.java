class ReverseInteger {
    public int reverse(int x) {
        // Create return variable
        int rev = 0;
        // 
        while (x != 0) {
            // Pop the last digit in the 10's place.
            // EX: 123 / 10 = 12.3 -> modulo 3
            int last = x % 10;
            
            // Update the power of 10 we are working with.
            // EX: 123/10 = 12.3 -> 12
            x /= 10;
            
            // Check for an positive integer that is larger than 32-bit bits.
            // MAX = 2,147,483,647 -> 01111111111111111111111111111111 (31-bits) with 1st bit for signing.
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && last > 7)) {
                return 0;
            }
            // Check for an negative integer that is larger than 32-bit bits.
            // MAX = -2,147,483,648 -> 01111111111111111111111111111111 (31-bits) with 1st bit for signing.
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && last < -8)) {
                return 0;
            }
            // Replacing the power of 10 we remove each time and add the popper number.
            // EX: 
            // 0 * 10 + 3 = 3
            // 3 * 10 + 2 = 32
            // 32 * 10 + 1 = 321
            rev = rev * 10 + last;
        }
        return rev;
    }
}
