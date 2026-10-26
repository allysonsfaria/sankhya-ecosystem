---
id: "35896344390551"
titulo: "Saiba como gerar guia de reembolso GNRE na devolução de ICMS-ST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35896344390551-Saiba-como-gerar-guia-de-reembolso-GNRE-na-devolu%C3%A7%C3%A3o-de-ICMS-ST"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:24:28Z"
rotulos: ["Configuração", "ICMS", "Impostos", "GNRE", "Financeiro", "Tipos de Título", "Devolução", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Tipo de Financeiro = \"Usar da Natureza Padrão\"", "Devolução de ICMS-ST", "Guia de Reembolso", "Reembolso ICMS-ST", "Saiba como gerar"]
---

# Saiba como gerar guia de reembolso GNRE na devolução de ICMS-ST

**SITUAÇÃO:**

Em casos de **devolução de mercadoria**, pode ser necessário **gerar uma guia de reembolso (**[**GNRE**](https://ajuda.sankhya.com.br/hc/pt-br/articles/14989813726743-GNRE-Guia-Nacional-de-Recolhimento)**)** referente ao **ICMS-ST**.

Para que o Sankhya realize esse processo corretamente, é necessário ajustar algumas configurações no sistema.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35896350902295)SOLUÇÃO:**

**(1)**  Acesse a tela [**''Tipos de Título'**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)**'** (Financeiro » Arquivos » Cadastros » Tipos de Título).

**(2)**  Crie um novo tipo de título com a descrição **“Reembolso ICMS-ST”**.

Esse tipo de título será utilizado nas devoluções para gerar a guia de reembolso.

![Imagem 2: Esse tipo de título será utilizado nas devoluções para gerar a guia de reembolso.](https://ajuda.sankhya.com.br/hc/article_attachments/36309453748503)

**(3)**  Posteriormente, acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências)

**(4)**  Busque pelo parâmetro **TIPTITGNRESTRB (**responsável pelo **Tipo de Título de Reembolso de ICMS-ST** no campo de busca) e nele insira o código do tipo de título criado no passo 2.

Isso garante que o sistema saiba qual título utilizar ao gerar o financeiro da devolução.

![Imagem 3: Isso garante que o sistema saiba qual título utilizar ao gerar o financeiro da devolução.](https://ajuda.sankhya.com.br/hc/article_attachments/36309453751191)

**(5)**  Em seguida, acesse a tela [**''Tipo de Negociação''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) (Comercial » Arquivo » Cadastros » Tipos de Negociação)

**(6)**  Localize o tipo de negociação utilizado nas **devoluções de venda** e **inclua uma nova parcela** referente à **Guia de Reembolso ICMS-ST**.

Na parcela criada, utilize a seguinte **fórmula**:

```
IF(queTGFCAB.TIPMOV = 'D' AND NVL(VLRSUBST, 0) <> 0, VLRSUBST, 0)
```

![Imagem 4: Na parcela criada, utilize a seguinte fórmula :](https://ajuda.sankhya.com.br/hc/article_attachments/35896350903703)

**Explicação da fórmula:**

- Gera o valor da parcela **apenas nas devoluções** (`TIPMOV = 'D'`);
- Considera o valor de **ICMS-ST (VLRSUBST)** apenas quando houver valor informado;
- Em outros casos, não gera a parcela.

**(7)**  Ainda na tela Tipo de negociação, no campo **"Natureza padrão"** informe a opção adequada à operação. Depois, no campo **"Tipo de Financeiro (REC/DESP)"** selecione a opção **"N- Usar da natureza padrão".**

Importante garantir que o tipo financeiro seja igual a natureza padrão. Pois, essa configuração define que o sistema **utilize automaticamente a natureza padrão** como **tipo de financeiro** nas operações vinculadas a esse tipo de negociação.

![Imagem 5: Importante garantir que o tipo financeiro seja igual a natureza padrão. Pois, essa configuração define que o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/36310315739927)

**Atenção:**

A geração da **GNRE de reembolso** deve ocorrer somente quando **houver direito legal à restituição do ICMS-ST**, conforme a **legislação do estado de origem**.

Nos casos em que o estado **exigir outro procedimento**, como pedido eletrônico de restituição, a GNRE **não deve ser gerada automaticamente**.

Recomenda-se **consultar o setor fiscal ou contábil** antes de aplicar o procedimento, assegurando o **cumprimento da legislação vigente**.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35896350903831) CAUSA:**

Ao **lançar uma nota de devolução** com **ICMS-ST**, o sistema **gera automaticamente** uma **linha no financeiro** com o valor correspondente ao **ICMS-ST da devolução (VLRSUBST)**.

Essa linha é utilizada para a emissão da GNRE de reembolso.
