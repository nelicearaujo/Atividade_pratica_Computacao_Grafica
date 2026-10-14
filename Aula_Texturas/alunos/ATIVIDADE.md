**Atv:** Cubo com Satélite Texturizado
**Integrantes:** João Vicente Batista da Cunha e Nelice Gomes Araujo

**Descrição:** 
Implementação de um sistema 3D composto por um cubo principal e um satélite orbitante, focando no mapeamento de texturas com coordenadas UV (PyOpenGL e Pygame). O projeto aplica texturas de imagem distintas aos objetos, estabelece uma relação hierárquica (pai/filho) para criar a órbita do satélite, e permite o controlo da velocidade de rotação através das setas do teclado. O satélite também apresenta uma rotação em torno do seu próprio eixo e utiliza a técnica de repetição de textura.

**Qual é o papel das coordenadas UV em uma textura e qual é o efeito da configuração repeatUV = [2,2]?** 
As coordenadas UV formam o sistema 2D utilizado para projetar e "embrulhar" uma imagem (textura) sobre os polígonos de um modelo 3D. O eixo U representa a horizontal da imagem e o V a vertical. Por padrão, estes valores variam de 0.0 a 1.0, esticando a imagem para preencher toda a face da geometria. 

Ao definirmos `repeatUV = [2,2]`, as coordenadas são multiplicadas por dois (passando a variar de 0.0 a 2.0). Como o valor ultrapassa o limite padrão de 1.0, a placa gráfica reinicia a amostragem da imagem. O efeito visual prático é que a textura original deixa de ser esticada uma única vez e passa a atuar como um mosaico, sendo desenhada repetidamente num formato de grelha (duas vezes na horizontal e duas vezes na vertical) em cada uma das faces do cubo satélite.