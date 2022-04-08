import pygame
from pygame import MOUSEBUTTONUP, MOUSEBUTTONDOWN
import math
pygame.init()


# Notes:
# add win screen when the sudoku is solved
# add option to erase a hint ( - to erase + to use hint)
# add a button for notes instead of having to press enter
# Future notes:
# add sound when making a mistake
#   buttons:
#    add a play again button  (when game is over)
#    add a solve button       (using the sudoku solver)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (161, 171, 170)
SIZE = (540, 540)
ALL_SIZE = (540,580)
mistakes_count = 0
screen = pygame.display.set_mode(ALL_SIZE)
pygame.display.set_caption("Sudoku by the pros")
font_size = 20
font = pygame.font.Font('freesansbold.ttf', 32)
GAME_OVER = font.render('Game Over', True, BLACK)
hints_count = 0

quiz =  [[0, 0, 4, 3, 0, 0, 2, 0, 9],
 [0, 0, 5, 0, 0, 9, 0, 0, 1],
 [0, 7, 0, 0, 6, 0, 0, 4, 3],
 [0, 0, 6, 0, 0, 2, 0, 8, 7],
 [1, 9, 0, 0, 0, 7, 4, 0, 0],
 [0, 5, 0, 0, 8, 3, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 1, 0, 5],
 [0, 0, 3, 5, 0, 8, 6, 9, 0],
 [0, 4, 2, 9, 1, 0, 3, 0, 0]]

solution = [[8, 6, 4, 3, 7, 1, 2, 5, 9],
 [3, 2, 5, 8, 4, 9, 7, 6, 1],
 [9, 7, 1, 2, 6, 5, 8, 4, 3],
 [4, 3, 6, 1, 9, 2, 5, 8, 7],
 [1, 9, 8, 6, 5, 7, 4, 3, 2],
 [2, 5, 7, 4, 8, 3, 9, 1, 6],
 [6, 8, 9, 7, 3, 4, 1, 2, 5],
 [7, 1, 3, 5, 2, 8, 6, 9, 4],
 [5, 4, 2, 9, 1, 6, 3, 7, 8]]

numbers_on_board_by_rows = [[0, 0, 4, 3, 0, 0, 2, 0, 9],
 [0, 0, 5, 0, 0, 9, 0, 0, 1],
 [0, 7, 0, 0, 6, 0, 0, 4, 3],
 [0, 0, 6, 0, 0, 2, 0, 8, 7],
 [1, 9, 0, 0, 0, 7, 4, 0, 0],
 [0, 5, 0, 0, 8, 3, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 1, 0, 5],
 [0, 0, 3, 5, 0, 8, 6, 9, 0],
 [0, 4, 2, 9, 1, 0, 3, 0, 0]]
guess_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]]




def decide_block(r, w):
    if math.floor(r/3) == 0 and math.floor(w/3) == 0:
        return 0
    elif math.floor(r/3) == 0 and math.floor(w/3) == 1:
        return 1
    elif math.floor(r/3) == 0 and math.floor(w/3) == 2:
        return 2
    elif math.floor(r/3) == 1 and math.floor(w/3) == 0:
        return 3
    elif math.floor(r/3) == 1 and math.floor(w/3) == 1:
        return 4
    elif math.floor(r/3) == 1 and math.floor(w/3) == 2:
        return 5
    elif math.floor(r/3) == 2 and math.floor(w/3) == 0:
        return 6
    elif math.floor(r/3) == 2 and math.floor(w/3) == 1:
        return 7
    elif math.floor(r/3) == 2 and math.floor(w/3) == 2:
        return 8
    else:
        return "Not Valid"


def numbers_on_board_by_blocks():
    numbers_on_board_by_blocks = [[], [], [], [], [], [], [], [], []]
    for row in range(9):
        for col in range(9):
            pos_block = int(decide_block(row, col))
            numbers_on_board_by_blocks[pos_block].append(numbers_on_board_by_rows[row][col])
    return numbers_on_board_by_blocks

def is_valid(number, row, col):
    numbers_on_board_by_blocks1 = numbers_on_board_by_blocks()

    if number in numbers_on_board_by_rows[int(row)]:
        return False
    for i in range(9):
        if number == numbers_on_board_by_rows[i][int(col)]:
           return False
    if number in numbers_on_board_by_blocks1[int(decide_block(int(row), int(col)))]:
        return False
    return True

