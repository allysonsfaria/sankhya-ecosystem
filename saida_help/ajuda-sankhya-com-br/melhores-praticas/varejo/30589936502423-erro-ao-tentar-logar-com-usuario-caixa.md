---
id: "30589936502423"
titulo: "Erro ao tentar logar com usuário caixa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30589936502423-Erro-ao-tentar-logar-com-usu%C3%A1rio-caixa"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-07-24T12:42:28Z"
rotulos: ["Relatórios", "Contas", "Usuários", "Financeiro", "Parâmetro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro ao tentar logar com usuário caixa", "Falha ao tentar chamar o serviço", "AberturaCaixaSP.abreCaixaAtualizandoSessao", "Erro"]
---

# Erro ao tentar logar com usuário caixa

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30589936490135) **MENSAGEM:**

Falha ao tentar chamar o serviço 'AberturaCaixaSP.abreCaixaAtualizandoSessao'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30589930720919)SOLUÇÃO:**

Verifique se a conta em questão está sendo utilizada por algum usuário e se permanece em aberto.

Para isso, utilize o seguinte comando no **DBExplorer** (Configurações » Avançado » DBExplorer):

**SELECT \* FROM TGFCAI WHERE DTFECHAMENTO IS NULL**

**Exemplo:**

![Imagem 3: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/30596774127895)

Se houver registros com o campo **DTFECHAMENTO** em branco, significa que existem caixas em aberto. Nesse caso, o respectivo usuário deverá realizar o fechamento antes de prosseguir.

Caso não tenha acesso à tela **DBExplorer**, a consulta pode ser realizada por meio da tela "**Fechamento de Caixa"** (Financeiro » Relatórios » Fechamento de Caixa).

Aplique o filtro informando o período (preferencialmente um período relativamente grande) e os usuários que utilizam a conta.

Na grade, será possível identificar as contas e verificar se há caixas sem fechamento (campo "**Dt. Fechamento"** vazio).

Exemplo:

![Imagem 4: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/30596774129559)

**![Imagem 5: Observação:](https://ajuda.sankhya.com.br/hc/article_attachments/30596674583959) Observação:**

Para fechar o caixa, o usuário deve acessar o sistema e realizar o fechamento pela tela **PDV WEB**, caso o parâmetro **USAABFCAIXAPDV** esteja ativado.

Se o parâmetro **não** estiver ativado, o fechamento do caixa deverá ser realizado manualmente ao sair do sistema.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30589936491159)CAUSA:**

Mensagem ocorre quando tenta logar no sistema com usuário caixa que tenha uma conta vinculada e a mesma esteja com caixa aberto aberto em outro usuário.
