class Solution {

    List<String> result= new ArrayList<>();
    Map<String,String> digiMap= new HashMap<>();


    public List<String> letterCombinations(String digits) {

        digiMap.put("2","abc");
        digiMap.put("3","def");
        digiMap.put("4","ghi");
        digiMap.put("5","jkl");
        digiMap.put("6","mno");
        digiMap.put("7","pqrs");
        digiMap.put("8","tuv");
        digiMap.put("9","wxyz");

        Solve(0,digits,new StringBuffer(""));
        return result;
        
    }

    void Solve(int i,String digits,StringBuffer path) {

        if(i == digits.length()){
            result.add(""+path);
            return;
        }

        String letter =digiMap.get(""+digits.charAt(i));
        for(char c: letter.toCharArray()) {  
            path.append(c);
            Solve(i+1,digits,path);
            path.deleteCharAt(path.length() - 1);
        }

    }





}