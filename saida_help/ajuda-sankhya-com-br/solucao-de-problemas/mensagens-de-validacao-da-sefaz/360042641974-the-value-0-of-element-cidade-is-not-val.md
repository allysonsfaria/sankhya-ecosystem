---
id: "360042641974"
titulo: "The value '0' of element 'Cidade' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042641974-The-value-0-of-element-Cidade-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:28Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "Cidades", "SEFAZ", "Valor '0' no Campo 'Cidade' Inválido", "Erro"]
---

# The value '0' of element 'Cidade' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16482544664471) MENSAGEM:**

cvc-pattern-valid: Value '0' is not facet-valid with respect to pattern '[0-9]{7}' for type 'tpCidade'.
cvc-type.3.1.3: The value '0' of element 'Cidade' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482544667415) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acessar: Configurações » Cadastros » Endereços » Cidades](https://ajuda.sankhya.com.br/hc/article_attachments/16482544672279) Acessar: Configurações » Cadastros » Endereços » Cidades

- Aba: **"Geral"**
- Campo **"Mun. domicílio fiscal":** Informe o valor válido

![Imagem 4: Campo "Mun. domicílio fiscal": Informe o valor válido](https://ajuda.sankhya.com.br/hc/article_attachments/14532552290967)

Para consultar, acesse o site do IBGE ou solicite informações com o contador da empresa.
<https://www.ibge.gov.br/>

![Imagem 5: Após o ajuste, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16482544675735) Após o ajuste, redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16482535606551) CAUSA:**

Ocorre quando no cadastro da cidade do Parceiro, Empresa ou Transportadora da Nota, não existe um valor válido para o campo **"Mun. domicílio fiscal".**
