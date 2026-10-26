---
id: "30602891550103"
titulo: "Aviso ao fechar o caixa no PDV WEB: \"É obrigatório a Apuração de Caixa antes do fechamento\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30602891550103-Aviso-ao-fechar-o-caixa-no-PDV-WEB-%C3%89-obrigat%C3%B3rio-a-Apura%C3%A7%C3%A3o-de-Caixa-antes-do-fechamento"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-29T12:41:03Z"
rotulos: ["Conferência", "Configuração", "Preferências", "Financeiro", "PDV Web", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Aviso ao fechar o caixa no PDV WEB", "antes do fechamento", "É obrigatório a Apuração de Caixa"]
---

# Aviso ao fechar o caixa no PDV WEB: "É obrigatório a Apuração de Caixa antes do fechamento"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30602891540503) **MENSAGEM:**

É obrigatório a Apuração de Caixa antes do fechamento

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30602891542935)SOLUÇÃO:**

![Imagem 3: Acesse a tela "Preferências" (Configurações » Avançado » Preferência) e verifique o parâmetro "EXIGECONFCAIXA" .](https://ajuda.sankhya.com.br/hc/article_attachments/31540804381719) Acesse a tela **"Preferências"** (Configurações » Avançado » Preferência) e verifique o parâmetro **"EXIGECONFCAIXA"**.

Quando esse parâmetro estiver ativado, a Apuração de Caixa deverá ser efetuada no pop-up Funções de Caixa, preenchendo os campos da coluna **"Informado"**.

**Observação:** caso a empresa não trabalhe com a conferência de caixa, esse parâmetro deve ser desabilitado.

![Imagem 4: Oriente o usuário do caixa a realizar a conferência, preenchendo na coluna "Informado" os valores conforme as vendas…](https://ajuda.sankhya.com.br/hc/article_attachments/31540849421719) Oriente o usuário do caixa a realizar a conferência, preenchendo na coluna "Informado" os valores conforme as vendas realizadas no dia.

**Observação:** caso o usuário deixe algum tipo de título (ex.: à vista, parcelado, cartão de crédito) zerado, mas tenha ocorrido uma negociação (venda) com esse tipo de título, o sistema ainda apresentará o aviso, pois entenderá que a conferência não foi realizada.

![Imagem 5: Após realizar a conferência, clique no botão "Fechar Caixa" para concluir o fechamento.](https://ajuda.sankhya.com.br/hc/article_attachments/31540849426711) Após realizar a conferência, clique no botão **"Fechar Caixa"** para concluir o fechamento.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30602891544087)CAUSA:**

Ocorre quando o parâmetro **EXIGECONFCAIXA** está habilitado e a conferência do caixa não foi realizada.
