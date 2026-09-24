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



    void Solve(int i,String s,List<String> path){
        if(i==s.length()){
            result.add(new ArrayList(path));
            return;
        }

        for(int j=i ; j< s.length(); j++){

            if(isValidPalindrome(i,j,s)){
                path.add(s.substring(i,j+1));
                System.out.println("path >>"+path );
                Solve(j+1,s,path);
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