# 스네이크 이동 처리
def move_snake():
    head_x, head_y = st.session_state.snake[0]
    dx, dy = st.session_state.direction
    new_head = (head_x + dx, head_y + dy)

    # **게임 오버 조건: 벽에 닿거나 자기 몸에 닿으면 죽음**
    if (
        not (0 <= new_head[0] < WIDTH)  # 벽 충돌 검사 (x 좌표가 범위 밖)
        or not (0 <= new_head[1] < HEIGHT)  # 벽 충돌 검사 (y 좌표가 범위 밖)
        or new_head in st.session_state.snake  # 자기 몸 충돌 검사
    ):
        st.session_state.game_over = True  # 게임 오버 상태로 변경
        st.session_state.running = False   # 게임 정지
        return

    # 정상 이동 시 머리 위치 추가
    st.session_state.snake.insert(0, new_head)

    # 별 먹은 경우
    if new_head == st.session_state.star:
        st.session_state.score += 1
        while True:
            st.session_state.star = (
                random.randint(0, WIDTH - 1),
                random.randint(0, HEIGHT - 1),
            )
            if st.session_state.star not in st.session_state.snake:
                break
    else:
        st.session_state.snake.pop()
