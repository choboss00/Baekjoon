import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        int T = Integer.parseInt(br.readLine());

        for(int i = 0; i < T; i++) {
            String[] arr = br.readLine().split("");

            ArrayDeque<String> left = new ArrayDeque<>();
            ArrayDeque<String> right = new ArrayDeque<>();
            for(String s : arr) {
                if (s.equals("<")) {
                    if (left.size() == 0) {
                        continue;
                    }
                    right.addFirst(left.removeLast());
                } else if (s.equals(">")) {
                    if (right.size() == 0) {
                        continue;
                    }
                    left.add(right.removeFirst());
                } else if (s.equals("-")) {
                    if (left.size() > 0) {
                        left.removeLast();
                    }
                } else {
                    left.add(s);
                }
                //System.out.println("left : " + left);
                //System.out.println("right : " + right);
            }

            StringBuilder s = new StringBuilder();

            for(String l : left) {
                s.append(l);
            }

            for(String r : right) {
                s.append(r);
            }

            System.out.println(s);

        }

    }
}
