---
id: "360044118493"
titulo: "A movimentação bancária a ser estornada foi feita na conta XX e somente o caixa desta conta pode estorná-la"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044118493-A-movimenta%C3%A7%C3%A3o-banc%C3%A1ria-a-ser-estornada-foi-feita-na-conta-XX-e-somente-o-caixa-desta-conta-pode-estorn%C3%A1-la"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:01:12Z"
rotulos: ["#criadoRoger", "#revisadohugo", "CORE_E01776", "Configuração", "Contas", "Segurança", "Movimentação Financeira", "Financeiro", "Movimentação restrita ao caixa", "Verificar usuário e conta", "Restrição de integridade", "Erro"]
---

# A movimentação bancária a ser estornada foi feita na conta XX e somente o caixa desta conta pode estorná-la

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16191375801623) MENSAGEM**:

[CORE\_E01776]  A movimentação bancária a ser estornada foi feita na conta XX e somente o caixa desta conta pode estorná-la.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16191390712343) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Quando no cadastro do " Usuário " (Caminho de acesso: Configurações » Controle de Acesso » Usuários ) está marcado a…](https://ajuda.sankhya.com.br/hc/article_attachments/16191375803287) Quando no cadastro do **"[Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)"** (Caminho de acesso: Configurações » Controle de Acesso » Usuários) está marcado a opção **"Caixa",** da aba **Identificação** e a Conta da baixa é do tipo **"Caixa"**, somente o usuário que efetuou a abertura do Caixa e baixou o título neste Caixa, poderá estornar o título.

- **Consulte usuário Caixa:**
  Configurações » Controle de Acesso » Usuários -  Aba: Identificação, Campo: Caixa

![Imagem 4: Consulte usuário Caixa: Configurações » Controle de Acesso » Usuários - Aba: Identificação , Campo: Caixa](https://ajuda.sankhya.com.br/hc/article_attachments/14606430792471)

- **Consulte a Conta Bancaria:**
  Configurações » Cadastros » Bancários » Contas - Aba: **Cadastros**, Campo: **"Tipo de Conta"**

![Imagem 5: Consulte a Conta Bancaria: Configurações » Cadastros » Bancários » Contas - Aba: Cadastros , Campo: "Tipo de Conta"](https://ajuda.sankhya.com.br/hc/article_attachments/14606431661207)

![Imagem 6: Oriente o próprio usuário que efetuou a baixa a acessar o sistema e efetuar o estorno.](https://ajuda.sankhya.com.br/hc/article_attachments/16191390714135) Oriente o próprio usuário que efetuou  a baixa a acessar o sistema e efetuar o estorno.

**![Imagem 7: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16191390716695) CAUSA**:

Ocorre quando outro usuário com acesso à baixa tenta efetuar o estorno de um título em que o usuário Caixa efetuou a baixa.

Quando o usuário caixa abre um Caixa Financeiro e efetua baixas em Contas Bancárias do tipo Caixa, somente este poderá estornar os títulos, devido a restrições de integridades e não impactar em relatórios de fechamento de caixa.
