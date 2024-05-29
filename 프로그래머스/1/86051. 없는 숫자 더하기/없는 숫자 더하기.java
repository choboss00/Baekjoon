import java.util.*;

class Solution {
    
    static HashMap<Integer, Boolean> map = new HashMap<>();
    
    public int solution(int[] numbers) {
        int ans = 0;
        
        for(int n : numbers) {
            map.put(n, true);
        }
        
        for(int i = 0; i < 10; i++) {
            if (!map.containsKey(i)) {
                ans += i;        
            }
        }
        return ans;
    }
}