---
id: "360044607514"
titulo: "Tela Geração ISS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607514-Tela-Gera%C3%A7%C3%A3o-ISS"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Escrituração dos livros"
atualizado_em: "2026-09-28T11:49:26Z"
rotulos: ["AJUDA DO SKW", "manual", "ISS", "Geração", "Notas", "Livros Fiscais", "Impostos", "Financeiro", "Canceladas", "Redução Z", "Aquisições", "Geração ISS", "Prestações", "zerado", "br.com.sankhya.mgeliv.mov.geracaoiss", "Geração ISS manual", "NFS-e", "EFD Contribuições", "Alimenta tabela TGFLIS; filtra por \"Data Inicial\" e \"Data Final\"", "\"Gerar Agora\" \"Consultar Nota Não Gerada\" \"Agendamento\"", "Ações (Notas Canceladas Financeiro Redução Z) e Filtros (Aquisições Prestações)"]
---

# Tela Geração ISS

**Módulo:** Livros Fiscais › Arquivos

**Caminho de acesso:** Menu Principal › Livros Fiscais › Arquivos › Geração ISS

## O que é e para que serve

A **Tela Geração ISS** gera, no módulo Livros Fiscais, as notas fiscais de serviço confirmadas e/ou autorizadas — no caso da Nota Fiscal de Serviços Eletrônica (NFS-e). A geração alimenta a tabela `TGFLIS` e deixa as notas disponíveis para as demais funcionalidades do Sankhya Om: o **Relatório Livro ISS** (em construção) e a **EFD Contribuições** (Escrituração Fiscal Digital), bloco A.

A tela não permite consultar nem ajustar os lançamentos já gerados. Para isso, acesse [Cadastro Livro ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608394-Cadastro-Livro-ISS).

---

## Configuração da geração

Antes de gerar, defina a empresa, o período e os conjuntos de dados que entram no livro.

### Empresa e período

- **Empresa** e **Empresa Destinatária** — informe a empresa pela qual as notas foram emitidas.
- **Data Inicial** e **Data Final** — definem o período em que o sistema filtra as notas para a geração.
- **Número Único** — informe para gerar uma única nota. O sistema busca apenas o documento correspondente à numeração indicada.

### Seção Ações

Marque os conjuntos de dados das notas que serão gerados:

- **Gerar Notas** — gera todas as informações das notas dentro do período estabelecido.
- **Gerar Canceladas** — considera apenas as notas canceladas dentro do período definido.
- **Gerar Financeiro** — considera apenas o financeiro das notas contidas no período estabelecido.
- **Gerar Redução Z** — gera os fechamentos fiscais diários do Emissor de Cupom Fiscal (ECF), que trabalha com base em movimentações diárias.

### Seção Filtros

Defina qual operação será considerada na geração. Você pode marcar uma ou as duas opções:

- **Aquisições** — considera apenas os serviços adquiridos (entrada).
- **Prestações** — busca os serviços fornecidos (saída).

---

## Botões da tela

Com a empresa, o período e as seções configurados, use os botões para gerar o livro, consultar notas que ficaram de fora ou agendar a geração.

### Geração

#### Gerar Agora

**O que faz**

O botão **Gerar Agora** gera no Livro de ISS as informações das notas de serviço, conforme a empresa, o período e as seções Ações e Filtros definidos.

**Quando usar**

Use depois de definir as configurações da geração.

**Como funciona**

1. O sistema busca as notas que têm pelo menos um item de serviço e que atendem às regras para serem geradas no livro.
2. Em seguida, com a marcação **Gerar notas com ISS zerado** habilitada, o sistema também busca as notas configuradas para ir ao livro, mesmo sem item de serviço. As notas que ainda não foram geradas vão para o livro com apenas um item e com os campos **Base**, **Alíquota** e **Valor ISS** zerados.

Com o parâmetro `LIVISSPAGINADO` habilitado, o botão dispara a geração em segundo plano. Para saber mais, acesse [Geração paginada do Livro de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607514-Tela-Gera%C3%A7%C3%A3o-ISS#paginada).

**Configurações relacionadas**

| **Necessidade** | **Onde configurar** |
| --- | --- |
| Gerar o livro em lotes, em segundo plano | Parâmetro `LIVISSPAGINADO` |
| Gerar notas sem item de serviço | Marcação **Gerar notas com ISS zerado** |

### Consulta e agendamento

- **Agendamento** — abre a tela [**Geração ISS Agendamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento).

#### Consultar Nota Não Gerada

**O que faz**

O botão **Consultar Nota Não Gerada** abre o pop-up **Consultar Nota Não Gerada**, que permite consultar uma nota que não foi gerada no Livro de ISS.

**Quando usar**

Use quando uma nota esperada não aparecer no livro após a geração.

**Como funciona**

No pop-up, busque a nota por:

- **Nro. único**
- **Chave NFe\CTe**
- **Nro. Nota**
- **Série**
- **Data de Negociação**
- **Empresa**

Os campos **Série**, **Data de Negociação** e **Empresa** só são habilitados para preenchimento depois que o campo **Nro. Nota** é informado.

**💡 Dica**

Para ver as causas mais comuns de uma nota não ir para o livro, acesse [Nota de Serviço não está sendo gerada no livro de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053292233-Nota-de-Servi%C3%A7o-n%C3%A3o-est%C3%A1-sendo-gerada-no-livro-de-ISS).

---

## Geração paginada do Livro de ISS

Disponível a partir da versão 4.36.

Em bases com grande volume de notas de serviço, você pode executar a geração do Livro de ISS de forma paginada. Nesse modo, o sistema divide as notas em páginas e grava os lançamentos em lotes, em vez de processar toda a competência em uma única transação. Isso evita o estouro de tempo limite nas gerações mais longas.

Para ativar, habilite o parâmetro `LIVISSPAGINADO`. Ele vem desabilitado por padrão; desabilitado, a geração continua em transação única, como antes. O tamanho da página é definido pelo parâmetro `LIVISSPAGTAM`, preenchido com `1000`. Na maioria dos cenários, esse valor não precisa ser alterado.

Com o parâmetro habilitado, a geração passa a ser executada em segundo plano. Ao clicar em **Gerar Agora**, o sistema abre a janela de acompanhamento do processo, onde você acompanha o andamento e pode cancelar a execução. Uma nova geração não é enfileirada enquanto houver outra em andamento para a mesma competência.

A paginação vale apenas para a geração das notas. As etapas de notas canceladas, financeiro e redução Z continuam sendo processadas em transação única.

**⚠️ Atenção**

No modo paginado, se a geração for interrompida por erro, os lançamentos já gravados permanecem no Livro. Antes de reexecutar a competência, confira o resultado da execução anterior. No modo padrão, uma falha desfaz todos os lançamentos.
