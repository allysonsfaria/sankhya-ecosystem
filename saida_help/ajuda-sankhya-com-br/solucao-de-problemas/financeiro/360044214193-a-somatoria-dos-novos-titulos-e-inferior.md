---
id: "360044214193"
titulo: "A somatória dos novos títulos é inferior aos títulos originais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044214193-A-somat%C3%B3ria-dos-novos-t%C3%ADtulos-%C3%A9-inferior-aos-t%C3%ADtulos-originais"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:42Z"
rotulos: ["#PUBLIFER", "#Revisadoclaudio", "Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "Somatória de novos títulos menor", "Renegociação Títulos Inferior", "Ativar parâmetros adequados", "Erro"]
---

# A somatória dos novos títulos é inferior aos títulos originais

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16192951227287) MENSAGEM:**

A somatória dos novos títulos é inferior aos títulos originais!
(Parâmetros: RENMENOR e RENMENORDESP)

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16192938300439) SITUAÇÃO:**

Mensagem apresentada ao realizar uma renegociação de títulos no sistema.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16192938304791) SOLUÇÃO:**

Valide na grade de **"Títulos a renegociar"** se os valores gerados correspondem ao esperado. Em caso positivo e a somatória desejada for inferior ao total dos títulos originais, ajuste os parâmetros abaixo:

![Imagem 4: Caso trate-se de despesas :](https://ajuda.sankhya.com.br/hc/article_attachments/16192951233303) Caso trate-se de **despesas**:

- Acesse **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Caminho de acesso: Configurações » Avançado » Preferências)
- Chave **'RENMENORDESP':** ligado

Permitir reneg. para valor MENOR em DESPESAS? - RENMENORDESP: Ao ativar este parâmetro será permitido consumar renegociações de títulos de despesa que estiverem com valor menor que os títulos originais.

![Imagem 5: Permitir reneg. para valor MENOR em DESPESAS? - RENMENORDESP : Ao ativar este parâmetro será permitido consumar…](https://ajuda.sankhya.com.br/hc/article_attachments/14609051559703)

![Imagem 6: Caso trate-se de Receitas:](https://ajuda.sankhya.com.br/hc/article_attachments/16192951234583) Caso trate-se de **Receitas:**

- Acesse Preferências (Caminho de acesso: Configurações » Avançado » Preferências)
- Chave **"RENMENOR":** ligado

Permitir reneg. para valor MENOR em RECEITAS? - RENMENOR: Ativando-se este parâmetro será permitido consumar renegociações de títulos de receita que estiverem com valor menor que os títulos originais.

![Imagem 7: Permitir reneg. para valor MENOR em RECEITAS? - RENMENOR : Ativando-se este parâmetro será permitido consumar…](https://ajuda.sankhya.com.br/hc/article_attachments/14609052796823)

![Imagem 8: Realizado o ajuste no respectivo parâmetro, refaça a renegociação.](https://ajuda.sankhya.com.br/hc/article_attachments/16192951236247) Realizado o ajuste no respectivo parâmetro, refaça a renegociação.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16192938311575) CAUSA:**

Mensagem apresentada ao executar renegociação de títulos e a somatória dos novos títulos for inferior aos títulos originais.
