---
id: "360044086113"
titulo: "Campo Tipo de Negociação obrigatório para nota de Nro Único: 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044086113-Campo-Tipo-de-Negocia%C3%A7%C3%A3o-obrigat%C3%B3rio-para-nota-de-Nro-%C3%9Anico-X"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:02Z"
rotulos: ["Configuração", "Empresa", "NF-e", "XML", "Importação", "Tipo de Negociação", "Preferências", "CORE_E01851", "Modelo de Importação de XML", "Configuração e Importação"]
---

# Campo Tipo de Negociação obrigatório para nota de Nro Único: 'X'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16171036216343) MENSAGEM:**

[CORE\_E01851] Campo Tipo de Negociação obrigatório para nota de Nro Único: 'X'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16171020835095) SOLUÇÃO:**

![Imagem 3: Acesse a tela "Empresa" (Caminho de acesso: Comercial » Preferências » Empresa ).](https://ajuda.sankhya.com.br/hc/article_attachments/16171020836119) Acesse a tela **"Empresa"** (Caminho de acesso: Comercial » Preferências » Empresa).

![Imagem 4: Na aba Modelo de Importação de XML identifique qual o "Modelo de notas e pedidos" utilizado (essa verificação também…](https://ajuda.sankhya.com.br/hc/article_attachments/16171036225687) Na aba **Modelo de Importação de XML** identifique qual o **"Modelo de notas e pedidos"** utilizado (essa verificação também pode ser realizada através do Nro único informado na mensagem de validação):

![Imagem 5: Na aba Modelo de Importação de XML identifique qual o "Modelo de notas e pedidos" utilizado (essa verificação também…](https://ajuda.sankhya.com.br/hc/article_attachments/14692054795287)

![Imagem 6: Acesse a tela " Modelo de notas e pedidos " (Caminho de acesso: Comercial » Consulta » Modelo de notas e pedidos ) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16171036227351) Acesse a tela **"[Modelo de notas e pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514)"** (Caminho de acesso: Comercial » Consulta » Modelo de notas e pedidos) , localize o respectivo modelo e preencha o campo **"Tipo de Negociação"**:

![Imagem 7: Acesse a tela " Modelo de notas e pedidos " (Caminho de acesso: Comercial » Consulta » Modelo de notas e pedidos ) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/14692063097879)

![Imagem 8: Realizada a configuração acima, realize a importação de XML normalmente.](https://ajuda.sankhya.com.br/hc/article_attachments/16171036230167) Realizada a configuração acima, realize a importação de XML normalmente. 

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16171036231831) CAUSA:**

Mensagem apresentada quando não foi vinculado nenhum "Tipo de Negociação" no Modelo de notas e pedidos utilizado para a importação de XML.
