import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        for (Character w : a.toCharArray()) {
            System.out.println(w);
        }
    }
}