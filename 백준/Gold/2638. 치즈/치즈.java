import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.*;

public class Main {

    static int[][] board;
    static boolean[][] visited;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        board = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //printNowBoard(N, M);

        findOutsidePaper(0, 0);

        //printNowBoard(N, M);

        // 치즈 집합 구하기
        Set<int[]> cheeseSet = makeSet(N, M);

        System.out.print(bfs(N, M, cheeseSet));
    }

    public static int bfs(int N, int M, Set<int[]> cheeseSet) {
        int ans = 0;

        while (!cheeseSet.isEmpty()) {
            Set<int[]> minusCheeseSet = new HashSet<>();

            for (int[] pos : cheeseSet) {
                int cnt = 0;

                int x = pos[0];
                int y = pos[1];

                int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

                for (int[] dir : directions) {
                    int dx = dir[0];
                    int dy = dir[1];

                    int nx = x + dx;
                    int ny = y + dy;

                    if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
                        if (board[ny][nx] == 2) {
                            cnt++;
                        }
                    }
                }
                if (cnt >= 2) {
                    minusCheeseSet.add(pos);
                }
            }

            // 녹은 치즈를 기준으로 탐색하기
            for (int[] pos : minusCheeseSet) {
                int x = pos[0];
                int y = pos[1];

                findOutsidePaper(x, y);
            }

            cheeseSet.removeAll(minusCheeseSet);
            ans++;
        }
        return ans;

    }

    public static Set<int[]> makeSet(int N, int M) {
        Set<int[]> returnSet = new HashSet<>();

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (board[y][x] == 1) {
                    returnSet.add(new int[]{x, y});
                }
            }
        }

        return returnSet;
    }

    private static void findOutsidePaper(int x, int y) {
        Queue<int[]> queue = new ArrayDeque<>();

        queue.add(new int[]{x, y});

        // 바깥 처리
        visited[y][x] = true;
        board[y][x] = 2;

        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int x1 = pos[0];
            int y1 = pos[1];

            int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

            for (int[] dir : directions) {
                int dx = dir[0];
                int dy = dir[1];

                int nx = x1 + dx;
                int ny = y1 + dy;
                    if (nx >= 0 && nx < board[0].length && ny >= 0 && ny < board.length) {
                        if (!visited[ny][nx] && board[ny][nx] == 0) {
                            board[ny][nx] = 2;
                            visited[ny][nx] = true;
                            queue.add(new int[]{nx, ny});
                        }
                    }
            }
        }
    }

    private static void printNowBoard(int N, int M) {
        System.out.println("현재 보드 상태 ");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }
}
