import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < speeds.length; i++) {
            deque.addLast((int)Math.ceil((100-progresses[i])/(double)speeds[i]));
        }
        
        int count;
        while (!deque.isEmpty()) {
            int s = deque.pollFirst();
            count = 1;
            while (!deque.isEmpty() && s >= deque.peekFirst()) {
                deque.pollFirst();
                count += 1;
            }
            answer.add(count);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}