---
id: "32402320224151"
titulo: "(Visto Fer) Erro ao Calcular Rescisão: Valor Inválido no Código de Afastamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32402320224151--Visto-Fer-Erro-ao-Calcular-Rescis%C3%A3o-Valor-Inv%C3%A1lido-no-C%C3%B3digo-de-Afastamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:52Z"
rotulos: ["Folha", "Pessoal", "Configuração Funcionários", "Erro ao Calcular Rescisão", "valor Inválido", "Código de Afastamento", "Character T is neither a decimal digit number", "decimal point", "nor 'e' notation exponential mark", "Erro"]
---

# (Visto Fer) Erro ao Calcular Rescisão: Valor Inválido no Código de Afastamento

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32552053957015) **MENSAGEM:**

Falha - Character T is neither a decimal digit number, decimal point, nor "e" notation exponential mark.

**SITUAÇÃO:**

Ao tentar calcular a rescisão de um funcionário, o sistema exibe a mensagem acima.

#### **(1)** Interpretando a Mensagem do Erro:

**Character T is neither a decimal digit number, decimal point, nor 'e' notation exponential mark.**

(O caractere "T" não é um número decimal, ponto decimal ou marca exponencial de notação "e").

Essa mensagem indica que há uma tentativa de realizar um cálculo ou conversão numérica sobre um campo que contém **letras**, o que não é permitido nesse contexto. Podendo haver os seguintes cenários:

**(2)** O código de afastamento vinculado ao aviso prévio ou desligamento **foi registrado com letras** (por exemplo: **"T C"**), o que é inválido para o campo **CAUSAAFAST** da tabela **TFPFUN**, que exige exclusivamente valores numéricos.

**(2)**O campo **CODAFASTCAGED**, por sua vez, aceita letras por ser do tipo **VARCHAR2**; no entanto, não pode ser utilizado diretamente em operações que exigem valores numéricos.

![Imagem 2: (2) O campo CODAFASTCAGED , por sua vez, aceita letras por ser do tipo VARCHAR2 ; no entanto, não pode ser utilizado…](https://ajuda.sankhya.com.br/hc/article_attachments/32533209098519)

**SOLUÇÃO:**

Para corrigir o problema e permitir o cálculo da rescisão, siga os passos abaixo:

![Imagem 3: Na Tela "Código de Afastamento'' (Pessoal+» Cadastros » Código de Afastamento) , cadastre um novo Código de Afastamento…](https://ajuda.sankhya.com.br/hc/article_attachments/32532414504855) Na Tela **"Código de Afastamento''** (Pessoal+» Cadastros » Código de Afastamento)**,** cadastre um novo **Código de Afastamento** utilizando apenas números:

![Imagem 4: Crie um novo código numérico (por exemplo: 99), contendo as informações compatíveis com o tipo de rescisão a ser…](https://ajuda.sankhya.com.br/hc/article_attachments/32532414509207) Crie um novo código numérico (por exemplo: 99), contendo as informações compatíveis com o tipo de rescisão a ser realizada, assegurando que não haja o uso de letras.

![Imagem 5: Na tela "Tipo de rescisão" (Pessoal+» Cadastros » Tipo de Rescisão) , vincule o novo código ao Tipo de Rescisão .](https://ajuda.sankhya.com.br/hc/article_attachments/32533534285207) Na tela **"Tipo de rescisão"** (Pessoal+» Cadastros » Tipo de Rescisão)**,** vincule o novo código ao **Tipo de Rescisão**.

**![Imagem 6: Exclua o aviso anterior do funcionário (que estava vinculado ao código inválido) e registre um novo aviso com o código…](https://ajuda.sankhya.com.br/hc/article_attachments/32533563722263)Exclua o aviso anterior do funcionário** (que estava vinculado ao código inválido) e **registre um novo aviso** com o código de afastamento correto.

![Imagem 7: Refaça o cálculo da rescisão.](https://ajuda.sankhya.com.br/hc/article_attachments/32533534289815) Refaça o cálculo da rescisão.

Após essa correção, o sistema conseguirá interpretar os dados corretamente e concluir o cálculo da rescisão sem apresentar erros.

**CAUSA:**

O erro está relacionado ao **código da causa do afastamento** vinculado ao aviso prévio ou ao desligamento do funcionário.

O sistema tenta interpretar o conteúdo do campo **"CAUSAAFAST"** como um valor numérico, porém foi identificado um valor inválido contendo letras, como exemplo: '**T C'**.

Dessa forma, o interpretador da aplicação não consegue realizar conversões ou comparações adequadas, pois espera um valor numérico e recebeu um valor alfanumérico.
