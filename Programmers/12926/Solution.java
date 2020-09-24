class Solution {
    public String solution(String s, int n) {
        String answer = "";

        String[] arr = s.split("");

        for (String item : arr) {
            if (!item.equals(" ")) {
                int ascii = (int) item.charAt(0);
                int r = ascii + n;

                if ((ascii < 91 && 90 < r) || (96 < ascii && ascii < 123 && 122 < r)) {
                    r = r - 26;
                }

                char c = (char) (r);

                answer += String.valueOf(c);

            } else {
                answer += item;
            }
        }

        return answer;
    }
}