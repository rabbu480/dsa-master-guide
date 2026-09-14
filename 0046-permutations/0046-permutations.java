class Solution {

    List<List<Integer>> result= new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {

        List<Integer> path= new ArrayList<>();
        boolean[] used= new boolean[nums.length];
        Solve(0,nums,path,used);
        return result;
        
    }

    void Solve(int i , int[] nums,List<Integer> path,boolean[] used) {
        if(path.size() == nums.length){
            result.add(new ArrayList(path));
            return ;
        }

        for(int j = 0 ; j < nums.length ; j++){
            if(!used[j]){
                used[j]=true;
                path.add(nums[j]);
                Solve(j,nums,path,used);
                path.remove(path.size()-1);
                used[j]=false;
            }

        }

    }
}