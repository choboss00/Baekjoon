import java.util.*;

class Solution {
    
    public String solution(int[] food) {
        StringBuilder sb = new StringBuilder();
        
        sb.append("0"); // 물 넣기
        
        for(int i = food.length-1; i > 0; i--) {
            int cnt = food[i] / 2;
            String f = String.valueOf(i).repeat(cnt);
            
            sb.append(f);
            sb.insert(0, f);
        }
        
        return sb.toString();
        
    }
}