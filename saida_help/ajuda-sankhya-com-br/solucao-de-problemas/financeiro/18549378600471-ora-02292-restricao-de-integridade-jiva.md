---
id: "18549378600471"
titulo: "ORA-02292: restrição de integridade (JIVA.FK_TGFFRE_NUFINORING_TGFFIN)violada - registro filho localizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18549378600471-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-JIVA-FK-TGFFRE-NUFINORING-TGFFIN-violada-registro-filho-localizado"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:52:23Z"
rotulos: ["TGFFRE", "Movimentação Financeira", "Financeiro", "DBExplorer", "Restrição de integridade violada", "Título com vínculo na tabela TGFFRE", "Desfaça processos e verifique lançamentos financeiros", "ORA-02292", "Erro"]
---

# ORA-02292: restrição de integridade (JIVA.FK_TGFFRE_NUFINORING_TGFFIN)violada - registro filho localizado

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18549325563543) **MENSAGEM:**

ORA-02292: restrição de integridade (JIVA.FK\_TGFFRE\_NUFINORING\_TGFFIN)violada - registro filho localizado.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18549366444055)CAUSA:**

Ocorre quando os títulos financeiros que está tentando excluir possui vínculo na tabela 'TGFFRE' e, para conseguir excluir o título precisa desfazer os processos anteriores que o título participou ( exemplo: Renegociação de Título, Compensação Financeira, Compensação de devolução realizada na Central).

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18549335441943)SOLUÇÃO:**

Verificado em qual rotina que o título consta vinculado na tabela TGFFRE. Certifique se realmente  deverá ser desfeito. Desfaça o processo que conseguirá excluir o título financeiro na 'Movimentação Financeira'.

Primeiro identifique se os lançamentos financeiros estão baixados. Se verificado que os lançamentos financeiros constam em aberto será necessário fazer uma consulta pela tela **DBEexplorer-** Configurações » Avançado » DBExplorer para verificar se ainda há algum registro na tabela TGFFRE.

Na tela DBExplorer faça o seguinte SELECT:

**SELECT \* FROM TGFFRE WHERE NUFIN =**

Fazendo o select acima será apresentado em qual rotina o título consta vinculado demonstrado no campo 'TIPACERTO' sendo:

A=Adiantamento/empréstimo
P=Baixa Parcial
C=Compensação (tela compensação financeira)
G=Compensação Garantia
F=Pagamento de Frete/ Pagamento de Frete por OC
L=Acerto com fornecedores
N=Antecipação de baixa
X=Crédito a compensar (Baixa de movimentação financeira com valor superior ao da receita gerando crédito a compensar)
D=Desconto de Títulos / Devolução de Pagamento
R=Renegociação de Títulos
V=Compensar devolução
