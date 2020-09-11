import java.util.*;

public class Solution {

  class Airport {
    String start;
    String destination;

    Airport(String start, String destination) {
      this.start = start;
      this.destination = destination;
    }
  }

  public String[] solution(String[][] tickets) {
    String[] answer = new String[tickets.length + 1];

    // BFS : Queue 너비 우선 탐색
    Queue<Airport> queue = new LinkedList<>();

    int ticketsLen = tickets.length; // 가지고 있는 티켓의 수
    boolean[] visited = new boolean[ticketsLen]; // 지나온 길인지 확인
    answer[0] = "ICN";
    int count = 1;

    for (int i = 0; i < ticketsLen; i++) {
      if (tickets[i][0].equals("ICN")) {
        queue.offer(new Airport(tickets[i][0], tickets[i][1]));
        visited[i] = true;

        bfs(queue, ticketsLen, tickets, visited, answer, count);
      }
    }
    return answer;
  }

  public void bfs(Queue<Airport> queue, int ticketsLen, String[][] tickets, boolean[] visited, String[] answer,
      int count) {
    while (!queue.isEmpty()) {
      Airport airport = queue.poll();

      for (int i = 0; i < ticketsLen; i++) {
        if (visited[i] == false) {
          if (airport.destination.equals(tickets[i][0])) {
            queue.offer(new Airport(tickets[i][0], tickets[i][1]));
            visited[i] = true;
            answer[count] = tickets[i][1];
            count++;
          }
        }
      }
    }
  }
}