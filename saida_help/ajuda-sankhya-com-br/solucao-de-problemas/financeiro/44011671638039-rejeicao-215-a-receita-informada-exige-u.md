---
id: "44011671638039"
titulo: "Rejeição: 215 - A Receita informada exige um produto!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011671638039-Rejei%C3%A7%C3%A3o-215-A-Receita-informada-exige-um-produto"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-10-05T19:08:35Z"
---

# Rejeição: 215 - A Receita informada exige um produto!

**MENSAGEM:**

[Rejeição 215]: A Receita informada exige um produto!

**SITUAÇÃO:**

Ao realizar o envio de um lote GNRE, ocorre uma rejeição informando que não há valor informado no campo de produto, de acordo com as regras estabelecidas pela Receita do Estado de destino.

**SOLUÇÃO:**

**(1)** Acesse a tela **“Estados” (**Configurações» Cadastros» Endereços» Estados) e localize o Estado de destino para o qual a GNRE está sendo gerada.

**(2)** Na aba **''Geral''** **(**Configurações» Cadastros» Endereços» Estados) identifique o campo **''Código do Produto''** utilizado no envio.

**(3)** Verifique se o campo '**'Código da Receita''** esta preenchido conforme as exigências do [**Portal GNRE**](https://www.gnre.pe.gov.br:444/gnre/portal/consultarTabelas.jsp) para o código do produto informado.

**Exemplo:**

- Código de Receita: 100048
- Produto: 36

![Imagem 1: Produto: 36](https://ajuda.sankhya.com.br/hc/article_attachments/44011671617559)

![Imagem 2: Produto: 36](https://ajuda.sankhya.com.br/hc/article_attachments/44011680122007)

**Dica:** Consulte a documentação oficial do Portal GNRE para confirmar quais produtos são aceitos para cada receita.

**(4)** Realize os ajustes necessários no cadastro do Estado.

**(5)** Após as correções, gere um novo lote e reenvie ao portal da GNRE.

**CAUSA:**

Esta rejeição ocorre quando o valor informado no campo **Código do Produto** não está preenchido conforme as normas estabelecidas para o Estado de destino no Portal GNRE.
