import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    ArrayList<Integer> arrayList = new ArrayList<Integer>();
    int num = scan.nextInt();

    String str = Integer.toString(num);

    for (int i = 0; i < str.length(); i++) {
      arrayList.add(Integer.parseInt(str.substring(i, i + 1)));
    }

    for (int i = 9; i > -1; i--) {
      for (int j = arrayList.size() - 1; j > -1; j--) {
        if (arrayList.get(j).equals(i)) {
          System.out.print(arrayList.get(j));
        }
      }
    }
  }
}