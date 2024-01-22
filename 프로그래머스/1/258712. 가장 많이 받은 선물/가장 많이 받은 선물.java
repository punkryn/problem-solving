import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        
        int n = friends.length;
        int[][] table = new int[n][n];
        Map<String, Integer> friendsMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            friendsMap.put(friends[i], i);
        }
        
        for (String gift : gifts) {
            String[] ab = gift.split(" ");
            int a = friendsMap.get(ab[0]), b = friendsMap.get(ab[1]);
            table[a][b] += 1;
        }
        
        int[] index = new int[n];
        for (int i = 0; i < n; i++) {
            int s = 0;
            for (int j = 0; j < n; j++) {
                s += table[i][j];
            }
            
            int r = 0;
            for (int j = 0; j < n; j++) {
                r += table[j][i];
            }
            index[i] = s - r;
        }
        
        int[] result = new int[n];
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (table[i][j] > table[j][i]) {
                    result[i] += 1;
                } else if (table[i][j] < table[j][i]) {
                    result[j] += 1;
                } else {
                    if (index[i] > index[j]) {
                        result[i] += 1;
                    } else if (index[i] < index[j]) {
                        result[j] += 1;
                    }
                }
            }
        }
        
        return Arrays.stream(result).max().getAsInt();
    }
}