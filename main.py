import pygame
import random
import sys

# 게임 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("별 먹는 지렁이 🐍⭐")

# 색상 정의
BLACK  = (0, 0, 0)
GREEN  = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)

# 게임 속도 설정
clock = pygame.time.Clock()
SPEED = 10

# 폰트 설정
font = pygame.font.SysFont("arial", 24)

# ⭐ 별 그리기 함수
def draw_star(surface, pos):
    pygame.draw.circle(surface, YELLOW, pos, CELL_SIZE // 2)

# 📢 메시지 출력 함수
def show_message(text, color, y_offset=0):
    message = font.render(text, True, color)
    rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(message, rect)

# 🐍 게임 메인 루프
def main():
    # 지렁이 초기 상태
    snake = [(100, 100)]
    direction = (CELL_SIZE, 0)
    score = 0

    # ⭐ 별 위치 무작위 생성
    def random_star():
        return (
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)
        )

    star = random_star()
    game_over = False

    # 🎮 메인 게임 루프
    while True:
        screen.fill(BLACK)

        # 사용자 입력 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                        direction = (0, -CELL_SIZE)
                    elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                        direction = (0, CELL_SIZE)
                    elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                        direction = (-CELL_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                        direction = (CELL_SIZE, 0)
                elif event.key == pygame.K_r:
                    main()

        # 게임 오버가 아니면 진행
        if not game_over:
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # 충돌 판정 (벽 또는 자기 몸)
            if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake):
                game_over = True
            else:
                snake.insert(0, new_head)

                # 별을 먹었을 경우
                if new_head == star:
                    star = random_star()
                    score += 1
                else:
                    snake.pop()

        # 지렁이 그리기
        for part in snake:
            pygame.draw.rect(screen, GREEN, (*part, CELL_SIZE, CELL_SIZE))

        # 별 그리기
        draw_star(screen, (star[0] + CELL_SIZE // 2, star[1] + CELL_SIZE // 2))

        # 점수 표시
        score_text = font.render(f"점수: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # 게임 오버 메시지
        if game_over:
            show_message("게임 오버! R 키로 재시작", RED, 40)

        # 화면 업데이트
        pygame.display.update()
        clock.tick(SPEED)

# 🧷 프로그램 시작점
if __name__ == "__main__":
    main()
