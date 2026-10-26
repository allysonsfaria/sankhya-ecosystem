---
id: "42426736700951"
titulo: "Manual Regra Tributária em Lote"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426736700951-Manual-Regra-Tribut%C3%A1ria-em-Lote"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Manuais Kolossus"
atualizado_em: "2026-08-03T12:30:59Z"
rotulos: ["asis", "sync_hc", "asis_52941201599635", "sync_hash_2c72f3699dc7"]
---

# Manual Regra Tributária em Lote

Sumário

[O que compõe o Módulo?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426736700951-Manual-Regra-Tribut%C3%A1ria-em-Lote#h2818slt5wxfwi1nk3qr612uuxll1ezw2je)

[Regra Tributária em Lote- Passo a Passo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426736700951-Manual-Regra-Tribut%C3%A1ria-em-Lote#h2844slt5wxmlbgr3vwj1dmyf0n15l8awm)

[Status de Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426736700951-Manual-Regra-Tribut%C3%A1ria-em-Lote#h2861slt5wxskv135byla1lrocrr1mq8y70)

## Regra Tributária em Lote

Através da importação de um arquivo (csv) com o detalhamento dos produtos e a seleção dos parâmetros, este aplicativo consegue processar e retornar a matriz tributária desses itens. Ferramenta atribui em lote as alíquotas de ICMS, IPI, PIS, COFINS e ICMS-ST (MVA, Convênios e Protocolos), para automatizar e facilitar a análise dos tributos incidentes sobre as mercadorias.

### O que compõe o Módulo?

TELA – PROCESSO – Através da área de processos você consegue verificar todos os processos que foram criados/importados no módulo Regra Tributária em Lote. 

TELA – MEUS PROCESSOS – Através da opção “Meus processos” você terá visualização de tudo o que o próprio usuário realiza no módulo.

### Regra Tributária em Lote- Passo a Passo

1°: Vá em Upload e baixe o modelo 

![Imagem 1: 1°: Vá em Upload e baixe o modelo](https://ajuda.sankhya.com.br/hc/article_attachments/42426753602199)

![Imagem 2: 1°: Vá em Upload e baixe o modelo](https://ajuda.sankhya.com.br/hc/article_attachments/42426708122903)

2°: Preencha o modelo 

![Tabela Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42426737066647) 

CST\_ORIGEM: Campo obrigatório, preencher apenas com o primeiro dígito do CST.

CODIGO\_PRODUTO: Campo obrigatório, código do item cadastrado.
DESCRICAO: Campo obrigatório, descrição do item cadastrado.
NCM: Campo obrigatório, NCM de oito dígitos sem pontos.
EX: Campo não obrigatório, três dígitos, especifica para a NCM indicada.

CEST: Campo obrigatório, preencher se o item apresentar código especificado e substituição tributária (Completo- sete dígitos, sem pontos) ou preencher com 9999999 (Número 9, sete vezes) para casos que o produto não tenha código CEST.

\*OBS: caso o objetivo seja identificar o CEST correspondente para o NCM, deixe o campo vazio para enquadramento e utilize a opção consulta CEST.

3°: Importe o arquivo .csv na plataforma 

![Imagem 4: 3°: Importe o arquivo .csv na plataforma](https://ajuda.sankhya.com.br/hc/article_attachments/42426708306583)

4°: Entre no aplicativo Regra Tributária em Lote e processe os tributos 

![Imagem 5: 4°: Entre no aplicativo Regra Tributária em Lote e processe os tributos](https://ajuda.sankhya.com.br/hc/article_attachments/42426737251991)

Tributos e Competência: Selecionar ao menos um tributo relacionado.

Selecionando Parâmetros: preencha as Unidades da Federação de Origem e Destino, Atividades e Regimes que deseja.

Data: os resultados serão apresentados com base na data corrente. Para resultados de outros períodos, selecione abaixo o Mês/Ano Referência.

![Imagem 6: Data: os resultados serão apresentados com base na data corrente. Para resultados de outros períodos, selecione abaixo…](https://ajuda.sankhya.com.br/hc/article_attachments/42426708606487)

Clique em “Aplicar” para executar os parâmetros!

Obs: Para melhor performance no retorno do resultado o ideal é realizar uma consulta estratégica com tributos e participantes bem definidos. A combinação de muitos tributos para diversos destinos e origens, pode causar um excesso de retornos que prejudica o tempo de processamento e também exceder o limite do Excel.

Exemplo ideal:

Todos os tributos, para 27 Origens e 27 Destinos, subir até 1000 linhas. 

AVISO: Inserido mais informações que no “Exemplo Ideal” o Excel não irá suportar e realizará um bloqueio automático. 

Caso o seu arquivo fique com o status de “EXPORTANDO” por mais de 24horas, provavelmente o Excel não suportou a quantidade gerada e não gerará o relatório, entrar em contato com o suporte. 

Caso trabalhe com grandes quantidades de itens, por gentileza, entre em contato com o comercial para melhor solução. 

5°: Consulte os resultados! 

Os resultados podem ser vistos em tela ou exportados.

Para consultar os resultados em tela basta selecionar o processo desejado e clicar em resultados.

![Imagem 7: Para consultar os resultados em tela basta selecionar o processo desejado e clicar em resultados.](https://ajuda.sankhya.com.br/hc/article_attachments/42426737468439)

Para consultar os resultados em tela basta selecionar o(s) processo(s) desejado(s), clicar em exportar, aguardar o processo, e clicar no clipe para baixar os resultados em uma planilha .xls excel.

![Imagem 8: Para consultar os resultados em tela basta selecionar o(s) processo(s) desejado(s), clicar em exportar, aguardar o…](https://ajuda.sankhya.com.br/hc/article_attachments/42426754347543)

![Imagem 9: Para consultar os resultados em tela basta selecionar o(s) processo(s) desejado(s), clicar em exportar, aguardar o…](https://ajuda.sankhya.com.br/hc/article_attachments/42426754441751)

## Status de Processamento

### ![Imagem 10: Status de Processamento](https://ajuda.sankhya.com.br/hc/article_attachments/42426708956183)

#### É possível diagnosticar o erro passando o mouse por cima do X.
