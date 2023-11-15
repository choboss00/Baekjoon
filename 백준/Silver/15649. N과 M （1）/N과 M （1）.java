import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static int[] arr;
    public static boolean[] visited;
    public static Stack<Integer> stack = new Stack<Integer>();;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        visited = new boolean[n];

        for (int i = 1; i <= n; i++) {
            arr[i-1] = i;
        }
        // depth, 현재 level
        back(m, 0);



    }

    private static void back(int depth, int level) {
        // stack 의 길이가 depth 까지 도달 했을 경우
        if ( stack.size() == depth ) {
            for (int i = 0; i < stack.size(); i++) {
                System.out.print(stack.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < arr.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                stack.add(arr[i]);
                back(depth, i+1);
                stack.pop();
                visited[i] = false;
            }

        }
    }
}
/**
 * 1. N 과 M
 * 1 ~ N 까지 자연수 중에서 중복 없이 M 개를 고른 수열
 *
 * **/
