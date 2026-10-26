---
id: "360055287353"
titulo: "A instrução INSERT conflitou com a restrição do FOREIGN KEY \"FK_TGFCOT_CODNAT_TGFNAT\". O conflito ocorreu no banco de dados \"SANKHYA_PROD\", tabela \"SANKHYA.TGFNAT\", column 'CODNAT'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360055287353-A-instru%C3%A7%C3%A3o-INSERT-conflitou-com-a-restri%C3%A7%C3%A3o-do-FOREIGN-KEY-FK-TGFCOT-CODNAT-TGFNAT-O-conflito-ocorreu-no-banco-de-dados-SANKHYA-PROD-tabela-SANKHYA-TGFNAT-column-CODNAT"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:28:37Z"
rotulos: ["Configuração", "Análise de Giro", "Preferências", "Financeiro", "Natureza", "#formatadoroger", "Restrição de Chave Estrangeira", "Banco de Dados Sankhya_PROD", "Natureza Analítica", "Erro"]
---

# A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK_TGFCOT_CODNAT_TGFNAT". O conflito ocorreu no banco de dados "SANKHYA_PROD", tabela "SANKHYA.TGFNAT", column 'CODNAT'

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/15916030630039) MENSAGEM**:

A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK\_TGFCOT\_CODNAT\_TGFNAT". O conflito ocorreu no banco de dados "SANKHYA\_PROD", tabela "SANKHYA.TGFNAT", column 'CODNAT'.

**![Imagem 2: A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK_TGFCOT_CODNAT_TGFNAT". O conflito ocorreu no banco de…](https://ajuda.sankhya.com.br/hc/article_attachments/15916077254039) CAUSA:**

Ocorre quando não existe ou a natureza informada nas Preferências para gerar a cotação não é analítica e/ou não esta ativa.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15916077257495) SOLUÇÃO:**

Para correção seguir os passos abaixo:

![Imagem 4: Acesse o botão em Comercial » Rotinas » Análise de Giro No campo 'Natureza', escolha uma Natureza do tipo 'Analítica' e…](https://ajuda.sankhya.com.br/hc/article_attachments/15916030642583) Acesse o botão   ![Imagem 5: Acesse o botão em Comercial » Rotinas » Análise de Giro No campo 'Natureza', escolha uma Natureza do tipo 'Analítica' e…](https://ajuda.sankhya.com.br/hc/article_attachments/360089396074)  em Comercial » Rotinas » Análise de Giro
No campo 'Natureza', escolha uma Natureza do tipo 'Analítica' e 'Ativa'
![Imagem 6: Acesse o botão em Comercial » Rotinas » Análise de Giro No campo 'Natureza', escolha uma Natureza do tipo 'Analítica' e…](https://ajuda.sankhya.com.br/hc/article_attachments/360089396414)

![Imagem 7: Após os ajustes, pode-se Gerar a Cotação novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/15916030650519) Após os ajustes, pode-se Gerar a Cotação novamente.
