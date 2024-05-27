import java.util.*;

class Solution {
    static List<Integer> list = new ArrayList<>();
    static HashMap<Character, Integer> map = new HashMap<>();
    
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        
        char[] arr = s.toCharArray();
        
        for (int i = 0; i < arr.length; i++) {
            char c = arr[i];
            
            if (!map.containsKey(c)) {
                map.put(c, i);
                list.add(-1);
            } else {
                int idx = map.get(c);
                map.put(c, i);
                //System.out.println(c + " " + idx + " " + i);
                list.add(i-idx);
            }
        }
        
        for (int j=0; j < list.size(); j++) {
            answer[j] = list.get(j);
        }
        
        return answer;
    }
}