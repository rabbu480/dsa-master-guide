class Solution {

    List<List<Integer>> result= new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> path = new ArrayList<>();
        Solve(0,candidates,target,path);
        return result;
    }

    void Solve(int i, int[] candidates,  int remaining,List<Integer>  path){
        if(remaining==0) { 
            result.add(new ArrayList(path));
            return ;
        }
        if(remaining < 0 ) { 
            return ;
        }
        for(int j = i; j< candidates.length; j++){
            path.add(candidates[j]);
            Solve(j,candidates,remaining-candidates[j],path);
            path.remove(path.size()-1);
        }
    }
}