---
id: "360044613414"
titulo: "Conclusão de Tarefas por Cód. de Barras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613414-Conclus%C3%A3o-de-Tarefas-por-C%C3%B3d-de-Barras"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:14:53Z"
rotulos: ["AJUDA DO SKW", "manual", "Conferência", "WMS", "Código de Barras", "Separação", "Conclusão de Tarefas por Cód. de Barras", "br.com.sankhya.wms.conclusaotarefascodbarras", "Conclusão de Tarefas por Cód. de Barras manual", "Checkout", "Conclusão de tarefas usando código de barras", "Separação por Pedidos e por Produto", "Processo de conferência e expedição no WMS"]
---

# Conclusão de Tarefas por Cód. de Barras

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311559919895) Módulo: WMS > Rotinas
```

---

A conclusão da separação por esta rotina, é similar à rotina [Conclusão de Separação Manual](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613254), contudo, nesta rotina você irá concluir o processo por meio do código de barras impresso no mapa de separação:

![Imagem 2: A conclusão da separação por esta rotina, é similar à rotina Conclusão de Separação Manual , contudo, nesta rotina você…](https://ajuda.sankhya.com.br/hc/article_attachments/360094370374)

Na tela Conclusão de Tarefas por Cód.Barras informe:

![Imagem 3: Na tela Conclusão de Tarefas por Cód.Barras informe:](https://ajuda.sankhya.com.br/hc/article_attachments/360096652213)

**Endereço de Checkout:** Para concluir a separação **"Por Pedidos"**, será necessário informar o Endereço de Checkout, para onde a separação foi levada. Para concluir a separação **"Por Produto"**, informe no Endereço de Checkout a Doca para onde a separação foi levada. Desta forma, quando você clicar no botão **"Concluir tarefas"** o sistema substituirá o endereço indefinido, que localizava-se no destino da tarefa, pelo endereço que foi informado na tela.

**Observação:** na busca por um Endereço de Checkout, efetue sua procura informando seu código independente de sua máscara, ou seja, não é necessário digitar da mesma maneira que no cadastro. Considere o seguinte exemplo:

Ao possuir um cadastro com a máscara/código **"01.06.01.01"**, para pesquisá-lo, basta digitar **"01060101"** e o endereço correspondente será localizado no decorrer da rotina.

**Executante:** Informe neste campo, o usuário que concluirá a tarefa de separação.

**Separação:** Indique aqui, o código de barras impresso no mapa de separação.

Ao acionar o botão **"Concluir tarefa"**, será apresentada uma tela com as informações sobre a separação e, ao **"Confirmar"**, o sistema concluirá a separação e passará a situação da expedição para **"Aguardando conferência"**.

Assim, iniciando a separação manual da **"Ordem de Carga (OC)"**:

Pedidos que estejam Aguardando Conferência poderão ser conferidos tanto pelo Coletor de Dados quanto manualmente pela tela [Conferência Manual](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120293). Contudo, uma vez iniciado o processo, ele deverá ser concluído da mesma forma, ou seja, se a conferência for iniciada pelo Coletor de Dados, deverá ser concluída pelo mesmo; caso seja iniciada pela rotina de Conferência Manual deverá ser concluída por esta.

![Imagem 4: Pedidos que estejam Aguardando Conferência poderão ser conferidos tanto pelo Coletor de Dados quanto manualmente pela…](https://ajuda.sankhya.com.br/hc/article_attachments/360086267473)

No caso de a Conferência ser feita manualmente pelo Sankhya-Om, quando finalizada, deverá ser enviada para a doca pelo botão **"Enviar para a Doca..."**.

Quando a Conferência for feita em áreas de **"Não paletizados"**, você não deverá informar a **"Área de conferência"**.

Finalizada as rotinas de Conferência, a situação da expedição no WMS passará a ser **"Conferência Validada"** e, a partir deste momento, para conclusão do processo será necessário apenas realizar a liberação da doca.

Na utilização da rotina de Conclusão de Tarefas por Cód. de Barras, você pode trabalhar com variações de pesos nos produtos. Para maiores detalhes sobre esta funcionalidade, clique em [Controle por Peso Variável](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914).
