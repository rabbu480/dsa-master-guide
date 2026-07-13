class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {

    // create course index with empty adjList
    List<List<Integer>> adjList= new ArrayList<>(); 
    int[] indegrees= new int[numCourses];
    int [] courseOrder= new int[numCourses];
    // int courseFinshedCount=0;
    for(int i=0; i< numCourses ; i++){
        adjList.add(new ArrayList<>());
    }
    //  build adjList && build indegrees array
    //  0  --after-> 1,2     --> 0
    //  1  --after-> 3    --> 1
    //  2  --after-> 3    --> 1
    //  3  --after-> 0  --> 2
    for(int[] prereq: prerequisites){
        int course = prereq[0];
        int prereqz= prereq[1];
        adjList.get(prereqz).add(course);
        indegrees[course]++;
    }
    System.out.println(Arrays.toString(indegrees));
    // System.out.prinln(Arrays.deepToString(indegrees));
    System.out.println(adjList);
    //  add strating course to queue
    Queue<Integer> q = new LinkedList();

    for(int i=0; i < indegrees.length ; i++){
        if(indegrees[i]==0){
            q.offer(i);
        }
    }

    int orderIndex=0;
    int totalCoursesFinshed=0;
    while(!q.isEmpty()){
        int currentCourse=q.poll();
        courseOrder[orderIndex++]=currentCourse;
        totalCoursesFinshed++;
        // mark course is done ; Move to next corses.
        // reduce in degree for courses next 
        List<Integer> nextCourses= adjList.get(currentCourse);
        for(int nextCourse:nextCourses){
            indegrees[nextCourse]--;
            if(indegrees[nextCourse] == 0 ){
                // orderIndex++;
                q.offer(nextCourse);
            }
        }
    }
    if(totalCoursesFinshed != numCourses){
         return new int[] {};
    }

    // courseFinshedCount--;
    //  DO bfs and reduce the indegrees 

        
        return courseOrder;
    }

}