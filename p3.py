# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 이동 방향 (상, 하, 좌, 우)

    while True:
        visited = [[False] * N for _ in range(N)]  # 방문 여부를 저장하는 배열
        queue = deque([(bear_x, bear_y, 0)])  # 큐 초기화 (현재 행, 현재 열, 현재까지의 거리)
        visited[bear_x][bear_y] = True  # 곰의 현재 위치 방문 처리
        found_honeycomb = False  # 벌집을 찾았는지 여부
        possible_honeycombs = []  # 먹을 수 있는 벌집 리스트

        while queue:
            r, c, dist = queue.popleft()  # 큐에서 위치와 거리를 꺼냄
            
            for dr, dc in directions:  # 네 방향으로 이동
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:  # 유효한 위치인 경우
                    if forest[nr][nc] == 0 or forest[nr][nc] <= bear_size:  # 이동 가능한 칸인 경우
                        visited[nr][nc] = True  # 방문 처리
                        queue.append((nr, nc, dist + 1))  # 큐에 추가
                        
                        if 0 < forest[nr][nc] < bear_size:  # 먹을 수 있는 벌집인 경우
                            possible_honeycombs.append((dist + 1, nr, nc))  # 벌집 리스트에 추가

        if possible_honeycombs:  # 먹을 수 있는 벌집이 있는 경우
            possible_honeycombs.sort()  # 거리 순으로 정렬
            dist, nr, nc = possible_honeycombs[0]  # 가장 가까운 벌집 선택
            bear_x, bear_y = nr, nc  # 곰의 위치 업데이트
            time += dist  # 이동 시간 추가
            honeycomb_count += 1  # 먹은 벌집 개수 증가
            forest[nr][nc] = 0  # 벌집을 먹었으므로 빈 칸으로 변경

            if honeycomb_count == bear_size:  # 벌집을 먹은 개수가 곰의 크기와 같으면
                bear_size += 1  # 곰의 크기 증가
                honeycomb_count = 0  # 먹은 벌집 개수 초기화
            found_honeycomb = True

        if not found_honeycomb:  # 더 이상 먹을 벌집이 없으면
            break

    result = time  # 총 소요된 시간 반환
    return result

result = problem3(input)

assert result == 14
print("정답입니다.")
