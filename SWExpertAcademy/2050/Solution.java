import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);
    String T;
    T = sc.next();

    for (int i = 0; i < T.length(); i++) {
      char str = T.substring(i, i + 1).charAt(0);
      System.out.print((int) str - 64 + " ");
    }
  }
}