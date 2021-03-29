import java.io.*;
import java.util.LinkedList;
import java.util.ListIterator;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        LinkedList<Character> list = new LinkedList<>();
        String s = bufferedReader.readLine();

        char[] chars = s.toCharArray();
        for (char c : chars) {
            list.add(c);
        }

        ListIterator<Character> iterator = list.listIterator();

        // iterator : 반복자
        // Container 안에 있는 값들을 하나씩 꺼낸다.
        while (iterator.hasNext()) {
            iterator.next();
        }

        int count = Integer.parseInt(bufferedReader.readLine());

        for (int i = 0; i < count; i++) {
            String str = bufferedReader.readLine();

            char com = str.charAt(0);
            switch (com) {
                case 'L':
                    if (iterator.hasPrevious()) {
                        iterator.previous();
                    }
                    break;
                case 'D':
                    if (iterator.hasNext()) {
                        iterator.next();
                    }
                    break;
                case 'B':
                    if (iterator.hasPrevious()) {
                        iterator.previous();
                        iterator.remove();
                    }
                    break;
                case 'P':
                    iterator.add(str.charAt(2));
                    break;
            }
        }

        for (Character item : list) {
            bufferedWriter.write(item);
        }
        bufferedWriter.flush();
        bufferedWriter.close();
    }
}