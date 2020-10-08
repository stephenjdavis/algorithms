class PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int rev = 0; 
        int temp = x;
        while (temp != 0) {
            int last = temp % 10;
            temp /= 10;
            rev = rev * 10 + last;
        }
        if (x == rev) {
            return true;
        } else {
            return false;
        }
    }
}
