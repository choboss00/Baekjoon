import java.util.*;

class Solution {
    
    static List<Character> stack = new ArrayList<>();
    
    static int cnt = 0;
    
    static void checkRotate(int i) {
        ArrayDeque<Character> stack2 = new ArrayDeque<>();
    
        Collections.rotate(stack, -i);
        //System.out.println("stack : " + stack);
        
        for (char c : stack) {
            if (stack2.isEmpty()) {
                stack2.add(c);
            } else {
                char sc = stack2.pollLast();
                if (sc == '(' && c == ')') {
                    continue;
                } else if (sc == '[' && c == ']') {
                    continue;
                } else if (sc == '{' && c == '}') {
                    continue;
                } else {
                    stack2.add(sc);
                    stack2.add(c);
                }
            }
            //System.out.println("현재 스택 : " + stack2);
        }
        //System.out.println("stack2 : " + stack2);
        
        if (stack2.isEmpty()) {
            cnt++;
        }
        Collections.rotate(stack, i);
    }
    
    public int solution(String s) {
        
        char[] arr = s.toCharArray();
        
        for (char c : arr) {
            stack.add(c);
        }
        
        for (int i = 0; i < stack.size(); i++) {
            checkRotate(i);
        }
        
        return cnt;
    }
}