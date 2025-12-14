import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int n = board.length;
        int count = 0;
        Stack<Integer> stack = new Stack<>();
        
        for (int m : moves) {
            for (int i = 0; i < n; i++) {
                int k = board[i][m-1];
                if (k == 0) continue;
                if (!stack.isEmpty() && k == stack.peek()) {
                    count += 1;
                    while (!stack.isEmpty() && k == stack.peek()) {
                        stack.pop();
                        count += 1;
                    }
                } else {
                    stack.push(k);
                }
                board[i][m-1] = 0;
                break;
            }
        }
        
        return count;
    }
}