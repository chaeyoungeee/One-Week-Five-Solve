class Solution {
    public int solution(int n) {
        int count = 1;
        int sum = 1;
        for (int i = 2; i < n; i++) {
            sum += i;
            int k = n - sum;
            if (k < 0) break;
            if (k % i == 0) count++;
        }
        return count;
    }
}