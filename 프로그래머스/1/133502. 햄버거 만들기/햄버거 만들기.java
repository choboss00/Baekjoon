import java.util.*;

class Solution {
    
    ArrayDeque<Integer> queue = new ArrayDeque<>();
    
    public int solution(int[] ingredient) {
        int answer = 0;
        
        for (int i : ingredient) {
            // 현재 들어올 원소가 빵일경우
            if (i == 1 && queue.size() >= 3) {
                int nowElement1 = queue.pollLast();
                int nowElement2 = queue.pollLast();
                int nowElement3 = queue.pollLast();
                
                //System.out.println(nowElement1 + " " + nowElement2 + " " + nowElement3);
                
                if (nowElement1 == 3 && nowElement2 == 2 && nowElement3 == 1) {
                    answer++; // 햄버거 하나 만듬
                    continue;
                } else { // 다시 차례대로 넣기
                    queue.add(nowElement3);
                    queue.add(nowElement2);
                    queue.add(nowElement1);
                    queue.add(i);
                }
            } else {
                queue.add(i);
            }
            
            //System.out.println(queue);
        }
        
        return answer;
    }
}