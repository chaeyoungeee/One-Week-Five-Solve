class Solution {
    boolean solution(String s) {
        int count = 0;
        
        for (char i : s.toCharArray()) {
            if (i == '(') {
                count += 1;
            } else {
                if (count <= 0) return false;
                count -= 1;
            }
        }

        return count == 0 ? true : false;
    }
}