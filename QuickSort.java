import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class QuickSort {

    public ArrayList<Integer> quickSort(ArrayList<Integer> listOfNums) {

        ArrayList<Integer> sorted = new ArrayList<>();

        // If the list has 1 or less elements we return the list.
        if (listOfNums.size() <= 1) {
            return listOfNums;
        }

        // Create three ArrayLists that will contain elements after they are compared.
        ArrayList<Integer> less = new ArrayList<>();
        ArrayList<Integer> equal = new ArrayList<>();
        ArrayList<Integer> greater = new ArrayList<>();

            // Create a pivot using the middle index.
            int pivot = listOfNums.get(listOfNums.size() / 2);

            // Iterate through every number in the array and add each to the appropriate new ArrayList
            // once they are compared to the value at the pivot index.
            for (int x : listOfNums) {
                if (x < pivot) {
                    less.add(x);
                } else if (x == pivot) {
                    equal.add(x);
                } else {
                    greater.add(x);
                }
            }

            // Run recursively by putting the new ArrayLists in order each time.
            sorted.addAll(quickSort(less));
            sorted.addAll(equal);
            sorted.addAll(quickSort(greater));

        return sorted;
    }

    @Test
    public void test () {
        ArrayList<Integer> testList = new ArrayList<>(Arrays. asList(2,66,33,876,98,0,-9,-33,124));
        ArrayList<Integer> correctList = new ArrayList<>(Arrays. asList(-33, -9, 0, 2, 33, 66, 98, 124, 876));
        System.out.println(quickSort(testList));
        assertEquals(correctList, quickSort(testList));
    }
}
