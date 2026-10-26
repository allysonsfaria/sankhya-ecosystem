---
id: "360044595094"
titulo: "Apuração de Divergências de ICMS-ST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Ressarcimento e complementação"
atualizado_em: "2026-09-15T17:22:29Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "NF-e", "XML", "Apuração de Divergências de ICMS-ST manual", "ICMS", "Impostos", "Estoque", "br.com.sankhya.mgeliv.ApuracaoDivergenciaICMSST", "Comparação de valores ICMS-ST", "Detalhes da apuração", "Preferências e opções adicionais"]
---

# Apuração de Divergências de ICMS-ST

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312919014935) Módulo: Livros Fiscais > Avançado > Rastreamento de Estoque/ST
```

---

Através desta rotina, será possível comparar os valores de ICMS-ST registrado nos itens, com os valores que são calculados no sistema.

**Observação:** os valores exibidos nesta tela terão em seu cálculo a proporcionalização de frete, seguro, embalagens e etc, de acordo com as configurações realizadas nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Despesas Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias).

**Nota:** esta rotina possui relação com a marcação **"Apura a Divergência de ICMS-ST"** da tela [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), [botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#botooutrasopes...), opção **"Preferências para importação de NF-e"**. Sendo assim, caso a marcação estiver selecionada, ao processar completamente um arquivo XML de NF-e de Compra que contenha diferença de impostos e o usuário tiver selecionado no campo **"Usar impostos"** a opção **"Usar Impostos do Arquivo"** (tela Portal de Importação de XML, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#divergnciasdeimpostos)), a rotina irá popular em paralelo, de modo assíncrono, a rotina de Apuração de Divergência de ICMS-ST.

| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#painelprincipal) |  | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#abageral) |
| --- | --- | --- |
| [Aba Itens da Apuração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#abaitensdaapurao) |  | [Botão Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#botopreferncias) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#botooutrasopes) |  |  |

## Painel Principal

O Painel Principal  que está em destaque, reúne as informações pertinentes às Divergências de ICMS-ST.

![Imagem 2: O Painel Principal que está em destaque, reúne as informações pertinentes às Divergências de ICMS-ST .](https://ajuda.sankhya.com.br/hc/article_attachments/5874911483031)

No campo "**Nro. Único Nota"** insira o número único da nota que gerou a Apuração de Divergência de ICMS-ST.

No campo **"Nro. Nota"** será inserido o número da nota que gerou a Apuração de Divergência de ICMS-ST.

O campo **"Número do financeiro"** será preenchido com o número único do financeiro que representa a guia GARE.

Em relação ao campo **"Dt. Neg"** tem-se que este será preenchido com a data de negociação da nota que gerou a Apuração de Divergência de ICMS-ST.

O **"Status"** atual da Apuração de Divergência de ICMS-ST será preenchido como **"Pendente"** ou **"Liberada"**.

A marcação **"Digitado"** será habilitada quando os valores de Substituição Tributária forem alteradas manualmente pelo usuário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#top)

## Aba Geral

![Imagem 3: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/5874953466007)

Nesta aba temos os campos:

A **"Base substituição Calculada"** será preenchida com a base de cálculo de ICMS-ST automaticamente pelo sistema.

O sistema preencherá o campo **"Vlr. substituição Calculada"** com o valor de ICMS-ST.

Preenche-se o campo **"Base substituição Nota"** com a base de cálculo de ICMS-ST registrada na nota.

O valor de ICMS-ST registrado na nota será informado no campo **"Vlr. substituição Nota"**.

No campo **"Vlr. Divergência de ICMS ST"** será informado o valor da diferença de ICMS-ST sobre o calculado e o registrado no sistema, variando conforme as configurações realizadas no pop-up **"Preferências"**, que será exibido ao acionar o botão Preferências localizado no topo da tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#top)

## Aba Itens da Apuração

![Imagem 4: Aba Itens da Apuração](https://ajuda.sankhya.com.br/hc/article_attachments/5874977891607)

Esta aba compreenderá os dados que dizem respeito aos Itens da Apuração de Divergências de ICMS-ST, conforme explicado abaixo:

No campo **"Sequência"** deve-se inserir a sequência que foi registrada no item.

Preencha o campo **"Produto"** com o código do produto referente ao item registrado.

O campo **"Tributação"** será preenchido automaticamente com o código de tributação registrado no item após salvar o registro dos Itens de Apuração.

Informe no campo **"Base substituição Calculada"** a base de cálculo de ICMS-ST na simulação efetuada pelo sistema.

O valor de ICMS-ST deverá ser inserido no campo **"Vlr. substituição Calculada"**.

A base de cálculo de ICMS-ST registrada no item será exibida no campo **"Base substituição Item"**.

O campo **"Vlr. substituição Item"** será preenchido com o valor de ICMS-ST registrado no item.

A marcação **"Digitado"** será habilitada quando os valores de Substituição Tributária forem alterados de forma manual.

Será possível visualizar nos campos **"Base ICMS Calculada"**, **"Vlr. ICMS Calculada"**, **"Base ICMS Item"**, **"Vlr. ICMS Item"** e **"Cód. Alíq. ICMS"** os valores de ICMS da Nota recalculada de forma centralizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#top)

## Botão Preferências

O botão **"Preferências"** está localizado no topo da tela, ao acioná-lo será aberto o pop-up a seguir:

![Imagem 5: O botão "Preferências" está localizado no topo da tela, a o acioná-lo será aberto o pop-up a seguir:](https://ajuda.sankhya.com.br/hc/article_attachments/5875079821207)

A marcação **"Gerar Financeiro ao Liberar"** quando habilitada possibilitará realizar a geração do financeiro após a liberação da Apuração de Divergência de ICMS-ST.

Quando for efetuada a marcação **"Recalcular Financeiro"** será possível excluir o financeiro da apuração antes de gerá-lo. Caso contrário, será exibida uma mensagem que já existe financeiro para a apuração em questão.

A marcação **"Apenas sem Cálc."** é responsável por enviar valor ao campo **"Vlr. Divergência de ICMS ST"** apenas se o sistema tiver gerado valor de Substituição Tributária e não tiver sido registrado no item.

Informe a operação a ser utilizada na geração do financeiro no campo **"Tipo de Operação"**.

No campo **"Tipo de Título"** insira qual o título utilizado na geração do financeiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#top)

## Botão Outras Opções...

O botão **"Outras Opções..."** é acionado por meio do ícone ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15509128650391) localizado no alto da tela, possuindo as seguintes funcionalidades:

![Imagem 7: O botão "Outras Opções..." é acionado por meio do ícone localizado no alto da tela, possuindo as seguintes…](https://ajuda.sankhya.com.br/hc/article_attachments/5875144517655)

**Gerar Guia do Financeiro:** Quando selecionada efetuará a geração da Guia do Financeiro - GARE, de acordo com o valor registrado no campo **"Vlr. Divergência de ICMS ST"** da aba Geral.

**Marcar como Liberado:** Ao acionar esta opção será liberado o registro de Apuração de Divergência de ICMS-ST caso o usuário possua permissão de liberação no [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos).

**Processar Apuração:** Esta opção irá carregar e apurar as notas de compra já confirmadas. Na execução desta, será apresentado um pop-up para que sejam apresentadas as notas e o usuário possa selecionar quais destas serão efetuadas a geração da Divergência de Apuração.

![Imagem 8: Processar Apuração: Esta opção irá carregar e apurar as notas de compra já confirmadas. Na execução desta, será…](https://ajuda.sankhya.com.br/hc/article_attachments/5875256720663)

**Observação:**no pop-up, após selecionar as notas desejadas, aciona-se o botão Processar; assim, será exibida a mensagem de que o processo de criação das Apurações de Divergência de ICMS-ST foi finalizado com sucesso.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094-Apura%C3%A7%C3%A3o-de-Diverg%C3%AAncias-de-ICMS-ST#top)
