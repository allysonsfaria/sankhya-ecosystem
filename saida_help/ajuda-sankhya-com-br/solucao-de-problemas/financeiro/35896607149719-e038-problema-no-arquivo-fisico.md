---
id: "35896607149719"
titulo: "E038 - Problema no arquivo físico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35896607149719-E038-Problema-no-arquivo-f%C3%ADsico"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:24:27Z"
rotulos: ["Configuração", "Layout", "Financeiro", "Processamento do Arquivo de Retorno", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "PROBLEMA", "NO", "FÍSICO", "layouts", "E038", "ARQUIVO", "EDI Bancário"]
---

# E038 - Problema no arquivo físico

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35896576724759) **MENSAGEM:**

[E038] PROBLEMA NO ARQUIVO FÍSICO

**SITUAÇÃO:**

Ao processar um arquivo na tela **''Processamento do Arquivo de Retorno'**' (Financeiro > EDI Bancário), a mensagem de erro é apresentada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35896576727575) SOLUÇÃO:**

**(1)** **Valide o arquivo utilizado:**

- Verifique se o arquivo corresponde ao mesmo banco e mesma estrutura definida no layout;
- Confirme o número de posições (240 ou 400) e a presença de segmentos.

![Imagem 3: Confirme o número de posições (240 ou 400) e a presença de segmentos.](https://ajuda.sankhya.com.br/hc/article_attachments/36238089869847)

**(2)** **Verifique se é a primeira execução:**

- Caso seja a primeira vez que o layout ou arquivo estão sendo utilizados, solicite o apoio da unidade para validação técnica.

**(3)** **Em casos de layout já utilizado anteriormente:**

- Valide se houve mudanças no arquivo enviado pelo banco (como inclusão de campos ou alteração de formato).
- Se houver, ajuste o layout na tela ''**Configuração do Arquivo de Retorno**''(Financeiro > EDI Bancário).

**(4)** **Revise os layouts disponíveis:**

- Confirme se o layout correto está sendo utilizado, especialmente quando há mais de um layout ativo para o mesmo banco.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35896576729239) CAUSA:**

Esse erro ocorre quando o arquivo de retorno bancário utilizado para processamento não é compatível com o layout configurado no sistema.
