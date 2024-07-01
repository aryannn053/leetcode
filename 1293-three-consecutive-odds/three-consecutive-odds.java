class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int maximum = 0;
        int cons = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 != 0) {
                cons += 1;
                maximum = Math.max(maximum, cons);
            } else {
                maximum = Math.max(maximum, cons);
                cons = 0;
            }

            if (maximum >= 3) {
                return true;
            }
        }
        
        return false;
    }
}