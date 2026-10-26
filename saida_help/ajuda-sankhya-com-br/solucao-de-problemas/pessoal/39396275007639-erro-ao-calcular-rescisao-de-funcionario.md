---
id: "39396275007639"
titulo: "Erro ao Calcular Rescisão de Funcionário Afastado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39396275007639-Erro-ao-Calcular-Rescis%C3%A3o-de-Funcion%C3%A1rio-Afastado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-19T19:54:19Z"
rotulos: ["Ocorrências", "Folha", "eSocial", "Configuração Funcionários", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro ao Calcular Rescisão de Funcionário Afastado

**MENSAGEM**

O sistema apresenta uma mensagem de atenção informando que o funcionário está afastado, impedindo o cálculo da rescisão.

**SITUAÇÃO**

Ao tentar calcular a rescisão de um funcionário, o sistema bloqueia o processo exibindo uma mensagem informando que o colaborador está com situação de **"Afastamento"**. Isso ocorre quando há registros de afastamento ativos no cadastro do funcionário que impedem o processamento da rescisão.

**SOLUÇÃO**

Para resolver o problema e permitir o cálculo da rescisão, siga os passos abaixo:

**(1)** Acesse a tela **"Configuração Funcionários"** (Pessoal+ >> Cadastros >> Configuração Funcionários) e localize o funcionário desejado.

**(2)** Verifique o campo **"Situação"** na aba Afastamento identifiquei se esta afastado.

![Imagem 1: Acesse a tela "Ocorrência" (Pessoal+ » Rotinas Folha » Ocorrências) e inclua a data fim no afastamento.](https://ajuda.sankhya.com.br/hc/article_attachments/40923300856599)

**(3)** Acesse a tela **"Ocorrência"** (Pessoal+ » Rotinas Folha » Ocorrências) e inclua a data fim no afastamento. 
![Imagem 2: (3) Acesse a tela "Ocorrência" (Pessoal+ » Rotinas Folha » Ocorrências) e inclua a data fim no afastamento.](https://ajuda.sankhya.com.br/hc/article_attachments/40923304300439)

**(4)** Após o ajuste, verifique se a situação do funcionário foi atualizada para **"Atividade Normal"** no cadastro.

**(5)** Retorne à tela de cálculo de rescisão e processe novamente o cálculo para o funcionário.

**CAUSA**

O erro ocorre porque o sistema identifica que o funcionário possui um **"Registro de afastamento ativo"** em seu cadastro.
