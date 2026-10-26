---
id: "360043661333"
titulo: "Validar silencioso: Nro Único: XXXXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043661333-Validar-silencioso-Nro-%C3%9Anico-XXXXXX"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:10Z"
rotulos: ["#RevisadoBraga", "Configuração", "Parceiro", "NF-e", "Crédito", "Financeiro", "Validar silencioso Nro Único: XXXXXX", "Ajustar \"Motivo bloqueio\" em Parceiros", "Parâmetros de bloqueio e venda a prazo", "Erro"]
---

# Validar silencioso: Nro Único: XXXXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16413951676823) MENSAGEM:**

Validar silencioso: Nro Único: XXXXXX
Aviso: [MENSAGEM DE AVISO]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16413951678231) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela ''Parceiros'' (Configurações » Cadastros » Parceiros).](https://ajuda.sankhya.com.br/hc/article_attachments/16413951679383) Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(2)** Na aba **''Crédito''**, verifique o campo **''Motivo de Bloqueio''**.

![Imagem 4: (2) Na aba ''Crédito'' , verifique o campo ''Motivo de Bloqueio'' .](https://ajuda.sankhya.com.br/hc/article_attachments/14681227538839)

**(3)** Considere verificar com a equipe Financeira para que seja apagada a mensagem de motivo do cadastro do parceiro, para que seja possível confirmar a Nota Fiscal.

**(4)** Após os ajustes, fature novamente a nota fiscal.

![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16413936806295) **CAUSA:**

Ocorre quando o parâmetro "**EXIBMOTBLOQ"** esta ativo, o parâmetro "**VALPEDATRASO"** desativado, a opção **"Bloquear venda a prazo"** desmarcado no parceiro e tenha informação no campo **"Motivo de Bloqueio"** do cadastro do Parceiro.
