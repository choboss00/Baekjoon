import java.util.*;
class Solution {
    public List<Integer> solution(int[] prices) {
        List<Integer> answer = new ArrayList<>();
        
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        
        for(int price : prices) {
            queue.add(price);
        }
        
        while (!queue.isEmpty()) {
            int p = queue.pollFirst();
            int cnt = 0;
            for (int q : queue) {
                if (p <= q) {
                    cnt++;
                } else {
                    cnt++;
                    break;
                }
            }
            answer.add(cnt);
            
        }
        
        return answer;
    }
}