---
id: "39293379829655"
titulo: "Como manter a sequência dos itens ao faturar pedidos de venda?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39293379829655-Como-manter-a-sequ%C3%AAncia-dos-itens-ao-faturar-pedidos-de-venda"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-10-20T19:53:42Z"
rotulos: ["Configuração", "Faturamento", "Central de Vendas", "Artigo criado KCS", "CVE - KCS", "Parâmetros do Sistema", "Pedidos de Venda"]
---

# Como manter a sequência dos itens ao faturar pedidos de venda?

Por padrão, o sistema pode reordenar ou reagrupar os itens ao faturar, alterando a sequência em que eles foram lançados. Para preservar a ordem original, ajuste os parâmetros abaixo em **Parâmetros do Sistema**:

### Configuração do parâmetro de ordenação

Para habilitar o parâmetro e garantir a ordenação correta:

1. **ORDITENS** → defina como `0`. Esse é o parâmetro que decide, em última instância, se a ordenação segue a sequência original (`0`) ou passa a ser por produto/local/controle (qualquer outro valor). Sem esse ajuste, os passos seguintes não garantem a preservação da ordem.
2. **ORDPRODDESCTOT** → **desligado**. Ligado, o sistema prioriza na ordenação os itens totalmente descontados (por exemplo, bonificação ou brinde com valor líquido zerado), colocando-os no início da lista.
3. **AGRUPFATSEMP** → **desligado**. Ligado, o sistema agrupa produtos repetidos e reordena por Código do Produto, Código do Local de Origem e Controle. Também, **quando o documento faturado é um pedido de venda** e o **parâmetro** está **ligado**, além dos campos anteriores, **o sistema irá considerar CFOP.**
4. **AGRUPAPROD** → **desligado**. Tem o mesmo efeito de reagrupamento e reordenação do item anterior.

Após ajustar os quatro parâmetros, salve e refaça o teste de faturamento para confirmar que a sequência foi mantida.

**ATENÇÃO!**Orientamos que todas alterações sejam feitas em ambiente de homologação, só após testados e validados sejam repassados para o ambiente de produção.
