---
id: "31872306056599"
titulo: "Falha ao executar a procedure Stp_Set_Session2. Erro: ORA-04068: estado atual dos pacotes foi descartado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31872306056599-Falha-ao-executar-a-procedure-Stp-Set-Session2-Erro-ORA-04068-estado-atual-dos-pacotes-foi-descartado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:32:20Z"
rotulos: ["CORE_E01003", "ORA-06512", "estado existente de package \"SANKHYA.VARIAVEIS_PKG\" foi invalidado", "package \"SANKHYA.VARIAVEIS_PKG\" não executado alterado ou eliminado", "ORA-06508", "PL/SQL: não foi localizada a unidade de programa que está sendo chamada:", "em \"SANKHYA.STP_SET_SESSION2\" line3", "ORA-06512: em line 1", "ORA-04061", "ORA-04065", "em \"SANKHYA.STP_SET_SESSION\" line 9", "Erro", "Sankhya", "ORA-04068", "Database", "Package"]
---

# Falha ao executar a procedure Stp_Set_Session2. Erro: ORA-04068: estado atual dos pacotes foi descartado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31999153052183) MENSAGEM:**

[CORE\_E01003] Falha ao executar a procedure Stp\_Set\_Session2. Erro: ORA-04068: estado atual dos pacotes foi descartado.
ORA-04061: estado existente de package "SANKHYA.VARIAVEIS\_PKG" foi invalidado
ORA-04065: package "SANKHYA.VARIAVEIS\_PKG" não executado, alterado ou eliminado
ORA-06508: PL/SQL: não foi localizada a unidade de programa que está sendo chamada: "SANKHYA.VARIAVEIS\_PKG"
ORA-06512: em "SANKHYA.STP\_SET\_SESSION", line 9
ORA-06512: em "SANKHYA.STP\_SET\_SESSION2", line 3
ORA-06512: em line 1

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31999126768663) SITUAÇÃO:**

Ao realizar qualquer processo nos portais (venda ou compra).

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31888056124823)SOLUÇÃO:**

Este erro ocorre pois o Package "**VARIAVEIS\_PKG**" que é um objeto nativo da Sankhya, foi excluído, alterado ou até mesmo compilado utilizando o Owner incorreto.

Então, para solução, entre em **contato com a equipe de Service Desk** para obter o Script atualizado do objeto para uma nova compilação.

**(2)** Esse pacote atua como um **repositório de variáveis e estruturas de apoio,** que podem ser usadas por diversos procedimentos e funções do sistema, ajudando a manter **consistência, desempenho e organização** em ambientes com lógica de negócio complexa.
