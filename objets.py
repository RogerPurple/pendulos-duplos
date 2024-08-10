from utils import *
from math import cos
import pygame
import numpy as np
import copy

class Simple_Pendulum():
    def __init__(self, _position: Vector, _width: float, markers_on: bool) -> None:
        self.center = _position
        self.width = _width
        self.position = self.center + Vector(self.width, 0)
        self.init_position = self.position
        self.t = 1
        self.t2 = 1.635
        self.markers_on = markers_on
        
        self.markers = []
  
  
    def stretching_hour_function_x(self):
        a = self.width 
        w = np.pi
        phi_0 = np.pi / 4
        
        x =  a * cos(phi_0 * w * self.t) 
        self.t += 1/60 
    
        return x
    
    def stretching_hour_function_y(self):
        a = self.width 
        w = np.pi
        phi_0 = np.pi / 4
        
        x =  a * cos(phi_0 * w * self.t2) 
        self.t2 += 1/60 
    
        return x
    
    
    def update(self):
        # Atualiza a movimentação do pendulo
        self.position.x = self.center.x + self.stretching_hour_function_x()
        self.position.y = self.center.y + self.stretching_hour_function_y()
        
        if self.markers_on:
            # Adiciona rastros para mostrar o movimento
            new_marker = copy.deepcopy(self.position) 
            self.markers.append(new_marker)
            
            # Deleta os rastros depois de N rastros
            if len(self.markers) > 300:
                self.markers.pop()
                
    
    # Atualiza os graficos
    def render_graphs(self, _surface):
        # Peças fixas
        pygame.draw.aaline(_surface, "white", self.center.tupla(), self.position.tupla())
        pygame.draw.circle(_surface, "white", self.center.tupla(), 10)
        pygame.draw.circle(_surface, "red", self.position.tupla(), 10)
        
        if self.markers_on:
            # Rastros
            for marker in self.markers:
                pygame.draw.circle(_surface, "yellow", marker.tupla(), 2)

