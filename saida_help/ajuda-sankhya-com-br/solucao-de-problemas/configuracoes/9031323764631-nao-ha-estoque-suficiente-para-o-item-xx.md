---
id: "9031323764631"
titulo: "Não há estoque suficiente para o item XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9031323764631-N%C3%A3o-h%C3%A1-estoque-suficiente-para-o-item-XX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:11:29Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Estoque", "Preferências", "CORE_E03881", "CORE_E01251", "Estoque Insuficiente para Item do Kit", "Erro"]
---

# Não há estoque suficiente para o item XX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16673233253911) MENSAGEM:**

[CORE\_E03881]: Não há estoque suficiente para o item XX.

[CORE\_E01251] Não há estoque suficiente para o item XX.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16673249225751) CAUSA:**

Ao vender um item do kit que não possui estoque suficiente.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16673233257367) SOLUÇÃO:**

![Imagem 4: Verifique as seguintes informações:](https://ajuda.sankhya.com.br/hc/article_attachments/16673249209111) Verifique as seguintes informações:

**(2)** Parâmetro **"LOCALPADRAO"** (Caminho de acesso: Configurações » Avançado » Preferências);

![Imagem 5: (2) Parâmetro " LOCALPADRAO" (Caminho de acesso: Configurações » Avançado » Preferências);](https://ajuda.sankhya.com.br/hc/article_attachments/9188249345559)

**(2)** Veja qual a validação do Grupos de Produtos/Serviços, aba Estoque »Validação;

![Imagem 6: (2) Veja qual a validação do Grupos de Produtos/Serviços, aba Estoque » Validação;](https://ajuda.sankhya.com.br/hc/article_attachments/15855753937815)

**(2)** Se componente realmente possui estoque;

**(2)** Habilite o parâmetro **"CONTROLECOMPON"** (Caminho de acesso: Configurações » Avançado » Preferências).

![Imagem 7: (2) Habilite o parâmetro " CONTROLECOMPON" (Caminho de acesso: Configurações » Avançado » Preferências).](https://ajuda.sankhya.com.br/hc/article_attachments/9188247109911)

(1)**NOTA:**

Para trabalhar com local padrão definido nos componentes do kit, habilite o parâmetro **"Mostrar o controle na aba de componentes - CONTROLECOMPON"**.

Assim, quando ligado, será apresentado no Cadastro de Produtos, aba **"Componentes"**, o campo **"Controle"** (que engloba o local).

![Imagem 8: Para processo de venda de KIT com Lote através da Explosão Automática de Lotes:](https://ajuda.sankhya.com.br/hc/article_attachments/16673249216663) Para processo de venda de KIT com Lote através da Explosão Automática de Lotes:

"A Explosão Automática de Lotes é uma funcionalidade disponível na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas),  em que, ao lançar um item em uma nota de venda ou pedido de venda, caso o produto seja controlado por lote e data de validade, será precisará informar o lote de cada item, porém, com essa funcionalidade, não será necessário informar o Lote (CONTROLE)."

**[Explosão Automática de Lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg1MTI3MDM3MTMsInRpY2tldF9pZCI6MTc3OTE0LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTY1MDIyODkzNn0.ZLXlEAL59X9Mi_pqBJv2LwtKsExnCfrrWW2gTRvIeCw)**

![Imagem 9: A explosão de lote para componente de KIT não funciona para "KIT Independente", parâmetro " CONFKITIND " (Caminho de…](https://ajuda.sankhya.com.br/hc/article_attachments/16673233287319) A explosão de lote para componente de KIT não funciona para "KIT Independente", parâmetro "**CONFKITIND**" (Caminho de acesso: Configurações » Avançado » Preferências) = Ligado.

![Imagem 10: Para que seja possível explodir o lote do componente "LOTAUTKIT" (Caminho de acesso: Configurações » Avançado »…](https://ajuda.sankhya.com.br/hc/article_attachments/9188260252695)

**(2)** Para que seja possível explodir o lote do componente **"LOTAUTKIT"** (Caminho de acesso: Configurações » Avançado » Preferências),  o sistema necessita que as seguintes condições sejam atendidas:

![Imagem 11: (2) Para que seja possível explodir o lote do componente "LOTAUTKIT" (Caminho de acesso: Configurações » Avançado »…](https://ajuda.sankhya.com.br/hc/article_attachments/9188313089815)

**(2)** O "Grupo de Produtos" do componente utilizado na operação deve validar estoque, ou seja, não pode ser igual a **"Não valida"** ou **"Pela Empresa, mas aceita"**. 

**(2)** O **"Local"** que contém estoque do produto em questão não pode estar contido no parâmetro **"DESCLOCALKIT"** (Caminho de acesso: Configurações » Avançado » Preferências).

![Imagem 12: Deve haver estoque no mesmo "Local" e "Empresa", informado na aba "Componentes do cadastro do produto KIT" para este…](https://ajuda.sankhya.com.br/hc/article_attachments/9188316072087)

**(2)** Deve haver estoque no mesmo "Local" e "Empresa", informado na aba **"Componentes do cadastro do produto KIT"** para este componente. 

**(2)** A soma de: ESTOQUE" - "RESERVADO" - "WMSBLOQUEADO" deve ser maior que zero.

**![Imagem 13: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16673233292055) OBSERVAÇÃO:**

Quando habilitando o parâmetro LOTAUTKIT (Caminho de acesso: Configurações » Avançado » Preferências), o sistema tem um controle automático por data de validade de lote para kit. Ao fazer a venda o sistema encontra o lote com a data mais próxima do vencimento.

![Imagem 14: Quando habilitando o parâmetro LOTAUTKIT (Caminho de acesso: Configurações » Avançado » Preferências) , o sistema tem…](https://ajuda.sankhya.com.br/hc/article_attachments/9188313089815)

Na baixa dos produtos componentes do kit, se não encontrar Matéria Prima suficiente não é permitido a inclusão do Produto Acabado.
Ou seja, se o componente tem controle por lote tem que seguir as configurações de explosão de lote.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9031323764631-N%C3%A3o-h%C3%A1-estoque-suficiente-para-o-item-XX#top)
