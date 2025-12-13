import java.util.*;

class Solution {
    public boolean valid(String s) {
        List<Character> left = List.of('(', '[', '{');
        List<Character> right = List.of(')', ']', '}');
        Stack<Character> stack = new Stack<>();
        
        for (char i : s.toCharArray()) {
            if (left.contains(i)) {
                stack.push(i);
            } else {
                if (stack.isEmpty()) return false;
                int j = stack.pop();
                for (int k = 0; k < 3; k++) {
                    if (j == left.get(k)) {
                        if (i != right.get(k)) return false;
                    }
                    if (j == right.get(k)) return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
    
    public int solution(String s) {
        int answer = 0;
        
        for (int i = 0; i < s.length(); i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(s.substring(i));
            sb.append(s.substring(0, i));
            
            if (valid(sb.toString())) {
                answer += 1;
            }
        }
        
        return answer;
    }
}