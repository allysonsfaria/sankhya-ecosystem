---
id: "360043712214"
titulo: "O título está em cobrança registrada e não pode ser excluído"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712214-O-t%C3%ADtulo-est%C3%A1-em-cobran%C3%A7a-registrada-e-n%C3%A3o-pode-ser-exclu%C3%ADdo"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:48Z"
rotulos: ["#PUBLIFER", "Configuração", "NF-e", "Movimentação Financeira", "Preferências", "Financeiro", "ORA-20101", "20101", "06512", "Título em cobrança impede exclusão", "Ative PERDESVFINREM", "Desvincule remessa"]
---

# O título está em cobrança registrada e não pode ser excluído

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16200944634391) MENSAGEM:**

Erro ao remover entidade:

ORA-20101: O título está em cobrança registrada e não pode ser excluído.

ORA-06512: em "SANKHYA.TRG\_INC\_UPD\_TGFFIN\_MONIOCOREM", line 79

ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_UPD\_TGFFIN\_MONIOCOREM'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16200918578967) SITUAÇÃO:**

Ao tentar efetuar o cancelamento de uma Nota, ocorre a mensagem.

**![Imagem 3: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16200918580247) SOLUÇÃO:**

Para proceder com o cancelamento da nota fiscal eletrônica é necessário permitir desvincular o(s) financeiro(s) gerado(s) da respectiva remessa bancária.

![Imagem 4: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16200944641559) Para essa permissão é necessário que o parâmetro **"PERDESVFINREM"** esteja 'ligado'.

- Acesse: Configurações » Avançado » Preferências
- Chave: PERDESVFINREM - Permite desvincular financeiro de remessa?
- Ligado/Desligado: ligado

![Imagem 5: Ligado/Desligado: ligado](https://ajuda.sankhya.com.br/hc/article_attachments/16200944642839) Acesse: Financeiro » EDI Bancário » Registro de Alteração Financeiro

Faça um filtro e pesquise pelo título, caso haja registro dele nesta tela, exclua-o. Se não houver, tente Desvincular Remessa na Movimentação Financeira.

![Imagem 6: Ligado/Desligado: ligado](https://ajuda.sankhya.com.br/hc/article_attachments/16200918588183) Após verificar o parâmetro, localize o financeiro na tela **"[Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)"**, no botão **"Outras Opções"** clique em **"Desvincular Remessa"**.

![Imagem 7: Ligado/Desligado: ligado](https://ajuda.sankhya.com.br/hc/article_attachments/16200918590359) Feito isso, teste o cancelamento da NF-e.

**![Imagem 8: Ligado/Desligado: ligado](https://ajuda.sankhya.com.br/hc/article_attachments/16200944647831) CAUSA**

Ocorre quando ao tentar cancelar NF-e que possui financeiro(s) vinculado(s) a arquivo de remessa bancária, será apresentada a mensagem.
