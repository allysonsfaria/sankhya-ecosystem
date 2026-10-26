---
id: "360046212574"
titulo: "Quais as regras para geração ou não da Carga Média Tributária referente a Lei da Transparência?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046212574-Quais-as-regras-para-gera%C3%A7%C3%A3o-ou-n%C3%A3o-da-Carga-M%C3%A9dia-Tribut%C3%A1ria-referente-a-Lei-da-Transpar%C3%AAncia"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:32:32Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Parceiro", "Impostos", "O.S1482423", "Movimentação: Tipo \"Venda\"", "Configurar em TOP Parceiros e \"Origem do produto\"", "Parâmetro: Preencher \"LEI12741FONTE\""]
---

# Quais as regras para geração ou não da Carga Média Tributária referente a Lei da Transparência?

**(1)** Vejamos as regras para geração ou não da Carga Média Tributária referente a Lei da Transparência:

![Imagem 1: Preencha devidamente o parâmetro "Fonte do cálculo da Carga Média Tributária - LEI12741FONTE" :](https://ajuda.sankhya.com.br/hc/article_attachments/16537026826263) Preencha devidamente o parâmetro **"Fonte do cálculo da Carga Média Tributária - LEI12741FONTE"**:

- Tela **"Preferências"** (Caminho de acesso: Configurações » Avançado), chave '**LEI12741FONTE**'

![Imagem 2: Tela "Preferências" (Caminho de acesso: Configurações » Avançado), chave ' LEI12741FONTE '](https://ajuda.sankhya.com.br/hc/article_attachments/15523137723415)

![Imagem 3: O Tipo de Movimentação da nota deve ser "Venda" (TGFCAB.TIPMOV = V);](https://ajuda.sankhya.com.br/hc/article_attachments/16537026829975) O Tipo de Movimentação da nota deve ser **"Venda"** (TGFCAB.TIPMOV = V);

![Imagem 4: O campo "Aplicar a lei da transparência" na tela: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba…](https://ajuda.sankhya.com.br/hc/article_attachments/16536997968791) O campo **"Aplicar a lei da transparência"** na tela: Comercial » Arquivo » Cadastros » **Tipos de Operação - TOP,** aba **"Validações"**, deve ser igual a **"Usar do parceiro"** ou **"Aplicar sempre"**:

- Se for igual a Usar do parceiro, assinale o campo Aplicar a lei da transparência na tela: Configurações » Cadastros » Parceiros, aba **"Fiscal".** Ou defina o campo **"Classificação ICMS"** (nesta mesma tela e aba) como **"Consumidor Final", "Produtor Rural" ou "Consumidor Contribuinte".**

![Imagem 5: Se o campo "Origem do produto" (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), aba "Geral",…](https://ajuda.sankhya.com.br/hc/article_attachments/16537026835351) Se o campo **"Origem do produto"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), aba **"Geral",** estiver entre 0, 3, 4, 5 ou 8, significa que a origem do item em questão é Nacional. Neste caso, as cargas médias geradas serão agrupadas (Nacional) ou separadas (Federal, Estadual e Municipal). Se for diferente dos valores inicialmente citados, significa que a origem é Estrangeira. Nesse caso, as cargas médias geradas serão de importação.

Se todas as condições até aqui mencionadas forem atendidas, o sistema irá buscar os percentuais para fazer o cálculo.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16536997974423) IMPORTANTE:**

Para mais detalhes verifique o Manual: [Lei da Transparência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600174)
