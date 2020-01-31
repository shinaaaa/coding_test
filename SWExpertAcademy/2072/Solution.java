import java.util.Scanner;

class Solution {
  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);
    int T;
    T = sc.nextInt();

    for (int test_case = 1; test_case <= T; test_case++) {
      int result = 0;
      int num = 0;
      for (int i = 0; i < 10; i++) {
        num = sc.nextInt();
        if (num % 2 == 1) {
          result = result + num;
        }
      }
      System.out.println("#" + test_case + " " + result);
    }
  }
}