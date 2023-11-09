# В данном случае воспользуемся библиотекой  Pygame она позволяет создать графический
# интерфейс игры, а также предлагает большое количество инструментов


import sys

import pygame


def check_win(mas, sign):  # Функция прооверки на победу
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:  # проверка одинакового знака по строкам
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][
            col] == sign:  # проверка одинакового знака по колонкам
            return sign
        if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:  # проверка одинакового знака по диагоналям
            return sign
        if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:  # проверка одинакового знака по диагоналям
            return sign
        if zeroes == 0:  # проверка когда все ячейки заполнены но нет выйгрыша
            return "Ничья"
    return False


pygame.init()
# создаем игровое окно
size_block = 100  # размер ячеек
margin = 15  # размер отступов
width = height = size_block * 3 + margin * 4  # расщитываем размер игрового поля
size_window = (width, height)  # задаем размер игрового поля
screen = pygame.display.set_mode(size_window)  # создаем окно игрового поля
font = pygame.font.SysFont('segoeprint', 80)  # шрифт
pygame.display.set_caption("Крестики-Нолики")  # название
img = pygame.image.load("images.png")
pygame.display.set_icon(img)  # картинка

# определяем цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

mas = [[0] * 3 for i in range(3)]  # создаем массив игровых ячеек заполнен нулями(пустая клетка)
game_over = False  # определяем что игра продолжается
query = 0  # Множество целых чисел 1 2 3 4 5 6 нужен для определения какой игрок походил, определяем по четности числа


# Цикл запуска игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # закрытие игры при нажатии на крестик окошка
            quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # определяем координаты клика мышки когда игра не окончена
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (margin + size_block)  # определяем номер колонки по которой кликнула мышка
            row = y_mouse // (margin + size_block)
            if mas[row][col] == 0:  # проверяем на пустоту ячейки
                if query % 2 == 0:  # определяем игрока и заносим х или о
                    mas[row][col] = 'X'
                else:
                    mas[row][col] = 'O'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # Запуск игры заново по нажатию клавиши Spase
            game_over = False
            query = 0
            mas = [[0] * 3 for i in range(3)]
            screen.fill(BLACK)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'X':  # определяем игрока и закрашиваем ячейку
                    color = RED
                elif mas[row][col] == 'O':  # определяем игрока и закрашиваем ячейку
                    color = GREEN
                else:
                    color = WHITE  # окрашиваем ячейки белым цветом и рисуем их по строкам и рядам с отступами
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == RED:  # отрысовываем крестик с помощью линий
                    pygame.draw.line(screen, WHITE, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
                    pygame.draw.line(screen, WHITE, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)
                elif color == GREEN:  # отрисивываем нолик из центра ячейки
                    pygame.draw.circle(screen, WHITE, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       5)
    if (query - 1) % 2 == 0:  # игрок Х
        game_over = check_win(mas, 'X')  # проверка на выйгрыш х
    else:
        game_over = check_win(mas, 'O')  # проверка на выйгрыш о
    # если выводится не пустая строка, кто либо выйграл или ничья выводим новое окно и пишем кто победил
    if game_over:
        screen.fill(BLACK)
        font = pygame.font.SysFont('segoeprint', 100)
        text1 = font.render(game_over, True, WHITE)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    # обновление состояния игры
    pygame.display.update()
