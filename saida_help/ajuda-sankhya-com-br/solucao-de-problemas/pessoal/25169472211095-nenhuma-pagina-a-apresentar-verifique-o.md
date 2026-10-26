---
id: "25169472211095"
titulo: "Nenhuma página a apresentar. Verifique o filtro e tente novamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25169472211095-Nenhuma-p%C3%A1gina-a-apresentar-Verifique-o-filtro-e-tente-novamente"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-18T20:02:13Z"
rotulos: ["Relatórios", "Fiscal", "Configuração Funcionários", "Cadastro", "Erro"]
---

# Nenhuma página a apresentar. Verifique o filtro e tente novamente

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/25169472191767) **MENSAGEM:**

[CORE\_E02500] Nenhuma página a apresentar. Verifique o filtro e tente novamente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/25169510485783)SOLUÇÃO:**

Acesse a tela  **"Configuração de funcionários"** e verifique principalmente a falta dos dados como CTPS, Série, UF CTPS e outros que contém o \* (asterisco) que são obrigatórios.

Após ajustar os dados no cadastro do funcionário, emita novamente o relatório para validar se a emissão será concluída com sucesso.

![Imagem 3: Após ajustar os dados no cadastro do funcionário, emita novamente o relatório para validar se a emissão será concluída…](https://ajuda.sankhya.com.br/hc/article_attachments/25169472200855)

![Imagem 4: Após ajustar os dados no cadastro do funcionário, emita novamente o relatório para validar se a emissão será concluída…](https://ajuda.sankhya.com.br/hc/article_attachments/25343871591703)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/25169472209047)CAUSA:**

O problema ocorre porque faltam informações no cadastro do funcionário. Visto que a query do relatório valida estes campos, caso falte algum ele não é gerado apresentando a mensagem acima.
