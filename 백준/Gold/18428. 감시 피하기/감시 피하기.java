import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

import static java.lang.System.exit;

public class Main {
    static String[][] board;
    static List obstacles = new ArrayList();
    static boolean[][] visited;
    static ArrayList teachers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        board = new String[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                board[i][j] = st.nextToken();
            }
        }

        // 방문처리
        visited = new boolean[N][N];

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                visited[i][j] = false;
            }
        }

        //printBoard();

        // 선생님들의 위치 저장하기
        getTeachers(N);

        // 장애물 설치하기
        setUpObstacles(N);
        System.out.println("NO");

    }

    static boolean up(int n, int x, int y) {
        while (y > 0) {
            y -= 1;
            if (board[y][x].equals("A")) {
                return true;
            }
            if (board[y][x].equals("S")) {
                return false;
            }
        }
        return true;
    }

    static boolean down(int n, int x, int y) {
        while (y < n-1) {
            y += 1;
            if (board[y][x].equals("A")) {
                return true;
            }
            if (board[y][x].equals("S")) {
                return false;
            }
        }
        return true;
    }

    static boolean left(int n, int x, int y) {
        while (x > 0) {
            x -= 1;
            if (board[y][x].equals("A")) {
                return true;
            }
            if (board[y][x].equals("S")) {
                return false;
            }
        }
        return true;
    }

    static boolean right(int n, int x, int y) {
        while (x < n-1) {
            x += 1;
            if (board[y][x].equals("A")) {
                return true;
            }
            if (board[y][x].equals("S")) {
                return false;
            }
        }
        return true;
    }

    static List<?> checkTeachers(int N) {
        List checkStudents = new ArrayList();
        for(int i = 0; i < teachers.size(); i++) {
            int[] teacher = (int[]) teachers.get(i);
            int y = teacher[0];
            int x = teacher[1];

            // 상 하 좌 우 체크하기
            if (up(N, x, y) && down(N, x, y) && left(N, x, y) && right(N, x, y)) {
                checkStudents.add(0);
            }
        }
        //System.out.println(checkStudents.toString());
        return checkStudents;
    }

    static void setUpObstacles(int N) {
        if (obstacles.size() == 3) {
            for(int i = 0; i < obstacles.size(); i++) {
                int[] obstacle = (int[]) obstacles.get(i);
                board[obstacle[0]][obstacle[1]] = "A";
            }

            //printBoard();

            // 선생님이 학생들을 볼 수 있는지 체크하기
            List<?> checkTs = checkTeachers(N);

            //System.out.println("걸린 학생 수 " + checkTs.size());
            //System.out.println("선생님 수 : " + teachers.size());

            if (checkTs.size() == teachers.size()) {
                System.out.println("YES");
                exit(0);

            } else {
                for(int i = 0; i < obstacles.size(); i++) {
                    int[] obstacle = (int[]) obstacles.get(i);
                    board[obstacle[0]][obstacle[1]] = "X";
                }
                return;
            }
        }

        for(int i = 0; i < N; i++) {
            for(int j = 0 ; j < N; j++) {
                if (board[i][j].equals("X") && !visited[i][j]) {
                    obstacles.add(new int[]{i, j});
                    visited[i][j] = true;
                    setUpObstacles(N);
                    // 이전으로 되돌리기
                    obstacles.remove(obstacles.size()-1);
                    visited[i][j] = false;
                }
            }
        }
    }

    static void getTeachers(int N) {
        teachers = new ArrayList();
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if (board[i][j].equals("T")) {
                    teachers.add(new int[]{i, j});
                    //System.out.println("선생님의 위치: " + i + " " + j);
                }
            }
        }

    }

    static void printBoard() {
        for (String[] strings : board) {
            for (String string : strings) {
                System.out.print(string + " ");
            }
            System.out.println();
        }
    }
}
