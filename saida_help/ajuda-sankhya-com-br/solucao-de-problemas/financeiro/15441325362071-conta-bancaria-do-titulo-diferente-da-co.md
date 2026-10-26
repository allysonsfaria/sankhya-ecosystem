---
id: "15441325362071"
titulo: "Conta bancária do título diferente da conta bancária 'XX' para gerar nosso número"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15441325362071-Conta-banc%C3%A1ria-do-t%C3%ADtulo-diferente-da-conta-banc%C3%A1ria-XX-para-gerar-nosso-n%C3%BAmero"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:56:53Z"
rotulos: ["Configuração", "Movimentação Financeira", "Boleto", "Financeiro", "CORE_E01376", "Conta bancária diferente", "Parâmetro BOLCONTAFIN habilitado", "Impressão permitida se contas iguais", "Erro"]
---

# Conta bancária do título diferente da conta bancária 'XX' para gerar nosso número

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16539016028823) MENSAGEM:**

[CORE\_E01376] Conta bancária do título diferente da conta bancária 'XX' para gerar nosso número.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16539004762007) SOLUÇÃO:**

Se o parâmetro **"Gerar boleto apenas para conta do financeiro? - BOLCONTAFIN"** estiver habilitado, será permitida a impressão na tela **"Impressão de Boletos"** se a conta informada na aba **"Parâmetros Boleto"**for a mesma do título selecionado.

Caso não seja a mesma conta, o sistema emitirá a seguinte mensagem de erro:

**"Conta bancária do título diferente da conta bancária '999-XXXXX' para gerar nosso número".**

Caso o parâmetro mencionado esteja desabilitado, será permitida a impressão com contas diferentes. Este parâmetro visa evitar que títulos do financeiro com contas bancárias específicas, tenham boletos gerados por outras contas bancárias em empresas em que isso não é permitido.

![Imagem 3: Caso o parâmetro mencionado esteja desabilitado, será permitida a impressão com contas diferentes. Este parâmetro visa…](https://ajuda.sankhya.com.br/hc/article_attachments/15441484627351)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16539004766487) CAUSA:**

Ocorre sempre que o parâmetro **"Gerar boleto apenas para conta do financeiro? - BOLCONTAFIN"**   está ligado e é informada uma conta para gerar nosso número diferente da conta bancária do título.
