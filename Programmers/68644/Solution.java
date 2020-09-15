import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};

        int nLen = numbers.length;

        ArrayList<Integer> aList = new ArrayList<>();

        for (int i = 0; i < nLen; i++) {
            for (int j = i + 1; j < nLen; j++) {
                int sum = numbers[i] + numbers[j];

                if (aList.isEmpty()) {
                    aList.add(sum);
                } else {
                    if (!aList.contains(sum)) {
                        aList.add(sum);
                    }
                }
            }
        }

        Collections.sort(aList);

        answer = aList.stream().mapToInt(i -> i).toArray();

        return answer;
    }
}