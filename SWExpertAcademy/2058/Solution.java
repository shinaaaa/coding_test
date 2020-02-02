import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
  public static void main(String args[]) throws Exception {

    Scanner sc = new Scanner(System.in);
    String T = sc.nextLine();
    sc.close();

    int result = 0;
    for (int i = 0; i < T.length(); i++) {
      result = result + Integer.parseInt(T.substring(i, i + 1));
    }

    System.out.print(result);
  }
}