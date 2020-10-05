import java.util.*;

class Solution {
    public int[] solution(long n) {
        int[] answer = {};

        String nString = String.valueOf(n);

        String[] nStrings = nString.split("");
        Arrays.sort(nStrings, Collections.reverseOrder());
        answer = Arrays.asList(nStrings).stream().mapToInt(Integer::parseInt).toArray();

        return answer;
    }
}