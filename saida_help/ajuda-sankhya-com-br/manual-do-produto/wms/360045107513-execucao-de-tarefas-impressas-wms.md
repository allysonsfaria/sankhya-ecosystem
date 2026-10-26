---
id: "360045107513"
titulo: "Execução de Tarefas Impressas WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107513-Execu%C3%A7%C3%A3o-de-Tarefas-Impressas-WMS"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:15:16Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Impressão", "Relatórios Formatados", "WMS", "br.com.sankhya.execucaodetarefasimpressaswms", "Execução de Tarefas Impressas WMS manual", "Estoque", "Armazenamento expedição transferência etc", "Navegar atualizar gerar cancelar iniciar finalizar modelos", "Configurar relatórios exigir início de mapa"]
---

# Execução de Tarefas Impressas WMS

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311578944279) Módulo: WMS > Rotinas
```

---

Esta tela possibilitará a impressão de mapas para execução de tarefas de forma manual, sem o uso de coletores.

Você poderá realizar através desta rotina a execução das seguintes tarefas:

- Armazenamento;
- Expedição;
- Expedição Balcão;
- Transferência;
- Reabastecimento;
- Retorno da expedição, ou;
- Todas conjuntamente.

**Nota:** o processo de conferência será realizado no formato padrão, através de emuladores.

Trataremos abaixo sobre os seguintes tópicos:

[Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107513-Execu%C3%A7%C3%A3o-de-Tarefas-Impressas-WMS#bot%C3%B5esdatela)                                                    [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107513-Execu%C3%A7%C3%A3o-de-Tarefas-Impressas-WMS#par%C3%A2metrosqueinfluenciamnestarotina)

## Botões da tela

A tela de Execução de Tarefas Impressas WMS é composta por botões que executam diversas funções dentro desta rotina, são eles:

![Imagem 2: - Anterior e Próximo: Temos aqui, os botões de navegação entre as tarefas já executadas.](https://ajuda.sankhya.com.br/hc/article_attachments/16845129040279) - **Anterior e Próximo:** Temos aqui, os botões de navegação entre as tarefas já executadas.

- **Atualizar:** Ao acionar este botão, será recarregado toda a tela de Execução de Tarefas Impressas WMS.

![Imagem 3: - Gerar Mapa: Através deste botão, será registrado o "Nro. Mapa" para o item da tarefa, bem como será gerado o modelo…](https://ajuda.sankhya.com.br/hc/article_attachments/16845129052183) - **Gerar Mapa:**Através deste botão, será registrado o **"Nro. Mapa"** para o item da tarefa, bem como será gerado o modelo de mapa da tarefa.

**Observação:** caso a tarefa em questão possua dependência em outra tarefa, não será gerado o mapa; desta forma, você deve primeiramente resolver a dependência para, posteriormente, realizar a geração do mesmo.

![Imagem 4: - Cancelar Mapa: Em relação a este botão, quando for acionado, ele cancelará o registro que foi gerado o mapa, porém,…](https://ajuda.sankhya.com.br/hc/article_attachments/16845177069719) - **Cancelar Mapa:** Em relação a este botão, quando for acionado, ele cancelará o registro que foi gerado o mapa, porém, que ainda não foi iniciado/finalizado o mapa para a tarefa.

![Imagem 5: - Início Mapa: Ao clicar neste botão , será registrado o início do mapa da tarefa.](https://ajuda.sankhya.com.br/hc/article_attachments/16845173642903) - **Início Mapa:** Ao clicar neste botão, será registrado o início do mapa da tarefa.

**Nota:** selecionando o botão acima, será exibido um pop-up solicitando o Nro. Mapa e o **"Executante"**.

![Imagem 6: - Cancela Execução do Mapa: este botão retornara o mapa para "Aberto" quando o mesmo estiver com a situação "Em…](https://ajuda.sankhya.com.br/hc/article_attachments/16919945978519) - **Cancela Execução do Mapa:** este botão retornara o mapa para **"Aberto"** quando o mesmo estiver com a situação **"Em Execução"**.

![Imagem 7: - Será realizado o registro da finalização da execução do mapa da tarefa ao acionar o botão "Finaliza Mapa" .](https://ajuda.sankhya.com.br/hc/article_attachments/16919980089623) - Será realizado o registro da finalização da execução do mapa da tarefa ao acionar o botão **"Finaliza Mapa"**.

**Observação:** ao acionar o botão acima mencionado, será aberto um pop-up para se informar o Executante, bem como o **"Endereço de Checkout"**, sendo que este último tem seu preenchimento obrigatório apenas quando a tarefa for de **"Expedição"**.

![Imagem 8: - Temos ainda o botão "Modelos de Impressões" , onde você poderá encontrar os modelos de relatórios de impressão (…](https://ajuda.sankhya.com.br/hc/article_attachments/16920044150935) - Temos ainda o botão **"Modelos de Impressões"**, onde você poderá encontrar os modelos de relatórios de impressão (\*.jrxml) das tarefas para serem baixadas.

**Importante:** para todos os Tipos de Tarefas, os procedimentos de Gerar, Cancelar, Iniciar e Finalizar o mapa serão os mesmos.

**Observação:** ainda será possível selecionar as tarefas e realizar a geração de mapas em grupo para cada tarefa, sendo que estas terão o mesmo Nro. Mapa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107513-Execu%C3%A7%C3%A3o-de-Tarefas-Impressas-WMS#top)

## Parâmetros que influenciam nesta rotina

**Exige início mapa WMS? - EXIGEINIMAPA:** este parâmetro está vinculado ao botão Início Mapa. Desta forma, quando o parâmetro estiver desabilitado, tem-se que o botão informado não será exibido na tela Execução de Tarefas Impressas WMS.

Para que seja possível realizar a geração/impressão dos mapas de Armazenamento, Transferência, Reabastecimento e Expedição, é necessário que os parâmetros abaixo estejam devidamente configurados de acordo com os [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados):

- **Relatório p/ mapa de recebimento manual - RELMAPRECMAN;**
- **Relatório p/ mapa de transferência manual - RELMAPTRAMAN;**
- **Relatório p/ mapa de reabastecimento manual - RELMAPREAMAN;**
- **Relatório p/ mapa de separação manual - RELMAPSEPMAN.**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107513-Execu%C3%A7%C3%A3o-de-Tarefas-Impressas-WMS#top)
