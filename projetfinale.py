import pygame
pygame.init()
screendisplay = pygame.display.set_mode((550, 550))
pygame.display.set_caption("Tic-Tac-Toe")
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

block1 = pygame.draw.rect(screendisplay, (255, 255, 255), (25, 25, 150, 150))
block2 = pygame.draw.rect(screendisplay, (255, 255, 255), (200, 25, 150, 150))
block3 = pygame.draw.rect(screendisplay, (255, 255, 255), (375, 25, 150, 150))
block4 = pygame.draw.rect(screendisplay, (255, 255, 255), (25, 200, 150, 150))
block5 = pygame.draw.rect(screendisplay, (255, 255, 255), (200, 200, 150, 150))
block6 = pygame.draw.rect(screendisplay, (255, 255, 255), (375, 200, 150, 150))
block7 = pygame.draw.rect(screendisplay, (255, 255, 255), (25, 375, 150, 150))
block8 = pygame.draw.rect(screendisplay, (255, 255, 255), (200, 375, 150, 150))
block9 = pygame.draw.rect(screendisplay, (255, 255, 255), (375, 375, 150, 150))

player_draw = 'circle'

def isWinning:
    if player_won(1):
        won = True
    if player_won(2):
        won = True

def player_won(number):
    for row in board:
        for tile in row:
            if tile == number:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == number:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == number:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2 - tile] == number:
            continue
        else:
            break
    else:
        return True


def main():
  run = True
  won = False
  while run:

    pygame.time.delay(100)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                block1_open = True
                block2_open = True
                block3_open = True
                block4_open = True
                block5_open = True
                block6_open = True
                block7_open = True
                block8_open = True
                block9_open = True
                run = True
                won = False
                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                block1 = pygame.draw.rect(screendisplay, (255, 255, 255), (25, 25, 150, 150))
                block2 = pygame.draw.rect(screendisplay, (255, 255, 255), (200, 25, 150, 150))
                block3 = pygame.draw.rect(screendisplay, (255, 255, 255), (375, 25, 150, 150))
                block4 = pygame.draw.rect(screendisplay, (255, 255, 255), (25, 200, 150, 150))
                block5 = pygame.draw.rect(screendisplay, (255, 255, 255), (200, 200, 150, 150))
                block6 = pygame.draw.rect(screendisplay, (255, 255, 255), (375, 200, 150, 150))
                block7 = pygame.draw.rect(screendisplay, (255, 255, 255), (25, 375, 150, 150))
                block8 = pygame.draw.rect(screendisplay, (255, 255, 255), (200, 375, 150, 150))
                block9 = pygame.draw.rect(screendisplay, (255, 255, 255), (375, 375, 150, 150))


        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()

            if won != True:
                if block1.collidepoint(position) and block1_open:

                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (100, 100), 50, 50)
                        player_draw = 'rect'
                        board[0][0] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (50, 50, 100, 100))
                        player_draw = 'circle'
                        board[0][0] = 2
                    block1_open = False

                if block2.collidepoint(position) and block2_open:
                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (275, 100), 50, 10)
                        player_draw = 'rect'
                        board[0][1] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (225, 50, 100, 100))
                        player_draw = 'circle'
                        board[0][1] = 2
                    block2_open = False

                if block3.collidepoint(position) and block3_open:
                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (450, 100), 50, 50)
                        player_draw = 'rect'
                        board[0][2] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (400, 50, 100, 100))
                        player_draw = 'circle'
                        board[0][2] = 2
                    block3_open = False

                if block4.collidepoint(position) and block4_open:
                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (100, 275), 50, 20)
                        player_draw = 'rect'
                        board[1][0] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (50, 225, 100, 100))
                        player_draw = 'circle'
                        board[1][0] = 2
                    block4_open = False

                if block5.collidepoint(position) and block5_open:
                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (275, 275), 50, 20)
                        player_draw = 'rect'
                        board[1][1] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (225, 225, 100, 100))
                        player_draw = 'circle'
                        board[1][1] = 2
                    block5_open = False

                if block6.collidepoint(position) and block6_open:
                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (450, 275), 50, 5)
                        player_draw = 'rect'
                        board[1][2] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (400, 225, 100, 100))
                        player_draw = 'circle'
                        board[1][2] = 2
                    block6_open = False

                if block7.collidepoint(position) and block7_open:
                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (100, 450), 50)
                        player_draw = 'rect'
                        board[2][0] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (50, 400, 100, 100))
                        player_draw = 'circle'
                        board[2][0] = 2
                    block7_open = False

                if block8.collidepoint(position) and block8_open:
                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (275, 450), 50)
                        player_draw = 'rect'
                        board[2][1] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (225, 400, 100, 100))
                        player_draw = 'circle'
                        board[2][1] = 2
                    block8_open = False

                if block9.collidepoint(position) and block9_open:
                    if player_draw == 'circle':
                        pygame.draw.circle(screendisplay, (0, 0, 0), (450, 450), 50)
                        player_draw = 'rect'
                        board[2][2] = 1
                    else:
                        pygame.draw.rect(screendisplay, (0, 0, 0), (400, 400, 100, 100))
                        player_draw = 'circle'
                        board[2][2] = 2
                    block9_open = False

    isWinning()


    pygame.display.update()

main()


if player_won(1):
    print("Player1 won")
if player_won(2):
    print("Player2 won")

pygame.quit()