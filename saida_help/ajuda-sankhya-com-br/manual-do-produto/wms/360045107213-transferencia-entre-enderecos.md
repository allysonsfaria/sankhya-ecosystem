---
id: "360045107213"
titulo: "Transferência entre Endereços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107213-Transfer%C3%AAncia-entre-Endere%C3%A7os"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:15:07Z"
rotulos: ["AJUDA DO SKW", "manual", "WMS", "Parceiro", "br.com.sankhya.wms.rot.transferenciaenderecos", "Transferência entre Endereços manual", "Estoque", "Endereços", "Transferência", "Transferência entre Endereços no WMS"]
---

# Transferência entre Endereços

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311550675223) Módulo: WMS > Rotinas
```

---

Através desta tela, você pode selecionar um produto de um determinado endereço e transferi-lo para outro endereço devidamente configurado, sendo que, este processo leva em consideração a quantidade informada do produto e a sua compatibilidade com o tamanho do endereço destinatário.

A movimentação entre endereços, possibilita que a equipe de controle de estoque efetue alterações no layout do armazém de maneira rápida e simples.

![Imagem 2: A movimentação entre endereços, possibilita que a equipe de controle de estoque efetue alterações no layout do armazém…](https://ajuda.sankhya.com.br/hc/article_attachments/360085320414)

Por meio do Painel de Filtros, você tem disponível alguns fitros que poderão auxiliá-lo na procura de determinado produto. Dentre os disponíveis na tela, temos o filtro **"Parceiro"**, para que você possa filtrar aqueles Parceiros que utilizam o [Controle de Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros) na rotina.

As transferências serão permitidas entre os seguintes endereços:

- Entre endereços de Armazenagem;
- Endereço de origem Armazenagem e destino Armazenagem, Avaria e Garantia;
- Endereço de origem Avaria para destino Armazenagem e Garantia;
- Endereço de origem Garantia para o destino Armazenagem e Avaria.

Na coluna **"Qtd. a Transferir"**, será preenchida a quantidade que se deseja transferir e, na coluna **"End. Destino"**, informe o endereço de destino.

Deste modo, é possível visualizar na coluna **"% de ocupação destino"** se o endereço de destino irá comportar esta quantidade. Caso o endereço se encontre totalmente ocupado ou a quantidade informada extrapole o tamanho do mesmo, o seu percentual será apresentado em 100%; negando-se assim, a transferência.

Ao clicar no botão ![Imagem 3: Ao clicar no botão "Gerar Transferências" , teremos o processamento das transferências configuradas de acordo com as…](https://ajuda.sankhya.com.br/hc/article_attachments/16925473973911) **"Gerar Transferências"**, teremos o processamento das transferências configuradas de acordo com as quantidades e destinos informados.

**Observação:** quando movimentações de transferências forem realizadas por meio das telas [Registro de Avarias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120333-Registro-de-Avarias), [Remanejamento de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612894-Remanejamento-de-Estoque) ou pela tela Transferência entre Endereços, ao realizar a execução da tarefa, você deverá informar a **"Data de Validade"** e/ou **"Data de Fabricação"** do produto que será movimentado. Dessa forma, o sistema irá validar se as datas informadas constam no endereço de origem da tarefa.

**Nota:** quando você tentar transferir um produto para outro endereço e ele não suportar a quantidade ou peso que você deseja, o sistema emitirá a mensagem abaixo:

[GIF animado: Imagem 4: Nota: quando você tentar transferir um produto para outro endereço e ele não suportar a quantidade ou peso que você…](https://ajuda.sankhya.com.br/hc/article_attachments/360103355513)

**Observação:** caso você tente realizar uma transferência entre endereços, e o endereço de destino estiver marcada como **"Lote Único"** (tela [Endereços de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral)), será possível realizar a transferências se ambos os endereços possuírem o mesmo produto e lote. Assim, a transferência não poderá acontecer entre endereços de lotes distintos, pois eles não podem ser alocados no mesmo endereço. O mesmo ocorrerá para [Remanejamento de Estoques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612894).
