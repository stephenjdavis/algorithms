class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        // Handle if only one number.
        if (nums.length == 1) {
            if (target <= nums[0]) {
                return 0;
            } else {
                return 1;
            }
        }
        // Handle target being greater than largest value.
        if (target > nums[nums.length - 1]) {
            return nums.length;
        }
        // Handle target being less than smallest value.
        if (target < nums[0]) {
            return 0;
        }
        // Create a left index point.
        int lp = 0;
        // Create a right index point.
        int rp = nums.length;
        // Create a mid point.
        int mp = -1;
        // Check each value at the middle point and cut the search in half each pass.
        while(rp >= lp) {
            mp = (lp + rp) / 2;
            // Return the index where find the value.
            if (target == nums[mp]) {
                return mp;
            }
            if (nums[mp] < target) {
                lp = mp + 1;
            }
            if (nums[mp] > target) {
                rp = mp - 1;
            }
        } 
        // Return left point if we haven't found the value.
        return lp;
    }
}
