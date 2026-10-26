---
id: "360044609634"
titulo: "Conferência de Inventário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609634-Confer%C3%AAncia-de-Invent%C3%A1rio"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-07-29T14:49:10Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Inventário", "Movimentação Financeira", "Conferência do Inventário", "br.com.sankhya.mgeinvent.conferencia.inventario", "Conferência do Inventário manual", "Estoque", "Conferência de inventário detalhada", "Configurações de filtros precisos", "Controle de estoque avançado"]
---

# Conferência de Inventário

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312597577367) Módulo: Inventário > Avançado
```

---

Esta tela é utilizada como uma ferramenta de auxílio de controle de estoque, apontando para produtos que serão inventariados. Nela, é feita a conferência do inventário do estoque, onde é levantada toda a movimentação de estoque no lançamento de notas, através da data inicial e final informada e das TOP's que atualizam os livros fiscais, detectando eventuais anomalias e, consequentemente, suas correções a tempo (por exemplo: a não inclusão no sistema de uma nota fiscal de compra).

![Imagem 2: Esta tela é utilizada como uma ferramenta de auxílio de controle de estoque, apontando para produtos que serão…](https://ajuda.sankhya.com.br/hc/article_attachments/360087918193)

Caso não exista cópia de estoque para a data informada, o sistema apresentará na grade, os itens das notas negociadas no período informado com suas quantidades negociadas negativas (pois indica baixa no estoque).

**Importante:** não serão apresentadas duplicidades de itens (registros iguais para o mesmo produto, empresa, controle e local, quando configurado para considerar).

O sistema considerará as notas que estão liberadas, TOP's que atualizam livros fiscais ou TOP's que sejam de Cupons Fiscais. Além disso, os itens não podem estar marcados para reservar.

No lado esquerdo da tela, você poderá configurar alguns campos para filtrar na rotina de Conferência de Inventário. Abaixo trataremos sobre eles:

Informe a **"Empresa"** cujo inventário será levantado.

O **"Período"** refere-se à Data Inicial/Data Final, que possibilitará a geração da conferência, dentro do período pré-estabelecido.

A data informada no campo **"Contagem p/ Estoque Inicial"** busca informações da TGFCTE, considerando a quantidade inventariada do item para início de saldo.

Efetue a marcação **"Usa Local no Inventário?"** se sua empresa utilizar controle de estoque por locais.

**Nota:** a marcação acima estará desabilitada, quando o parâmetro **"Utiliza a coluna Local para controlar o estoque -UTILIZALOCAL"** estiver desligado.

Efetue a marcação **"Usa Controle no Inventário?"** se sua empresa utilizar controles de estoque adicionais. Exemplo: Lote, Série e etc.

**Observação:** a marcação acima estará desabilitada, quando o parâmetro **"Controle para controlar o estoque -UTILIZACONTROLE"** estiver desligado.

Se a marcação **"Exibir TOPs que não atualizam estoque?"** estiver efetuada, fará com que o sistema considere as TOP's que não atualizam estoque.

Quando a marcação **"Somente produtos contados?"** não estiver selecionada, permitirá que você visualize também os produtos não contados, individualmente.

Quando a marcação **"Ler contagem de Próprios em poder de Terceiros?"** estiver realizada na Conferência de Inventário, o sistema traz para a visualização do produto, o seu estoque inicial acrescido das quantidades que estiverem em poder de terceiros, onde **"CODPARC <> 0"** e **"TIPO = P"**.

Efetuando a marcação **"Ler contagem de Terceiros em poder da Empresa?"**na Conferência de Inventário, o sistema traz para a visualização do produto, somente o estoque do produto que esteja em poder da empresa, seja ele próprio ou de terceiros, onde CODPARC = 0, TIPO = P e CODPARC = 0 e **"TIPO = T"**.

**Importante:** ainda não foi implementado o relatório no Sankhya Om, referente à parte **"Parâmetros para relatório"** da tela de Conferência de Inventário.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609634-Confer%C3%AAncia-de-Invent%C3%A1rio#top)
