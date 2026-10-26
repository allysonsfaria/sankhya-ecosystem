---
id: "360043191573"
titulo: "IE inválida [local de retirada/entrega]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043191573-IE-inv%C3%A1lida-local-de-retirada-entrega"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:59Z"
rotulos: ["ERRONF", "#criadoRoger", "Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "971", "Insira \"Contato de Entrega\" no layout", "Acesse \"Parceiros\" e ajuste endereço", "Informe contato correto na nota", "Erro"]
---

# IE inválida [local de retirada/entrega]

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16513316903575) MENSAGEM**:

[971 - Rejeição]: IE inválida [local de retirada/entrega].

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16513332984855) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Parceiros:](https://ajuda.sankhya.com.br/hc/article_attachments/16513332986519) Acesse: Configurações » Cadastros » Parceiros:

- Aba "**Contatos"**: realize o cadastro do contato/endereço de entrega.

![Imagem 4: Aba " Contatos" : realize o cadastro do contato/endereço de entrega.](https://ajuda.sankhya.com.br/hc/article_attachments/12129068881815)

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16513332989463) IMPORTANTE:**

- Se parceiro for pessoa jurídica ou produtor rural, os campos de "**Endereço"** e **"Inscrição Estadual"** devem ser preenchidos na aba "**Contatos"** com uma I.E válida na UF do respectivo endereço. **Ex.:** Se endereço de entrega de SP, a IE deve ser de SP.
- Na tela "**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Configurações » Avançado) considere ligar o parâmetro "**PERMCNPJCONTATO"** para que seja possível informar CNPJ no Contato do parceiro.

![Imagem 6: Acesse: Comercial » Configuração » Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/article_attachments/16513342464023) Acesse: Comercial » Configuração » Configurador de Layout da Nota

- Selecione o layout utilizado na respectiva emissão.
- Insira no "**Cabeçalho"** desse layout o campo "**Contato de Entrega"**:

![Imagem 7: Insira no " Cabeçalho" desse layout o campo " Contato de Entrega" :](https://ajuda.sankhya.com.br/hc/article_attachments/14634532369047)

![Imagem 8: Ao realizar o lançamento, na Central de Vendas/Compras , informe no campo " Contato de Entrega" o contato cadastrado…](https://ajuda.sankhya.com.br/hc/article_attachments/16513383577623) Ao realizar o lançamento, na **Central de Vendas/Compras**, informe no campo "**Contato de Entrega"** o contato cadastrado para entrega, conforme item 1.

**![Imagem 9: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16513342473623) OBSERVAÇÕES:**

A rejeição acontecerá apenas se enviados os dados da <entrega>, essa tag será enviada no XML nas seguintes condições:

![Imagem 10: Campo " Contato de Entrega" preenchido no cabeçalho da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16513332986519) Campo "**Contato de Entrega"** preenchido no cabeçalho da nota.

![Imagem 11: Marcação " Gerar endereço de entrega no XML da NF-e " no cadastro da TOP;](https://ajuda.sankhya.com.br/hc/article_attachments/16513342464023) Marcação "**Gerar endereço de entrega no XML da NF-e**" no cadastro da TOP;

![Imagem 12: Quando for preenchida os dados da entrega, deixe o campo I.E em branco caso o parceiro de entrega seja isento de I.E.](https://ajuda.sankhya.com.br/hc/article_attachments/16513383577623) Quando for preenchida os dados da entrega, deixe o campo I.E em branco caso o parceiro de entrega seja isento de I.E.

**![Imagem 13: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16513342477591) CAUSA**:

Se informado para o grupo de retirada/entrega uma Inscrição Estadual inválida para o respectivo Estado, será retornada a rejeição.

Quando forem preenchidos os dados da entrega, deixar o campo I.E em branco caso o parceiro de entrega seja isento de I.E.
