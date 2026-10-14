## `Aula_Transformacoes/LEIA_PRIMEIRO.md`

# Material da aula de Transformações Geométricas

- `Aula_Transformacoes_OpenGL_26_Slides.pptx`: slides com notas e roteiro das demonstrações.
- `alunos/`: framework didático, 3 demonstrações, arquivo inicial da atividade, enunciado e instruções para Windows/macOS. **Entregue apenas esta pasta à turma.**
- `professor/`: solução de referência, captura esperada e rubrica.

A aula continua o checkpoint `test-3.py` do repositório: as mesmas classes (`Base`, `Input`, `Utils`, `Attribute`, `Uniform`, `Matrix`) e a mesma convenção de multiplicação (global à esquerda, local à direita).

Diferença importante em relação ao `core/` da raiz do repositório: o `alunos/core/uniform.py` suporta o tipo `mat4`, que o `test-3.py` precisa. O `alunos/core/base.py` também pede OpenGL 3.3 core e trata ESC, captura (tecla P) e execução por N quadros.

As classes e convenções seguem o livro *Developing Graphics Frameworks with Python and OpenGL*, de Lee Stemkoski e Michael Pascale (CRC Press, 2022), capítulo 3.

Próxima aula: `Aula_GrafoCena` (capítulo 4), que transforma as matrizes desta aula em uma árvore de objetos, e depois `Aula_Texturas` (capítulo 5).

---

## `Aula_GrafoCena/LEIA_PRIMEIRO.md`

# Material da aula de Grafo de Cena

Ordem das aulas do repositório:

1. `Aula_Transformacoes`: matrizes 4x4, composição, global x local e projeção (capítulo 3).
2. **`Aula_GrafoCena`**: Object3D, Scene, Camera, Mesh, Geometry, Material e Renderer (capítulo 4).
3. `Aula_Texturas`: Texture, UV e TextureMaterial sobre o mesmo framework (capítulo 5).

- `Aula_GrafoCena_OpenGL_24_Slides.pptx`: slides com notas e roteiro das demonstrações.
- `alunos/`: framework, 3 demonstrações, arquivo inicial da atividade, enunciado e instruções. **Entregue apenas esta pasta à turma.**
- `professor/`: solução de referência, captura esperada e rubrica.

O framework é o mesmo usado na Aula_Texturas (mesmos nomes de classes e métodos), mas escrito por extenso e comentado para leitura em aula. Em vez de texturas, usa `BasicMaterial` com cores por vértice.

As classes e convenções seguem o livro *Developing Graphics Frameworks with Python and OpenGL*, de Lee Stemkoski e Michael Pascale (CRC Press, 2022), capítulo 4.

---

## `Aula_Texturas/LEIA_PRIMEIRO.md`

# Material da aula de Texturas

Pré-requisito: `Aula_GrafoCena` (capítulo 4). Esta aula usa Object3D, Scene, Camera, Mesh, Geometry, Material e Renderer sem reapresentá-los.

Atividade: cubo com textura `mosaico.png` e um satélite filho com `grade_uv.png` repetida 2x2 (`repeatUV`), orbitando o cubo e girando no próprio eixo, com velocidade controlada pelas setas. O retângulo aceita `--repetir 2` para demonstrar o slide 19.

A pasta alunos contém o framework didático, exemplos, imagens locais, atividade e instruções Windows/macOS. Entregue apenas essa pasta à turma.

A pasta professor contém a solução de referência e a rubrica. Use o mesmo ambiente Python da pasta alunos para executar a solução.

As classes e convenções seguem o livro *Developing graphics frameworks with Python and OpenGL*, de Lee Stemkoski e Michael Pascale, CRC Press, 2022. O README explica as adaptações de compatibilidade do subconjunto fornecido.
