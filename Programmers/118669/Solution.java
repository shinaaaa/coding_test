import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    private static ArrayList<Path>[] list;
    private static int[] distance;
    private static boolean[] isSummit;

    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        list = new ArrayList[n + 1];
        distance = new int[n + 1];
        isSummit = new boolean[n + 1];

        //초기화


        for (int i = 0; i <= n; i++) {
            list[i] = new ArrayList<>();
            distance[i] = Integer.MAX_VALUE;
        }

        for (int summit : summits) {
            isSummit[summit] = true;
        }

        for (int[] path : paths) {
            list[path[0]].add(new Path(path[1], path[2]));
            list[path[1]].add(new Path(path[0], path[2]));
        }

        for (int gate : gates) {
            dijkstra(gate);
        }

        int[] answer = {0, Integer.MAX_VALUE};
        Arrays.sort(summits);   // 산봉우리가 가장 낮은 번호 순서로 정렬
        for (int summit : summits) {
            if (answer[1] <= distance[summit]) continue;
            answer[0] = summit;
            answer[1] = distance[summit];
        }
        return answer;
    }

    private static void dijkstra(int gate) {
        distance[gate] = 0;
        PriorityQueue<Path> pq = new PriorityQueue<>();
        pq.add(new Path(gate, 0));
        while (!pq.isEmpty()) {
            Path now = pq.poll();
            if (distance[now.node] < now.weight) continue;
            for (Path next : list[now.node]) {
                int w = Math.max(now.weight, next.weight);
                if (distance[next.node] <= w) continue;
                distance[next.node] = w;
                if (isSummit[next.node]) continue;
                pq.add(new Path(next.node, w));
            }
        }
    }

    private static class Path implements Comparable<Path> {
        int node;
        int weight;

        public Path(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }

        @Override
        public int compareTo(Path p) {
            return this.weight - p.weight;
        }
    }
}