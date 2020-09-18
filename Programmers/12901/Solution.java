class Solution {
    public String solution(int a, int b) {
        String answer = "";

        int day = 0;

        int[] m = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 };

        for (int i = 0; i < a-1; i++) {
            day += m[i];
        }

        day += b;

        if (day % 7 == 5) {
            answer = "TUE";
        } else if (day % 7 == 6) {
            answer = "WED";
        } else if (day % 7 == 0) {
            answer = "THU";
        } else if (day % 7 == 1) {
            answer = "FRI";
        } else if (day % 7 == 2) {
            answer = "SAT";
        } else if (day % 7 == 3) {
            answer = "SUN";
        } else if (day % 7 == 4) {
            answer = "MON";
        }

        return answer;
    }
}