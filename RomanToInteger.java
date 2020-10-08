class RomanToInteger {
    public int romanToInt(String s) {
        HashMap<String, Integer> map = new HashMap<>();
        
        map.put("I", new Integer(1));
        map.put("V", new Integer(5));
        map.put("X", new Integer(10));
        map.put("L", new Integer(50));
        map.put("C", new Integer(100));
        map.put("D", new Integer(500));
        map.put("M", new Integer(1000));
        
        // Create a String array so that we can use each character as a key.
        // Whe can't index the string itself, because the map won't find a char as a key reference.
        String[] string = s.split("");
        
        // Create a variable to hold our return value.
        int num = 0;
        
        // Create a left and right index so we can compare the currently indexed and the next indexed value.
        int lp = 0;
        int rp = 1;
        
        while(lp < string.length) {
            // If we have no next numeral to compare and the numeral is less that the numeral after it...
            if (rp != string.length && map.get(string[lp]).intValue() < map.get(string[rp]).intValue()) {
                // We subtract the numberal value from our number.
                num -= map.get(string[lp]);
            } else {
                // We add the value to our number.
                num += map.get(string[lp]);
            }
            lp++;
            rp++;
        }
        return num;
    }
}
