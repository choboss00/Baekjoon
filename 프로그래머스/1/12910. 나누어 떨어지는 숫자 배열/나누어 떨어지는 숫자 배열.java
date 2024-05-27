import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<>();
        
        for(int a : arr) {
            if(a % divisor == 0) {
                list.add(a);
            }
        }
        
        if(list.isEmpty()) {
            list.add(-1);
            return list;
        }
        
        Collections.sort(list);
        
        return list;
        
        
    }
}