import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);
    int T;
    T = sc.nextInt();

    ArrayList<Integer> arrayList = new ArrayList<Integer>();

    for (int test_case = 1; test_case <= T; test_case++) {
      arrayList.add(sc.nextInt());
    }
    arrayList.sort(null);
    System.out.print(arrayList.get(arrayList.size() / 2));
  }
}