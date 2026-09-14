class Solution {

    List<List<Integer>> result = new ArrayList();
    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> paths=new ArrayList<>();
        solve(nums,0,paths);
        return result;

    }
    //s i ,c take skip
    // take : path.add(nums[i]) solve(i+1,path) path.remove(path.length()-1); skip:solve(i+1,path)
    // add path explore
    // recursion 
    // remove

    void solve(int[] nums,int i,List<Integer> path){

        if(i == nums.length){
            System.out.println("path :::>> "+ path);
            result.add(new ArrayList(path));
            return;
        }
               //skip:
        System.out.println("SKIP >>" +nums[i]);
        solve(nums,i+1,path);
        
        // take : 
        path.add(nums[i]);
        System.out.println("takE >>" +nums[i]);
        solve(nums,i+1,path);
        path.remove(path.size()-1); 
        
 
    }
}