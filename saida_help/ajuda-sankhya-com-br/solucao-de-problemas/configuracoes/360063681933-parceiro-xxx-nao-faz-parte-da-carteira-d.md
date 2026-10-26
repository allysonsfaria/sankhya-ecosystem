---
id: "360063681933"
titulo: "Parceiro XXX não faz parte da carteira do vendedor logado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360063681933-Parceiro-XXX-n%C3%A3o-faz-parte-da-carteira-do-vendedor-logado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:13Z"
rotulos: ["Configuração", "Parceiro", "Vendas", "não apagar", "#validadoPenelope", "#criadoHyago", "CORE_E01471", "Restrição de Venda por Vendedor", "Erro"]
---

# Parceiro XXX não faz parte da carteira do vendedor logado

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16334641027991) MENSAGEM**:

[CORE\_E01471] Parceiro XXX não faz parte da carteira do vendedor logado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334641031319) SOLUÇÃO:**

Esta mensagem é diretamente relacionada ao cadastro de Parceiros aba **Identificação > Vend. Preferencial**. O campo **"Vend. Preferencial"** diz respeito ao vendedor responsável pelo parceiro nas vendas, caso exista, deverá ser informado neste campo. Para conseguir realizar a venda, o vendedor logado deverá ser o mesmo vendedor informado no cadastro do parceiro, ou no parceiro esse campo deverá permanecer vazio, caso qualquer vendedor possa realizar vendas a ele.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16334641035799) CAUSA:**

O incidente é causado pela ativação do campo restringir carteira. Estando esse botão ativado, a marcação quando acionada, impedirá que um vendedor efetue lançamentos para os parceiros que se encontrem fora da sua carteira. Além disso, na Ficha de Parceiros, o sistema permitirá que o vendedor logado e o gerente deste consulte apenas os parceiros pertinentes a sua carteira.
