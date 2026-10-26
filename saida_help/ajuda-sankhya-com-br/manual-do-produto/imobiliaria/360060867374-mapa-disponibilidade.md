---
id: "360060867374"
titulo: "Mapa Disponibilidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360060867374-Mapa-Disponibilidade"
trilha: "Manual do Produto > Imobiliária > Imobiliária"
atualizado_em: "2026-07-29T14:11:39Z"
rotulos: ["Configuração", "Mapas", "br.com.sankhya.tim.rotinas.mapadisponibilidade", "Posicionamento pixels proposta", "Código mapa estágios", "Mapa lotes posições", "Loteamentos", "Imobiliária", "Prospecção"]
---

# Mapa Disponibilidade

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311416088087) Módulo: Imobiliária > Rotinas > Prospecção
![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311416089751) Versão disponível: a partir da 3.31
```

---

Esta tela tem a finalidade de apresentar, graficamente, os lotes vinculados a um loteamento, mostrando suas localizações no mapa informado para o loteamento e seus respectivos estágios.

![Imagem 3: Esta tela tem a finalidade de apresentar, graficamente, os lotes vinculados a um loteamento, mostrando suas…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002196562)

No campo **"Loteamento"**, informe o código do [Loteamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609354) que você deseja visualizar.

O botão **"Atualizar Mapa"** atualiza todo o mapa, incluindo suas definições de tamanho para os marcadores e a imagem utilizada.

Já o botão **"Atualizar Lotes"**, quando acionado, irá atualizar as informações de posicionamento, disponibilidade e valor, podendo alterar a legenda do lote conforme os dados atualizados.

**Observação:** ao lado desse botão é apresentada a data da última atualização da tela, seja do mapa completo ou apenas dos lotes. Essa informação é importante pois, as informações podem ser atualizadas tanto pelos botões que citei acima, quanto automaticamente, conforme tiver sido definido no parâmetro **"Delay para atualizar lotes Mapa Disponib. -** **TIMDELMDISP"**.

A imagem carregada nessa tela, que será utilizada para marcar os lotes, é obtida no repositório de arquivos, na pasta definida no parâmetro **"Pasta para mapa do loteamento - TIMPMAPLOT"**, na subpasta que tem o nome do código do loteamento, ou seja, o caminho a ser informado no parâmetro deve estar dentro do repositório, como exemplo: C:\Repositorio\mapa de disponibilidade\1; assim, no parâmetro TIMPMAPLOT você informará "mapa de disponibilidade".

**Nota:** o arquivo deve estar nomeado como **"mapa.jpg"**.

O botão **"Editar"** permite posicionar os lotes em seus lugares corretos, clicando no lote e em sua posição de destino. A cada alteração de posicionamento, os campos **"LTEX"** e **"LTEY"** são atualizados com as posições em pixels dos lotes no mapa. Uma vez finalizados os apontamentos, clique em **"Sair"** para finalizar o processo.

**Observação:** ao clicar no marcador do lote, você será direcionado para a tela [Apresentação de Lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117353), para que você realize uma proposta, com o código do lote já informado.
