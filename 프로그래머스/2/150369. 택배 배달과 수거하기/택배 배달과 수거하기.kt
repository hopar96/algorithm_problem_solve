
class Solution {
    fun solution(cap: Int, n: Int, deliveries: IntArray, pickups: IntArray): Long {
        var answer: Long = 0
        
        var i = n-1
        while (0 <= i){
            var deliveryCap = cap
            var pickupCap = cap
            
            if(deliveries[i] > 0 || pickups[i] > 0){
                var j = i

                while(j >= 0 && deliveryCap > 0){
                    deliveryCap = deliOrPick(j, deliveryCap,deliveries)        
                    j--
                }
                
                j = i
                while(j >= 0 && pickupCap > 0){
                    pickupCap = deliOrPick(j, pickupCap, pickups)
                    j--
                }
                answer += (i+1)*2L
            }else{
                i--
            }
            
            // if(deliveries[i] == 0 && pickups[i] == 0){
            //     i--    
            // }
        }
        
        return answer
    }
    fun deliOrPick(j: Int, cap: Int,list: IntArray):Int{
        
        var curCap = cap
        val spend = curCap - list[j]
        if(spend < 0){
            list[j] -= curCap
            curCap = 0
        }else{
            curCap = spend
            list[j] = 0
        }
        
        return curCap
    }
    
}