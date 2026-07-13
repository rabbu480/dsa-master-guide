class Solution {
    public int[] findRedundantConnection(int[][] edges) {

        //write adjecent matrix.
        // parents rank 
        // find() 
        // union() if rank and no rank 
        
        UnionFind uf = new UnionFind(edges.length + 1);

        for (int[] edge : edges) {

            int u = edge[0];
            int v = edge[1];

            if (uf.find(u) == uf.find(v)) {
                return edge;
            }

            uf.union(u, v);
        }

        return new int[]{};
        
    }

}

class UnionFind {

    // parent[node] = immediate parent of the node
    int[] parent;

    // rank[node] = approximate tree height
    int[] rank;

    // Initialize
    UnionFind(int n) {

        parent = new int[n];
        rank = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;      // Every node is its own leader
            rank[i] = 1;        // Every tree starts with height 1
        }
    }

    // Find the ultimate parent (Leader)
    public int find(int x) {

        // Base Case
        if (parent[x] == x) {
            return x;
        }

        // Path Compression
        parent[x] = find(parent[x]);

        return parent[x];
    }

    // Merge two groups
    public void union(int x, int y) {

        int rootX = find(x);
        int rootY = find(y);

        // Already in same group
        if (rootX == rootY) {
            return;
        }

        // Union by Rank
        if (rank[rootX] > rank[rootY]) {

            parent[rootY] = rootX;

        } else if (rank[rootX] < rank[rootY]) {

            parent[rootX] = rootY;

        } else {

            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }
}