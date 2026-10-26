---
id: "4410647082135"
titulo: "Critério Repetido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4410647082135-Crit%C3%A9rio-Repetido"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-10-15T13:59:07Z"
rotulos: ["Parceiro", "Movimentação Financeira", "Centro de Resultado", "Financeiro", "Natureza", "#causaRaiz", "CORE_E04982", "Critério duplicado", "Alterar rateio duplicado", "Financeiro Movimentação", "Erro"]
---

# Critério Repetido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15993326941079) MENSAGEM:**

[CORE\_E04982] Critério repetido, verifique.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16121168826647)CAUSA:**

 A mensagem é apresentada quando é selecionado um título na **"Movimentação Financeira"**, rateado, e incluído um novo rateio.  Após salvar, o usuário clica em **Duplicar** o rateio já criado, gerando os mesmos critérios de rateio.

| **Exemplo:**   - Manutenção - Cadastrar Rateio - % Rateio: 50% - Centro de Resultado : 110.000 ddddd - Cod. Natureza : 110001 Laranja - - Cod Parceiro : 1 - Salvar |
| --- |

![Imagem 3: Salvar](https://ajuda.sankhya.com.br/hc/article_attachments/4417224276247)

![Imagem 4: Salvar](https://ajuda.sankhya.com.br/hc/article_attachments/4417212895511)

Ocorre a mensagem pois os critérios ficarão iguais, se o titulo está sendo rateado, o sistema entende que será dividido para **departamentos/naturezas** diferentes.

**![Imagem 5: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15993172760727) SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo:

![Imagem 6: Entre na tela da movimentação financeira (Financeiro » Rotinas » Movimentação Financeira);](https://ajuda.sankhya.com.br/hc/article_attachments/16121168829847) Entre na tela da movimentação financeira **(Financeiro » Rotinas » Movimentação Financeira);**

![Imagem 7: Selecione o título na movimentação;](https://ajuda.sankhya.com.br/hc/article_attachments/16121194053911) Selecione o título na movimentação;

![Imagem 8: Altere os critérios de rateio que foi duplicado;](https://ajuda.sankhya.com.br/hc/article_attachments/16121194055447) Altere os critérios de rateio que foi duplicado;
