class Solution {
    public int removeElement(int[] nums, int val) {
        // No array will be declared - O(1) memory

        int residueLength = 0; // Tracking the length
        int pointer=0;          // Tracking the non-unique value index

        if (nums.length<=0) return 0; // Null Validation
        for (int i = 0; i<nums.length; i++){
            if (nums[i]!=val){
                nums[pointer] = nums[i];
                residueLength++;
                pointer++;
            }

        }
        
        return residueLength;

    }
}
