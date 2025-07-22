class Solution {
    fun solution(schedules: IntArray, timelogs: Array<IntArray>, startday: Int): Int {
        var answer: Int = 0
        val failList: Array<Boolean> = Array(schedules.size) { false }
        
        for(i in 0..6){
            val day = (startday + i) % 7
            
            if(day == 0 || day == 6){
                continue
            }
            
            schedules.forEachIndexed{ idx, schedule ->
                val limit =
                    if((schedule % 100) + 10 >= 60){
                        schedule + 50
                    }else{
                        schedule + 10
                    }
                
                if(timelogs[idx][i] > limit){
                    failList[idx] = true
                }
            }
            
        }
        
        answer = failList.count{!it}
        
        
        return answer
    }
}