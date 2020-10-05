class Solution {
    public String solution(String phone_number) {
        String answer = "";

        int endIndex = phone_number.length();
        int startIndex = endIndex-4;

        answer =  phone_number.substring(startIndex, endIndex);

        for (int i = 0; i < startIndex; i++) {
            answer= "*" + answer;
        }

        return answer;
    }
}