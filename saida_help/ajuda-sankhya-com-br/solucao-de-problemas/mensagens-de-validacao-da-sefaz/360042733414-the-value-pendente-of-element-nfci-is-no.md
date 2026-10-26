---
id: "360042733414"
titulo: "The value 'PENDENTE' of element 'nFCI' is not valid."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042733414-The-value-PENDENTE-of-element-nFCI-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:29Z"
rotulos: ["ERRONF", "#criadoRoger", "#RevisadoGilmar", "Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "Valor Inválido para Código FCI", "FCI"]
---

# The value 'PENDENTE' of element 'nFCI' is not valid.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16451982909719) MENSAGEM:**

cvc-type.3.1.3: The value 'PENDENTE' of element 'nFCI' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16451982917783) SOLUÇÃO:**

Para correção seguir os passos abaixo:

![Imagem 3: Acesse: " Produtos " (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos )](https://ajuda.sankhya.com.br/hc/article_attachments/16451982922263) Acesse: "**[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos)

- Aba: "**Impostos"**
- Campo: "**Código da FCI"**: [Preencher o código de acordo dados fornecidos pela SEFAZ SP]
- Campo**: "Valor de Comercialização"** - (R$): [Dados preenchidos de acordo com SEFAZ]
- Campo: **"Valor da Parcela Importada do Exterior"** - (R$): [Dados preenchidos de acordo com SEFAZ]

**Nota:** Quando a Origem do produto(aba: Geral), for 3, 5 e 8, se faz necessário a obtenção dos dados da FCI (código e Valores Comercialização e Parcela Importada do Ex.),  existe recurso de exportar dados de produtos PENDENTE através da tela [Comercial » Rotinas » Ficha de Conteúdo de Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600854)

- **FCI - PENDENTE**

![Imagem 4: FCI - PENDENTE](https://ajuda.sankhya.com.br/hc/article_attachments/360060888253)

- **FCI-Dados atualizados**

![Imagem 5: FCI-Dados atualizados](https://ajuda.sankhya.com.br/hc/article_attachments/360059971614)

![Imagem 6: Após os ajustes, redigitar os itens na nota e gerar um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16451982923927) Após os ajustes, redigitar os itens na nota e gerar um novo lote.

**![Imagem 7: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16451982934551) CAUSA**:

Ocorre quando para a nota em questão o código da FCI, informado na TAG **nFCI**, não está de acordo com o Manual do contribuinte.
