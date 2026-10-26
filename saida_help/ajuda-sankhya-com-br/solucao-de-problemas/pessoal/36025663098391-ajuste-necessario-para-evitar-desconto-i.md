---
id: "36025663098391"
titulo: "Ajuste necessário para evitar desconto incorreto de DSR em casos sem faltas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36025663098391-Ajuste-necess%C3%A1rio-para-evitar-desconto-incorreto-de-DSR-em-casos-sem-faltas"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-27T18:28:44Z"
rotulos: ["Configuração", "Ponto", "Folha", "desconto", "Erro", "necessário", "DSR", "faltas", "Ajuste", "evitar", "incorreto", "casos", "Atualiza Atrasos p/ Descontos de DSR"]
---

# Ajuste necessário para evitar desconto incorreto de DSR em casos sem faltas

**SITUAÇÃO:**

Ao realizar o cálculo da folha de pagamento, foi identificado que o evento de desconto de DSR está sendo apresentado indevidamente, mesmo sem existirem faltas lançadas. Essa ocorrência acontece mesmo com a regra de cálculo configurada com o campo “Atualiza Atrasos p/ Descontos de DSR” definido como “Nunca atualiza”

**SOLUÇÃO:**

Para evitar que o desconto de DSR seja apresentado de forma indevida no cálculo da folha, é necessário definir um limite de horas de atraso no campo “Limite de Atrasos para Perda de DSR”, conforme a regra estabelecida pela empresa.

Para ajustar a configuração, siga os passos abaixo:

**(1)** Acesse a tela **''Regra de Cálculo''** (Pessoal+» Cadastros), na aba **''Ponto''**, e localize os campos:

- “**Atualiza Atrasos p/ Descontos de DSR”**
- **“Limite de Atrasos para Perda de DSR”**

**(2)** Mantenha o campo Atualiza Atrasos p/ Descontos de DSR configurado como “**Nunca atualiza**”;

**(3)** Preencha o campo Limite de Atrasos para Perda de DSR com o valor desejado (por exemplo, 1000, equivalente a 10 horas; 

Após essa configuração, o sistema passará a considerar o limite de horas informado, deixando de aplicar o desconto de DSR de forma indevida.

![Imagem 1: Após essa configuração, o sistema passará a considerar o limite de horas informado, deixando de aplicar o desconto de…](https://ajuda.sankhya.com.br/hc/article_attachments/36157305948823)

**CAUSA:**

Mesmo com o campo Atualiza Atrasos p/ Descontos de DSR configurado como “Nunca atualiza”, o desconto de DSR foi gerado porque o campo Limite de Atrasos para Perda de DSR não estava devidamente preenchido.

Quando este campo permanece com o valor 0 (zero), o sistema interpreta que qualquer atraso já ultrapassa o limite permitido, resultando automaticamente na aplicação do desconto de DSR durante o cálculo da folha.
