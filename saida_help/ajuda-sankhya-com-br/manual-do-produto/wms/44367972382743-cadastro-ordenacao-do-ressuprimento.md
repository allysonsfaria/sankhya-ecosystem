---
id: "44367972382743"
titulo: "Cadastro Ordenação do Ressuprimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-10-19T20:38:48Z"
---

# Cadastro Ordenação do Ressuprimento

**Caminho de acesso:** Menu Principal › Configurações › Cadastros › Empresas › aba **WMS** › botão **Configurar Critério de Ressuprimento**

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#o-que-%C3%A9-e-para-que-serve) [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#antes-de-come%C3%A7ar)    ↳ [Se o botão não aparecer](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#se-o-bot%C3%A3o-n%C3%A3o-aparecer) [Como configurar o critério](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#como-configurar-o-crit%C3%A9rio)    ↳ [A validade vem sempre primeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#a-validade-vem-sempre-primeiro)    ↳ [Cálculo da proximidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#c%C3%A1lculo-da-proximidade) | [Quando o critério não é aplicado](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#quando-o-crit%C3%A9rio-n%C3%A3o-%C3%A9-aplicado) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#pontos-de-aten%C3%A7%C3%A3o) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#perguntas-frequentes) |
| --- | --- |

## O que é e para que serve

O **Cadastro Ordenação do Ressuprimento** permite que cada empresa defina o critério que o WMS usa para escolher de qual pulmão tirar o estoque ao gerar uma tarefa de ressuprimento: o pulmão com mais estoque, o com menos estoque ou o mais próximo do endereço de picking. Ele serve para quem precisa adequar essa escolha ao layout do armazém ou à estratégia de armazenagem, por exemplo para reduzir o deslocamento do operador ou consumir primeiro as sobras. Ele não altera as regras de elegibilidade já existentes (validade, bloqueio, quarentena e endereços de exceção) nem o disparo do ressuprimento: muda só a ordem de escolha entre as origens que já são elegíveis.

**ℹ️ Nota**

A aba **WMS** fica na tela **Preferências da Empresa**. Esta configuração está disponível a partir da versão 5.15.0 do módulo WMS.

## Antes de começar

Os dois parâmetros do módulo WMS a seguir precisam estar configurados assim:

| **Parâmetro** | **Valor** |
| --- | --- |
| Habilita nova rotina de ressuprimento (`HABNOVORESSUP`) | **Ligado** |
| Estratégia de busca antiga por estoque com dt.val (`WMSBUSCAESTVALA`) | **Desligado** |

**⚠️ Atenção**

O parâmetro `HABNOVORESSUP` vem desligado de fábrica. Sem ele ligado, o sistema ignora a configuração feita nesta tela, sem exibir aviso. Depois de ligar, limpe o cache e feche e reabra a tela (ou saia e entre de novo no Sankhya Om). Só limpar o cache pode não atualizar uma tela que já estava aberta.

### Se o botão não aparecer

O botão **Configurar Critério de Ressuprimento** vem configurado para aparecer na aba **WMS**, no grupo **Configurações Gerais**. Se ele não estiver visível, confira:

- Se a versão do módulo WMS é 5.15.0 ou superior
- Se o cache foi limpo e a tela foi fechada e reaberta
- Se o seu perfil de acesso tem permissão para o botão
- Se a tela **Preferências da Empresa** foi personalizada na sua base: nesse caso, os campos novos de uma atualização não entram no layout automaticamente e ficam em **Campos disponíveis**

Para adicionar o botão a uma tela personalizada:

1. Na tela **Preferências da Empresa**, abra a **Configuração da Tela**.
2. Selecione a aba **WMS**.
3. Em **Campos disponíveis**, busque **Configurar Critério de Ressuprimento**.
4. Mova o campo para a aba e clique em **Salvar**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#sumario)

## Como configurar o critério

Clique no botão **Configurar Critério de Ressuprimento** e arraste os critérios para colocá-los na ordem que você quer:

- **Maior Estoque** — prioriza o pulmão com mais saldo. Use para gerar menos tarefas e resolver o ressuprimento de uma vez.
- **Menor Estoque** — prioriza o pulmão com menos saldo. Use para consumir sobras e liberar endereços.
- **Origem por Proximidade** — prioriza o pulmão mais próximo do picking. Use para reduzir o deslocamento do operador.

A ordem define a prioridade: o primeiro critério decide a origem e, se houver empate, o sistema aplica o próximo. Você pode usar de 1 a 3 critérios.

**ℹ️ Nota**

**Maior Estoque** e **Menor Estoque** avaliam o mesmo saldo em sentidos opostos. Se você usar os dois, só vale o que estiver primeiro na sequência.

### A validade vem sempre primeiro

Quando o produto tem controle de validade, por FEFO (primeiro que vence, primeiro que sai) ou FIFO (primeiro que entra, primeiro que sai), a validade é sempre o primeiro critério. O critério configurado nesta tela só ordena os estoques elegíveis que restam depois dela.

### Cálculo da proximidade

**Origem por Proximidade** não mede distância em metros. O sistema calcula a diferença entre o campo **Ordem** do endereço de picking e o campo **Ordem** de cada pulmão, no cadastro do endereço, e considera mais perto o pulmão com a menor diferença.

| **Endereço** | **Ordem** | **Distância calculada até o picking** |
| --- | --- | --- |
| Picking | 100 | — |
| Pulmão A | 98 | 2 |
| Pulmão B | 130 | 30 |
| Pulmão C | 180 | 80 |

Se o campo **Ordem** dos endereços não refletir o caminho real do armazém, o resultado não fará sentido na prática. Isso é uma questão de cadastro: ajuste a **Ordem** em [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento) antes de usar este critério.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#sumario)

## Quando o critério não é aplicado

- Quando `INIBEREABMAXPICKING` está ligado, o sistema prioriza um pulmão que atenda toda a necessidade de uma vez, e o critério desta tela deixa de valer.
- No ressuprimento preventivo com `HABNOVORESSUP` desligado (rotina antiga), o critério é ignorado e vale o campo **Priorização de endereços de origem** da tela **Ressuprimento Preventivo**.

Com o critério ativo, ele substitui o campo **Priorização de endereços de origem** da tela [Ressuprimento Preventivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120193-Ressuprimento-Preventivo).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#sumario)

## Pontos de atenção

- A configuração vale para a empresa inteira. Não é possível defini-la por produto, curva ou armazém.
- Só pulmões elegíveis entram como origem. Endereços de exceção (avaria, perda, sobra, divergência, armazenagem indefinida, garantia e endereço flutuante) nunca entram.
- Uma alteração no critério vale só para as tarefas geradas depois dela. As tarefas que já existiam não mudam.
- Depois de alterar o critério, limpe o cache.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44367972382743-Cadastro-Ordena%C3%A7%C3%A3o-do-Ressuprimento#sumario)

## Perguntas frequentes

### Deu erro ao salvar a configuração. O que pode ser?

A configuração aceita só os critérios **Maior Estoque**, **Menor Estoque** e **Origem por Proximidade** e não pode ficar vazia. Confira se pelo menos um critério está na sequência.
