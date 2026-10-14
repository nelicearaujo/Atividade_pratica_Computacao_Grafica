# Sistema Solar com Composição de Matrizes

Atividade prática da aula de Transformações Geométricas, desenvolvida com Python, PyGame e PyOpenGL.

O projeto implementa um mini sistema solar animado usando matrizes de translação, rotação e escala. A cena contém um Sol, um planeta que orbita o Sol e uma Lua que orbita o planeta acompanhando o seu movimento.

## Integrantes

- João Vicente Batista da Cunha
- Nelice Gomes Araujo

## Demonstração

![Resultado da atividade](capturas/resultado.png)

## Requisitos

- Python 3;
- OpenGL 3.3 ou superior;
- Dependências listadas em `requirements.txt`.

## Como executar

No terminal, dentro da pasta `alunos`, instale as dependências:

```bash
pip install -r requirements.txt
```

Depois, execute a atividade:

```bash
python atividade_sistema_solar.py
```

Também é possível salvar uma captura pela linha de comando:

```bash
python atividade_sistema_solar.py --frames 1 --screenshot capturas/resultado.png
```

## Controles

- `Seta para cima`: aumenta a velocidade da órbita do planeta;
- `Seta para baixo`: diminui a velocidade da órbita do planeta;
- `P`: salva uma captura em `capturas/resultado.png`;
- `ESC`: encerra a execução.

A velocidade da órbita nunca fica negativa.

## Composição das transformações

As transformações são aplicadas aos vértices da direita para a esquerda. Por isso, a matriz do planeta é composta como:

```text
R_orbita @ T_orbita @ R_propria @ S
```

Em que:

- `S` reduz o tamanho do objeto;
- `R_propria` faz o planeta girar em torno do próprio eixo;
- `T_orbita` afasta o planeta do centro até o raio da órbita;
- `R_orbita` gira a posição já transladada ao redor do Sol.

A órbita utiliza `R @ T` porque a translação deve acontecer antes da rotação orbital. Assim, o planeta é deslocado para a distância correta do Sol e depois essa posição é rotacionada em torno da origem, formando a órbita.

A rotação própria fica à direita da translação porque deve ser aplicada primeiro, ainda no sistema de coordenadas local do planeta, antes que ele seja deslocado para a órbita.

## Estrutura principal

- `atividade_sistema_solar.py`: código da atividade e animação da cena;
- `core/`: classes de suporte para janela, entrada, matrizes e shaders;
- `formas.py` e `objeto.py`: criação e desenho dos objetos;
- `capturas/`: imagens geradas durante a execução;
- `requirements.txt`: dependências do projeto.
