import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] arr = br.readLine().split("");

        int ans = 0;

        for(String s : arr) {
            int num = s.charAt(0);

            if (num >= 65 && num <= 67) {
                ans += 3;
            } else if (num >= 68 && num <= 70) {
                ans += 4;
            } else if (num >= 71 && num <= 73) {
                ans += 5;
            } else if (num >= 74 && num <= 76) {
                ans += 6;
            } else if (num >= 77 && num <= 79) {
                ans += 7;
            } else if (num >= 80 && num <= 83) {
                ans += 8;
            } else if (num >= 84 && num <= 86) {
                ans += 9;
            } else if (num >= 87 && num <= 90) {
                ans += 10;
            }
        }

        System.out.println(ans);
    }
}
