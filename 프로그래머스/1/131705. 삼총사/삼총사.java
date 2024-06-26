import java.util.*;

class Solution {
    static int answer;
    
    static boolean[] visited;
    
    static Deque<Integer> stack = new ArrayDeque<>();
    
    static int length;
    
    static void dfs(int[] number, int depth) {
        
        if (stack.size() == 3) {
            int s = stack.stream().mapToInt(Integer::intValue).sum();
            
            if (s == 0) {
                answer++;
            }
            return;
            
        }
        
        for(int i = depth; i < length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                stack.add(number[i]);
                
                dfs(number, i+1);
                
                visited[i] = false;
                stack.pollLast();
            }
        }
    }
    
    public int solution(int[] number) {
        length = number.length;
        
        visited = new boolean[length];
        
        dfs(number, 0);
        
        return answer;
    }
}