---
id: "21893908203543"
titulo: "CÃ³digo: BHISS0003 DescriÃ§Ã£o: Essa prefeitura nÃ£o suporta emissÃ£o de Nota Fiscal com tomador com endereÃ§o incompleto ou invÃ¡lido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21893908203543-C%C3%83-digo-BHISS0003-Descri%C3%83-%C3%83-o-Essa-prefeitura-n%C3%83-o-suporta-emiss%C3%83-o-de-Nota-Fiscal-com-tomador-com-endere%C3%83-o-incompleto-ou-inv%C3%83-lido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:49:44Z"
rotulos: ["Configuração", "Parceiro", "Prefeituras", "NFS-e", "Erro"]
---

# CÃ³digo: BHISS0003 DescriÃ§Ã£o: Essa prefeitura nÃ£o suporta emissÃ£o de Nota Fiscal com tomador com endereÃ§o incompleto ou invÃ¡lido.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/21893892465815) **MENSAGEM:**

CÃ³digo: BHISS0003 DescriÃ§Ã£o: Essa prefeitura nÃ£o suporta emissÃ£o de Nota Fiscal com tomador com endereÃ§o incompleto ou invÃ¡lido.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/21893892468119)CAUSA:**

Ocorre quando está sendo realizado o envio de NFSe para a prefeitura e não está sendo enviado os dados do endereço, a prefeitura não aceita mais o envio dos dados em branco ou incompletos, como por exemplo a prefeitura de Ribeirão Preto - SP.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21893892467095)SOLUÇÃO:**

- Acesse o cadastro do parceiro da nota
- Aba "Endereço"
- Preencha todas as informações do campo endereço de acordo com os dados do CEP pesquisando no site dos correios (Endereço, Bairro, Número)
  - Caso não tenha número, informar o número 0
- Link: <https://buscacepinter.correios.com.br/app/endereco/index.php>
- Após informar os dados no cadastro gerar lote da nota novamente.
