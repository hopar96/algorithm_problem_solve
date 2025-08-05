class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        var answer = mutableListOf<Int>()
        val todayInt = today.replace(".","").toInt()
        val termMap = hashMapOf<String, Int>()
        for (term in terms){
            val tList = term.split(" ")
            termMap.put(tList[0], tList[1].toInt())
        }
        privacies.forEachIndexed{ idx, privacy ->
        
            val pList = privacy.split(" ")
            val date =
                pList[0].replace(".", "").let{
                    
                    var year = it.substring(0,4).toInt()
                    var month = it.substring(4,6).toInt() + termMap.get(pList[1])!!
                    val day = it.substring(6).toInt()
                    
                    year += month / 12
                    month = month % 12
                    
                    if(month % 12 == 0){
                        month = 12
                        year--
                    }
                    
                    var date = "$year".padStart(4,'0')
                    date += "$month".padStart(2,'0')
                    date += "$day".padStart(2,'0')
                    date.toInt()
                }
            println(date)
            
            if(todayInt >= date){
                answer.add(idx+1)
            }
        }
        
        return answer.toIntArray()
    }
}