# graph problem based on  directed acyclic graph (DAG)
# you are given a DAG with nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# this problem is similar to this problem on leetcode :  https://leetcode.com/problems/all-paths-from-source-to-target/


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
        all_paths=[[0]]
        path = []
        
        while len(queue) > 0: 
            top = all_paths.pop(0)
            
            if top[-1] == len(graph) - 1:
                ans.append(top)
                continue
            
    
            for neigbour in graph[top[-1]]:
                all_paths.append(top + [neigbour])

                
        return path 