def print_board():
    for row in range(9):
        for col in range(9):
            if not is_empty(row,col) :
                draw_real(col,row,numbers_on_board_by_rows[row][col])


def is_empty(row,col):
    if(numbers_on_board_by_rows[int(row)][int(col)] == 0):
        return True
    return False

def mark_square(row,col,remove):
    if remove:
        pygame.draw.line(screen, RED, [int(row * SIZE[0] / 9), int(col * SIZE[0] / 9)], [int((row + 1) * SIZE[0] / 9), int(col * SIZE[0] / 9)], 7)
        pygame.draw.line(screen, RED, [int(row * SIZE[0] / 9), int(col * SIZE[0] / 9)], [int(row * SIZE[0] / 9), int((col + 1) * SIZE[0] / 9)], 7),
        pygame.draw.line(screen, RED, [int((row + 1) * SIZE[0] / 9), int((col + 1) * SIZE[0] / 9)], [int((row + 1) * SIZE[0] / 9), int((col) * SIZE[0] / 9)], 7),
        pygame.draw.line(screen, RED, [int((row + 1) * SIZE[0] / 9), int((col + 1) * SIZE[0] / 9)], [int((row) * SIZE[0] / 9), int((col + 1) * SIZE[0] / 9)], 7)

    lines = [pygame.draw.line(screen, RED, [int(row*SIZE[0]/9), int(col*SIZE[0]/9)], [int((row+1)*SIZE[0]/9), int((col)*SIZE[0]/9)], 7),
             pygame.draw.line(screen, RED, [int(row*SIZE[0]/9), int(col*SIZE[0]/9)], [int((row)*SIZE[0]/9), int((col+1)*SIZE[0]/9)], 7),
             pygame.draw.line(screen, RED, [int((row+1)*SIZE[0]/9), int((col+1)*SIZE[0]/9)], [int((row+1)*SIZE[0]/9), int((col)*SIZE[0]/9)], 7),
             pygame.draw.line(screen, RED, [int((row+1)*SIZE[0]/9), int((col+1)*SIZE[0]/9)], [int((row)*SIZE[0]/9), int((col+1)*SIZE[0]/9)], 7)]





def place_real_num(row,col,num):
    if is_empty(row, col):
        numbers_on_board_by_rows[int(row)][int(col)] = num
#        numbers_on_board_by_blocks1 = numbers_on_board_by_blocks()

def place_num(row,col,num):
    guess_board[int(row)][int(col)] = num
#        numbers_on_board_by_blocks1 = numbers_on_board_by_blocks()


def draw_num(col,row,num):
    pygame.draw.rect(screen, WHITE, pygame.Rect((row)*SIZE[0]/9+7, (col)*SIZE[1]/9 +7, 60-14, 60-14))
    pos = [(row)*SIZE[0]/9+SIZE[0]/18 - 12.5, (col)*SIZE[1]/9+SIZE[1]/18 - 30]
    font = pygame.font.SysFont('arial', 50)
    text = font.render(str(num), True, GRAY)
    screen.blit(text, pos)
    pygame.display.update()


def draw_real(col,row,num):
    pygame.draw.rect(screen, WHITE, pygame.Rect((row)*SIZE[0]/9+7, (col)*SIZE[1]/9 +7, 60-14, 60-14))
    pos = [(row)*SIZE[0]/9+SIZE[0]/18 - 12.5, (col)*SIZE[1]/9+SIZE[1]/18 - 30]
    font = pygame.font.SysFont('arial', 50)
    text = font.render(str(num), True, BLACK)
    screen.blit(text, pos)
    pygame.display.update()

