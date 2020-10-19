class Solution {
    boolean solution(String s) {

        int sLen = s.length();

        if (s.charAt(0) == ')' || s.charAt(sLen - 1) == '(' || sLen % 2 != 0)
            return false;

        int count = 0;

        for (int i = 0; i < sLen; i++) {
            if (s.charAt(i) == '(')
                count++;
            else
                count--;

            if (count < 0)
                return false;
        }

        if (count == 0)
            return true;
        else
            return false;
    }
}