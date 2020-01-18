import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int range = scan.nextInt();
    ArrayList<Integer> arrayList = new ArrayList<Integer>();
    for (int i = 0; i < range; i++) {
      arrayList.add(scan.nextInt());
    }

    int range2 = scan.nextInt();
    ArrayList<Integer> arrayList2 = new ArrayList<Integer>();
    for (int i = 0; i < range2; i++) {
      arrayList2.add(scan.nextInt());
    }
    for (int i = 0; i < range2; i++) {
      boolean bool = false;
      for (int j = 0; j < range; j++) {
        if (arrayList2.get(i) == arrayList.get(j)) {
          bool = true;
          break;
        }
        bool = false;
      }
      if (bool) {
        System.out.println(1);
      } else {
        System.out.println(0);
      }
    }
    scan.close();
  }
}