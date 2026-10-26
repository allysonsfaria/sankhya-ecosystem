---
id: "42950885649687"
titulo: "Manual Dhara Contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos"
trilha: "DHARA: Gestão de safra e de projetos no ERP > Manuais"
atualizado_em: "2026-09-29T14:46:46Z"
rotulos: ["dhara", "sync_hc", "dhara_Manuais/Manual_Dhara_Contratos.docx", "sync_hash_210b932b98cd"]
---

# Manual Dhara Contratos

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42950885854615)

**Dhara Contratos**

Manual de Ajuda do Add-on

Gestão de Contratos de Medição — Plataforma Sankhya

**Dhara Tecnologia**

Documento de ajuda • Uso do sistema e referência técnica

## Sumário

[Sumário 2](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417455)

[1. Visão Geral do Módulo 3](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417456)

[1.1 Principais recursos 3](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417457)

[1.2 Ciclo de status 3](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417458)

[2. Estrutura de Menu 4](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417459)

[3. Cadastros 5](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417460)

[3.1 Ocorrências do Contrato 5](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417461)

[3.2 Tabela de Precificação de Medições 5](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417462)

[4. Rotinas 6](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417463)

[4.1 Contratos de Medição 6](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417464)

[4.2 Apontamento de Medições 7](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417465)

[4.3 Faturamento de Contratos Medição 7](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417466)

[5. Conceitos e Regras de Negócio 9](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417467)

[5.1 Precificação (simples e por faixa) 9](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417468)

[5.2 Ocorrências e situação do produto 9](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417469)

[5.3 Somatórios e saldos 9](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417470)

[6. Apêndice Técnico — Dicionário de Dados 10](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417471)

[6.1 DH\_CONTRATOMED — Contrato de Medição (DhContratoMedicao) 10](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417472)

[6.2 DH\_CONTRATOPROD — Produtos/Serviços (DhProdutoServicoCont) 10](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417473)

[6.3 DH\_APONTAMENTO — Apontamentos de Medição (DhApontamentosMedicao) 10](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417474)

[6.4 Precificação 10](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417475)

[6.5 Ocorrências e Anexos 10](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417476)

[6.6 Views (consultas) 10](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417477)

[6.7 Extensões em entidades padrão do Sankhya 11](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417478)

[6.8 Componentes de servidor e regras 11](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417479)

