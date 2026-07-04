class Solution {
    public boolean isAnagram(String s, String t) {
    //    APproch1 : 
        // int[] freq = new int[26];

        // for(char c : s.toCharArray()) freq[c-'a']++;
        // for(char c : t.toCharArray()) freq[c-'a']--;

        // for(int charVal: freq){
        //     if(charVal != 0){
        //         return false;
        //     }
        // }
        // return true;

        HashMap<Character,Integer> seen= new HashMap();
        if(s.length() != t.length()){
            return false;
        }

        for(char c : s.toCharArray()){
            seen.put(c,seen.getOrDefault(c,0)+1);
        }

        for(char c : t.toCharArray()){
            if(!seen.containsKey(c)){
               return false ;
            }
            if(seen.get(c) == 1){
                seen.remove(c);
            } else {
                seen.put(c,seen.get(c)-1); 
            }
        }
        System.out.println("seen" +seen);
        return seen.isEmpty();
    }
}