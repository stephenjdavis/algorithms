// This algorithm is the first "solution" I ever submitted to LeetCode for public view.
// It doesn't use a Queue, has a time of O(n log n) & space of O(1).

class LastStoneWeight {
    public int lastStoneWeight(int[] stones) {
        if (stones.length <= 1) {
            return stones[0];
        }
        Arrays.sort(stones);
        while (stones[stones.length-2] > 0) {
            for (int i=0; i<stones.length-1;i++) {
                int x = stones[stones.length-2];
                int y = stones[stones.length-1];
                if (y==x) {
                    stones[stones.length-2] = 0;
                    stones[stones.length-1] = 0;
                }
                else {
                    stones[stones.length-2] = 0;
                    stones[stones.length-1] = y - x;
                }
                Arrays.sort(stones); 
            }
        } return stones[stones.length-1];
    }
}
