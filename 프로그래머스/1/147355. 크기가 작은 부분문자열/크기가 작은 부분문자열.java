class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        
        int pSize = p.length();
        long pLong = Long.parseLong(p);
        char[] arr = t.toCharArray();
        
        for (int i = 0; i <= arr.length-pSize; i++) {
            StringBuilder sb = new StringBuilder();
            
            for (int j = i; j < i+pSize; j++) {
                sb.append(arr[j]);
            }
            
            long sbLong = Long.parseLong(sb.toString());
            //System.out.println(sbLong);
            if (sbLong <= pLong) {
                answer++;
            }
            
            
        }
        
        return answer;
    }
}