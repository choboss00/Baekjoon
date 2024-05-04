import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        
        Map<String, Integer> hashMap = new HashMap<>();
        
        for (int i=0; i < players.length; i++) {
            hashMap.put(players[i], i);
        }
        
        for (String call : callings) {
            int playerIndex = hashMap.get(call);
            
            String frontPlayer = players[playerIndex-1];
            // 앞 사람을 뒤로 밀어내기
            hashMap.put(frontPlayer, playerIndex);
            players[playerIndex] = frontPlayer;
            
            // 현재 사람을 앞으로 밀기
            hashMap.put(call, playerIndex-1);
            players[playerIndex-1] = call;
            
        }
        
        return players;
        
        
    }
}