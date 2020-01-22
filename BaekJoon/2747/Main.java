import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int count = scan.nextInt();
    scan.close();

    int num = 0;
    int num1 = 1;

    while (count > 0) {
      int n = num;
      num = num1;
      num1 = n + num1;
      count--;
    }
    System.out.print(num);
  }
}