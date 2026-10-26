---
id: "360050394514"
titulo: "Erro interno: PreparedStatement com parâmetro nulo na entidade 'HistoricoBancario': param[0] = nullde"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050394514-Erro-interno-PreparedStatement-com-par%C3%A2metro-nulo-na-entidade-HistoricoBancario-param-0-nullde"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-08-19T14:24:19Z"
rotulos: ["Configuração", "Preferências", "Financeiro", "Sankhya Checkout", "WKF_E00040", "Configure lançamentos bancários", "Erro interno PreparedStatement", "Falta de configurações de lançamento bancário", "Erro"]
---

# Erro interno: PreparedStatement com parâmetro nulo na entidade 'HistoricoBancario': param[0] = nullde

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18611284513943) MENSAGEM**:

Erro interno: PreparedStatement com parâmetro nulo na entidade 'HistoricoBancario':
param[0] = nullde.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18611310494359) CAUSA:**

Erro ao processar venda na Administração do Checkout, causada pela ausência de configurações de lançamento bancário.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18611310501015) **SOLUÇÃO:**

- Tela **'Empresa'** (Comercial » Preferências)
  Aba: Propriedades
  Campos **"Lançamento bancário receitas:"** e **"Lançamento bancário despesas:"** devem estar preenchidos.

![Imagem 4: Tela 'Empresa' (Comercial » Preferências) Aba: Propriedades Campos "Lançamento bancário receitas:" e "Lançamento…](https://ajuda.sankhya.com.br/hc/article_attachments/18611310515223)

**No Checkout :**

- Preferencias > Integração
- Os campos **'Código de lançamento Bancário para Sangria'** e **'Código de lançamento para Suprimento'** devem estar preenchidos:

![Imagem 5: Os campos 'Código de lançamento Bancário para Sangria' e 'Código de lançamento para Suprimento' devem estar preenchidos:](https://ajuda.sankhya.com.br/hc/article_attachments/18611310518039)
