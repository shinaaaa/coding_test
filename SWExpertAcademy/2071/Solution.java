import java.util.Scanner;

class Solution {
  public static void main(String args[]) throws Exception {

    Scanner sc = new Scanner(System.in);
    int T;
    T = sc.nextInt();
    /*
     * 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
     */

    for (int test_case = 1; test_case <= T; test_case++) {
      int result = 0;

      for (int i = 0; i < 10; i++) {
        int num = sc.nextInt();
        result = result + num;
      }

      if (result % 10 > 4) {
        result = result / 10;
        System.out.println("#" + test_case + " " + (result + 1));
      } else {
        result = result / 10;
        System.out.println("#" + test_case + " " + result);
      }
    }
  }
}