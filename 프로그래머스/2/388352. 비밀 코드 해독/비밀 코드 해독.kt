class Solution {
    
    
	var answer: Int = 0
	fun solution(n: Int, q: Array<IntArray>, ans: IntArray): Int {

		dfs(1, mutableListOf(), n, q, ans)

		return answer
	}

	private fun dfs(target: Int,cur: MutableList<Int>,n: Int, q: Array<IntArray>, ans: IntArray){
		if(cur.size == 5){
			checkAnswer(cur, q ,ans)
			return
		}

		for (i in target .. n){
			cur.add(i)
			dfs(i+1, cur, n, q, ans)
			cur.removeLast()
		}
	}

	private fun checkAnswer(cur: MutableList<Int>, q: Array<IntArray>, ans: IntArray){
		q.forEachIndexed {i, question ->
			var count = 0
			question.forEach {
				if(cur.contains(it)){
					count++
				}
			}
			if(count != ans[i]){
				return
			}
		}
		
		answer++
	}
}