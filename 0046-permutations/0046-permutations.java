class Solution {

    List<List<Integer>> result= new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {

        List<Integer> path= new ArrayList<>();
        Arrays.sort(nums);
        boolean[] used= new boolean[nums.length];
        Solve(0,nums,path,used);
        return result;
        
    }

    void Solve(int i , int[] nums,List<Integer> path,boolean[] used) {
        if(path.size() == nums.length){
            System.out.println(path);
            result.add(new ArrayList(path));
            return ;
        }

        for(int j = 0 ; j < nums.length ; j++){
            if(!used[j]){
                used[j]=true;
                path.add(nums[j]);
                System.out.println("j do "+j +"path >> "+ path);
                Solve(j,nums,path,used);
                path.remove(path.size()-1);
                System.out.println("j undo"+j +"path >> "+ path);
                used[j]=false;
            }

        }

    }
}