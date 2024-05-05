import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int[][] n_list = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            n_list[i][0] = Integer.parseInt(st.nextToken());
            n_list[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(n_list, Comparator.comparingInt(a -> a[0]));

        int ans = 0;
        int range = 0;

        for (int i = 0; i < N; i++) {
            if (n_list[i][0] > range) {
                range = n_list[i][0];
            }

            if (n_list[i][1] > range) {
                while (n_list[i][1] > range) {
                    range += L;
                    ans++;
                }
            }
        }


        System.out.println(ans);
        br.close();

    }
}
