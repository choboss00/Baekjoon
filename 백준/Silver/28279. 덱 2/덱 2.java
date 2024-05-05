import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        Deque<Integer> deque = new LinkedList<>();

        int N = Integer.parseInt(st.nextToken());

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken());

            switch (idx){
                case 1 : //명령어 1 X : 덱의 앞에 넣는다
                    deque.addFirst(Integer.parseInt(st.nextToken()));
                    break;
                case 2 : //명령어 2 X : 덱의 뒤에 넣는다
                    deque.addLast(Integer.parseInt(st.nextToken()));
                    break;
                case 3 : //명령어 3 : 덱의 맨 앞의 정수를 빼서 출력한다.(없다면 -1)
                    sb.append(deque.isEmpty()? -1 : deque.pollFirst()).append("\n");
                    break;
                case 4 : //명령어 4 : 덱의 맨 뒤의 정수를 빼서 출력한다.(없다면 -1)
                    sb.append(deque.isEmpty()? -1 : deque.pollLast()).append("\n");
                    break;
                case 5 : //명령어 5 : 덱에 들어있는 정수의 개수 출력
                    sb.append(deque.size()).append("\n");
                    break;
                case 6 : //명령어 6 : 덱이 비어있으면 1 출력 비어있지 않으면 0
                    sb.append(deque.isEmpty()? 1 : 0).append("\n");
                    break;
                case 7 : //명령어 7 : 덱에 정수가 있다면 맨 앞의 정수를 출력(없다면 -1)
                    sb.append(deque.isEmpty()? -1 :deque.peekFirst()).append("\n");
                    break;
                case 8 : //명령어 8 : 덱에 정수가 있다면 맨 뒤의 정수를 출력(없다면 -1)
                    sb.append(deque.isEmpty()? -1 : deque.peekLast()).append("\n");
                    break;
            }

        }
        
        br.close();
        System.out.println(sb);

    }
}
