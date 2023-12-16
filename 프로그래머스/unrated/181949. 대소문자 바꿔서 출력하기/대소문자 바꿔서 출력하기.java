import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        String ans = "";
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) - 'A' <= 26) {
                ans += (char)((int)a.charAt(i) + 32);
            } else {
                ans += (char)((int)a.charAt(i) - 32);
            }
        }
        System.out.println(ans);
    }
}