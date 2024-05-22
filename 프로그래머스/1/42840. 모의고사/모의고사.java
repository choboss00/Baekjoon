import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        
        int[] p1 = {1,2,3,4,5};
        int[] p2 = {2,1,2,3,2,4,2,5};
        int[] p3 = {3,3,1,1,2,2,4,4,5,5};
        
        // 사람마다 맞춘 개수
        int a1 = 0;
        int a2 = 0;
        int a3 = 0;
        
        for(int i = 0; i < answers.length; i++) {
            if (p1[i % 5] == answers[i]) {
                a1 += 1;
            }
            if (p2[i % 8] == answers[i]) {
                a2 += 1;
            }
            if (p3[i % 10] == answers[i]) {
                a3 += 1;
            }
        }
        
        int maxNum = Math.max(a1, Math.max(a2, a3));
        
        if (a1 == maxNum) {
            answer.add(1);
        }
        
        if (a2 == maxNum) {
            answer.add(2);
        }
        
        if (a3 == maxNum) {
            answer.add(3);
        }
        
        int[] result = new int[answer.size()];
        for(int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}