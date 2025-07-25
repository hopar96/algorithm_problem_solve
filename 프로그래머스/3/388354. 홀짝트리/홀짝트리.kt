class Solution {
    fun solution(nodes: IntArray, edges: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf(0,0)
        var edgeMap = hashMapOf<Int, MutableList<Int>>()
        
        for(node in nodes){
            edgeMap[node] = mutableListOf()
        }
        
        for (edge in edges){ 
            edgeMap[edge[0]]!!.add(edge[1])
            edgeMap[edge[1]]!!.add(edge[0])
        }
        // print("$edgeMap")
        val vList = hashSetOf<Int>()
        for (node in nodes) {
            val que = ArrayDeque<Int>()
            if(vList.contains(node)) continue
            var sameCnt = 0
            var diffCnt = 0
            // val vList = BooleanArray(1000001){false}

            que.add(node)
            vList.add(node)
            while(que.isNotEmpty()){
                val target = que.removeFirst()
                val children = edgeMap[target]
                val childrenCnt = children?.size ?: 0

                if(target%2 == childrenCnt%2) sameCnt++
                else diffCnt++
                
                children?.forEach{
                    if(!vList.contains(it)){
                        vList.add(it)
                        que.add(it)
                    }
                }
            }
            // if(isContinue){
            //     continue
            // }
            // if(isOpposit){
            //     answer[1]++
            // }else if (!isOpposit){
            //     answer[0]++
            // }
            if(sameCnt == 1) answer[0]++
            if(diffCnt == 1) answer[1]++
            
        }
        
       

        
        return answer
    }
    
}