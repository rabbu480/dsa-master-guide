class Solution {
    
    List<List<Integer>> result= new ArrayList<>();
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<Integer> path = new ArrayList<>();
        Arrays.sort(candidates);
        Solve(0,candidates,target,path);
        return result;
    }

    void Solve(int i,int[] candidates, int remaining,List<Integer> path){

        if(remaining == 0 ){
            result.add(new ArrayList(path));
            return ;
        }
        if(remaining <0){
            return ;
        }

        for(int j =i; j< candidates.length; j++){
            if (j > i && candidates[j] == candidates[j - 1]) {
                continue;
            }
            path.add(candidates[j]);
            Solve(j+1,candidates,remaining-candidates[j],path);
            path.remove(path.size()-1);
        }

    }
}