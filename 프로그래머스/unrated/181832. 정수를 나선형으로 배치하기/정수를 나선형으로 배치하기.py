def solution(n):
    # n x n 크기의 빈 배열 생성
    result = [[0] * n for _ in range(n)]
    
    # 방향 설정 (오른쪽, 아래, 왼쪽, 위)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 초기 위치와 숫자 설정
    row, col = 0, 0
    num = 1
    
    for _ in range(1, n * n + 1):
        result[row][col] = num
        num += 1
        
        # 다음 위치 계산
        next_row, next_col = row + directions[0][0], col + directions[0][1]
        
        # 다음 위치가 유효하고 빈 칸이면 계속 진행
        if 0 <= next_row < n and 0 <= next_col < n and result[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            # 방향을 바꾸어야 할 때 방향을 바꾸고 다음 위치 계산
            directions.append(directions.pop(0))
            row, col = row + directions[0][0], col + directions[0][1]

    return result