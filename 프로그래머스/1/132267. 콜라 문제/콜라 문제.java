class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        
        while(n >= a) {
            int n1 = n / a;
            int n2 = n % a;
            
            answer += (n1 * b);
            n = (n1 * b + n2);
        }
        
        return answer;
    }
}