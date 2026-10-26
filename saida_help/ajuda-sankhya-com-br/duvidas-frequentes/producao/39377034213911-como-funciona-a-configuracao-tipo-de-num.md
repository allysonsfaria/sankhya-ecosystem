---
id: "39377034213911"
titulo: "Como funciona a configuração \"Tipo de numeração de lote\" nas configurações dos Produtos Intermediários?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39377034213911-Como-funciona-a-configura%C3%A7%C3%A3o-Tipo-de-numera%C3%A7%C3%A3o-de-lote-nas-configura%C3%A7%C3%B5es-dos-Produtos-Intermedi%C3%A1rios"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-08-18T19:00:51Z"
rotulos: ["Produtos", "Configuração", "Lote", "Ordem de Produção", "Produção", "Artigo criado KCS", "Produção - KCS"]
---

# Como funciona a configuração "Tipo de numeração de lote" nas configurações dos Produtos Intermediários?

Durante a geração de uma **Ordem de Produção** **(Produção » Rotinas » Ordens de Produção » Nova)** para um **Produto Acabado** cuja composição contenha **Produtos Intermediários**, é fundamental compreender como o sistema trata a configuração de lotes desses itens.

Esse comportamento está diretamente relacionado à configuração do campo **"Tipo de numeração de lote"**, definido para cada **Produto Intermediário** na tela **Composição do Produto**.

O sistema disponibiliza diferentes opções de controle de lote, que determinam a forma como os Produtos Intermediários receberão seus respectivos números de lote ao longo do processo produtivo.

## Configuração de numeração de lote para produto intermediário:

Acesse a **Composição do Produto** **> Aba Matérias-Primas** **>** **Botão Outras Opções,** selecione o produto intermediário, clique em **Configurações de PI.** No campo **"Tipo de numeração de lote",** possui três opções de configuração:

**Obs.:** O campo apenas fica disponível se o **"Tipo do PI"** for **"Sub-ordem".**

- **"Nro. de lote independente"**: o **"Produto Intermediário"** gera seu próprio número de lote, independente do **"Produto Acabado"**.
- **"PI usa o mesmo lote do PA"**: o **"Produto Intermediário"** herda o número de lote do **"Produto Acabado"**.
- **"PA usa o mesmo lote do PI"**: o **"Produto Acabado"** herda o número de lote do **"Produto Intermediário"**.

**Obs.:** Se tiver mais de um Produto Intermediário na composição do Produto Acabado que use a configuração "**PA usa o mesmo lote do PI**", no momento de gerar a **Ordem de Produção**, o sistema apresentará uma mensagem de erro. Isto ocorre devido ao sistema não conseguir identificar qual destes PI's o PA herdará o lote. Portanto, apenas um PI poderá utilizar essa configuração.
