---
id: "33439866994967"
titulo: "Rejeição 302 - Valor do documento de origem inválido para o tipo informado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33439866994967-Rejei%C3%A7%C3%A3o-302-Valor-do-documento-de-origem-inv%C3%A1lido-para-o-tipo-informado"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:29:02Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "GNRE", "Estados", "Passos para resolver", "Razão do erro", "Detalhe do erro", "valor do documento de origem", "[Rejeição 302]", "Rejeição 302", "inválido para o tipo informado.", "Portal GNRE", "Erro"]
---

# Rejeição 302 - Valor do documento de origem inválido para o tipo informado.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33439870382999) **MENSAGEM:**

[Rejeição 302]: valor do documento de origem inválido para o tipo informado.

**SITUAÇÃO:**

Ao enviar um lote GNRE, ocorre uma rejeição indicando que o valor informado para o documento de origem é incompatível com o tipo definido, conforme as regras estabelecidas pelo Estado de destino.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33439870386967)SOLUÇÃO:**

**(1)** Acesse a tela **“Estados” (**Configurações» Cadastros» Endereços» Estados) e localize o Estado de destino para o qual a GNRE está sendo gerada.

**(2)** Na aba **''Geral'' (**Configurações» Cadastros» Endereços» Estados) identifique o campo **''Código da Receita''** utilizado no envio.

**(3)** Verifique se os campos ''**Tipo de Documento''** e ''**Tipo da Informação''** estão preenchidos conforme as exigências do [**Portal GNRE**](https://www.gnre.pe.gov.br:444/gnre/portal/consultarTabelas.jsp) para o código de receita informado.

**Exemplo:**

- Código de Receita: 100102
- Tipo de documento: 10
- Tipo da informação: Nota fiscal

![Imagem 3: Tipo da informação: Nota fiscal](https://ajuda.sankhya.com.br/hc/article_attachments/33479322620055)![Imagem 4: Tipo da informação: Nota fiscal](https://ajuda.sankhya.com.br/hc/article_attachments/33479322621591)

**Dica:** Consulte a documentação oficial do Portal GNRE para confirmar quais tipos são aceitos para cada receita.

**(4)** Realize os ajustes necessários no cadastro do Estado ou no campo **''Código da receita''**.

**(5)** Após as correções, gere um novo lote e reenvie ao portal da GNRE.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33439866993815) CAUSA:**

Esta rejeição ocorre quando o valor informado no campo Tipo da Informação não está preenchido conforme as normas estabelecidas para o Estado de destino no Portal GNRE.
