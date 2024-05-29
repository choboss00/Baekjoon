import java.util.*;

class Solution {
    
    static HashMap<Integer, Integer> myLotto = new HashMap<>();
    
    static HashMap<Integer, Integer> correctMap = new HashMap<>();
    
    static void pushCorrectMap() {
        correctMap.put(6, 1);
        correctMap.put(5, 2);
        correctMap.put(4, 3);
        correctMap.put(3, 4);
        correctMap.put(2, 5);
    }
    
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        
        int rank = 0;
        
        pushCorrectMap();
        
        for (int l : lottos) {
            if (!myLotto.containsKey(l)) {
                myLotto.put(l, 1);
            } else {
                myLotto.put(l, myLotto.get(l)+1);
            }
        }
        
        // win_nums 체크하기
        for (int win : win_nums) {
            if (myLotto.containsKey(win)) {
                rank++;
            }
        }
        
        int cnt1 = 0, cnt2 = 0;
        
        if (myLotto.containsKey(0)) {
            cnt1 = rank + myLotto.get(0);
            cnt2 = rank;
        } else {
            cnt1 = rank;
            cnt2 = rank;
        }
        
        //System.out.println(cnt1 + " " + cnt2);
        
        if (correctMap.containsKey(cnt1)) {
            answer[0] = correctMap.get(cnt1);
        } else {
            answer[0] = 6;
        }
        
        if (correctMap.containsKey(cnt2)) {
            answer[1] = correctMap.get(cnt2);
        } else {
            answer[1] = 6;
        }
        return answer;
    }
}