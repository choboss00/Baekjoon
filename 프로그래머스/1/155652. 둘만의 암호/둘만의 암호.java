import java.util.*;

class Solution {
    static HashMap<Character, Boolean> map = new HashMap<>();
    
    static List<Character> list = new ArrayList<>();
    
    static void setHashMap(String skip) {
        char[] skipArray = skip.toCharArray();
        
        for (char sa : skipArray) {
            map.put(sa, true);
        }
    }
    
    public String solution(String s, String skip, int index) {
        setHashMap(skip);
        
        char[] arr = s.toCharArray();
        
        for(char c : arr) {
            int idx = 1;
            
            while (idx <= index) {
                c = (char) (97 + (c - 97 + 1) % 26);
                idx++;
                
                if (map.containsKey(c)) {
                    idx--;
                }
            }
            
            list.add(c);
        }
        
        //System.out.println(list);
        
        StringBuilder sb = new StringBuilder();
        
        for (char cl : list) {
            sb.append(cl);
        }
        
        return sb.toString();
        
    }
}