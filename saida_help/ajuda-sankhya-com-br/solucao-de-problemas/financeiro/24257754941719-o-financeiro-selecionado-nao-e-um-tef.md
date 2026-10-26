---
id: "24257754941719"
titulo: "O financeiro selecionado não é um TEF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24257754941719-O-financeiro-selecionado-n%C3%A3o-%C3%A9-um-TEF"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:47:17Z"
rotulos: ["Movimentação Financeira", "TEF", "Financeiro", "CORE_E03304", "Erro"]
---

# O financeiro selecionado não é um TEF

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24257768250135) **MENSAGEM:**

[CORE\_E03304] O financeiro selecionado não é um TEF

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24257768251287) **SOLUÇÃO:**

Esse tipo de situação pode ocorrer quando o Sankhya por algum motivo não recebe a resposta da operadora. **Para esse tipo de situação foi criada uma opção dentro da Movimentação Financeira** >> Botão **"Outras opções"** >> "Recebimento com cartão (Admin)"
**Essa opção deve ser utilizada para os casos em que não se consegue receber a resposta do TEF** referente à aprovação do recebimento. Assim, para que essa opção possa ser usada, é necessário que o acesso **"Recebimento com cartão (Administrativo)"** seja liberado para os usuários autorizados.

Apenas os títulos que tiveram erro durante a rotina de recebimento estarão elegíveis para proceder com o recebimento administrativo. Caso contrário, será apresentada a mensagem abaixo:

"O título selecionado não está elegível para proceder com o recebimento administrativo. Não foi encontrado registro de tentativa de recebimento malsucedida".

Clicando na opção Recebimento com cartão (Administrativo), será exibido um pop-up, para que os dados relativos ao recebimento administrativo sejam inseridos. **Após informar todos os dados e clicar em "Registrar recebimento", o botão concluir será apresentado.**

![Imagem 3: Clicando na opção Recebimento com cartão (Administrativo) , será exibido um pop-up, para que os dados relativos ao…](https://ajuda.sankhya.com.br/hc/article_attachments/24257768252951)

**Observação:** essa opção está liberada nas versões do sistema que usam o layout HTML5 da tela. Exemplo: a versão 4.13b235.

![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24257754933271)**CAUSA:**

Retorno da transação do TEF não inseriu dados no banco de dados. Pela consulta na intermediaria a transação ocorreu, porém o comprovante não foi possível de ser impresso no sistema.
