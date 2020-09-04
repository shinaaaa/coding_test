import java.util.*;

public class Solution {

  class Position {
    int x;
    int y;

    Position(int x, int y) {
      this.x = x;
      this.y = y;
    }

    boolean isValid(int width, int height) {
      if (x < 0 || x >= width)
        return false;
      if (y < 0 || y >= height)
        return false;
      return true;
    }
  }

  public int solution(int[][] maps) {
    // BFS : Queue 너비 우선 탐색
    Queue<Position> queue = new LinkedList<>();

    // 최단 거리를 구해야함으로 맵의 크기 구함
    int mpaHeight = maps.length;
    int mapWidth = maps[0].length;

    int[][] count = new int[mpaHeight][mapWidth]; // 도착한 위치의 카운트
    boolean[][] visited = new boolean[mpaHeight][mapWidth]; // 지나온 길인지 확인

    queue.offer(new Position(0, 0)); // 플레이어 초기값 설정
    count[0][0] = 1; // 초기값 카운트
    visited[0][0] = true; // 지나온 길

    while (!queue.isEmpty()) {
      Position current = queue.poll();

      // 현재 카운트 값
      int currentCount = count[current.y][current.x];

      // 4가지 경우 기본틀, 동서남북
      final int[][] moving = { { 0, -1 }, { 0, 1 }, { -1, 0 }, { 1, 0 } };
      for (int i = 0; i < moving.length; i++) {
        Position moved = new Position(current.x + moving[i][0], current.y + moving[i][1]); // 이동하게될 위치
        if (!moved.isValid(mapWidth, mpaHeight))
          continue; // 지도 밖을 벗어 나는 경우
        if (visited[moved.y][moved.x])
          continue; // 이미 방문한 경우
        if (maps[moved.y][moved.x] == 0)
          continue; // 이동하는 방향이 벽이 아닌 경우
        count[moved.y][moved.x] = currentCount + 1; // 이동하게될 카운트 값
        visited[moved.y][moved.x] = true;
        queue.offer(moved);
      }
    }
    int answer = count[mpaHeight - 1][mapWidth - 1];
    if (answer == 0)
      return -1;
    return answer;
  }
}