import kotlin.math.min

class Solution {
    var leastA = -1
	val visited:HashSet<Triple<Int,Int,Int>> = hashSetOf()

	fun solution(info: Array<IntArray>, n: Int, m: Int): Int {
		var answer: Int = 0
		dfs(0,0,0,info,n,m)

		return leastA
	}

	fun dfs(cur:Int, aSum:Int, bSum:Int, info: Array<IntArray>, n: Int, m: Int){
		visited.add(Triple(cur,aSum, bSum))
        
		if(aSum >= n || bSum >= m){
			return
		}
		else if(info.size == cur){
			leastA = if(leastA == -1 ) aSum else min(aSum, leastA)
			return
		}

		if(!visited.contains(Triple(cur+1, aSum + info[cur][0], bSum))){
			dfs(cur+1, aSum + info[cur][0], bSum, info, n, m)
		}

		if(!visited.contains(Triple(cur+1, aSum, bSum+info[cur][1]))){
			dfs(cur+1, aSum, bSum+info[cur][1], info, n, m)
		}

	}
}