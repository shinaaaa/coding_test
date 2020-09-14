import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;

        int bHeigth = board.length;
        int mLen = moves.length;

        Stack<Integer> items = new Stack();

        for (int i = 0; i < mLen; i++) {
            int index = moves[i] - 1;
            int item = 0;
            for (int j = 0; j < bHeigth; j++) {
                if (board[j][index] != 0) {
                    item = board[j][index];
                    board[j][index] = 0;
                    break;
                }
            }
            if (!items.isEmpty() && items.peek() == item) {
                items.pop();
                answer += 2;
            } else if (item != 0) {
                items.push(item);
            }
        }

        return answer;
    }
}