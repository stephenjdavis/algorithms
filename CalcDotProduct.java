package com.stephenjohnny.tools;

/**
 * Created by sdavis on 8/16/17.
 */
public class CalcDotProduct {

    /*
     * Simple dot product calculation method
     * @param array1
     * @param array2
     */
    public static double calcDotProduct(double[] array1, double[] array2) {

        double iProduct;
        double dp = 0;
        // Check that both arrays are of equal length and throw an exception if they are not
        if (array1.length != array2.length) {
            throw new IllegalArgumentException("Arrays must be the same length.");
        }

        // Multiply each element of the first array by it's corresponding element in the other
        for (int i = 0; i < array1.length; i++) {
            iProduct = array1[i] * array2[i];

            // Add the products of each to a total sum
            dp = iProduct + iProduct;
        }

        return dp;
    }

    // Test method
    public static void main(String[] args) {

        double[] array1 = {2, 3, 4, 5, 6};
        double[] array2 = {3, 5, 7, 8, 9};
        System.out.println(calcDotProduct(array1, array2));
    }
}
