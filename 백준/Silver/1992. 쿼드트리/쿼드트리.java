import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int[][] board;
    static int N;

    static ArrayList<String> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        // 생성
        board = new int[N][N];

        for(int i = 0; i < N; i++) {
            String[] strArr = br.readLine().split("");

            for(int j = 0; j < strArr.length; j++) {
                board[i][j] = Integer.parseInt(strArr[j]);
            }

        }

        // board 출력
        //printBoard();

        int num0Cnt = 0;
        int num1Cnt = 0;

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if (board[i][j] == 0) {
                    num0Cnt++;
                } else {
                    num1Cnt++;
                }
            }
        }

        if (num0Cnt == 0 && num1Cnt > 0) {
            list.add("1");
        } else if (num1Cnt == 0 && num0Cnt > 0) {
            list.add("0");
        } else {
            // 처음 위치 넣기
            list.add("(");
            탐색(0, N/2, 0, N/2);
            탐색(N/2, N, 0, N/2);
            탐색(0, N/2, N/2, N);
            탐색(N/2, N, N/2, N);
            list.add(")");
        }

        for(String s : list) {
            System.out.print(s);
        }
    }

    static void 탐색(int x0, int x1, int y0, int y1) {
        int num0Cnt = 0;
        int num1Cnt = 0;

        //System.out.println("x0 : " + x0 + " x1 : " + x1 + " y0 : " + y0 + " y1 : " + y1);

        for (int y = y0; y < y1; y++) {
            for (int x = x0; x < x1; x++) {
                if (board[y][x] == 0) {
                    num0Cnt++;
                } else {
                    num1Cnt++;
                }
            }
        }

        //System.out.println("0의 갯수 : " + num0Cnt);
        //System.out.println("1의 갯수 : " + num1Cnt);

        if (num0Cnt == 0 && num1Cnt == 0) {
            return;
        }
        if (num0Cnt == 0 && num1Cnt > 0) {
            list.add("1");
        } else if (num1Cnt == 0 && num0Cnt > 0) {
            list.add("0");
        } else {
            // 처음 위치 넣기
            list.add("(");
            탐색(x0, (x0+x1)/2, y0, (y0+y1)/2);
            탐색((x0+x1)/2, x1, y0, (y0+y1)/2);
            탐색(x0, (x0+x1)/2, (y0+y1)/2, y1);
            탐색((x0+x1)/2, x1, (y0+y1)/2, y1);
            list.add(")");
        }
    }

    static void printBoard() {
        for(int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(board[i]));
        }
    }
}
