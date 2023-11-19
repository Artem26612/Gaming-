import sys

import pygame

from settings import Settings


class AlienInvasion:
    '''Класс для управления ресурсами и поведением игры'''

    def __init__(self):
        '''Инициализирует игру и создает игровые ресурсы'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption('Alien Invasion')
        '''Цвет фона'''
        self.bg_color = self.settings.bg_color


    def run_game(self):
        '''Запуск основного цикла игры'''
        while True:
            '''Отслеживание событий клавиатуры и мышки'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            '''Отображение последнего прорисованного экрана'''
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
