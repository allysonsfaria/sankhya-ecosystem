---
id: "39385120812695"
titulo: "GraphQL Error (Code: 500) ao abrir a tela Movimentação Financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39385120812695-GraphQL-Error-Code-500-ao-abrir-a-tela-Movimenta%C3%A7%C3%A3o-Financeira"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T13:31:06Z"
rotulos: ["Movimentação Financeira", "Atualização", "Financeiro", "Erro", "Artigo criado KCS", "Financeiro - KCS", "GraphQL"]
---

# GraphQL Error (Code: 500) ao abrir a tela Movimentação Financeira

**MENSAGEM**

GraphQL Error (Code: 500)

Ou mensagens de erro genéricas ao tentar abrir a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira), seja em ambiente de teste ou produção.

**SITUAÇÃO**

Ao acessar a tela **Movimentação Financeira** (**Financeiro » Rotinas » Movimentação Financeira**) utilizando o layout **Design System**, o sistema apresenta mensagens de erro e não exibe os títulos corretamente.

**SOLUÇÃO**

A solução para este erro envolve a atualização do módulo **"BFF Financeiro"** e a remoção de filtros padrão conflitantes. Siga os passos abaixo:

**(1)** Acesse o sistema com o usuário **"SUP"**.

**(2)** Abra a tela **"Movimentação Financeira"** (Financeiro Movimentação Financeira).

**(3)** No canto superior da tela, clique no ícone **"SUP"**.

**(4)** Selecione a opção **"Atualizar telas do Design System"**.

**(5)** Aguarde alguns minutos enquanto a atualização é processada. Pode ser exibida uma mensagem de **"tempo excedido"**, mas a atualização será aplicada normalmente.

**(6)** Clique em **"OK"** na mensagem de erro apresentada.

**(7)** Feche a tela **"Movimentação Financeira"** e acesse-a novamente para validar se o erro foi corrigido.

**Observação:** A solução está disponível a partir da versão **"BFF Financeiro 1.19.1"** ou superior (versões 1.19.0, 1.20.11 também corrigem problemas relacionados). Realize sempre a atualização em ambiente de **"teste"** antes de aplicar em produção.

**CAUSA**

O problema ocorre devido a uma incompatibilidade causada por alterações na classe da **Movimentação Financeira**, presentes em versões anteriores do módulo **Financeiro BFF**.
