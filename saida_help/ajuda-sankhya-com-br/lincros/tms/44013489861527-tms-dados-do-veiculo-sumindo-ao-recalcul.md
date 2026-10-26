---
id: "44013489861527"
titulo: "[TMS] Dados do veículo sumindo ao recalcular, embarcar, ou integrar o embarque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013489861527--TMS-Dados-do-ve%C3%ADculo-sumindo-ao-recalcular-embarcar-ou-integrar-o-embarque"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T19:59:57Z"
rotulos: ["sync_hc", "lincros", "sync_hash_e4d208f63714", "lincros_13432090"]
---

# [TMS] Dados do veículo sumindo ao recalcular, embarcar, ou integrar o embarque

**Menu**: Operacional > Cargas > Embarques

**Objetivo**: Auxiliar na solução do cadastro do embarque, focando no cadastro de veículos.

**Considerações**: Dados do veículo estão sumindo ao recalcular, embarcar ou integrar o embarque, devido divergências no embarque.

Ao adicionar dados do veículo ao embarque e salvar, os mesmos ficam visíveis, porém ao realizar uma ação de recalcular, embarcar, ou integrar, os dados “somem” e não é concluída a ação.

**Por que ocorre este comportamento?**

O motivo deste comportamento está relacionado ao cadastro do veículo da transportadora, vinculada ao embarque, que possuem divergência em seu cadastro.

**Exemplo:** Filial da transportadora vinculada ao embarque difere da filial vinculada ao cadastro do veículo, e por esse motivo que o comportamento de “sumir” ocorre.

## Como corrigir?

A correção é muito simples, basta seguir este passo a passo:

**1-** Clique no lápis ao lado do “veículo” que o cadastro deste será aberto.

![Imagem 1: A correção é muito simples, basta seguir este passo a passo: 1- Clique no lápis ao lado do “veículo” que o cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/44013527654423)

**2-** No cadastro do veículo, se já existir uma transportadora vinculada, basta clicar no X(vermelho) e desvincular

**3-** Depois clique em “Vincular a transportadora"

![Imagem 2: 3- Depois clique em “Vincular a transportadora"](https://ajuda.sankhya.com.br/hc/article_attachments/44013527781015)

**4-** Será aberta uma janela > clique na lupa

![Imagem 3: 4- Será aberta uma janela > clique na lupa](https://ajuda.sankhya.com.br/hc/article_attachments/44013490300951)

**5-** Será aberto o filtro de transportadoras, então use o filtro “Documento da Filial” e informe o CNPJ correspondente a filial da transportadora que está realizando o embarque.

![Imagem 4: 5- Será aberto o filtro de transportadoras, então use o filtro “Documento da Filial” e informe o CNPJ correspondente a…](https://ajuda.sankhya.com.br/hc/article_attachments/44013527978903)

**6-** Salve o cadastro.

**Conclusão:** Pronto, agora já pode realizar as ações necessárias no embarque.

**Observação:** Pode adicionar mais de uma transportadora ou filial ao registro de veículo.
