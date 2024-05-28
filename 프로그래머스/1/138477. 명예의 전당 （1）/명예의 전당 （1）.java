import java.util.*;

class Solution {
    
    static List<Integer> queue = new ArrayList<>();
    static List<Integer> answer = new ArrayList<>();
    
    public List<Integer> solution(int k, int[] score) {
        for(int i : score) {
            if (queue.isEmpty()) {
                queue.add(i);
                answer.add(i);
                continue;
            }
            
            if (queue.size() < k) {
                queue.add(i);
                
                Collections.sort(queue);
                answer.add(queue.get(0));
            } else {
                int nowScore = queue.remove(0);
                
                if (nowScore < i) {
                    queue.add(i);
                    Collections.sort(queue);
                    answer.add(queue.get(0));
                } else {
                    queue.add(nowScore);
                    Collections.sort(queue);
                    answer.add(nowScore);
                }
                
            }
        }
        
        return answer;
        
    }
}