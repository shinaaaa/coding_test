import java.util.Stack;

class Solution {
    public int solution(String dartResult) {
        int answer = 0;

        int sLen = dartResult.length();
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < sLen; i++) {
            String str = dartResult.substring(i, i + 1);

            int num = 0;

            try {
                num = Integer.parseInt(str);

                if (!stack.isEmpty() && stack.peek() == 1 && num == 0) {
                    stack.pop();
                    stack.add(10);
                } else {
                    stack.add(num);
                }

            } catch (Exception e) {
                int n = 0;
                int m = 0;
                switch (str) {
                    case "S":
                        break;
                    case "D":
                        n = stack.pop();
                        stack.add(n * n);
                        break;
                    case "T":
                        n = stack.pop();
                        stack.add(n * n * n);
                        break;
                    case "*":
                        n = stack.pop();
                        if (!stack.isEmpty()) {
                            m = stack.pop();
                            stack.add(m * 2);
                        }
                        stack.add(n * 2);
                        break;
                    case "#":
                        n = stack.pop();
                        stack.add(n * -1);
                        break;
                }
            }

        }

        while (!stack.isEmpty()) {
            answer += stack.pop();
        }

        return answer;
    }
}