import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static HashMap<Integer, ArrayList<int[]>> map = new HashMap<>();
    static int N;
    static int Q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        for(int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());

            int p = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            // 양방향 그래프
            map.computeIfAbsent(p, k -> new ArrayList<>()).add(new int[]{q, r});
            map.computeIfAbsent(q, k -> new ArrayList<>()).add(new int[]{p, r});
        }
        // map 에 원소들이 잘 들어갔는지 확인
        //printMap();

        // Q 개의 질문
        for(int j = 0; j < Q; j++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            boolean[] visited = new boolean[N+1];

            // 각 질문에 대해 그래프 탐색 진행
            System.out.println(bfs(k, v, visited));

        }

    }
    static int bfs(int k, int v, boolean[] visited) {
        ArrayDeque<int[]> queue = new ArrayDeque<>();

        ArrayList<int[]> values = map.get(v);
        visited[v] = true;

        int cnt = 0;

        for(int[] value : values) {
            int node = value[0];
            int cost = value[1];

            if (!visited[node] && cost >= k) {
                queue.add(value);
                visited[node] = true;
                cnt++;
            }
        }

        while (!queue.isEmpty()) {
            int[] arr = queue.removeFirst();

            int prevNode = arr[0];

            ArrayList<int[]> nowValues = map.get(prevNode);

            for (int[] nowValue : nowValues) {
                int nowNode = nowValue[0];
                int nowCost = nowValue[1];

                if (!visited[nowNode] && nowCost >= k) {
                    queue.add(nowValue);
                    visited[nowNode] = true;
                    cnt++;
                }
            }


        }
        return cnt;
    }

    static void printMap() {
        for (int key : map.keySet()) {
            ArrayList<int[]> edges = map.get(key);
            System.out.print(key + " : ");
            for (int[] edge : edges) {
                System.out.print(Arrays.toString(edge) + " ");
            }
            System.out.println();
        }
    }
}
