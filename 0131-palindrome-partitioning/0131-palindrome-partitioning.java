class Solution {

    List<List<String>> result= new ArrayList<>(); 
    public List<List<String>> partition(String s) {
        Solve(0,s,new ArrayList<String>());
        return result;
    }

    // s ==> starting & ending position , j is start , i is end 
    // choice ==> take cuurent to end check if palindorm
    // Save 
    // recursion for each char satrt check end ing (j) Solve(j+1,s)
    // undo



    void Solve(int j,String s,List<String> path){
        if(j==s.length()){
            result.add(new ArrayList(path));
            return;
        }

        for(int i=j ; i< s.length(); i++){

            if(isValidPalindrome(j,i,s)){
                path.add(s.substring(j,i+1));
                System.out.println("path >>"+path );
                Solve(i+1,s,path);
                path.remove(path.size()-1); 
            }

            
        }
    }


    boolean isValidPalindrome(int i,int j,String s){

        while(i<=j){
            if(s.charAt(i) != s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    
}