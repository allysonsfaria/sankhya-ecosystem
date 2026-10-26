---
id: "360045119253"
titulo: "Fila de Operações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119253-Fila-de-Opera%C3%A7%C3%B5es"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:55:53Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Centro de Trabalho", "Ordens de Produção", "Produção", "Fila de Operações", "br.com.sankhya.prod.filaoperacoeswc", "Fila de Operações manual", "Em execução planejadas não planejadas", "Definir Centro de Trabalho OP Plano Produto", "Mover Cancelar Salvar Alterar CT Histórico Folga"]
---

# Fila de Operações

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312833034647) Módulo: Produção > Rotinas
```

---

O objetivo desta tela é exibir a Fila de Atividades condizente com um **"Centro de Trabalho"**, **"Ordem de Produção"**, **"Plano Mestre de Produção"** e/ou **"Produto Acabado".** Referente aos Centros de Trabalho, estes possuem uma espécie de Fila de Execução correspondente às atividades de Ordens de Produção que estão sendo executadas ou serão executadas no Centro de Trabalho. Essas atividades podem ser classificadas em três grupos, sendo estes:

- **Atividades em execução:** se referem às atividades de ordens que estão em execução, naquele momento no Centro de Trabalho;
- **Atividades planejadas:** correspondem às atividades de ordens originadas de um planejamento de produção, que foram programadas para serem executadas em algum momento no Centro de Trabalho;
- **Atividades não planejadas:** diz respeito às atividades de ordens lançadas manualmente e sem programação, mas com definição para serem executadas no Centro de Trabalho.

O passo inicial para apresentação das informações pertinentes às operações na tela, é a definição de um Centro de Trabalho, **"Ordem de Produção"**, **"Plano Mestre de Produção"** e **"Produto Acabado"** para filtragem das suas respectivas atividades.

![Imagem 2: O passo inicial para apresentação das informações pertinentes às operações na tela, é a definição de um Centro de…](https://ajuda.sankhya.com.br/hc/article_attachments/9907504356631)

Deste modo, o operador responsável por executar as tarefas de um determinado Centro de Trabalho tem a necessidade de visualizar sua Fila de Execuções com objetivo de ter ciência sobre qual a ordem de execução das tarefas alocadas para ele, assim como executar possíveis alterações na ordem de execução em consequência de algum tipo de imprevisto que possa acontecer no dia a dia.

Na grade de resultados da Fila de Operações, temos a coluna **"Saldo a Produzir"**, que apresentará a diferença entre o **"Tam. Lote"** e a soma dos apontamentos parciais, incluindo as perdas, exibindo o mesmo valor que o campo Saldo a Produzir da tela [Ordens de Produção - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova#h_01ER0B3Q52ETZXJKM4PSCEXFYZ).

**Observação:** se não houverem apontamentos parciais no momento da consulta, o campo Saldo a Produzir apresentará o mesmo valor previsto, ou seja, o valor igual ao campo Tam. Lote.

A coluna **"Status OP"** da grade exibe o status da OP relacionada à atividade listada.

## Botões do topo da tela

![Imagem 3: Mover: estes botões são responsáveis por realizar a ordenação das atividades correspondentes ao Centro de Trabalho…](https://ajuda.sankhya.com.br/hc/article_attachments/15526769515927) **Mover:** estes botões são responsáveis por realizar a ordenação das atividades correspondentes ao Centro de Trabalho indicado. Ao selecionar a linha desejada, você pode movimentá-la para cima ou para baixo, respectivamente, definindo a ordem de execução das atividades.

![Imagem 4: Cancelar: este botão é responsável por anular as modificações que foram realizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/15526821909655) **Cancelar:** este botão é responsável por anular as modificações que foram realizadas.

![Imagem 5: Salvar: de forma contrária ao botão anterior, este realiza a gravação das alterações efetuadas.](https://ajuda.sankhya.com.br/hc/article_attachments/15526821913751) **Salvar:** de forma contrária ao botão anterior, este realiza a gravação das alterações efetuadas.

![alterar](https://ajuda.sankhya.com.br/hc/article_attachments/15526821915287) **Alterar CT:** por meio deste botão, realize a modificação do Centro de Trabalho, de modo a serem exibidas suas respectivas atividades na Fila de Operações.

![HISTÓRICO](https://ajuda.sankhya.com.br/hc/article_attachments/15526844512535) **Histórico Execuções:** através desse botão você poderá verificar o histórico de execuções por centro de trabalho de ordens em andamento e/ou finalizadas. Ao acioná-lo, será apresentada a tela abaixo: 

![Imagem 8: Histórico Execuções: através desse botão você poderá verificar o histórico de execuções por centro de trabalho de…](https://ajuda.sankhya.com.br/hc/article_attachments/9907647034135)

![INDICADOR](https://ajuda.sankhya.com.br/hc/article_attachments/15526821919895) **Indicador de folga:** este botão ao ser acionado, apresenta o pop-up **"Preferências"**:

![Imagem 10: Indicador de folga: este botão ao ser acionado, apresenta o pop-up "Preferências" :](https://ajuda.sankhya.com.br/hc/article_attachments/1500014840642)

Neste pop-up determine, inicialmente, o tempo (em minutos) de atualização automática dos registros, ou seja, o intervalo de tempo em que a grade será recarregada, de modo que, se for inserido o tempo **"0"** (zero), a tela não será atualizada automaticamente; essa atualização automática irá ocorrer apenas se for inserido um tempo diferente de zero.

É importante entendermos dois conceitos:

**Folga:** é um indicador utilizado para identificar se existe uma margem para iniciar a atividade, com base na **"Data/hora Início Previsto"** calculado pelo sistema considerando a execução das atividades. O cálculo será:

- **Atividades em execução: "Data/hora** **atual"** subtraída da **"Data/hora Final Prevista"** (resultado em minutos);
- **Atividades que não estão em execução:** Data/hora atual subtraída da Data/hora Início Prevista (resultado também em minutos).

**Folga Programação:** trata-se de um indicador de folga em relação a programação realizada para aquela atividade. Será feita a subtração entre a Data/hora Início Previsto e a **"Data/hora Início Programada"** (resultado em minutos). Este indicador é utilizado para identificação da existência de folga entre o início previsto e o início planejado da atividade, levando em consideração o ritmo de trabalho do Centro de Trabalho.

Diante disto, determine nas abas **"Folga"** e **"Folga Prog."** os tempos em minutos para indicador de cada uma das folgas, considerando as colorações possíveis, ou seja:

-Folga menor que "X minutos";

-Folga menor que "Y minutos";

-Folga maior ou igual a 180 minutos.

**![Imagem 11: Configurar grade: ao ser acionado apresenta um pop-up denominado "Configuração da Grade" que permite a estruturação das…](https://ajuda.sankhya.com.br/hc/article_attachments/16649182913815) Configurar grade:** ao ser acionado apresenta um pop-up denominado **"Configuração da Grade"**  que permite a estruturação das colunas que compõem a tela.

**![Imagem 12: Exportar grade para PDF: este botão possibilita a extração dos dados presentes na grade para outros formatos. São eles:](https://ajuda.sankhya.com.br/hc/article_attachments/16649182918423) Exportar grade para PDF:** este botão possibilita a extração dos dados presentes na grade para outros formatos. São eles:

- Exportar para PDF;
- Exportar para planilha;
- Exportar para cubo.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119253-Fila-de-Opera%C3%A7%C3%B5es#top)
