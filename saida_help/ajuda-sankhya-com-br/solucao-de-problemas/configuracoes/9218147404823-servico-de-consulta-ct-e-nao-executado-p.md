---
id: "9218147404823"
titulo: "Serviço de consulta CT-e não executado. Próxima execução permitida a partir de"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9218147404823-Servi%C3%A7o-de-consulta-CT-e-n%C3%A3o-executado-Pr%C3%B3xima-execu%C3%A7%C3%A3o-permitida-a-partir-de"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:20Z"
rotulos: ["ERROCTE", "CT-e", "Configuração", "XML", "SEFAZ", "CORE_E03285", "Resolução do Erro de Consulta CT-e: Procedimentos e Configurações", "Documentos Eletrônicos"]
---

# Serviço de consulta CT-e não executado. Próxima execução permitida a partir de

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19604188972695) MENSAGEM:**

[CORE\_E03285] Serviço de consulta CT-e não executado. Próxima execução permitida a partir de:

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19604178432791) SITUAÇÃO:**

Ao tentar buscar o serviço de CT-e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19604178438807) CAUSA:**

Ao tentar executar o Serviço de consulta CT-e.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19604188981655) SOLUÇÃO:**

Realize a marcação do campo 'Realizar ciência automatizada' da tela **Configuração MD-e/DF-e** (Caminho de acesso à tela: Comercial » Rotinas » Configuração MD-e/DF-e).

![Imagem 5: Realize a marcação do campo 'Realizar ciência automatizada' da tela Configuração MD-e/DF-e (Caminho de acesso à tela:…](https://ajuda.sankhya.com.br/hc/article_attachments/19604188995607)

Realizada a marcação, para que o sistema busque o XML dos arquivos que já foram importados pela rotina, é preciso seguir o processo conforme abaixo:
![Imagem 6: Realizada a marcação, para que o sistema busque o XML dos arquivos que já foram importados pela rotina, é preciso…](https://ajuda.sankhya.com.br/hc/article_attachments/20471252187927) Selecione o documento no Portal de Importação de XML **(Caminho de acesso à tela: Comercial » Rotinas » Portal de importação de XML);**
![Imagem 7: Realizada a marcação, para que o sistema busque o XML dos arquivos que já foram importados pela rotina, é preciso…](https://ajuda.sankhya.com.br/hc/article_attachments/19604189001367) Feito isso, clique em MD-e > Ciência da Operação;
![Imagem 8: Realizada a marcação, para que o sistema busque o XML dos arquivos que já foram importados pela rotina, é preciso…](https://ajuda.sankhya.com.br/hc/article_attachments/19604189004951) MD-e > Download NF-e
![Imagem 9: Realizada a marcação, para que o sistema busque o XML dos arquivos que já foram importados pela rotina, é preciso…](https://ajuda.sankhya.com.br/hc/article_attachments/19604189014039) Processar Arquivo.

Verifique o próximo horário de execução da consulta dos documentos, caso não esteja configurado, estabeleça o horário da próxima execução.
