**Atv:** Braço Robótico
**Integrantes:** João Vicente Batista da Cunha e Nelice Gomes Araujo

**Descrição:** 
A estrutura é composta por base, ombro, braço, cotovelo, antebraço e garra. O projeto aplica o conceito de parentesco (pai/filho) e matrizes de transformação locais, permitindo controlar as articulações independentemente através do teclado, onde as peças conectadas acompanham o movimento da sua estrutura pai.

**Por que foi necessário utilizar pivôs em vez de simplesmente girar diretamente as caixas que representam o braço e o antebraço?**
Foi necessário utilizar pivôs (`Object3D` vazios) porque as formas geométricas, como a `caixa(...)`, são geradas e rotacionadas a partir do seu próprio centro (origem local). Se aplicássemos a rotação diretamente às caixas, o braço giraria em torno do seu próprio meio, como uma hélice, e não a partir da extremidade. Ao criar um `Object3D` para representar a articulação e colocar a caixa como sua filha (deslocada para cima pela metade da sua altura), transformamos esse pivô invisível numa "dobradiça". Assim, quando giramos o pivô, toda a geometria conectada a ele gira em torno da base correta, garantindo que o resto da estrutura hierárquica (antebraço e garra) acompanhe o movimento de forma interligada e natural.