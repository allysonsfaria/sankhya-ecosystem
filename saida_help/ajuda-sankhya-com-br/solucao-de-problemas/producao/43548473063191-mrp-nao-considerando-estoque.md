---
id: "43548473063191"
titulo: "MRP não considerando Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548473063191-MRP-n%C3%A3o-considerando-Estoque"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-10-13T20:45:59Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# MRP não considerando Estoque

Ao executar o MRP na tela "**Planejamento de Produção (MRP I)"** (Produção » Rotinas » Planejamento de Produção (MRP I)), o sistema não considera o estoque disponível no cálculo da necessidade de materiais. Com isso, sugere compra ou produção em quantidades superiores às reais, mesmo com o estoque abastecido. O comportamento aparece apenas no resultado do cálculo.

Neste caso, é sempre necessário validar se as configurações estão corretas conforme a necessidade da empresa, portanto siga o passo a passo abaixo:

**(1)** Acesse a tela de **"Planejamento de Produção (MRP I)"** (Produção » Rotinas » Planejamento de Produção (MRP I)) e selecione a configuração utilizada no **Nro. Plano** selecionado.

**(2)** Na aba **"Filtros de Estoque (MP)"**, verifique o campo **"Estoque Atual"**. Certifique-se de que está selecionada a opção **"Considera (Filtro Estoque)"** ou **"Considera (Procedimento Personalizado)"**, conforme a necessidade do processo.

Obs.: Para considerar estoque de **PI** (Produto Intermediário), é necessário acessar a aba **"Filtros de Estoque (PA)"** e considerar o estoque nesta aba selecionando os locais necessários.

**(3)** Se utilizar a opção **"Considera (Filtro Estoque)"**, configure corretamente os filtros de empresa, locais e estoque, garantindo que o estoque do produto esteja sendo considerado no cálculo.

**(4)** Caso utilize **"Considera (Procedimento Personalizado)"**, valide se o procedimento está retornando corretamente o saldo de estoque para os produtos.

**(5)** Após ajustar as configurações, salve e reprocesse o plano mestre de produção (MPS) e execute novamente o MRP para validar se o estoque está sendo considerado corretamente.

**(6)** Se o sistema ainda continuar não considerando o estoque no **MRP**, após estes procedimentos acima, será necessário abrir um chamado com o Service Desk para análise do cenário.
