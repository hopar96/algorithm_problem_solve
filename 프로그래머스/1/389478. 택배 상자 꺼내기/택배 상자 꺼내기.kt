class Solution {
    fun solution(n: Int, w: Int, num: Int): Int {
        var answer: Int = 0
        val lines = if(n%w == 0) n/w else n/w+1
        val array = Array<IntArray>(lines){IntArray(w){0}}
        var isRightTurn = true
        var targetXY = 0 to 0
        for (i in 1..n){
            var x = if(isRightTurn) i % w - 1 else w - (i % w)
            if(i % w == 0 && isRightTurn)  x += w
            else if(i % w == 0 && !isRightTurn)  x -= w
            
            val y = lines - (if(i%w == 0) i/w else i/w+1)
            array[y][x] = i
            if(i%w == 0){
                isRightTurn = !isRightTurn
            }
            if(i == num){
                targetXY = x to y
            }
        }
        
        answer = 
        if(array[0][targetXY.first] == 0){
            targetXY.second
        }else{
            targetXY.second + 1
        }
        
        return answer
    }
}