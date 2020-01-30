import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int range = scan.nextInt();
    ArrayList<Integer> arrayList = new ArrayList<Integer>();

    for (int i = 0; i < range; i++) {
      arrayList.add(scan.nextInt());
    }
    scan.close();
    arrayList.sort(null);
    for (int i = 0; i < arrayList.size(); i++) {
      System.out.println(arrayList.get(i));
    }
  }
}

/*
 * import java.util.*;
 * 
 * public class Main { public static void main(String[] args) {
 * 
 * } }
 */