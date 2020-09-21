class Solution {
    public String solution(int n) {
        String answer = "";

        int num = n;

        if (n == 1) {
            return "1";
        } else if (n == 2) {
            return "2";
        } else if (n == 3) {
            return "4";
        }

        while (true) {

            int q = num / 3;
            int r = num % 3;

            if (r == 1) {
                answer = "1" + answer;
            } else if (r == 2) {
                answer = "2" + answer;
            } else if (r == 0) {
                answer = "4" + answer;
                q--;
            }

            if (q == 1) {
                answer = "1" + answer;
                break;
            } else if (q == 2) {
                answer = "2" + answer;
                break;
            } else if (q == 3) {
                answer = "4" + answer;
                break;
            }

            num = q;
        }

        return answer;
    }
}