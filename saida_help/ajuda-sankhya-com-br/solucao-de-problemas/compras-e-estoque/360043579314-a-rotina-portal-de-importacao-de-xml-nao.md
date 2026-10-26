---
id: "360043579314"
titulo: "A rotina Portal de Importação de XML não está baixando os XMLs automaticamente, consultados pelo MD-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579314-A-rotina-Portal-de-Importa%C3%A7%C3%A3o-de-XML-n%C3%A3o-est%C3%A1-baixando-os-XMLs-automaticamente-consultados-pelo-MD-e"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-31T14:54:25Z"
rotulos: ["Configuração", "XML", "Importação", "SEFAZ", "MD-e", "Problema na Importação Automática de XMLs", "Erro"]
---

# A rotina Portal de Importação de XML não está baixando os XMLs automaticamente, consultados pelo MD-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16107459826327) MENSAGEM:**

A rotina Portal de Importação de XML não está baixando os XMLs automaticamente, consultados pelo MD-e. 

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16107459842071) CAUSA:**

Ocorre quando a opção para consulta e download automático dos XMLs emitidos contra a empresa, não estão devidamente configurados na MD-e. 

**![Imagem 3: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16107461815063) SITUAÇÃO:**

Não foi retornado um XML válido. Uma das possíveis causas para esse erro é algum erro que ocorreu no servidor (SEFAZ) e foi redirecionado para uma página HTML.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16107459829271) SOLUÇÃO:**

![Imagem 5: Acesse: Comercial » Rotinas » Configuração MD-e/DF-e](https://ajuda.sankhya.com.br/hc/article_attachments/16107461819031) Acesse: Comercial » Rotinas » Configuração MD-e/DF-e

- Campo **"Versão de Consulta"**: Distribuição de DF-e (NT2014)
- O campo **"Versão de Consulta"** deve estar selecionado **"Distribuição de DF-e"** para que o sistema busque e baixe os XMLs automaticamente.

![Imagem 6: Após os ajustes, a rotina continuará efetuando as consultas de acordo com o intervalo configurado e baixará os XML's…](https://ajuda.sankhya.com.br/hc/article_attachments/16107461820183) Após os ajustes, a rotina continuará efetuando as consultas de acordo com o intervalo configurado e baixará os XML's automaticamente.

**Importante:**

É importante ressaltar que se tudo estiver correto e  na tela de Configuração MD-e/DF-e mesmo assim não baixar nada,  verifique o "NSU" na aba  "**Configuração DF-e**"  pois poderá ocorrer os erros 656 **motivo: Rejeição:** Consumo Indevido (Ultrapassou o limite de 20 consultas por hora) ou;

**Motivo: Rejeição:** Consumo Indevido (Deve ser utilizado o ultNSU nas solicitações subsequentes. Tente após 1 hora). Ai precisa ajustar o NSU.

**Dica:** Informe um NSU mais baixo do que estiver configurado nessa aba.
