class Solution {
    fun solution(video_len: String, pos: String, op_start: String, op_end: String, commands: Array<String>): String {
        var answer: String = ""
        
        val vList = video_len.split(":")
        val vM = vList[0]
        val vS = vList[1]
        
        // val oSList = op_start.split(":")
        // val oSM = oSList[0]
        // val oSS = oSList[1]
        
        val oEList = op_end.split(":")
        val oEM = oEList[0]
        val oES = oEList[1]
        
        val videoLenInt = video_len.replace(":","").toInt()
        val opStartInt = op_start.replace(":","").toInt()
        val opEndInt = op_end.replace(":","").toInt()
        
        val posList = pos.split(":")
        var cM = posList[0]
        var cS = posList[1]
        
        for (c in commands){
            // 오프닝 건너뛰기 체크
            if(opStartInt <= (cM + cS).toInt() && (cM + cS).toInt() <= opEndInt){
                cM = oEM
                cS = oES
            }
            var nM:String = cM
            var nS:String = cS
            
            if(c == "next"){
                nM = cM
                nS = cS.toInt().let{
                    if(it+10 > 59){
                        nM = (nM.toInt()+1).toString().padStart(2, '0')
                        return@let (it-50).toString().padStart(2, '0')
                    }else{
                        return@let (it+10).toString().padStart(2, '0')
                    }
                }
                if((nM + nS).toInt() > videoLenInt){ // 비디오 시간보다 클경우
                    nM = vM
                    nS = vS
                }
                
            }else{
                nM = cM
                nS = cS.toInt().let{
                    if(it-10 < 0){
                        nM = (nM.toInt()-1).toString().padStart(2, '0')
                        return@let (it+50).toString().padStart(2, '0')
                    }else{
                        return@let (it-10).toString().padStart(2, '0')
                    }
                }
                if(nM.toInt() < 0){ // 비디오 시간보다 클경우
                    nM = "00"
                    nS = "00"
                }
            }
            // 오프닝 건너뛰기 체크
            if(opStartInt <= (nM + nS).toInt() && (nM + nS).toInt() <= opEndInt){
                nM = oEM
                nS = oES
            }
            cM = nM
            cS = nS
            // println("c: $c , $cM:$cS")
        }
        
        return cM + ":" + cS
    }
}