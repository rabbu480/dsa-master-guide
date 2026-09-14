class Solution {

    List<List<Integer>>  result = new ArrayList<>();
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<Integer> path= new ArrayList<>();
        boolean[] used= new boolean[nums.length];
         Arrays.sort(nums);
        Solve(nums,path,used);
        return result;
    }

    void Solve(int[] nums,List<Integer> path,boolean[] used){

        if(path.size() == nums.length){
            result.add(new ArrayList(path));
            return ;
        }
        for(int j=0; j< nums.length ;  j++){
            if(j>0 && !used[j-1] && nums[j] == nums[j-1]){
                continue;
            }
            if(!used[j]){
                used[j]=true;
                path.add(nums[j]);
                Solve(nums,path,used);
                path.remove(path.size()-1);
                used[j]=false;

            }
        }

    }
}