[6.9 Observações técnicas 11](https://ajuda.sankhya.com.br/hc/pt-br/articles/42950885649687-Manual-Dhara-Contratos#_Toc234417480)

## 1. Visão Geral do Módulo

O add-on Dhara Contratos gerencia contratos de medição com faturamento periódico baseado em medições/apontamentos, de forma integrada ao ERP Sankhya. É indicado para contratos de prestação de serviços recorrentes cuja cobrança depende da quantidade efetivamente medida em cada período (por exemplo, serviços mensais medidos por volume, área, unidades executadas, etc.).

O ciclo de vida é encadeado: cadastra-se o Contrato de Medição e seus produtos/serviços; o sistema gera os Apontamentos mensais de cada produto ao longo da vigência; em cada período o usuário informa a quantidade medida (apontamento), que é precificada automaticamente; a medição é aprovada; e, por fim, os contratos com medições aprovadas são faturados, gerando as notas fiscais. A precificação pode ser por valor unitário simples ou por faixas de quantidade.

### 1.1 Principais recursos

- Cadastro de contratos de medição com produtos/serviços, natureza, centro de resultado e projeto.
- Geração automática dos apontamentos mensais por produto ao longo da vigência do contrato.
- Apontamento (medição) da quantidade por período, com precificação automática (simples ou por faixa).
- Aprovação das medições e faturamento em lote, gerando as notas fiscais.
- Precificação por tabela: valor unitário simples ou por faixas de quantidade.
- Ocorrências que alteram a situação do produto no contrato (ativo, suspenso, cancelado, bonificado).
- Controle de saldos: valor total do contrato, faturado e saldo a faturar, por contrato e por produto.
- Anexos do contrato e acompanhamento por views (medições, faturamento, notas, faixas).

### 1.2 Ciclo de status

Cada produto/apontamento percorre um ciclo de status que orienta as ações disponíveis:

| Status | Significado | Ação seguinte |
| --- | --- | --- |
| PA | Pendente de Apontamento | Informar a quantidade medida |
| AR | Apontamento Realizado | Aprovar a medição |
| VC | Valor Calculado (no produto do contrato) | — |
| MA | Medição Aprovada | Faturar |
| FT | Faturado | Concluído |

## 2. Estrutura de Menu

O add-on é acessado pelo menu Dhara Contratos, com um grupo de cadastros e três telas operacionais:

| Grupo | Item de menu | Tipo / Finalidade |
| --- | --- | --- |
| Cadastros Contratos | Ocorrências do Contrato | Formulário — tipos de ocorrência e situação associada |
| Cadastros Contratos | Tabela de Precificação de Medições | Formulário — tabelas de preço (simples ou por faixa) |
| (rotina) | Contratos de Medição | Tela — cadastro do contrato e geração de apontamentos |
| (rotina) | Apontamento de Medições | Tela — informar quantidade medida e aprovar |
| (rotina) | Faturamento de Contratos Medição | Tela — faturar medições aprovadas (gerar notas) |

## 3. Cadastros

### 3.1 Ocorrências do Contrato

Cadastro dos tipos de ocorrência que podem ser registrados nos produtos de um contrato. Cada ocorrência está associada a uma situação que será aplicada ao produto quando a ocorrência tiver efeito (por exemplo, suspender ou cancelar o item).

| Campo | Tipo | Chave/Obrig. | Descrição |
| --- | --- | --- | --- |
| CODIGO | Inteiro | PK (automático) | Código da ocorrência |
| DESCRICAO | Texto | Obrigatório | Descrição |
| SITUACAO | Lista | Obrigatório | Situação aplicada: A=Ativo, C=Cancelado, B=Bonificado, S=Suspenso |

### 3.2 Tabela de Precificação de Medições

Define como os produtos/serviços do contrato são precificados. Cada tabela tem um tipo de medição: preço unitário simples (um único valor por unidade) ou preço por faixa (o valor unitário varia conforme a quantidade). No preço por faixa, cadastram-se as faixas com a quantidade máxima ("até") e o valor unitário correspondente.

| Campo | Tipo | Chave/Obrig. | Descrição |
| --- | --- | --- | --- |
| CODIGO | Inteiro | PK (automático) | Número da tabela |
| DESCRICAO | Texto | — | Descrição da tabela |
| TIPOMEDICAO | Lista | Obrigatório | S=Preço Unitário Simples, F=Preço por Faixa |
| VLRUNIT | Decimal | — | Valor unitário (quando tipo Simples) |
| CODEMP / CODGRUPOPROD / CODPROD / CODPARC | Inteiro (FK) | — | Abrangência opcional (empresa, grupo, produto, parceiro) |
| ATIVO | Checkbox | — | Tabela ativa |

#### Faixas de Preço (quando tipo por Faixa)

| Campo | Tipo | Chave/Obrig. | Descrição |
| --- | --- | --- | --- |
| NUFAIXA | Inteiro | PK (automático) | Número da faixa |
| QTDFAIXA | Decimal | Obrigatório | Quantidade até (limite superior da faixa) |
| VLRUNIT | Decimal | Obrigatório | Valor unitário da faixa |

**Como a faixa é escolhida:** o sistema seleciona a menor faixa cuja "Quantidade até" é maior ou igual à quantidade medida/prevista, e aplica o valor unitário dessa faixa sobre toda a quantidade.

## 4. Rotinas

As três telas operacionais implementam o fluxo do módulo: cadastrar o contrato e gerar os apontamentos, medir/aprovar e faturar. Cada botão dispara um processamento no servidor; a seguir, a função de cada um vem acompanhada das regras de negócio aplicadas.

### 4.1 Contratos de Medição

Tela de cadastro e manutenção do contrato de medição. O cabeçalho identifica o contrato (empresa, parceiro, contato, natureza, centro de resultado, projeto, tipo de negociação, vigência e periodicidade) e a grade de Produtos/Serviços lista os itens contratados. A partir dela, o botão gera os apontamentos mensais dos produtos selecionados.

#### Campos do cabeçalho

| Campo | Tipo | Chave/Obrig. | Descrição |
| --- | --- | --- | --- |
| NUMCONTRATOMED | Inteiro | PK (automático) | Número do contrato |
| CODEMP / CODPARC / CODCONTATO | Inteiro (FK) | Obrigatório | Empresa, parceiro e contato |
| DTCONTRATO / DTFIMCONTR | Data | Início obrig. | Vigência do contrato (início e término) |
| CODNAT / CODCENCUS / CODPROJ | Inteiro (FK) | Nat./CR obrig. | Natureza, centro de resultado e projeto |
| CODTIPVENDA | Inteiro (FK) | Obrigatório | Tipo de negociação |
| PERIODICIDADE / REFULTFAT / REFPROXFAT | Lista/Data | — | Periodicidade (mensal) e referências de faturamento |
| VLRTOTALCONTR / VLRTOTALFAT / VLRSALDOFAT | Decimal | Calculado | Valor total, faturado e saldo a faturar |

#### Grade de Produtos/Serviços

| Campo | Tipo | Chave/Obrig. | Descrição |
| --- | --- | --- | --- |
| CODPROD | Inteiro (FK Produto) | PK | Produto/serviço do contrato |
| TIPOMEDICAO | Lista | — | S=Preço Unitário Simples, F=Preço por Faixa |
| CODTABPREC | Inteiro (FK Tabela) | — | Tabela de precificação |
| QTDPREVISTA | Decimal | Obrigatório | Quantidade prevista |
| VLRUNIT / VLRTOTAL | Decimal | Calc./— | Valor unitário (da tabela) e total contratado |
| VLRFATURADO / VLRSALDO | Decimal | Calculado | Valor faturado e saldo a faturar do item |
| SITUACAO | Lista | Calculado | A=Ativo, C=Cancelado, S=Suspenso, B=Bonificado |
| STATUS | Lista | Calculado | PA, AR, VC, MA, FT |

#### Botão e regras de negócio

| Botão | Função e regras de negócio |
| --- | --- |
| Gerar Apontamentos Medição | Cria os apontamentos mensais para os produtos selecionados, um por mês entre o início e o fim do contrato. Exige seleção ("Selecione pelo menos um produto na grade.") e confirma "Gerar apontamentos para N item(s)?". Só gera para produtos com situação Ativa — os demais retornam em "Produto Inativo! Apontamentos não gerados...". Não duplica meses já existentes ("...já possuem apontamentos para os meses deste contrato."). Os apontamentos nascem com status Pendente de Apontamento (PA). Sucesso: "Apontamentos gerados com sucesso!". |

**Regras do cabeçalho:** as datas de início e fim são obrigatórias ("As datas de início e fim do contrato são obrigatórias.") e a data de término não pode ser anterior à de início ("A data de término do contrato deve ser igual ou posterior à data de início."). O valor total do contrato é recalculado automaticamente somando os itens ativos.

### 4.2 Apontamento de Medições

Tela onde o usuário informa a quantidade efetivamente medida em cada apontamento gerado e aprova as medições. Os apontamentos não podem ser inseridos manualmente — apenas os gerados pela tela de contratos são editados. Ao informar a quantidade, o sistema calcula o valor automaticamente e avança o status.

#### Campos principais

| Campo | Tipo | Chave/Obrig. | Descrição |
| --- | --- | --- | --- |
| CODAPONT | Inteiro | PK (automático) | Número do apontamento |
| REFERENCIA | Data | Somente leitura | Referência (mês) para faturamento |
| NUMCONTRATOMED / CODPARC / CODPROD | Inteiro (FK) | Somente leitura | Contrato, parceiro e produto |
| TIPOMEDICAO / NUTABPREC | Lista/Inteiro | Somente leitura | Tipo de medição e tabela de preço |
| QUANTIDADE | Decimal | Editável | Quantidade medida (informada pelo usuário) |
| VLRUNIT / VLRCALCULADO | Decimal | Calculado | Valor unitário e valor calculado da medição |
| STATUS / ACAO | Lista | Calculado | Status (PA→AR→MA→FT) e ação sugerida |
| DTAPROVACAO / NUNOTA / DTFAT | Data/Inteiro | Calculado | Aprovação, nota e data de faturamento |

#### Botão e regras de negócio

| Botão | Função e regras de negócio |
| --- | --- |
| Aprovar Medição | Aprova os apontamentos selecionados, mudando o status para Medição Aprovada (MA) e a ação para Pronto para Faturar (PF), com data de aprovação. Exige seleção ("Selecione pelo menos um apontamento na grade.") e confirma "Deseja aprovar N registro(s)?". Só aprova apontamentos com status Apontamento Realizado (AR) — os demais retornam em "Apontamento com status diferente de 'Apontamento Realizado'! Aprovação não efetivada...". Sucesso: "Apontamento(s) aprovado(s) com sucesso!". |

**Precificação e status automáticos:** ao salvar a quantidade, o sistema calcula o valor conforme a tabela de precificação — no tipo Simples, quantidade × valor unitário; no tipo por Faixa, aplica o valor unitário da menor faixa que comporta a quantidade. Se a quantidade for maior que zero, o status passa automaticamente para Apontamento Realizado (AR); caso contrário, volta para Pendente (PA).

### 4.3 Faturamento de Contratos Medição

Tela que fatura, em lote, os contratos com medições aprovadas em uma referência, gerando as notas fiscais. Possui painel lateral com os filtros de busca e os parâmetros de faturamento; a grade central lista os contratos elegíveis (view de faturamento).

#### Filtros e parâmetros (painel lateral)

- Filtros de busca: Referência (obrigatória), Número do Contrato, Empresa e Parceiro.
- Parâmetros de faturamento: Tipo de Operação (TOP, obrigatória — apenas TOPs habilitadas para faturar medição), Data do Faturamento e Série.
- **Importante:** a grade só carrega registros depois que a TOP é informada ("Antes de carregar os registros, é necessário informar o Tipo de Operação (TOP).").

#### Botão e regras de negócio

| Botão | Função e regras de negócio |
| --- | --- |
| Faturar Selecionados | Gera a nota fiscal de cada contrato selecionado a partir das medições aprovadas da referência. Exige registros na grade e a TOP e a Data do Faturamento preenchidas ("Informe a TOP e a Data do Faturamento nos parâmetros laterais!"). Ao final, exibe um resumo com as notas geradas e os contratos não faturados (com o motivo). |

**Validações de elegibilidade (por contrato):** o contrato não pode já ter sido faturado na mesma referência ("Contrato já faturado para esta referência."); não pode haver medições já faturadas na referência ("Existem medições já faturadas nesta referência."); e todo item ativo do contrato precisa ter medição aprovada ("Item {produto} ativo sem medição aprovada na referência."). A TOP deve estar habilitada para faturar medição ("A TOP informada não está habilitada para faturamento de medições.").

**Efeitos do faturamento:** é gerada a nota (cabeçalho e itens a partir das medições aprovadas), vinculada ao contrato e à referência; as medições passam a Faturado (FT), gravando a nota e a data; e o contrato tem suas referências (último/próximo faturamento) e seus valores (total faturado, saldo a faturar, por item) atualizados.

## 5. Conceitos e Regras de Negócio

### 5.1 Precificação (simples e por faixa)

A precificação é definida pela tabela associada ao produto. No tipo Preço Unitário Simples, o valor é a quantidade multiplicada pelo valor unitário da tabela. No tipo Preço por Faixa, o sistema seleciona a menor faixa cuja quantidade máxima ("até") é maior ou igual à quantidade e aplica o valor unitário dessa faixa sobre toda a quantidade. Essa mesma lógica é usada tanto no valor previsto do item do contrato quanto no valor calculado do apontamento.

### 5.2 Ocorrências e situação do produto

As ocorrências registradas em um produto do contrato alteram a sua situação (ativo, suspenso, cancelado, bonificado), conforme a situação associada ao tipo de ocorrência. Ocorrências com data até hoje têm efeito imediato ao serem registradas; ocorrências futuras são aplicadas automaticamente por uma rotina diária (job) no dia correspondente. Regras: não é permitido registrar duas ocorrências para o mesmo contrato/produto na mesma data ("Já existe outra ocorrência para esse contrato/produto na mesma data."); e não se exclui ocorrência sem data ou com data anterior a hoje.

### 5.3 Somatórios e saldos

O valor total do contrato é a soma dos valores totais dos itens ativos. À medida que as notas são geradas no faturamento, o sistema atualiza o valor faturado e o saldo a faturar, tanto no contrato quanto em cada produto (saldo = valor contratado − faturado, nunca negativo).

## 6. Apêndice Técnico — Dicionário de Dados

Consolida a estrutura de dados do add-on: tabelas, views, extensões em entidades nativas e os componentes de servidor que aplicam as regras.

### 6.1 DH\_CONTRATOMED — Contrato de Medição (DhContratoMedicao)

Cabeçalho do contrato. PK NUMCONTRATOMED (automático). Campos principais: empresa, parceiro, contato, natureza, centro de resultado, projeto, tipo de negociação, vigência (data do contrato e término), periodicidade, referências de faturamento e os valores calculados (total do contrato, total faturado e saldo a faturar).

### 6.2 DH\_CONTRATOPROD — Produtos/Serviços (DhProdutoServicoCont)

Itens do contrato. PK NUMCONTRATOMED + CODPROD. Campos: tipo de medição, tabela de precificação, quantidade prevista, valor unitário, valor total contratado, valor faturado, saldo, situação (A/C/S/B) e status (PA/AR/VC/MA/FT).

### 6.3 DH\_APONTAMENTO — Apontamentos de Medição (DhApontamentosMedicao)

Apontamentos mensais. PK CODAPONT (automático). Campos: referência, contrato, parceiro, produto, tipo de medição, tabela, quantidade, unidade, valor unitário, valor calculado, status, ação, data de aprovação, nota e data de faturamento.

### 6.4 Precificação

| Tabela / Entidade | Finalidade | Campos principais |
| --- | --- | --- |
| DH\_TABPRECIFICA / DhTabPrecificaMedicoes | Tabela de precificação (simples ou por faixa) | CODIGO, DESCRICAO, TIPOMEDICAO, VLRUNIT, abrangência (empresa/grupo/produto/parceiro), ATIVO |
| DH\_TABPRECIFICAFX / DhPrecoFaixa | Faixas de preço | CODIGO, NUFAIXA, QTDFAIXA (até), VLRUNIT |

### 6.5 Ocorrências e Anexos

| Tabela / Entidade | Finalidade | Campos principais |
| --- | --- | --- |
| DH\_OCORCONTR / DhOcorrenciasContrato | Tipos de ocorrência e situação associada | CODIGO, DESCRICAO, SITUACAO |
| DH\_CONTRATOOCOR / DhOcorrenciaProdContrato | Ocorrências por produto do contrato | NUOCOR, NUMCONTRATOMED, CODPROD, DTOCORRENCIA, CODOCOR, DESCCOMP |
| DH\_CONTRATOANEXO / DhAnexoContrato | Anexos do contrato | SEQUENCIA, NUMCONTRATOMED, DESCRICAO, ARQUIVO |

### 6.6 Views (consultas)

| View / Entidade | Finalidade |
| --- | --- |
| VW\_DH\_APONTMEDICOES / VwDhApontMedicoes | Apontamentos de medição por contrato |
| VW\_DH\_CONTRATONOTAS / VwDhContratoNotas | Pedidos/notas vinculados ao contrato |
| VW\_DH\_FAT\_MED\_CONTRATOS / VwDhFaturamentoContrato | Contratos elegíveis a faturamento por referência |
| VW\_DH\_MEDICOES / VwDhMedicoes | Medições (quantidades apontadas) por contrato/produto |
| VW\_DH\_TABPRECIFICAFX / VwDhTabPrecificaFx | Faixas de preço por contrato/produto |

### 6.7 Extensões em entidades padrão do Sankhya

| Entidade padrão | Campos adicionados (DH\_\*) |
| --- | --- |
| CabecalhoNota (TGFCAB) | DH\_NUMCONTRATOMED (contrato vinculado à nota); DH\_REFFATCONTR (referência de faturamento da medição) |
| TipoOperacao (TGFTOP) | DH\_FATMED (TOP fatura medição? S/N) |

### 6.8 Componentes de servidor e regras

| Componente | Responsabilidade |
| --- | --- |
| GeraApontamentoContratoServiceSP | Gera os apontamentos mensais dos produtos do contrato. |
| AprovaApontMedicaoServiceSP | Aprova as medições (AR → MA). |
| FaturamentoContratoServiceSP | Valida elegibilidade e gera as notas de faturamento; atualiza saldos e referências. |
| SomatoriosApontMed (listener) | Calcula o valor da medição (simples/faixa) e avança o status do apontamento. |
| SomatoriosContratos (listener) | Calcula valor unitário/total do item e o valor total do contrato (itens ativos). |
| Ocorrencias (listener) | Aplica a situação do produto conforme a ocorrência e valida datas/duplicidade. |
| ValidaData (listener) | Valida as datas de vigência do contrato. |
| AtualizaSituacaoProdSP (job diário) | Aplica no dia as ocorrências agendadas para o futuro, atualizando a situação dos produtos. |

### 6.9 Observações técnicas

- Os apontamentos são gerados pela rotina de contratos e não podem ser inseridos manualmente; a quantidade medida é o único campo digitado, e a partir dela o valor e o status são automáticos.
- A situação do produto no contrato é governada pelas ocorrências (efeito imediato até hoje; efeito futuro aplicado pelo job diário).
- O faturamento usa apenas TOPs marcadas como "TOP Fatura Medição" e vincula a nota ao contrato e à referência, evitando faturamento em duplicidade.
- A visão de negócio deste manual foi baseada no código-fonte do add-on; o documento do Google Drive não pôde ser incorporado automaticamente por exigir autenticação.
