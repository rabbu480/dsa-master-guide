class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {

        // prerequisites to course adjList next course & indegrees
        // 0 -> 1 
        // 0 -> [1]
        // Create adjIndexes with empty nextcourse
        List<List<Integer>> adjList= new ArrayList<>();
        int[] indegrees=new int[numCourses];
        for(int i =0 ; i< numCourses  ; i++){
            adjList.add(new ArrayList());
        }
        for(int[] preq:prerequisites){
            int course=preq[0];
            int preqz=preq[1];
            // System.out.println(course+"---"+preqz);
            // 0 -> 1 , 1-> 0
            adjList.get(preqz).add(course);
            indegrees[course]++;
        }

        // get the starting course /initial course add it queue
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0 ; i<numCourses; i++ ){
            if(indegrees[i]==0){
                queue.offer(i);
            }
        }
        System.out.println("indegrees::"+Arrays.toString(indegrees));
        System.out.println("adjList :"+adjList);
        System.out.println("queue :"+queue);
        // Now Process COurse the pre-req then decrese indegrees 
        // for those couses dependent on this
        int compltedCourse=0;
        while(!queue.isEmpty()){
            int currentCourse= queue.poll();
            System.out.println("currentCourse"+currentCourse);
            compltedCourse++;

            // get Next course as we finsh current course.
            List<Integer> nextCourses = adjList.get(currentCourse);
            // System.out.println("nextCourses"+nextCourses);
            for(int nextCourse: nextCourses){
                indegrees[nextCourse]--; 
                if(indegrees[nextCourse] == 0 ){
                  queue.offer(nextCourse);
                }
            }
        }
        System.out.println(compltedCourse);
        if(compltedCourse != numCourses ){
            return false;
        }
        return true;

    }


}