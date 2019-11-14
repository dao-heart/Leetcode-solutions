public class Solution extends VersionControl {
    public int firstBadVersion(int n) {

        int beg =1;
        int end = n;
        int midpoint=0;

        while (beg<end){            
           midpoint = beg + (end-beg)/2;
            if (isBadVersion(midpoint)){
                end = midpoint;
            }
            else {

                beg = midpoint+1;
            }

        }
        return beg;

    }
}
