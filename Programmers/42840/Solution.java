import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};

        int aLen = answers.length;

        int[] ans1 = { 1, 2, 3, 4, 5 };
        int[] ans2 = { 2, 1, 2, 3, 2, 4, 2, 5 };
        int[] ans3 = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

        int c1 = 0;
        int c2 = 0;
        int c3 = 0;

        int r1 = 0;
        int r2 = 0;
        int r3 = 0;

        for (int i = 0; i < aLen; i++) {
            int r = answers[i];

            if (ans1[c1] == r) {
                r1++;
            }

            if (ans2[c2] == r) {
                r2++;
            }

            if (ans3[c3] == r) {
                r3++;
            }

            c1++;
            c2++;
            c3++;
            if (c1 == ans1.length)
                c1 = 0;
            if (c2 == ans2.length)
                c2 = 0;
            if (c3 == ans3.length)
                c3 = 0;

        }

        int MAX = r1 >= r2 ? r1 : r2;
        MAX = MAX >= r3 ? MAX : r3;

        ArrayList<Integer> aList = new ArrayList<>();

        if (MAX == r1) {
            aList.add(1);
        }
        if (MAX == r2) {
            aList.add(2);
        }
        if (MAX == r3) {
            aList.add(3);
        }

        answer = aList.stream().mapToInt(i -> i).toArray();

        return answer;
    }
}