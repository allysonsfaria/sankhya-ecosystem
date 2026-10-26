---
id: "360043607894"
titulo: "Restrição de integridade (SANKHYA.FK_TGFCTC_CODBCO_TSIBCO) violada - chave mãe não localizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043607894-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFCTC-CODBCO-TSIBCO-violada-chave-m%C3%A3e-n%C3%A3o-localizada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:01:16Z"
rotulos: ["Configuração", "Contas", "Financeiro", "ORA-02291", "Cadastro", "Erro ORA-02291: chave mãe não localizada", "Verificar e cadastrar o banco", "Banco não cadastrado no sistema", "Erro"]
---

# Restrição de integridade (SANKHYA.FK_TGFCTC_CODBCO_TSIBCO) violada - chave mãe não localizada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16171932935319) MENSAGEM:**

ORA-02291: restrição de integridade (SANKHYA.FK\_TGFCTC\_CODBCO\_TSIBCO) violada - chave mãe não localizada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16171946316567) SOLUÇÃO:**

![Imagem 3: Verifique o 'Banco' vinculado ao respectivo cheque, através das informações de CMC7:](https://ajuda.sankhya.com.br/hc/article_attachments/16171946319767) Verifique o 'Banco' vinculado ao respectivo cheque, através das informações de CMC7:

![Imagem 4: Verifique o 'Banco' vinculado ao respectivo cheque, através das informações de CMC7:](https://ajuda.sankhya.com.br/hc/article_attachments/14599928096279)

![Imagem 5: Acesse a tela "Bancos" (Caminho de acesso: Configurações » Cadastros » Bancários » Bancos ) e verifique se o banco…](https://ajuda.sankhya.com.br/hc/article_attachments/16171932942743) Acesse a tela [**"Bancos"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598894) (Caminho de acesso: Configurações » Cadastros » Bancários » Bancos) e verifique se o banco constatado no item 1 encontra-se cadastrado. Em caso negativo, efetue o cadastro.

![Imagem 6: Acesse a tela "Bancos" (Caminho de acesso: Configurações » Cadastros » Bancários » Bancos ) e verifique se o banco…](https://ajuda.sankhya.com.br/hc/article_attachments/12245792900119)

![Imagem 7: Realizado o cadastro do Banco, teste o procedimento de baixa.](https://ajuda.sankhya.com.br/hc/article_attachments/16171946325655) Realizado o cadastro do Banco, teste o procedimento de baixa.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16171932947479) CAUSA:**

Mensagem apresentada quando o 'Banco' utilizado na operação de baixa não está cadastrado no sistema.
