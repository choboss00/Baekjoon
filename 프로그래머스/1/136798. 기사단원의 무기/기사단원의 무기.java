import java.util.*;

class Solution {
    
    static int[] arr;
    
    static void countArr(int i) {
        int cnt = 0;
        for(int j = 1; j < i/2+1; j++) {
            if (i % j == 0) {
                cnt++;
            }
        }
        
        arr[i] = cnt+1;
    }
    
    public int solution(int number, int limit, int power) {
        int answer = 0;
        arr = new int[number+1];
        
        for(int i = 1; i <= number; i++) {
            countArr(i);
        }
        
        for (int j = 1; j <= number; j++) {
            if (arr[j] > limit) {
                answer += power;
            } else {
                answer += arr[j];
            }
        }
        
        //System.out.println(Arrays.toString(arr));
        
        return answer;
        
    }
}