class Solution {
    public int removeDuplicates(int[] nums) {

        // No extra array -> O(1)
        int uniqueNumbers = 0; // Keep the lenght count.
        int counter = 0;       // Keep track of the redundant integer index.

        if (nums.length >0){  // check whether the array is null.
            uniqueNumbers = 1;
            counter = 1;
        }
        for (int i = 1; i< nums.length; i++){
            if (nums[i]!=nums[i-1]){
                uniqueNumbers++;
                nums[counter] = nums[i]; // Remove the duplicate element by assigning the next                                            //  unique element.
                counter++;

            }



        }




        return uniqueNumbers;

    }
}
