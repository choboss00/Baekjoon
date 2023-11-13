import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static boolean[] visited = new boolean[9];
    public static int[] arr = new int[9];

    public static void main(String[] args) throws IOException {
        // bufferReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for ( int i = 0; i < 9; i++ ) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        dfs(0, 0);


    }

    private static void dfs(int start, int depth) {
        if ( depth == 7 ) {
            int sum = 0;
            StringBuilder sb = new StringBuilder();

            for ( int i = 0; i < 9; i ++ ) {
                // 방문처리가 된 경우
                if ( visited[i] ) {
                    sum += arr[i];
                    sb.append(arr[i]).append("\n");
                }
            }
            if ( sum == 100 ) {
                System.out.println(sb.toString());
                System.exit(0);
            }
        }

        for ( int i = start; i < 9; i++ ) {
            visited[i] = true;
            dfs(i+1, depth+1);
            visited[i] = false;
        }

    }

}

/**
 * 1. 난쟁이가 일곱명이 아닌 아홉명
 * 2. 일곱 난쟁이의 키의 합이 100
 * 3. 아홉 난쟁이의 키가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램 작성하기
 * - 가능한 정답이 여러가지인 경우에는 아무거나 출력
 * - 일곱 난쟁이의 키를 오름차순으로 출력하기
 * **/