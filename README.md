# Project name: Space Shooter (jogo/sistema interativo)

### Membros:
- Matheus Batista de Araújo
- Marcus 

### Organização do projeto
- No diretório principal do projeto estão: 
    - Pasta "resources", nela estão todos os arquivos de imagem utilizados ao longo do projeto, as imagens utilizadas na contrução de botões e similares já possuem essa informação indicada em seu nome.
    - Pasta "sounds", nesta pasta estão todos os arquivos de som que foram necessários para a elaboração do projeto, desde musicas para o background quanto sons utilizados em ações de botões e similares.
    - Arquivo "main.py", nele está sendo executado o jogo como um todo a partir das funções importadas a partir do s outros arquivos do projeto.
    - Arquivo "constants.py", inclui todas as constantes definidas para o projeto, desde cores a tamanhos de tela.
    - Arquivo "shapes.py", inclui todos os formatos de nave disponiveis para o player e para os inimigos, os formatos são reservados para facilitar a distinção entre player e inimigos.
    - Arquivo "classes.py", neste arquivo estão os objetos e funções atrelados ao player e aos inimigos gerados pelo jogo, tendo em vista que ambos o objeto "player" e o objeto "enemy" derivam de uma mesma classe.
    - Arquivo "screens.py", neste arquivo estam localizadas as funções que "imprimem/exibem" o jogo na tela, assim como um simples andamento entre as telas, integrando os sons, imagens e inputs do player.
    - Arquivo "projectiles.py", nele estão a criação dos projeteis e atualização dos mesmos (movimento).
    - Arquivo "functions.py", contem a criação dos inimigos durante o gameplay.

### Ferramentas
- Para elaboração e conclusão deste projeto utilizamos:
    - O framework "Pygame" por facilitar uma série de funcionalidades que desejávamos implementar no projeto
    - Estamos utilizando o repositório do github pela facilidade em gerenciar o versionamento do código do projeto, assim como integrar as partes desenvolvidas separadamente
    - Ao longo do projeto utilizamos as bibliotecas:
        - pygame : possiblitando a utilização das funções presentes no framework 
        - sys : necessária para funcionalidades de sistema que fossem necessárias
        - math : utlizada para cálculos de ângulos e outros parâmetros ao longo do projeto
        - random : utilizada para geração de valores aleatórios necessários

### Divisão de tarefas
- A divisão de tarefas foi sendo feita a medida que diferentes partes do projeto estavam sendo concluídas, com a intenção de agilizar o desenvolvimento do projeto
    - Marcus: criação do player e recebimento de inputs para controle do player, criação e comportamento dos inimigos, criação e mecânica de colisões dos projeteis do player e dos inimigos, criação dos power-ups. 
    - Matheus: criação do player e recebimento de inputs para controle do player, criação das telas apresentadas no jogo, recebimento de inputs para customização do player, fluxo das telas e funcionamento do jogo, adição de sons e musicas ao jogo.

### Aulas no projeto
- Procuramos utilizar ao máximo os temas abordados nas aulas da disciplina ao longo do projeto, utilizamos implementação de funções, armazenamento e tratamento de dados (variáveis locais, constantes, arrays), laços de repetição, condicionais, orientação a objetos.
    - Utilizamos diversas formas de variáveis para armazenar os dados gerados pelo jogo (desde tuplas, constantes, arrays e etc) e receber os inputs do jogador para os controles.
    - Utilizamos laços de repetição durante todo o projeto para atualizar o que estava sendo mostrado na tela (atualização constante dos elementos da tela e transições entre as mesmas), recebimento de inputs (controles do player e botões) e progressão de funcionalidades (contagem de tempo).
    - Utilizamos várias condicionais para filtrar os inputs e eventos que aconteciam durante o jogo, permitindo a tomada de decisões do programa.
    - Utilizamos orientação a objetos para a elaboração da nave do jogador e os inimigos gerados pelo jogo.

### Desafios ao longo do projeto
- O primeiro desafio do projeto foi encontrar as ferramentas que nos seriam uteis para elaboração do projeto, a maior parte delas estava presente no framework do pygame, que até então era algo novo para a equipe.
- Criar uma mecânica eficiente para o player, recebendo os inputs do player de forma ininterrupta e dividida entre mouse e teclado.
- Criar a lógica adequada para rotação e translado utilizando os inputs do player, uma vez que estavamos criando a nave do player e futuramente os inimigos a partir de polígonos ao invés de uma imagem já pronta.
- Realizar a interatividade entre a nave do player e os outros objetos (implementação de colisões entre player, projeteis e inimigos).
- Gerar uma animação/movimento ao background criado para as telas.
- Criar transições agradáveis entre as telas, para não ocorrerem surgimentos de tela repentinos ou ocorresse muito delay.
- Formatar as imagens e ajusta-las para tamanhos corretos, posicionar as imagens em posições relativas ao tamanho da tela (visando futura modificação do tamanho da tela).
- Integrar sons a todas as telas e a alguns eventos e ações do player e inimigos.          
             

### Funções:

- Uma função que recebe os vértices do player e calcula os novos vértices com checando se as teclas WASD estão posicionadas como uma translação.
- Uma função que recebe o ângulo do player e vértices e retorna o angulo entre o player e a reta que passa pelo centro do player.
- Uma função que recebe um conjunto de vertices e um angulo e aplica uma rotação sobre os vértices.