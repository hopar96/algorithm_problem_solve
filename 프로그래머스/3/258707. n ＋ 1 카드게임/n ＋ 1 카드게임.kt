class Solution {
    var answer: Int = 0
    val visited = hashSetOf<Triple<Int,HashSet<Int>, Int>>()
    fun solution(coin: Int, cards: IntArray): Int {
        val curCards = hashSetOf<Int>()
        for (i in 0 until cards.size/3){
            curCards.add(cards[i])
        }
        
        // dfs(0, curCards, coin, cards)
        val n = cards.size+1
        val keepCards = hashSetOf<Int>()
        var restCoin = coin
        for (i in 1..(cards.size - cards.size/3)/2+1){
            if(cards.size <= cards.size/3 + i*2 -2){
                return i    
            }
            keepCards.add(cards[cards.size/3 + i*2 -2])    
            keepCards.add(cards[cards.size/3 + i*2 -1])
            if(keepCards.isEmpty()){
                return i
            }
            
            var isNone = true
            for (card in curCards) {
                if(curCards.contains(n - card)){
                    curCards.remove(n - card)
                    curCards.remove(card)
                    isNone = false
                    break
                }
            }
            // 처음 받은 카드에 없는 경우
            if(isNone){
                for (card in curCards) { // 기존카드 + keepcard
                    if(keepCards.contains(n - card)){
                        keepCards.remove(n - card)
                        curCards.remove(card)
                        restCoin--
                        isNone = false
                        break
                    }
                }
            }
            // 기존카드 + keepcard 없는 경우
            if(isNone){
                for (card in keepCards) { // keepcard만
                    if(keepCards.contains(n - card)){
                        keepCards.remove(n - card)
                        keepCards.remove(card)
                        restCoin -= 2
                        isNone = false
                        break
                    }
                }
            }
            // println("$i , $isNone")
            if(isNone || restCoin < 0){
                return i
            }
            
        }
        
        
        
        return answer
    }
    
//     fun dfs(round: Int, curCards: HashSet<Int>, restCoin: Int, cards: IntArray){
//         if(visited.contains(Triple(round, curCards, restCoin))){
//            return
//         }
//         visited.add(Triple(round, curCards, restCoin))
//         val cardIdx = cards.size/3 + round * 2
//         // println("$curCards , round: $round, restCoin: $restCoin")
//         if(cards.size < cardIdx || restCoin < 0){
//             if(answer < round){
//                 answer = round
//             }
//             // println("끝1")
//             return
//         }
//         val n = cards.size + 1
//         var isNone = true
//         if(round != 0){
//             for (card in curCards) {
//                 if(curCards.contains(n - card)){
//                     curCards.remove(n - card)
//                     curCards.remove(card)
//                     isNone = false
//                     break
//                 }
//             }
//             // println("$curCards")
//             if(isNone){
//                 if(answer < round){
//                     answer = round
//                 }
//                 // println("끝2")
//                 return
//             }

//         }
        
//         // 두개 다 선택
//         var tmpCards: HashSet<Int>
//         if(cards.size > cardIdx){
//             tmpCards = HashSet<Int>(curCards).also{
//                 it.add( cards[cardIdx ])
//                 it.add( cards[cardIdx + 1])
//             }
//             dfs(round+1, tmpCards , restCoin -2, cards)
//             tmpCards = HashSet<Int>(curCards).also{
//                 it.add( cards[cardIdx])
//             }
//             dfs(round+1,tmpCards, restCoin -1, cards)
//             tmpCards = HashSet<Int>(curCards).also{
//                 it.add( cards[cardIdx + 1])
//             }
//             dfs(round+1, tmpCards, restCoin -1, cards)
//         }
        
//         tmpCards = HashSet<Int>(curCards)
//         dfs(round+1, tmpCards, restCoin, cards)
//     }
}