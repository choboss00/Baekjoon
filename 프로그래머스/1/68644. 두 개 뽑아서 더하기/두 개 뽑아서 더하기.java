import java.util.*;

class Solution {
    public List<Integer> solution(int[] numbers) {
        int[] answer = {};
        
        List<Integer> arr = new ArrayList<>();
        
        for(int i = 0; i < numbers.length; i++) {
            for(int j = i+1; j < numbers.length; j++) {
                arr.add(numbers[i] + numbers[j]);
            }
        }
        
        boolean[] visited = new boolean[201];
        
        for(int num : arr) {
            visited[num] = true;
        }
        
        List<Integer> arr2 = new ArrayList<>();
        
        for(int i = 0; i < 201; i++) {
            if (visited[i]) {
                arr2.add(i);
            }
        }
        
        return arr2;
    }
}