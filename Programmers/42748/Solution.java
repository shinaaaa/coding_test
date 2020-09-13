import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int i = 0; i < commands.length; i++) {
            int start = commands[i][0] - 1;
            int last = commands[i][1];
            int index = commands[i][2] - 1;

            int[] array1 = Arrays.copyOfRange(array, start, last);
            if (array1 != null) {
                Arrays.sort(array1);
            }

            answer[i] = array1[index];

        }
        return answer;
    }
}