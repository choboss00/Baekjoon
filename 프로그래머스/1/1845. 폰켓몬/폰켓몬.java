import java.util.*;

class Solution {
    static HashMap<Integer, Integer> map = new HashMap<>();
    public int solution(int[] nums) {
        int n = nums.length / 2;
        
        for(int num : nums) {
            if (!map.containsKey(num)) {
                map.put(num, 1);
            } else {
                map.put(num, map.get(num)+1);
            }
        }
        
        Set<Integer> set = map.keySet();
        
        if (n > set.size()) {
            return set.size();
        } else {
            return n;
        }
        
        
    }
}