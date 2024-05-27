import java.util.*;

class Solution
{
    public int solution(String s)
    {
        char[] arr = s.toCharArray();
        
        ArrayDeque<Character> stack = new ArrayDeque<>();
        
        for(char c : arr) {
            if (stack.isEmpty()) {
                stack.add(c);
            } else {
                char sc = stack.pollLast();
                
                if (sc == c) {
                    continue;
                } else {
                    stack.add(sc);
                    stack.add(c);
                }
            }
        }
        
        if (stack.isEmpty()) {
            return 1;
        } else {
            return 0;
        }
        
    }
}