import java.util.ArrayList;
import java.util.HashMap;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    private final int MAX_SIZE = 1_000_001;
    private HashMap<Integer, ArrayList<Integer>> list = new HashMap<>();
    private HashMap<Integer, Integer> inv = new HashMap<>();
    private int[] v = new int[MAX_SIZE];
    
    public int[] solution(int[][] edges) {
        
        int[] answer = new int[4];
                
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            if (!list.containsKey(a)) {
                list.put(a, new ArrayList<>());
            }
            
            if (!list.containsKey(b)) {
                list.put(b, new ArrayList<>());
            }
            
            list.get(a).add(b);
            if (!inv.containsKey(a)) {
                inv.put(a, 0);
            }
            
            if (!inv.containsKey(b)) {
                inv.put(b, 1);
                continue;
            }
            inv.put(b, inv.get(b) + 1);
        }
        
        int created_v = 1;
        int bar = 0, belt = 0;
        
        for (int key : list.keySet()) {
            int size = list.get(key).size();
            int inv_cnt = inv.get(key);
            
            if (size >= 2 && inv_cnt == 0) {
                created_v = key;
                continue;
            }
             
            if (inv_cnt >= 1 && size == 0) {
                bar++;
                v[key] = 2;
                continue;
            }
            
            if (size == 2 && inv_cnt >= 2) {
                belt++;
                v[key] = 3;
                continue;
            }
        }
        
        for (var start : list.get(created_v)) {
            if (v[start] != 0) {
                continue;
            }
            boolean donut = bfs(start);
            if (donut) {
                answer[1]++;
            }
        }
        
        answer[0] = created_v;
        answer[2] = bar;
        answer[3] = belt;
        return answer;
    }
    
    private boolean bfs(int start) {
        v[start] = 1;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            if (list.get(cur).size() == 2) {
                return false;
            }
            
            for (var nxt : list.get(cur)) {
                if (v[nxt] == 2 || v[nxt] == 3) {
                    return false;
                }
                
                if (v[nxt] != 0) {
                    continue;
                }
                
                v[nxt] = 1;
                q.add(nxt);
            }
        }
        return true;
    }
}