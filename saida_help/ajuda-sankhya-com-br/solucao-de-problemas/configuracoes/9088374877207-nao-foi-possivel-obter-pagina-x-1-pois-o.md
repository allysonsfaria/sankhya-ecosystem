---
id: "9088374877207"
titulo: "Não foi possível obter página \"X[1]\", pois o processo demorou demais. Código: CORE_E00359"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9088374877207-N%C3%A3o-foi-poss%C3%ADvel-obter-p%C3%A1gina-X-1-pois-o-processo-demorou-demais-C%C3%B3digo-CORE-E00359"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:10:37Z"
rotulos: ["SQL", "Configuração", "CORE_E00359", "Performance", "Parâmetro", "Erro de Timeout ao Carregar Página", "Erro", "pois o processo demorou demais", "-Djape.global.query.timeout", "DESABPAGINA", "Não foi possível obter página \"X[1]\"", "MAXRSLTSIZE", "Timeout"]
---

# Não foi possível obter página "X[1]", pois o processo demorou demais. Código: CORE_E00359

**MENSAGEM:**

[CORE\_E00359] Não foi possível obter página "X[1]", pois o processo demorou demais.

![Imagem 1: (CORE_E00359) Não foi possível obter página "X(1)", pois o processo demorou demais.](https://ajuda.sankhya.com.br/hc/article_attachments/34101055019287)

**SOLUÇÃO:**

**(1)** Parâmetro ''**MAXRSLTSIZE'':**

O parâmetro MAXRSLTSIZE limita a quantidade de registros retornados nas consultas das telas. Quando configurado com um valor muito alto ou desativado, pode causar lentidão e exceder o tempo máximo de resposta. Ajustá-lo para restringir os registros ajuda a evitar esse problema.

**(2)** Timeout da consulta **''-Djape.global.query.timeout'':**

O argumento -Djape.global.query.timeout define o tempo limite para execução de consultas SQL, com valor padrão de 600 segundos. Consultas que excedem esse tempo geram erro. Aumentar o limite é possível, mas deve ser feito com cautela, pois pode ocultar problemas de desempenho.

**(1)**Local para ajuste:

- Linux: WILDFLY\_INSTALL/bin/standalone.conf
- Windows: WILDFLY\_INSTALL/bin/standalone.conf.bat

⚠️ **Importante:** Antes de qualquer alteração, é essencial validar se a tela realmente precisa de tanto tempo para concluir a consulta. Aumentar o timeout resolve o erro imediato, mas não trata a causa raiz de lentidão.

**(3)** Parâmetro **''DESABPAGINA'':**

O parâmetro DESABPAGINA desativa a paginação nas consultas, fazendo com que todos os dados sejam retornados de uma vez. Isso pode reduzir o tempo de execução em alguns casos, ao evitar múltiplas chamadas ao banco. No entanto, seu uso deve ser criterioso, pois pode aumentar o volume de dados retornado e agravar problemas de desempenho se não for combinado com filtros adequados e ajuste do MAXRSLTSIZE.

**CAUSA:**

A causa raiz do erro está relacionada ao tempo excessivo de execução das consultas SQL acionadas por determinadas telas do sistema. Isso geralmente ocorre devido a:

- Volume elevado de dados processados de uma só vez;
- Ausência ou uso inadequado de filtros nas consultas;
- Má configuração de parâmetros de performance (como MAXRSLTSIZE, DESABPAGINA e -Djape.global.query.timeout);
- Consultas mal otimizadas ou uso de visões complexas que exigem alto tempo de processamento.

Caso o problema persista mesmo após seguir as orientações deste artigo, recomenda-se abrir um chamado com o time de Service Desk.
