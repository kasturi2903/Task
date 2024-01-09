# robot_module.py
import pygame
import random
import math

class RobotSimulation:
    def __init__(self, arena_size=(640, 480), robot_radius=5, speed=2):
        pygame.init()

        
        self.screen_width, self.screen_height = arena_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Robot Movement in Arena")

        
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

    
        self.robot_radius = robot_radius
        self.robot_x = self.screen_width // 2
        self.robot_y = self.screen_height // 2

        
        self.speed = speed
        self.angle = random.uniform(0, 2*math.pi)  

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False


        self.robot_x += self.speed * math.cos(self.angle)
        self.robot_y += self.speed * math.sin(self.angle)

        
        if not (0 <= self.robot_x <= self.screen_width and 0 <= self.robot_y <= self.screen_height):
            
            self.angle = random.uniform(0, 2*math.pi)

        
        self.screen.fill(self.BLACK)
        pygame.draw.circle(self.screen, self.WHITE, (int(self.robot_x), int(self.robot_y)), self.robot_radius)
        pygame.display.flip()

    
        pygame.time.Clock().tick(60)

        return True

    def run_simulation(self):
        running = True
        while running:
            running = self.update()

        pygame.quit()


if __name__ == "__main__":
    simulation = RobotSimulation()
    simulation.run_simulation()
