class Solution {
    boolean[] visitedCity;
    public int findCircleNum(int[][] isConnected) {
        visitedCity=new boolean[isConnected.length];
      // city0 -> dfs(0);
      //         Rabbani  Alice  Bob
            // Rabbani     1      1     0
            // Alice       1      1     0
            // Bob         0      0     1
      int count=0;
      for(int city=0; city < isConnected.length ; city++ ){
        if(!visitedCity[city]){
            count++;
            dfs(isConnected,city);
        }
      }
      return  count;
        
    }

    public void dfs(int[][] isConnected, int cityIndex ){
         // conditions
         // if only not visited 
         // get negihbors itearate all negbours
        if (visitedCity[cityIndex]) {
            return;
        }

            visitedCity[cityIndex]=true;
            for(int city=0; city< isConnected.length; city++ ){
                if(city != cityIndex && isConnected[cityIndex][city] != 0 ){
                    dfs(isConnected,city);
                }
            }



    } 

}