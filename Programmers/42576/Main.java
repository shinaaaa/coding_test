import java.util.*;

class Solution {
  public String solution(String[] participant, String[] completion) {
    String answer = "";

    Arrays.sort(participant);
    Arrays.sort(completion);

    int n = 0;
    int m = 0;
    while (m < completion.length) {
      if (participant[n].equals(completion[m])) {
        n++;
        m++;
      } else {
        answer = participant[n];
        n++;
      }
      if (n == m) {
        answer = participant[n];
      }
    }

    return answer;
  }
}