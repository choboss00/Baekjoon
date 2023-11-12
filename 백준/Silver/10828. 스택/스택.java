import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 스캐너
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 명령의 수 ( 1 ~ 10000 이므로 int 형으로 처리 )
        int t = Integer.parseInt(br.readLine());
        // stack
        Stack<String> stack = new Stack<>();

        for(int i = 0; i < t; i ++) {
            // 입력 받기
            st = new StringTokenizer(br.readLine(), " ");

            String checkFunction = st.nextToken();

            // 리스트의 길이가 1 일경우, 2일 경우 쪼개기
            if (checkFunction.equals("push")) {
                stack.add(st.nextToken());
            } else {
                stackFunction(stack, checkFunction);
            }
        }
    }

    private static void stackFunction(Stack<String> stack, String s) {
        if ( s.equals("top") ) {
            if ( stack.empty() ) {
                System.out.println(-1);
            }
            else {
                System.out.println(stack.peek());
            }
        }
        else if ( s.equals("size") ) {
            System.out.println(stack.size());
        }
        else if ( s.equals("pop") ) {
            if ( stack.empty() ) {
                System.out.println(-1);
            }
            else {
                System.out.println(stack.pop());
            }
        }
        else if ( s.equals("empty") ) {
            if ( stack.empty() ) {
                System.out.println(1);
            }
            else {
                System.out.println(0);
            }
        }
    }

}

/**
 * 1. 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령 처리 프로그램 작성하기
 * 2. push, pop, size, empty, top
 * **/