def draw_backround(mistakes_count,hints_count):
  screen.fill(WHITE)
  # Draws the lines for every row and collum (creates a 9 by 9 matrix)
  for i in range(8):
      pygame.draw.rect(screen, BLACK, ((SIZE[0]/9)*(i+1) - 1.5, 0, 3, SIZE[1]))
  for i in range(8):
      pygame.draw.rect(screen, BLACK, (0, ((SIZE[1])/9)*(i+1) - 1.5, SIZE[0], 3))
  # Draws the thicker lines that creates all 9 boxes
  for i in range(2):
      pygame.draw.rect(screen, BLACK, ((SIZE[0]/3)*(i+1) - 3.5, 0, 7, SIZE[1]))
  for i in range(2):
      pygame.draw.rect(screen, BLACK, (0, ((SIZE[1])/3)*(i+1) - 3.5, SIZE[0], 7))
  # Draw the outlines
  for i in range(2):
    pygame.draw.rect(screen, BLACK, (0, i*SIZE[0] , SIZE[0], 7))
  for i in range(2):
    pygame.draw.rect(screen, BLACK, (i*SIZE[0] - 7, 0, 14, SIZE[1]))
  # Prints mistakes at the buttom
  print_mistakes_and_hints(mistakes_count,hints_count)

  print_board()


def print_mistakes_and_hints(mistakes_count,hints_count):
    erase_mistakes_and_hints()
    mistakes_pos = [(40-font_size)/2, SIZE[1]+(40-font_size)/2]
    hints_pos = [(40-font_size)/2 + 120, SIZE[1]+(40-font_size)/2]
    font = pygame.font.SysFont('arial', font_size)
    mistakes = font.render("Mistakes: "+ str(mistakes_count) + "/3", True, BLACK)
    hints = font.render("Hints: "+ str(hints_count) + "/3", True, BLACK)
    screen.blit(mistakes, mistakes_pos)
    screen.blit(hints, hints_pos)

    pygame.display.update()

def erase_mistakes_and_hints():
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, SIZE[1]+7, SIZE[0], 40))


done = False

def game_over(mistakes_count):
    if is_over(mistakes_count):
        pygame.draw.rect(screen, WHITE, (0, 0, 540, 580))
        screen.blit(GAME_OVER, (SIZE[0] / 2 - 85, SIZE[1] / 2))
        done = True

def is_over(mistakes_count):
    if mistakes_count >= 3:
        return True
    return False

def hint(row,col):
    pygame.draw.rect(screen, WHITE, pygame.Rect((row)*SIZE[0]/9+5, (col)*SIZE[1]/9 +7, 60-12, 60-12))
    if is_empty(row,col):
        draw_real(col, row, solution[int(row)][int(col)])


draw_backround(mistakes_count, hints_count)

while not done:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          done = True
      if not is_over(mistakes_count):
          if event.type == MOUSEBUTTONDOWN:
              row = event.pos[0] // (SIZE[1] / 9)
              col = event.pos[1] // (SIZE[0] / 9)

          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_0 and hints_count < 3 and is_empty(row,col):
                  hint(row,col)
                  hints_count += 1
                  print_mistakes_and_hints(mistakes_count,hints_count)
              if is_empty(row, col):  # and
                  if event.key == pygame.K_1:
                      place_num(row, col, 1)
                      draw_num(col, row, 1)
                  elif event.key == pygame.K_2:
                      place_num(row, col, 2)
                      draw_num(col, row, 2)
                  elif event.key == pygame.K_3:
                      place_num(row, col, 3)
                      draw_num(col, row, 3)
                  elif event.key == pygame.K_4:
                      place_num(row, col, 4)
                      draw_num(col, row, 4)
                  elif event.key == pygame.K_5:
                      place_num(row, col, 5)
                      draw_num(col, row, 5)
                  elif event.key == pygame.K_6:
                      place_num(row, col, 6)
                      draw_num(col, row, 6)
                  elif event.key == pygame.K_7:
                      place_num(row, col, 7)
                      draw_num(col, row, 7)
                  elif event.key == pygame.K_8:
                      place_num(row, col, 8)
                      draw_num(col, row, 8)
                  elif event.key == pygame.K_9:
                      place_num(row, col, 9)
                      draw_num(col, row, 9)

                  elif event.key == pygame.K_RETURN:
                      if is_valid(guess_board[int(row)][int(col)], row, col):
                        place_real_num(row, col, guess_board[int(row)][int(col)])
                        draw_real(col,row, guess_board[int(row)][int(col)])
                      else:
                          mistakes_count += 1
                          print_mistakes_and_hints(mistakes_count,hints_count)


      game_over(mistakes_count)
  pygame.display.update()