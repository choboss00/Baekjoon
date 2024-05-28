import java.util.*;

class Solution {
    
    static List<Integer> list = new ArrayList<>();
    static int answer;
    
    public int solution(int k, int m, int[] score) {
        
        for(int i = 0; i < score.length; i++) {
            list.add(score[i]);
        }
        // 정렬
        Collections.sort(list);
        
        if (list.size() < m) {
            return 0;
        } else {
            for(int i = list.size() % m; i < list.size(); i += m) {
                // 최소 사과 구하기
                int minApple = k+1;
                for(int l = i; l < i+m; l++) {
                    if (list.get(l) < minApple) {
                        minApple = list.get(l);
                    }
                }
                answer += (minApple * m);
            }
        }
        
        return answer;
    }
}