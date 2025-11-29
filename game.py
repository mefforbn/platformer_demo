import pygame, sys

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Ninja Gaming")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("data/images/clouds/cloud_1.png")
        self.image.set_colorkey("black")


        self.image_pos = [160, 260]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)


    def run(self):
        while True:
            self.screen.fill("skyblue")
            self.image_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.image, self.image_pos)

            image_r = pygame.Rect(self.image_pos[0], self.image_pos[1], self.image.get_width(), self.image.get_height()) 

            if image_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, "blue", self.collision_area)
            else:
                pygame.draw.rect(self.screen, "red", self.collision_area)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()