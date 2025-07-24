class Solution {
    val dx: IntArray = intArrayOf(1,-1,0,0)
	val dy: IntArray = intArrayOf(0,0,1,-1)
    
    fun solution(storage: Array<String>, requests: Array<String>): Int {
		var answer: Int = 0
		val n = storage.size
		val m = storage[0].length

		val pickedList: Array<BooleanArray> = Array(n) {BooleanArray(m) {false}}
		val outsideList: Array<BooleanArray> = Array(n) {BooleanArray(m) {false}}
		val newStorage :Array<Array<String>> = Array(n+2) { r ->
			Array(m+2) { c ->
				if(r == 0 || c == 0 || r == n+1 || c == m +1){
					"0"
				}else{
					if(storage[r-1][c-1].toString() == " "){
                        pickedList[r-1][c-1] = true
                    }
                    storage[r-1][c-1].toString()
				}
			}
		}
        
		requests.forEachIndexed{requestIdx, request ->
			if(request.length > 1) {
				pickCrain(request[0].toString(), newStorage, pickedList)
			}else{
				pickZige(request[0].toString(), newStorage, pickedList,outsideList,n,m)
			}
		}

		pickedList.forEach{ list ->
			list.forEach{
				if(!it){
					answer++
				}
			}
		}

		return answer
	}

	private fun pickCrain(word: String,storage :Array<Array<String>>,pickedList: Array<BooleanArray>){
		storage.forEachIndexed{ rIdx, row ->
			row.forEachIndexed{ cIdx, t ->
				if(t == word){
					// t = "0"
					storage[rIdx][cIdx] = "1"
					pickedList[rIdx-1][cIdx-1] = true
				}
			}
		}
	}

	private fun pickZige(word: String,storage :Array<Array<String>>,pickedList: Array<BooleanArray>,outsideList: Array<BooleanArray>, n: Int, m:Int){
		storage.forEachIndexed{ rIdx, row ->
			row.forEachIndexed{ cIdx, t ->
				if(t == word){
					val que: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
					que.add(rIdx to cIdx)
					val visitedList:Array<BooleanArray> = Array(n) {BooleanArray(m) {false}}

					while(que.isNotEmpty()){
						val cur = que.removeFirst()
						val r = cur.first
						val c = cur.second
                        
						if(storage[r-1][c] == "0" || storage[r+1][c] == "0"
							|| storage[r][c-1] == "0" || storage[r][c+1] == "0"){
							
							pickedList[rIdx-1][cIdx-1] = true
							que.clear()
						} else{
                            for (i in 0..3){
                                val nextR = r + dx[i]
                                val nextC = c + dy[i]
                                if(!visitedList[nextR-1][nextC-1] && storage[nextR][nextC] == "1"){
                                    visitedList[nextR-1][nextC-1] = true
                                    que.add(nextR to nextC)
                                }
                            }
                            
                        }
                        
					}

				}
			}
		}

		pickedList.forEachIndexed{ rIdx, row ->
			row.forEachIndexed {cIdx, t ->
				if(t){
					storage[rIdx+1][cIdx+1] = "1"
				}
			}
		}

	}
}