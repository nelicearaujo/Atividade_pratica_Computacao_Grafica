**Atv:** Sistema Solar com Composição de Matrizes
**Integrantes:** João Vicente Batista da Cunha e Nelice Gomes Araujo

**Descrição:**
Implementação de um mini sistema solar 3D animado utilizando Python e PyOpenGL. O projeto aplica transformações geométricas (matrizes de translação, rotação e escala) para simular o movimento hierárquico de corpos celestes, incluindo a órbita de um planeta em torno do Sol e a órbita de uma lua acompanhando o planeta.

**Por que a órbita utiliza R @ T e a rotação própria do planeta fica à direita da translação?**
A ordem das multiplicações não é comutativa. Ao definir a órbita como `R @ T`, o objeto é primeiro transladado (afastado da origem para o seu raio de órbita) e, em seguida, essa posição já transladada é rotacionada em torno do centro do sistema global (o Sol), gerando o percurso orbital. 

A rotação própria do planeta é colocada à direita da translação (ex: `R_orbita @ T @ R_propria`) porque as transformações nos vértices são aplicadas da direita para a esquerda. Ao ser a primeira matriz na ordem de execução, ela faz com que o planeta gire em torno do seu próprio eixo local (centro geométrico) antes de ser deslocado e orbitar pelo espaço.