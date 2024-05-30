import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Long> heap = new PriorityQueue<>();
        
        for (long sc : scoville) {
            heap.add(sc);
        }
        
        while (heap.peek() < K && heap.size() >= 2) {
            long sc1 = heap.poll();
            long sc2 = heap.poll();
            
            heap.add(sc1 + 2 * sc2);
            answer++;
        }
        
        if (heap.peek() < K) {
            return -1;
        } else {
            return answer;
        }
    }
}