class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        // Set<List<Integer>> resultSet= new HashSet<>();
        
        // for(int i =0 ; i< nums.length ; i++){
        //     Set<Integer> set = new HashSet<>();
        //     for(int j =i+1 ; j< nums.length ; j++){
        //         if(set.contains(-nums[i] - nums[j])){
        //             resultSet.add(Arrays.asList(-nums[i]-nums[j],nums[i],nums[j]));
        //         }
        //         set.add(nums[j]);
        //     }
        // }

        // List<List<Integer>> result=new ArrayList();

        // for(List sums: resultSet){
        //     result.add(sums);
        // }
        

        // return result;


        // Fix one element till length-2 skip duplicate i 
        // left =i +1 right=n-1 
        // Arrays.sort()
        // sum < target  left++
        // sum > taregt right--
        // sum == target  left++ right --
            // Arrays.asList(num[i],num[left],num[right]);
            // eleminate duplicates left < right num[left] == nums[left-1]
            // eleminate duplicates left < right num[right] == nums[right-1] 
        Arrays.sort(nums);
        System.out.println("nums ->" +Arrays.toString(nums));
        List<List<Integer>> result=new ArrayList<>();
        for(int i=0; i< nums.length-2; i++) {
            int left=i+1;
            int right=nums.length-1;
            // Skip duplicate first element
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            while(left < right ){
                int sum=nums[i]+nums[left]+nums[right];
                if(sum < 0) left++;
                else if(sum > 0) right--;
                else {
                    result.add(Arrays.asList(nums[i],nums[left],nums[right]));
                    left++;
                    right--;
                    while(left < right && nums[left]==nums[left-1]){
                        left++;
                    }
                    while(left < right && nums[right]==nums[right+1]){
                        right--;
                    }
                }

            }
        }
        return result ;

        
    }
}