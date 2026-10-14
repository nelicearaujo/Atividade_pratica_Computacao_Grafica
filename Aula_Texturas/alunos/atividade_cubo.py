# Arquivo inicial da atividade. Leia ATIVIDADE.md e altere os trechos marcados com TODO.
from pathlib import Path
import argparse
import pygame

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial
from geometry.boxGeometry import BoxGeometry

IMAGENS = Path(__file__).resolve().parent / 'images'
TEXTURA = 'mosaico.png'  # TODO 1: trocado de 'grade_uv.png' para 'mosaico.png'
VELOCIDADE = 0.8  # radianos por segundo


class Cubo(Base):
    def initialize(self):
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=960 / 640)
        self.camera.setPosition([0, 0, 3.2])
        self.velocidade = VELOCIDADE

        # cubo principal
        textura = Texture(IMAGENS / TEXTURA)
        self.mesh = Mesh(BoxGeometry(), TextureMaterial(textura))
        self.mesh.rotateX(0.35)
        self.mesh.rotateY(0.5)
        self.scene.add(self.mesh)

        # TODO 2: crie self.satelite, um segundo cubo com grade_uv.png repetida 2x2
        textura_satelite = Texture(IMAGENS / 'grade_uv.png')
        material_satelite = TextureMaterial(textura_satelite, {'repeatUV': [2, 2]})
        self.satelite = Mesh(BoxGeometry(), material_satelite)

        # TODO 3: adicione o satélite como FILHO do cubo principal, a 1.3 unidades do centro, escala 0.4
        # É importante definir a posição antes da escala para que a distância não seja encolhida
        self.satelite.setPosition([1.3, 0, 0])
        self.satelite.scale(0.4)
        self.mesh.add(self.satelite)

    def update(self):
        # Lendo o teclado via pygame para garantir que funciona sem erros de atributos
        teclas = pygame.key.get_pressed()

        # TODO 4: as setas 'up' e 'down' aumentam e diminuem self.velocidade
        aceleracao = 1.5  # Valor arbitrário de aceleração
        if teclas[pygame.K_UP]:
            self.velocidade += aceleracao * self.deltaTime
        if teclas[pygame.K_DOWN]:
            self.velocidade -= aceleracao * self.deltaTime

        self.mesh.rotateY(self.velocidade * self.deltaTime)

        # TODO 5: o satélite também gira em torno do PRÓPRIO eixo X, a 2 rad/s.
        self.satelite.rotateX(2 * self.deltaTime)

        self.renderer.render(self.scene, self.camera)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int)
    parser.add_argument('--screenshot')
    args = parser.parse_args()
    Cubo(title='Atividade: Cubo com satélite').run(args.frames, args.screenshot)