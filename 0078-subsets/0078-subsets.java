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

    // void solve(int[] nums,int i,List<Integer> path){

    //     if(i == nums.length){
    //         System.out.println("path :::>> "+ path);
    //         result.add(new ArrayList(path));
    //         return;
    //     }

    //     // take : 
    //     path.add(nums[i]);
    //     System.out.println("takE >>" +nums[i]);
    //     solve(nums,i+1,path);
    //     path.remove(path.size()-1); 

    //     //skip:
    //     System.out.println("SKIP >>" +nums[i]);
    //     solve(nums,i+1,path);
        
 
    // }

    void solve(int[] nums, int i, List<Integer> path) {

        System.out.println("ENTER  i=" + i + " path=" + path);

        if (i == nums.length) {
            System.out.println("BASE   i=" + i + " path=" + path);
            result.add(new ArrayList<>(path));
            return;
        }

    // TAKE
        path.add(nums[i]);
        System.out.println("TAKE   " + nums[i] + " → " + path);

        solve(nums, i + 1, path);

        // UNDO
        path.remove(path.size() - 1);
        System.out.println("UNDO   " + nums[i] + " → " + path);

        // SKIP
        System.out.println("SKIP   " + nums[i] + " → " + path);

        solve(nums, i + 1, path);
    }

    // void solve(int[] nums, int i, List<Integer> path) {
    //     result.add(new ArrayList<>(path));
    //     // choose one each combinations
    //     for(int j = i ; j< nums.length ; j++ ){
    //         path.add(nums[j]);
    //         System.out.println("TAKE   " + nums[j] + " → " + path);
    //         solve(nums, j + 1, path);
    //         path.remove(path.size() - 1);
    //     }

    // }
}