class Solution {
    public int solution(int[][] sizes) {
        
        // 가로 : 큰 길이, 세로 : 작은 길이로 몰기
        for(int i = 0; i < sizes.length; i++) {
            int temp = 0;
            
            if (sizes[i][0] < sizes[i][1]) {
                temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }
        }
        
        int maxX = 0, maxY = 0;
        
        for(int[] arr : sizes) {
            if (maxX < arr[0]) {
                maxX = arr[0];
            }
            if (maxY < arr[1]) {
                maxY = arr[1];
            }
        }
        
        return maxX * maxY;
        
    }
}