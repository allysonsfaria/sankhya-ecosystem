---
id: "360056245914"
titulo: "Aguarde, estamos identificando seu computador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056245914-Aguarde-estamos-identificando-seu-computador"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:27:20Z"
rotulos: ["#criadoroger", "Configuração", "Liberação de Computadores", "Segurança", "Controle de Acessos", "Identificação de Computador", "Controle de Acesso", "Sankhya", "Artigo atualizado KCS", "Plataforma - KCS", "WebConnection"]
---

# Aguarde, estamos identificando seu computador

A funcionalidade de **"Liberação de Computadores"** no sistema Sankhya permite controlar o acesso dos usuários, garantindo que eles possam fazer login apenas em máquinas previamente autorizadas. É importante compreender que essa mensagem aparecerá até que o WebConnection seja configurado no computador.

Muitos usuários têm dúvidas sobre como funciona o processo de captura do endereço MAC e a liberação de acesso. Este artigo esclarece o funcionamento correto dessa funcionalidade e orienta sobre a melhor forma de realizar as configurações necessárias.

### Mensagem

"Aguarde, estamos identificando seu computador"

### Causa

Ocorre quando no cadastro de usuário, há a marcação para acessar apenas computadores liberados, e está acessando em uma máquina onde o **"WebConnection"** não está devidamente configurado.

![Imagem 1: Ocorre quando no cadastro de usuário, há a marcação para acessar apenas computadores liberados, e está acessando em uma…](https://ajuda.sankhya.com.br/hc/article_attachments/14441257440151)

### Como funciona a liberação de computadores

A liberação de computadores no sistema Sankhya é realizada **por usuário**. Isso significa que quando você habilita a marcação para que um usuário acesse o sistema apenas por computadores liberados, cada combinação de **usuário + computador** precisa ser autorizada individualmente mas o WebConnection basta configurar apenas uma vez por computador.

Quando um usuário tenta fazer login em um computador pela primeira vez, o sistema captura automaticamente o endereço MAC da máquina e solicita a liberação. Essa solicitação deve ser aprovada na tela **"Liberação de Computadores"** (Configurações >> Controle de Acesso >> Liberação de Computadores).

### Estratégia para configurar Web Connection em vários computadores com apenas um usuário.

Uma estratégia para a instalação do WebConnection em várias máquinas utilizando um único usuário para registrar cada computador. Para evitar que todos usuários tenham que realizar o processo:

- Acessar com o SUP ou algum usuário que não esteja com a marcação: acessar apenas computadores liberados na máquina em que deseja configurar o WebConection.
- Realizar a instalação do Web Connection de acordo com: [Instalar Web Connection](https://sankhya.zendesk.com/knowledge/editor/01KAEVJ2X90M0VRJRKNKEZVDHB/pt-br?brand_id=360003747033)
- Acessar portal de vendas, selecionar uma nota/pedido e realizar a impressão ou download de algum PDF
- Após esses passos já estará configurado na máquina, basta os demais usuários usarem normalmente
- Observação: Esse processo é apenas para configurar o Web Connection, para liberar o computador, é preciso que a liberação seja feita indívidualmente para cada usuário por computador.

### Como realizar a liberação do computador caso não esteja

Acesse a tela **"Usuários"** (Configurações >> Controle de Acesso >> Usuários), vá até a aba **"Segurança"** e marque: **"Acessar apenas por computadores liberados?"**.

Oriente o usuário a fazer login no computador. Caso apareça a mensagem de identificação, acesse a tela **"Liberação de Computadores"** (Configurações >> Controle de Acesso >> Liberação de Computadores).

Identifique os computadores pendentes, altere o campo **"Status Liberação"** de Pendente para Liberado e salve.

Solicite ao usuário que acesse a aplicação novamente. Repita o processo para cada combinação de usuário e computador.

###
