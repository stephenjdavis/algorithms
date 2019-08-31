package com.stephenjohnny.tools;

public class LongestCommonSubstring {

    public static void main(String[] args) {
        longestSubstring("abcdefg", "andabcdemore");
    }
    public static int longestSubstring(String s1, String s2) {

        // We create a 'table' that looks like this:
        //   a b c d e f g h i j 
        // o 0 0 0 0 0 0 0 0 0 0 
        // r 0 0 0 0 0 0 0 0 0 0 
        // a 1 0 0 0 0 0 0 0 0 0 = new maxLength = 1
        // b 0 2 0 0 0 0 0 0 0 0 = new maxLength = 2 (because adding 1 to the value of [0][2] equals 2)
        // c 0 0 3 0 0 1 0 0 0 0 = new maxLength = 3 (because adding 1 to the value of [1][3] equals 3)
        // i 0 0 0 0 0 0 0 0 1 0
        // n 0 0 0 0 0 0 0 0 0 0 
        // s 0 0 0 0 0 0 0 0 0 0 
        // t 0 0 0 0 0 0 0 0 0 0 
        // e 0 0 0 0 1 0 0 0 0 0 
        // a 1 0 0 0 0 0 0 0 0 0
        // d 0 0 0 1 0 0 0 0 0 0 

        // This is set to '0' by default
        int[][] num = new int[s1.length()][s2.length()];
        
        // This will be the placeholder for the value we need to return
        int maxLength = 0;

        for (int i = 0; i < s1.length(); i++) {
            
            for (int j = 0; j < s2.length(); j++) {
                
                // If the index character of string 1 equals the index character of string 2
                if (s1.charAt(i) == s2.charAt(j)) {

                    if ((i == 0) || (j == 0))
                        num[i][j] = 1;
                    else                 
                        // We add 1 to the value of the previous index positions
                        num[i][j] = 1 + num[i - 1][j - 1];
                    
                    // If we've now added a value and it's greater than the max placeholder
                    // We assign it to the new max placeholder
                    if (num[i][j] > maxLength) {
                        maxLength = num[i][j];
                    }
                }
            }
        }
        System.out.println("The longest common substring contains: " + maxLength + " characters.");
        return maxLength;
    }
}
