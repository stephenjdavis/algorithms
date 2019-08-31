package com.stephenjohnny.tools;

/**
 * Created by sdavis on 8/16/17.
 */
public class BinarySearch {

    public static boolean foundNumber(int number, int[] arr) {

        // Left point starts at zero.
        int lp = 0;

        // Right point starts at the end position.
        int rp = arr.length;

        // Do this until there is no position between the left and right points.
        while(rp >= lp) {

            // Set the middle point halfway between the left and right points.
            int mp = (lp + rp) / 2;

            // If we found the number...
            if (arr[mp] == number) {

                // End of method
                return true;
             }

             // If the value of the middle position is less than our number:
             if (arr[mp] < number) {

                // Move the left point to one position past the middle point since it's not our number.
                lp = mp + 1;
            }

            // If the value of the middle position is greater than our number:
            if (arr[mp] > number) {

                // Move the right point to one position before the middle point.
                rp = mp - 1;
            }
        }
        return false;
    }


    // Test method
    public static void main(String[] args) {

        int sortedArr1[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
        foundNumber(4, sortedArr1);
        System.out.println(foundNumber(4, sortedArr1));

        int sortedArr2[] = {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
        foundNumber(4, sortedArr2);
        System.out.println(foundNumber(4, sortedArr2));
    }
}
