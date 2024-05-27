import java.util.*;

class Solution {
    
    static ArrayDeque<Character> queue = new ArrayDeque<>();
    
    static int answer = 0;
    
    static void setStack(String s) {
        char[] arr = s.toCharArray();
        
        for (char c : arr) {
            queue.add(c);
        }
    }
    
    static void checkArrays() {
        int cnt1 = 1, cnt2 = 0;
        
        char c = queue.pollFirst();
        
        while (cnt1 != cnt2 && !queue.isEmpty()) {
            if (c != queue.pollFirst()) {
                cnt2++;
            } else {
                cnt1++;
            }
        }
    }
    
    public int solution(String s) {    
        setStack(s);
        
        while (!queue.isEmpty()) {
            checkArrays();
            answer++;
        }
        
        return answer;
    }
}