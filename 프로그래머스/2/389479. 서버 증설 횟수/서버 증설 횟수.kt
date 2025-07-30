class Solution {
    fun solution(players: IntArray, m: Int, k: Int): Int {
        var answer: Int = 0
        var curMax = m
        val que = ArrayDeque<Int>()
        // que.add(k)
        
        for (i in 0..23){
            
            while(que.isNotEmpty()){
                if(que.firstOrNull() == i){
                    que.removeFirst()
                    curMax -= m
                }else{
                    break
                }
            }
            
            while(curMax <= players[i]){
                que.add(i+k)
                curMax += m
                answer++
            }
            
            // println("i : $i, answer : $answer , curMax: $curMax")
        }
        
        return answer
    }
}