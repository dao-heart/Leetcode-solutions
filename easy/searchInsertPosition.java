class Solution {
    public int searchInsert(int[] nums, int target) {
        int pointer = 0;

        if (nums.length<=0) return 0; // Null Validation



        for (int i = 0;i<nums.length;i++){

            if (nums[i]<target){
                pointer++;
                System.out.println(pointer+"-->"+i);
            }

            if(nums[i]>target){
                System.out.println(pointer+"-->"+i);
                return pointer;
            }
            if(nums[i]==target) {
                pointer=i;
            }

        }

        return pointer;
