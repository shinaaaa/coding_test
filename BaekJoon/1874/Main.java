import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int range = scan.nextInt();

    Stack<Integer> stack = new Stack<Integer>();
    ArrayList<String> arrayList = new ArrayList<String>();

    int num = 1;
    boolean result = true;

    for (int i = 0; i < range; i++) {
      int n = scan.nextInt();

      while (true) {
        if (stack.size() == 0 || stack.peek() <= n) {
          if (stack.size() == 0 || stack.peek() != n) {
            stack.push(num);
            arrayList.add("+");
            num++;
          } else if (stack.peek() == n) {
            stack.pop();
            arrayList.add("-");
            break;
          }
        } else {
          if (!stack.empty()) {
            result = false;
            break;
          }
          stack.pop();
          arrayList.add("-");
        }
      }
    }
    if (result) {
      for (int i = 0; i < arrayList.size(); i++) {
        System.out.println(arrayList.get(i));
      }
    } else {
      System.out.println("NO");
    }
    scan.close();
  }
}