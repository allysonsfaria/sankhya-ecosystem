---
id: "23861517253911"
titulo: "ORA-20101: Histórico não pode ser zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/23861517253911-ORA-20101-Hist%C3%B3rico-n%C3%A3o-pode-ser-zero"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:31:54Z"
rotulos: ["Configuração", "Histórico", "Contabilização", "Financeiro", "ORA-20101", "Erro"]
---

# ORA-20101: Histórico não pode ser zero

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/23861517232919) **MENSAGEM:**

MGE - Pessoal --------------------------- General SQL error. ORA-20101: Histórico não pode ser zero. ORA-06512: em "SANKHYA.TRG\_INC\_TCBLAN".

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/23861517247767)CAUSA:**

Esta mensagem ocorre devido a uma 'Trigger" (bloqueio) que foi criado para evitar de enviar informações para contabilidade com 'Histórico contábil de débito e crédito = ZERO.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/23861487678615)SOLUÇÃO:**

Acesse as **configurações contábeis** (Menu Arquivos\Cadastros\Informações Contábeis\Configurações Contábeis) para tipo de contabilização = normal, localize todos os histórico de crédito e débito que estiverem = 0 e informe os históricos contábeis **(essas informações deverá pegar com a Contabilidade)**.

![Imagem 4: Acesse as configurações contábeis (Menu Arquivos\Cadastros\Informações Contábeis\Configurações Contábeis) para tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/23938853546647)

Se desejar enviar a integração para contabilidade sem os históricos, será necessário desmarcar a opção abaixo no menu (Pessoal/Arquivos/Empresas) localizando a Empresa, aba (informações contábeis / lançamentos) e marcar a opção 'Aceitar histórico zero" conforme demonstrado a seguir:
 

![Imagem 5: Se desejar enviar a integração para contabilidade sem os históricos, será necessário desmarcar a opção abaixo no menu…](https://ajuda.sankhya.com.br/hc/article_attachments/23938838881815)
