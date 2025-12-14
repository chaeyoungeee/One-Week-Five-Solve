import java.util.ArrayDeque;
import java.util.Arrays;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        ArrayDeque<String> c1 = new ArrayDeque<>(Arrays.asList(cards1));
        ArrayDeque<String> c2 = new ArrayDeque<>(Arrays.asList(cards2));
        
        for (String g : goal) {
            if (!c1.isEmpty() && c1.peekFirst().equals(g)) {
                c1.pollFirst();
            } else if (!c2.isEmpty() && c2.peekFirst().equals(g)) {
                c2.pollFirst();
            } else {
                return "No";
            }
        }
        return "Yes";
    }
}