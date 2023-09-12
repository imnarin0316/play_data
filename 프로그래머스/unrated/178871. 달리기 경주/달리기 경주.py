def solution(players, callings):
    players_ranking = {player: int(idx) for idx, player in enumerate(players)}

    for call in callings:
        current_rank = players_ranking[call] 

        players_ranking[call] -= 1
        players_ranking[players[current_rank - 1]] += 1

        # players 배열에서 선수들의 순위 바꿔주기
        players[current_rank - 1], players[current_rank] = call, players[current_rank - 1]

    return players