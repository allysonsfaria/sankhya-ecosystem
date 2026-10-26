---
id: "39359196046103"
titulo: "Erro ao imprimir/visualizar DANFE : \"Erro no modelo do documento adotado para impressão. Detalhes: null\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39359196046103-Erro-ao-imprimir-visualizar-DANFE-Erro-no-modelo-do-documento-adotado-para-impress%C3%A3o-Detalhes-null"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-13T19:20:37Z"
rotulos: ["Configuração", "Impressão", "NF-e", "XML", "SEFAZ", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# Erro ao imprimir/visualizar DANFE : "Erro no modelo do documento adotado para impressão. Detalhes: null"

**Mensagem**

Documento [número]: Erro no modelo do documento adotado para impressão. Detalhes: null

**Situação**

Este erro ocorre ao tentar "**Imprimir o DANFE**" ou "**Visualizar a nota fiscal**" após a aprovação da nota. O sistema apresenta a mensagem de erro indicando problema no modelo de impressão, impedindo a geração do documento.

(1)**Principais causas do erro**

- **XML não retornado/gravado no sistema:** embora a nota tenha sido "Aprovada" com sucesso pela SEFAZ, o XML autorizado não foi retornado ou não foi gravado no sistema. Como o modelo de impressão busca as informações diretamente do XML da nota fiscal, a ausência desse arquivo impede a geração do documento.
- **XML presente, porém com inconsistência:** o XML foi gravado no sistema, mas contém tags obrigatórias ausentes, com valores inválidos ou fora do padrão esperado pelo modelo de impressão. Nesse caso, o modelo tenta ler um campo que não existe ou está nulo no XML, resultando no mesmo erro ("Detalhes: null").

**Causa**

Se o problema persistir após validar XML e modelo de impressão, se faz necessario analise do log, pois "Detalhes: null" é um erro genérico que pode mascarar causas distintas.
