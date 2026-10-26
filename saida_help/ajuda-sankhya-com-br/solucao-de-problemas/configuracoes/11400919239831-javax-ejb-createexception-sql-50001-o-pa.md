---
id: "11400919239831"
titulo: "javax.ejb.CreateException: SQL-50001 O parceiro deve ser diferente de zero na nota de nro único: X. Integração Máxima"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11400919239831-javax-ejb-CreateException-SQL-50001-O-parceiro-deve-ser-diferente-de-zero-na-nota-de-nro-%C3%BAnico-X-Integra%C3%A7%C3%A3o-M%C3%A1xima"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:01:47Z"
rotulos: ["Configuração", "Parceiro", "Financeiro", "não apagar", "Integração Máxima", "Erro javax.ejb.CreateException Resolvido", "Erro"]
---

# javax.ejb.CreateException: SQL-50001 O parceiro deve ser diferente de zero na nota de nro único: X. Integração Máxima

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16334609040023) MENSAGEM**:

javax.ejb.CreateException: SQL-50001 O parceiro deve ser diferente de zero na nota de nro único: X.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334609043863) SOLUÇÃO:**

Para resolver o erro, acesse o cadastro da Empresa "Configurações » Cadastros » Empresas" utilizada no Retorno de Carga e vincule um Parceiro no campo "Cód. Parceiro".

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16334570776471)CAUSA:**

- O erro acontece ao processar um Retorno de Carga na Integração Máxima;
- Isso ocorre quando a Empresa referente ao Retorno de Carga não possui um Parceiro vinculado;
- Ao processar um Retorno de Carga é gerada uma nota de retorno com o Parceiro vinculado a Empresa.
