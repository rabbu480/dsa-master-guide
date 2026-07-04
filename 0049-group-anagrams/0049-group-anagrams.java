class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {


        // first convert strings into frequencies then we can compare frequncies.
        // to compare frequncies, tthese freq are list need connvert as string 
        // to convert There is chance that it can be interprited 11 i.e aa as k
        // so to avoid this we will build key with a char that separate each frequency 
        // we will comprae that key

        HashMap<String, List<String>> angramGroups= new HashMap<>();
        for(String str: strs){
            int[] freqs = new int[26];
            for(char c: str.toCharArray()){
                freqs[c-'a']++;
            }
            StringBuilder key= new StringBuilder();
            for(int freq:freqs ) {
                key.append(freq).append("#");
            }
            angramGroups.computeIfAbsent(key.toString(),k->new ArrayList()).add(str);
        }
        return angramGroups.values().stream().toList();
    }




        /***
        HashMap Approch............
         */

        // HashMap<String,List<String>> hm = new HashMap<>();
        // for(String str :strs){
        //     char[] charA = str.toLowerCase().toCharArray();
        //     Arrays.sort(charA);
        //     String newStr = new String(charA);
        //     System.out.println("newStr :: "+newStr);
        //     if(hm.containsKey(newStr)){
        //         List<String> value =hm.get(newStr).add(str);
        //         hm.put(newStr,value);
        //     } else {
        //         List<String> value=new ArrayList();
        //         value.add(str);
        //         hm.put(newStr,value);
        //     }
        // }
        // return new ArrayList<>(hm.values());

    //     HashMap<String,List<String>> hm = new HashMap();

    //     for(String str: strs){
    //         int[] freq=new int[26];
    //         char[] charA=str.toCharArray();
    //         for(char c: charA) freq[c-'a']++;
    //         StringBuffer key=new StringBuffer(); 
    //         for(int f: freq){
    //             key=key.append(f).append("@");
    //         }
    //         String keyString= new String(key);
    //         List<String> al= hm.getOrDefault( keyString,new ArrayList() );
    //          al.add(str);
    //         hm.put(keyString,al );
    //     }
    //     return hm.values().stream().toList();
        
    // }

    // public boolean isAnagram(String s1,String s2){
    //     if(s1.length() != s2.length()){
    //         return false;
    //     }
    //     int[] freq = new int[26];
    //     char[] cs1 = s1.toLowerCase().toCharArray();
    //     char[] cs2 = s2.toLowerCase().toCharArray();
    //     for(char c1 : cs1) freq[c1-'a']++;
    //     for(char c2 : cs2) freq[c2-'a']--;
    //     for(int val:freq) {
    //         if(val !=0){
    //             return false;
    //         }
    //     }
    //      return true;

    // }
}
