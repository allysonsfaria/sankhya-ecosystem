---
id: "43674933542039"
titulo: "Relatório TRCT com layout fora do padrão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43674933542039-Relat%C3%B3rio-TRCT-com-layout-fora-do-padr%C3%A3o"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-02T15:46:33Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Relatório TRCT com layout fora do padrão

**Mensagem**

Relatório de rescisão não pode ser gerado pois os eventos não estão configurados corretamente para o layout do TRCT.

**Situação**

Ao tentar gerar o relatório TRCT (Termo de Rescisão do Contrato de Trabalho), o sistema apresenta uma mensagem de erro informando que a rescisão não pode ser gerada devido à configuração incorreta dos eventos, ou que o layout está fora do padrão esperado. Isso ocorre geralmente quando os eventos necessários para compor o TRCT não estão devidamente vinculados ou configurados na aba específica do TRCT na tela de **"Regra de Cálculo"** (Pessoal Arquivos Cadastros Regra de Cálculo).

**Solução**

Siga o passo a passo abaixo para corrigir a configuração dos eventos e garantir que o relatório TRCT seja gerado corretamente:

**(1)** Acesse a tela **"Regra de Cálculo"** Pessoal+ » Cadastros » Regras de Cálculo.

**(2)** Localize a regra de cálculo utilizada para o colaborador cuja rescisão está sendo processada.

**(3)** Acesse a aba **"TRCT"** dentro da regra de cálculo.

![Imagem 1: Verifique se todos os eventos obrigatórios para o TRCT estão devidamente configurados e vinculados aos campos corretos…](https://ajuda.sankhya.com.br/hc/article_attachments/43812094345751)

**(4)** Verifique se todos os eventos obrigatórios para o TRCT estão devidamente configurados e vinculados aos campos corretos do layout.

**(5)** Caso algum evento esteja faltando ou configurado de forma incorreta, realize o ajuste conforme a necessidade, seguindo as orientações do artigo de configuração de eventos para TRCT.

![Imagem 2: Salve as alterações realizadas na "Regra de Cálculo" . Tente gerar novamente o relatório TRCT para validar se o erro…](https://ajuda.sankhya.com.br/hc/article_attachments/43812094349079)

**(6)** Salve as alterações realizadas na **"Regra de Cálculo"**.

**(7)** Tente gerar novamente o relatório TRCT para validar se o erro foi solucionado.

**Causa**

A causa do erro está relacionada à configuração inadequada dos eventos na aba **"TRCT"** da tela **"Regra de Cálculo"**. Quando os eventos necessários para compor o layout do TRCT não estão corretamente vinculados ou configurados, o sistema não consegue gerar o relatório conforme o padrão exigido, resultando na mensagem de erro.
