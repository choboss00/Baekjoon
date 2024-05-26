import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int P;

    static int cnt = 0;
    static HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());

        // N개의 리스트를 관리할 해시맵
        for(int i = 1; i <= N; i++) {
            map.put(i, new ArrayList<>());
        }

        //printMap();

        for(int j = 0; j < N; j++) {
            st = new StringTokenizer(br.readLine());
            // 줄
            int n = Integer.parseInt(st.nextToken());
            // 프렛
            int p = Integer.parseInt(st.nextToken());

            ArrayList<Integer> values = map.get(n);
            // value 가 비어있으면 그대로 넣고 + 1
            if (!isValueEmpty(values, p)) {
                // 크기 비교하기
                valueCompare(values, p);
            }
            //printMap();
        }
        System.out.println(cnt);

    }
    static void valueCompare(ArrayList<Integer> values, int p) {
        while (!values.isEmpty()) {
            // 마지막 원소 pop
            int value = values.remove(values.size()-1);

            if (value < p) {
                values.add(value);
                values.add(p);
                cnt++;
                break;
            } else if (value == p){
                // 원상복구
                values.add(value);
                break;
            } else {
                cnt++;
            }
        }

        // 마지막 원소까지 다 비어버린 경우
        if (values.isEmpty()) {
            values.add(p);
            cnt++;
        }
    }

    static boolean isValueEmpty(ArrayList<Integer> values, int p) {
        if (values.isEmpty()) {
            values.add(p);
            cnt++;
            return true;
        }
        return false;
    }

    static void printMap() {
        for(int key : map.keySet()) {
            System.out.println("key : " + key + " values : " + map.get(key));
        }
    }
}
