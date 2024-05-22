import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 1; i <= N+1; i++) {
            if (!map.containsKey(i)) {
                map.put(i, 0);
            }
        }
        
        for (int stage : stages) {
            int value = map.get(stage);
            map.put(stage, value+1);
        }
        
        // 2차원 배열을 포함하는 리스트 생성
        List<double[]> list = new ArrayList<>();
        
        // 전체 인원수
        int total = stages.length;
        
        for (int j = 1; j <= N; j++) {
            int reached = map.get(j);
            if (total > 0) {
                double silpae = (double) reached / total;
                list.add(new double[]{j, silpae});
                // 스테이지에 남아있는 인원수만큼 제거
                total -= reached;    
            } else {
                list.add(new double[]{j, 0});
            }
            
        }
        /**
        for(double[] l : list) {
            System.out.println(Arrays.toString(l));
        }
        **/
        
        list.sort(new Comparator<double[]>() {
            @Override
            public int compare(double[] a, double[] b) {
                if(b[1] != a[1]) {
                    return Double.compare(b[1], a[1]);
                } else {
                    return Double.compare(a[0], b[0]);
                }
            }
        });
        
        int[] answer = new int[N];
        
        for(int i = 0; i < N; i++) {
            answer[i] = (int) list.get(i)[0];
        }
        
        return answer;
    }
}