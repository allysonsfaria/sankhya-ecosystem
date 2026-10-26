---
id: "39363243973911"
titulo: "Eventos de Desconto não acionados - PDV WEB"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39363243973911-Eventos-de-Desconto-n%C3%A3o-acionados-PDV-WEB"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T13:43:48Z"
rotulos: ["Configuração", "Nota Fiscal", "Desconto", "Preferências", "PDV Web", "Artigo criado KCS", "Varejo - KCS"]
---

# Eventos de Desconto não acionados - PDV WEB

### SITUAÇÃO

Ao importar um pedido pelo **PDV Web** (**Portal de Caixa > Comercial > Consulta**), o sistema pode apresentar o valor unitário dos itens sem considerar os descontos informados no pedido. Como consequência, o valor total da nota fiscal é calculado sem os descontos aplicados.

Além disso, os eventos de liberação **2** e **25** não são acionados automaticamente durante a importação do pedido.

### SOLUÇÃO

Para corrigir o comportamento, siga os passos abaixo:

**(1)** Acesse a tela **Preferências** (**Configurações > Avançado**).

**(2)** Localize o parâmetro **VALAPRRECPDV**.
![Imagem 1: (1) Acesse a tela Preferências ( Configurações > Avançado ). (2) Localize o parâmetro VALAPRRECPDV . Verifique o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/41585439600279)

**(3)** Verifique o campo **Ligado/Desligado**:

- Se o parâmetro estiver **Ligado**, altere-o para **Desligado**.
- Salve a alteração.

**(4)** Após a alteração, realize uma nova importação do pedido no **PDV Web** para validar o comportamento.

### CAUSA

Esse comportamento ocorre quando o parâmetro **VALAPRRECPDV** está habilitado.

Quando esse parâmetro está ativo, o sistema altera o fluxo de aprovação das notas no recebimento, interferindo no processamento dos descontos dos itens durante a importação do pedido pelo **PDV Web**. Como consequência:

- os descontos informados no pedido não são considerados no cálculo do valor total da nota fiscal;
- os eventos de liberação **2** e **25** deixam de ser acionados automaticamente.
