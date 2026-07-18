class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        // speed is from 1,11 this bruteforce,
        // koko can eat one pile max in 1 hours so assuming 1 maxpilesize
        int max=0;
        for(int num : piles ){
            max=Math.max(max,num);
        }
        // for(int i=1; i< max+1 ; i++){
        //    int hours= hours(piles,i);
        //    System.out.println("hours"+hours);
        //    if(hours <= h){
        //     return i;
        //    }
        // }
        int left=1;
        int right=max;
        int mid=0;
        while(left<=right){
            mid = left+(right-left)/2;
            long hours= hours(piles,mid);
            // 1,2,  3, 4,5,6,7,8,9,10,11
            // 23,15,12,8,4,4,4,4,4,4
            //30,11,23,4,20  ,, 1,30 h=6
            // 1,5,10,15,
            if(hours <= h){
                right= mid-1; // search for a smaller valid answer
            } else {
                left=mid+1;
            }

        }

        return left; // first valid answer

    }

    
    long hours(int[] piles, int speed){
        long totalHours=0;
        for(int pile :piles){
            // totalHours= totalHours + (int)Math.ceil((double)pile/speed);
            totalHours += (pile + speed - 1) / speed;
        }
        return totalHours;
    }


}