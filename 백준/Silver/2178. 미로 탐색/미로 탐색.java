import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static boolean[][] visited;
    static int y;
    static int x;
    static int[][] graph;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        // bufferReader 로 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // StringTokenizer
        StringTokenizer st = new StringTokenizer(br.readLine());
        // x, y 입력값 처리하기
        y = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        graph = new int[y][x];
        visited = new boolean[y][x];

        // 입력값 받아오기
        for(int i=0; i<y; i++) {
            String s = br.readLine();
            for(int j=0; j<x; j++) {
                graph[i][j] = s.charAt(j) - '0';
            }
        }

        bfs(0, 0);
        System.out.println(graph[y-1][x-1]);

    }

    private static void bfs(int x1, int y1) {
        Queue<int[]> que = new LinkedList<>();
        // queue 에 첫번째 위치 넣기
        que.add(new int[]{x1,y1});

        // 방문처리
        visited[y1][x1] = true;

        while ( !que.isEmpty() ) {
            // 현재 위치
            int[] tmp = que.poll();
            int nowX = tmp[0];
            int nowY = tmp[1];
            // 4방향 이동
            for ( int i = 0; i < 4; i++ ) {
                int newX = nowX + dx[i];
                int newY = nowY + dy[i];

                // 예외 처리
                if (newX < 0 || newY < 0 || newX >= x || newY >= y)
                    continue;

                if ( visited[newY][newX] || graph[newY][newX] == 0)
                    continue;

                que.add(new int[] {newX, newY});
                graph[newY][newX] = graph[nowY][nowX] + 1;
                visited[newY][newX] = true;
            }
        }

    }
}

/**
 * 1. 미로탐색 ( 실버 1 )
 * 2. 크기 : n * m
 * 3. 1 : 이동할 수 있는 칸, 0 : 이동할 수 없는 칸
 * - (1,1) 위치에서 출발, (N,M) 위치로 이동
 * - 칸을 셀 때는 시작 위치, 도착 위치도 포함
 * 입력
 * 1. 두 정수 N, M
 * - 각 수들은 붙어서 입력으로 주어짐
 * 출력
 * 1. 지나야하는 최소의 카수 출력하기
 * **/