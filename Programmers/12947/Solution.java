class Solution {
    public boolean solution(int x) {

        String num = Integer.toString(x);

        String[] arr = num.split("");

        int n = 0;
        for (String item : arr) {
            n += Integer.parseInt(item);
        }
        
        return x%n == 0 ? true : false;
    }
}