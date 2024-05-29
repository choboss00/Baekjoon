import java.util.*;

class Solution {
    
    static HashMap<Character, Integer> mapX = new HashMap<>();
    
    static HashMap<Character, Integer> mapY = new HashMap<>();
    
    static List<Character> list = new ArrayList<>();
    
    static char[] xArr;
    static char[] yArr;
    
    static void setHashMap() {
        for(int i = 0; i < 10; i++) {
            mapX.put(Character.forDigit(i, 10), 0);
            mapY.put(Character.forDigit(i, 10), 0);
        }
    }
    
    static void countChar() {
        for(char x : xArr) {
            int xn = mapX.get(x);
            mapX.put(x, xn+1);
        }
        
        for(char y : yArr) {
            int yn = mapY.get(y);
            mapY.put(y, yn+1);
        }
    }
    
    static void listPush() {
        for(int i = 9; i >= 0; i--) {
            char s = Character.forDigit(i, 10);
            
            int cnt = Math.min(mapX.get(s), mapY.get(s));
            
            for(int j = 0; j < cnt; j++) {
                list.add(s);
            }
        }
        //System.out.println(list);
    }
    
    public String solution(String X, String Y) {
        StringBuilder sb = new StringBuilder();
        
        xArr = X.toCharArray();
        yArr = Y.toCharArray();
        // map 초기화
        setHashMap();
        
        // 갯수 세기
        countChar();
        
        //System.out.println(mapX);
        //System.out.println(mapY);
        
        // get 후 count, min 값 구하고 list에 담기
        listPush();
        
        //System.out.println(list);
        
        if (list.size() == 0) {
            return "-1";
        } else {
            for(int i = 0; i < list.size(); i++) {
                if (list.get(0) == '0') {
                    return "0";
                } else {
                    sb.append(list.get(i));
                }
            }
            return sb.toString();
        }
    }
}