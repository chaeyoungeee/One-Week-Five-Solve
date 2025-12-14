import java.util.ArrayDeque;

class Solution {
    public ArrayDeque<String> getCards(String[] cards) {
        ArrayDeque<String> dq = new ArrayDeque<>();
        for (String c : cards) {
            dq.addLast(c);
        }
        return dq;
    }
    
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        ArrayDeque<String> c1 = getCards(cards1);
        ArrayDeque<String> c2 = getCards(cards2);
        
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