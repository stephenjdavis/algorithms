package com.stephenjohnny.tools;

public class MaxProfit {

    public static void main(String[] args) {

        // Create an array of double integers for prices
        double [] stockPrices = {44, 74, 90, 4, 122, 123, 23};

        // Call the maxProfit method
        getMaxProfit(stockPrices);
    }

    private static double getMaxProfit(double[] prices) {

        double maxProfit = 0;
        // Loop through each day's price
        for (int i = 0; i <= prices.length -1; i++)

            // For each day, compare it with only the days...
            for (int j = 1; j <= prices.length -1 ;j++) {

                // ...that come after it
                if (j > i) {

                    // Each day's price is compared to the days previous
                    if ((prices[j] - prices[i] > maxProfit)){
                        maxProfit = prices[j] - prices[i];
                        System.out.println ("Buy day: " + (i+1) +
                                "... Sell day: " + (j+1) + " for profit of: " + "$"+maxProfit + ".");
                    }
                }
            }
        System.out.println("Maximum profit: $" + maxProfit);
        return maxProfit;
    }
}
