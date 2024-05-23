import java.io.*;
import java.util.ArrayDeque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[][] board;
    static int[][] direction = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        // 성의 크기, 공주에게 걸린 저주
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        board = new int[N][M];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for(int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // 입력값 검증
        //printBoard(N, M);

        // 현 위치에서 bfs 탐색 진행
        int ans1 = bfs(N, M);

        //printBoard(N, M);

        clearBoard(N, M);

        //printBoard(N, M);

        // 검이 있을 때 탐색 진행
        int[] ans2 = bfs2(N, M);

        int x = ans2[0];
        int y = ans2[1];
        int ans = board[y][x] + Math.abs(M - x - 1) + Math.abs(N - y - 1);

        if (ans1 > 0 && ans > 0) {
            int cnt = Math.min(ans1, ans);

            if (cnt <= T) {
                System.out.println(cnt);
            } else {
                System.out.println("Fail");
            }

        } else if (ans1 > 0 && ans == 0) {
            if (ans1 <= T) {
                System.out.println(ans1);
            } else {
                System.out.println("Fail");
            }
        } else if (ans1 == 0 && ans > 0) {
            if (ans <= T) {
                System.out.println(ans);
            } else {
                System.out.println("Fail");
            }
        } else {
            System.out.println("Fail");
        }



    }

    static int[] bfs2(int n, int m) {
        ArrayDeque<int[]> queue = new ArrayDeque<>();

        queue.add(new int[]{0, 0});
        board[0][0] = 10;
        while(!queue.isEmpty()) {
            int[] arr = queue.removeFirst();
            int x = arr[0];
            int y = arr[1];

            for(int[] d : direction) {
                int nx = x + d[0];
                int ny = y + d[1];

                // 예외 처리
                if ((0 <= nx && nx < m) && (0 <= ny && ny < n)) {

                    if (board[ny][nx] == 2) {
                        board[ny][nx] = board[y][x] - 9;
                        return new int[]{nx, ny};
                    }

                    if (board[ny][nx] == 0) {
                        board[ny][nx] = board[y][x] + 1;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }
        return new int[]{m-1, n-1};
    }

    static void clearBoard(int n, int m) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if (board[i][j] >= 10) {
                    board[i][j] = 0;
                }
            }
        }
    }
    static int bfs(int n, int m) {
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        // 초기 좌표
        queue.add(new int[]{0, 0});
        board[0][0] = 10;

        while (!queue.isEmpty()) {
            int[] arr = queue.removeFirst();
            int x = arr[0];
            int y = arr[1];

            for(int[] d : direction) {
                int nx = x + d[0];
                int ny = y + d[1];

                // 예외 처리
                if ((0 <= nx && nx < m) && (0 <= ny && ny < n)) {
                    if (nx == m-1 && ny == n-1) {
                        return board[y][x] - 9;
                    }

                    if (board[ny][nx] == 0) {
                        board[ny][nx] = board[y][x] + 1;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }

        }
        return board[n-1][m-1];
    }

    static void printBoard(int n , int m) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                System.out.print(board[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
