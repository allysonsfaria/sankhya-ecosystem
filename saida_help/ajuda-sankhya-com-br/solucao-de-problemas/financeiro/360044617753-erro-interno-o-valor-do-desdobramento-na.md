---
id: "360044617753"
titulo: "Erro interno: O valor do desdobramento não pode ser zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617753-Erro-interno-O-valor-do-desdobramento-n%C3%A3o-pode-ser-zero"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:52:33Z"
rotulos: ["#PUBLIFER", "Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "CORE_E02398", "Erro interno CORE_E02398", "Ative \"VLRBAIXAZERO\"", "Valor de baixa zero não permitido", "Erro"]
---

# Erro interno: O valor do desdobramento não pode ser zero

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16617025801239) MENSAGEM:**

[CORE\_E02398]: Erro interno: O valor do desdobramento não pode ser zero.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16617025804055) SOLUÇÃO:**

![Imagem 3: Certifique-se que o valor de baixa = 0 corresponde ao esperado.](https://ajuda.sankhya.com.br/hc/article_attachments/16617063156375) Certifique-se que o valor de baixa = 0 corresponde ao esperado.

![Imagem 4: Caso a baixa com valor desdobramento zerado seja necessária, ajuste o parâmetro "VLRBAIXAZERO" para ligado:](https://ajuda.sankhya.com.br/hc/article_attachments/16617025809815) Caso a baixa com valor desdobramento zerado seja necessária, ajuste o parâmetro **"VLRBAIXAZERO"** para ligado:

- Tela **"Preferências"** (Caminho de acesso: Configurações » Avançado)
- Chave **'VLRBAIXAZERO': ligado.** Se estiver "Sim" permite que o usuário efetue baixa com valor zero. Se estiver "Não", só serão aceitas baixas com valores maiores que zero.

![Imagem 5: Chave 'VLRBAIXAZERO': ligado. Se estiver "Sim" permite que o usuário efetue baixa com valor zero. Se estiver "Não", só…](https://ajuda.sankhya.com.br/hc/article_attachments/14919162365591)

![Imagem 6: Ajustado o parâmetro, proceda com a baixa.](https://ajuda.sankhya.com.br/hc/article_attachments/16617063160087) Ajustado o parâmetro, proceda com a baixa.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16617063163415) CAUSA:**

Mensagem apresentada ao tentar realizar o procedimento de baixa, quando o valor do desdobramento for igual a zero, e o parâmetro Aceita valor de baixa igual a zero estiver desligado.
