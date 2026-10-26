---
id: "11098954586647"
titulo: "Erro ao carregar página de dados 1 para EmpresaFinanceiro. ORA-06502: PL/SQL: erro numérico ou de valor ORA-06512: em line 1 "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11098954586647-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-EmpresaFinanceiro-ORA-06502-PL-SQL-erro-num%C3%A9rico-ou-de-valor-ORA-06512-em-line-1"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:02:05Z"
rotulos: ["Configuração", "Preferências", "Financeiro", "não apagar", "ORA-06512", "Solução para Erro ORA-06502 em Empresa Financeiro", "Erro"]
---

# Erro ao carregar página de dados 1 para EmpresaFinanceiro. ORA-06502: PL/SQL: erro numérico ou de valor ORA-06512: em line 1 

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/19033033152279) MENSAGEM**:

[CORE\_E00358] Erro ao carregar página de dados 1 para EmpresaFinanceiro.
ORA-06502: PL/SQL: erro numérico ou de valor
ORA-06512: em line 1

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19033033166999) CAUSA:**

Erro de leitura da query via procedure.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033033177751) SOLUÇÃO:**

Para que o erro não seja mais apresentado e necessário realizar as configurações abaixo: 

![Imagem 4: Para que o erro não seja mais apresentado e necessário realizar as configurações abaixo: Desative o parâmetro Usar…](https://ajuda.sankhya.com.br/hc/article_attachments/18611018895255) Desative o parâmetro **Usar Stored Procedure ao exec. queries do sistema - USESTPQUERY** na tela **Preferências** (Configurações » Avançado » Preferências), conforme imagem abaixo:

![Imagem 5: Para que o erro não seja mais apresentado e necessário realizar as configurações abaixo: Desative o parâmetro Usar…](https://ajuda.sankhya.com.br/attachments/token/tkVGgJyvKpPNxF2sgYvTqPfl2/?name=image.png)

![Imagem 6: Para que o erro não seja mais apresentado e necessário realizar as configurações abaixo: Desative o parâmetro Usar…](https://ajuda.sankhya.com.br/hc/article_attachments/18611018901015) Reinicie o servidor do sistema na tela **Administração do Servidor** (Configurações » Avançado » Administração do Servidor)

![Imagem 7: Para que o erro não seja mais apresentado e necessário realizar as configurações abaixo: Desative o parâmetro Usar…](https://ajuda.sankhya.com.br/hc/article_attachments/18611018906647)

Assim ele mudará a forma de ler os dados, onde a query que traz o erro pare de ser executada via procedure e a tela consiga carregar corretamente.
