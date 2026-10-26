---
id: "360043674553"
titulo: "É obrigatório informar o contato do parceiro para entrega"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043674553-%C3%89-obrigat%C3%B3rio-informar-o-contato-do-parceiro-para-entrega"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:26Z"
rotulos: ["#criadoRoger", "Configuração", "Parceiro", "Vendas", "CORE_E00806", "Contato de entrega obrigatório", "Parâmetro habilitado sem contato cadastrado", "Ativar \"USENDENTREGA\" cadastrar contato com endereço", "Erro"]
---

# É obrigatório informar o contato do parceiro para entrega

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16146104715543) MENSAGEM**:

[CORE\_E00806] É obrigatório informar o contato do parceiro para entrega.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16146097701015) SOLUÇÃO**:

Para que seja possível concluir o lançamento, informe no cabeçalho do Pedido/Nota o contato do parceiro que tenha endereço preenchido em seu cadastro.

![Imagem 3: Para que seja possível concluir o lançamento, informe no cabeçalho do Pedido/Nota o contato do parceiro que tenha…](https://ajuda.sankhya.com.br/hc/article_attachments/27594697383831)

**![Imagem 4: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16146097715479) CAUSA**:

Ocorre quando o campo 'Contato' do cabeçalho do lançamento está vazio e as configurações abaixo existem na base:

- Parâmetro **"Usa endereço de entrega dos contatos - USENDENTREGA"** ligado;
- Lançamento é Pedido de Venda ou Nota de Venda;
- No cadastro do parceiro, da nota que está sendo lançada, o campo '**Utiliza endereço de entrega do contato'** está marcado.

![Imagem 5: No cadastro do parceiro, da nota que está sendo lançada, o campo ' Utiliza endereço de entrega do contato' está marcado.](https://ajuda.sankhya.com.br/hc/article_attachments/27595052723223)
