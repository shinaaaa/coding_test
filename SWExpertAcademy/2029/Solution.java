import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
  public static void main(String args[]) throws Exception {

    Scanner sc = new Scanner(System.in);
    int T;
    T = sc.nextInt();
    int result = 0;

    for (int test_case = 1; test_case <= T; test_case++) {
      result = result + test_case;
    }
    System.out.print(result);
  }
}