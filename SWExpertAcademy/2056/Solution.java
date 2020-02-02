import java.util.Scanner;

class Solution {
  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);
    int T;
    String str;
    T = sc.nextInt();
    sc.nextLine();
    for (int test_case = 1; test_case <= T; test_case++) {
      str = sc.nextLine();
      String year = str.substring(0, 4);
      String month = str.substring(4, 6);
      String day = str.substring(6, 8);
      if (Integer.parseInt(month) > 12 || Integer.parseInt(month) <= 0) {
        System.out.println("#" + test_case + " " + "-1");
      } else if (Integer.parseInt(day) <= 0 || Integer.parseInt(day) > 31) {
        System.out.println("#" + test_case + " " + "-1");
      } else {
        if (Integer.parseInt(month) == 4 || Integer.parseInt(month) == 6 || Integer.parseInt(month) == 9
            || Integer.parseInt(month) == 11) {
          if (Integer.parseInt(day) == 31) {
            System.out.println("#" + test_case + " " + "-1");
          } else {
            System.out.println("#" + test_case + " " + year + "/" + month + "/" + day);
          }
        } else if (Integer.parseInt(month) == 2) {
          if (Integer.parseInt(day) > 28) {
            System.out.println("#" + test_case + " " + "-1");
          } else {
            System.out.println("#" + test_case + " " + year + "/" + month + "/" + day);
          }
        } else {
          System.out.println("#" + test_case + " " + year + "/" + month + "/" + day);
        }
      }
    }
  }
}