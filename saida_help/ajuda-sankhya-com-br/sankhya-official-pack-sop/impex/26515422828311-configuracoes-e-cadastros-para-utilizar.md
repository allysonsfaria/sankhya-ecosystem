---
id: "26515422828311"
titulo: "Configurações e cadastros para Utilizar o SOP ImpEx - Importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26515422828311-Configura%C3%A7%C3%B5es-e-cadastros-para-Utilizar-o-SOP-ImpEx-Importa%C3%A7%C3%A3o"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:41:41Z"
rotulos: ["Configuração", "br.com.sankhya.fin.cad.tipooperacao", "Importação", "br.com.sankhya.core.cad.projetos", "TOP", "br.com.sankhya.configuracao.importacao.ptax", "br.com.sankhya.core.cad.paises", "Financeiro", "Configurações e cadastros para Utilizar o SOP ImpEx - Importação", "ImpEx", "br.com.sankhya.comercioexterior.Incoterms", "br.com.sankhya.comercioexterior.AliquotaImportacao", "br.com.sankhya.core.cfg.Preferencias", "br.com.sankhya.os.cad.valoresMoedas", "Incoterms", "Comércio Exterior"]
---

# Configurações e cadastros para Utilizar o SOP ImpEx - Importação

Confira abaixo as configurações e cadastros básicos que precisam ser feitos para utilização do
SOP ImpEx na Importação.

## 1. Cadastro de TOP

Comercial > Arquivo > Cadastros / Financeiro > Arquivos > Cadastros

Para utilização do SOP Impex, é necessário realizar o cadastro de três TOPs, duas com tipo de movimento de O-Pedido de Compra e outra com tipo de movimento C-Compra.

Para cadastrar um TOP devem se seguir o manual abaixo:
[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)

Mas é preciso se atentar as informações cruciais para utilização do SOP Impex:

(1)** O - Pedido de Compra Nacionalização:**

- **Aba Geral**
  - **Financeiro:** não atualizar

- **Aba Financeiro**
  - **Operação em Moeda**

- **Aba Imposto**
  - **Cálculo de ICMS, IPI e ISS:** calcula e digita
  - **Tem ll**
  - **Tem Pis**
  - **Tem Cofins**
  - **Tem ICMS**
  - **Classificação ICMS: Revendedor**
  - **Tem IPI**

(1)** O - Pedido de Embarque:**

- **Aba Geral**
  - **Financeiro:** não atualizar

- **Aba Comércio Exterior**
  - **Gera importação:** essa opção tem que estar marcada na TOP que gera o processo de importação para o portal de importação;
  - **Pedido de Compra Importação:** essa opção tem que estar marcada na TOP que gera o processo de importação, pois com essa opção assinalada o sistema irá criar automaticamente o Follow-Up desse processo;
  - **Projeto Filho:** essa opção serve para que caso o usuário deseje criar um projeto para o Pedido de Compra de Nacionalização e um projeto diferente para o Pedido de embarque.

![Imagem 1: Projeto Filho: essa opção serve para que caso o usuário deseje criar um projeto para o Pedido de Compra de…](https://ajuda.sankhya.com.br/hc/article_attachments/26515434305815)

- **Aba Financeiro**
  - Operação em Moeda

- **Aba Impostos**
  - **Cálculo de ICMS, IPI e ISS:** calcula e digita
  - **Tem ll**
  - **Tem Pis**
  - **Tem Cofins**
  - **Tem ICMS**
  - **Classificação ICMS:** revendedor
  - **Tem IPI**

(1)** C - Compra**

- **Aba Geral**
  - Digitar informações sobre importação

- **Aba Financeiro**
  - Operação em Moeda

- **Aba Impostos**
  - **Cálculo de ICMS, IPI e ISS:** não Calcula e não digita
  - **Tem ll**
  - **Tem Pis**
  - **Tem Cofins**
  - **Tem ICMS**
  - **Tem IPI**

- **Aba Desp. Acessorias**
  - Nenhuma opção pode estar marcada, para que o sistema não calcule impostos proporcionais na nota de nacionalização.

![Imagem 2: Nenhuma opção pode estar marcada, para que o sistema não calcule impostos proporcionais na nota de nacionalização.](https://ajuda.sankhya.com.br/hc/article_attachments/26517298411287)

## 2. Cadastro de Incoterms

Comércio Exterior > Cadastros
O cadastro de Incoterms é necessário, por ser responsável pela padronização dos rateios das despesas e quais despesas aduaneiras podem incorrer naquele processo de importação.

**Exemplos de Incoterms:**

- **EXW — Ex Works:** na Origem (local de entrega nomeado);
- **FCA — Free Carrier:** Livre No Transportador (local de entrega nomeado);
- **FAS — Free Alongside Ship:** Livre Ao Lado Do Navio (porto de embarque nomeado);
- **FOB — Free On Board:** Livre A Bordo (porto de embarque nomeado);
- **CPT — Carriage Paid To:** Transporte Pago Até (local de destino nomeado);
- **CIP — Carriage And Insurance Paid To:** Transporte E Seguro Pagos Até (local de destino nomeado);
- **CFR — Cost And Freight:** Custo E Frete (porto de destino nomeado);
- **CIF — Cost Insurance And Freight:** Custo, Seguro E Frete (porto de destino nomeado);
- **DAP — Delivered At Place:** Entregue No Local (local de destino nomeado);
- **DPU — Delivered At Place Unloaded:** Entregue No Local Desembarcado (Local de destino nomeado);
- **DDP — Delivered Duty Paid:** Entregue Com Direitos Pagos (local de destino nomeado).

É necessário o levantamento dos Incoterms utilizados pelo cliente para cadastro.

No cabeçalho do Incoterm é necessário definir para cada grupo de despesas, qual critério de rateio o sistema deverá assumir quando o mesmo ser escolhido em um processo de importação para ser utilizado. Os rateios podem ser feitos por Valor ou Peso Líquido.

Os grupos de despesas são divididos conforme abaixo:
- Frete
- Seguro
- Taxa Siscomex
- AFRMM
- THC
- Outras Despesas
- Outros Sem ICMS
- VIr.ICMS ST

![Imagem 3: Os grupos de despesas são divididos conforme abaixo: - Frete - Seguro - Taxa Siscomex - AFRMM - THC - Outras Despesas -…](https://ajuda.sankhya.com.br/hc/article_attachments/26517275957399)

Além disso, é possível definir, conforme necessidade, quais informações relevantes serão inseridas automaticamente na observação da nota de nacionalização.
- Dt. Registro DI
- Declaração de Importação 
- Invoice
- Parceiro Importador
- Projeto
- Frete
- Seguro
- II
- COFINS
- Siscomex

![Imagem 4: Além disso, é possível definir, conforme necessidade, quais informações relevantes serão inseridas automaticamente na…](https://ajuda.sankhya.com.br/hc/article_attachments/26517298414359)

### 2.1 Aba Naturezas do Incoterms

Na aba **"Naturezas"**, você poderá realizar a configuração das Despesas Aduaneiras que podem ocorrer no processo de importação, tanto aquelas relacionadas à nota de nacionalização quanto às que não possuem ligação com ela. Além disso, será possível definir se essas despesas serão automaticamente geradas na movimentação financeira ou se precisarão ser inseridas manualmente, proporcionando maior controle e flexibilidade para o gerenciamento das operações de importação.

Configuração das Despesas Aduaneiras na Aba Naturezas:

#### **(1)** Sinal

O sinal sempre que se tratar de uma despesa deverá ser soma.

![Imagem 5: O sinal sempre que se tratar de uma despesa deverá ser soma.](https://ajuda.sankhya.com.br/hc/article_attachments/26517298421783)

#### **(1)** Natureza

Deverá buscar a natureza da Despesa, previamente já cadastrada em **“Natureza de Receitas e Despesas”**. Caso tenha alguma dúvida sobre o cadastro de Naturezas, acesse o artigo: [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas)

![Imagem 6: Deverá buscar a natureza da Despesa, previamente já cadastrada em “Natureza de Receitas e Despesas” . Caso tenha alguma…](https://ajuda.sankhya.com.br/hc/article_attachments/26517275961367)

#### **(1)** Opcional

Essa opção deverá ser marcada, caso o usuário queira que a despesa não seja apresentada na aba **“Despesas de Importação"** no **“Portal de Importação”.** Assim, se marcada, a despesa não é apresentada. E para ser incluída, deverá ser feita manualmente pelo usuário na aba Despesas de Importação no Portal de Importação.

![Imagem 7: Essa opção deverá ser marcada, caso o usuário queira que a despesa não seja apresentada na aba “Despesas de Importação"…](https://ajuda.sankhya.com.br/hc/article_attachments/26517298424343)

#### **(1)** Despesa Complementar

Essa opção deverá ser marcada, caso a despesa em questão seja uma despesa complementar do processo de importação, que deve ser levada para o custo mas não entra na nota de nacionalização. Pois, na simulação de Custo/Preço, do portal de importação, essa despesa entra para o cálculo.

![Imagem 8: Essa opção deverá ser marcada, caso a despesa em questão seja uma despesa complementar do processo de importação, que…](https://ajuda.sankhya.com.br/hc/article_attachments/26517275964823)

#### **(1)** Ligação com a Nota de Nacionalização:

Essa opção é definida para determinar se a despesa em questão terá relação com a nota fiscal de nacionalização ou se será apenas uma despesa complementar a ser somada ao custo. Existe uma regra para este campo, se for uma despesa que tenha ligação com a nota de nacionalização, deverá procurar o campo que representa e tenha o mesmo nome que a despesa.

**Exemplo:** despesa Frete Internacional, devera ser vinculada no campo Vlr.Frete.

![Imagem 9: Exemplo: despesa Frete Internacional, devera ser vinculada no campo Vlr.Frete.](https://ajuda.sankhya.com.br/hc/article_attachments/26517450895255)

Caso a despesa tenha ligação com a nota de nacionalização, mas não possua campo com o mesmo nome, deverá ser vinculada ao campo Vlr.Destaque.

**Exemplo:** Despesa Taxa Siscomex, deverá ser vinculado ao campo VIr.Destaque.

![Imagem 10: Exemplo: Despesa Taxa Siscomex, deverá ser vinculado ao campo VIr.Destaque.](https://ajuda.sankhya.com.br/hc/article_attachments/26517439480215)

#### **(1)** Receita/Despesa:

Neste campo deve-se indicar se trata de uma Despesa ou de uma Receita, por ser possível cadastrar Naturezas do tipo receita no Incoterms.

![Imagem 11: Neste campo deve-se indicar se trata de uma Despesa ou de uma Receita, por ser possível cadastrar Naturezas do tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/26517450901911)

#### **(1)** Provisão

Nesse campo é definido se, conforme a opção **“Gera Financeiro”**, estiver marcada, ao colocar valor dessa despesa o sistema irá gerar um financeiro como **“Provisão”**, caso ele esteja selecionado. Caso não esteja marcado, o sistema irá criar um financeiro “Real”.

![Imagem 12: Nesse campo é definido se, conforme a opção “Gera Financeiro” , estiver marcada, ao colocar valor dessa despesa o…](https://ajuda.sankhya.com.br/hc/article_attachments/26517675542423)

#### **(1)** Grupo de Naturezas

Nessa opção é definido qual critério de rateio o Grupo de Despesa deve seguir conforme definido no cabeçalho.

**Exemplo:** se definido no cabeçalho que, para o grupo de despesa frete, o rateio é feito por **“Peso”**, ao vincular a despesa ao grupo Frete, ela irá realizar o rateio da mesma pelo **“Peso líquido”.**

![Imagem 13: Exemplo: se definido no cabeçalho que, para o grupo de despesa frete, o rateio é feito por “Peso” , ao vincular a…](https://ajuda.sankhya.com.br/hc/article_attachments/26518174082711)

#### **(1)** Tipo de Operação

Deve selecionar qual TOP Financeiro o sistema deverá utilizar para criar a movimentação financeira.

![Imagem 14: Deve selecionar qual TOP Financeiro o sistema deverá utilizar para criar a movimentação financeira.](https://ajuda.sankhya.com.br/hc/article_attachments/26518174083863)

#### **(1)** Tipo de Título

Essa opção deverá vincular Tipo de Título padrão para ser utilizado nessa Despesa Aduaneira, para criação da movimentação financeira.

![Imagem 15: Essa opção deverá vincular Tipo de Título padrão para ser utilizado nessa Despesa Aduaneira, para criação da…](https://ajuda.sankhya.com.br/hc/article_attachments/26518186561815)

#### **(1)** Parceiro

Essa opção deverá vincular o parceiro padrão que deve ser utilizado para geração da movimentação financeira a partir da despesa de importação. Lembrando caso não tenha padrão deverá ser preenchido com parceiro “0”.

![Imagem 16: Essa opção deverá vincular o parceiro padrão que deve ser utilizado para geração da movimentação financeira a partir da…](https://ajuda.sankhya.com.br/hc/article_attachments/26518174087191)

#### **(1)** Gera Financeiro

Quando o usuário marca a opção **“Gera Financeiro”** e preenche valor na aba **“Despesas de Importação”**, na tela Portal de Importação, o sistema cria automaticamente a movimentação financeira, baseada nos campos acima preenchidos.

![Imagem 17: Quando o usuário marca a opção “Gera Financeiro” e preenche valor na aba “Despesas de Importação” , na tela Portal de…](https://ajuda.sankhya.com.br/hc/article_attachments/26518174088599)

#### **(1)**Conta Bancária

Nessa opção deverá ser selecionada uma conta bancária padrão já previamente cadastrada, em “Contas”. Para cadastrar uma Conta Bancária, siga o manual abaixo: [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)

![Imagem 18: Nessa opção deverá ser selecionada uma conta bancária padrão já previamente cadastrada, em “Contas”. Para cadastrar uma…](https://ajuda.sankhya.com.br/hc/article_attachments/26518275142935)

#### **(1)** Moeda

Nessa opção o Usuário deverá escolher a moeda padrão de lançamento da natureza de despesa de Importação. Já previamente cadastrada em **“Valores de moedas”.** Conforme o Item 8 desse manual:

![Imagem 19: Nessa opção o Usuário deverá escolher a moeda padrão de lançamento da natureza de despesa de Importação. Já previamente…](https://ajuda.sankhya.com.br/hc/article_attachments/26518471048983)

## 3. Alíquota de importação

Comércio Exterior > Cadastros

O cadastro de alíquota de Importação é necessário, pois é onde vinculamos as alíquotas dos impostos federais (Il, IPI, PIS, COFINS), os CSTs, pelo NCM, Empresa e Cód. Exc NCM. E sendo possível criar suas variações conforme a necessidade do cliente ou legislação.

#### **(1)**Descrição

Nesse campo deverá inserir a descrição de identificação de qual regra se trata. Por se tratar de um campo texto livre o usuário precisará inserir uma descrição mais objetiva e informativa. 

![Imagem 20: Nesse campo deverá inserir a descrição de identificação de qual regra se trata. Por se tratar de um campo texto livre o…](https://ajuda.sankhya.com.br/hc/article_attachments/26518471050647)

#### **(1)** Empresa

Nesse campo deverá ser apontada para qual empresa a regra cadastrada pertence, pois o sistema buscará a regra conforme a empresa que é vinculada ao processo de importação.

![Imagem 21: Nesse campo deverá ser apontada para qual empresa a regra cadastrada pertence, pois o sistema buscará a regra conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/26518569923735)

#### **(1)** Cod. Fiscal NCM

Deverá informar o código NCM que pertence a essa regra. Pois, através do NCM, o sistema irá fazer o vínculo das alíquotas com os produtos registrados neste NCM.

![Imagem 22: Deverá informar o código NCM que pertence a essa regra. Pois, através do NCM, o sistema irá fazer o vínculo das…](https://ajuda.sankhya.com.br/hc/article_attachments/26733459971991)

#### **(1)**Cod. Exceção NCM

Esse campo é utilizado para criar códigos de exceção das alíquotas de importação, ele é utilizado para criar variações de tributações para o mesmo NCM, conforme Ex Tarifário, acordos nacionais ou identificar grupo de produtos específicos do mesmo NCM com tributações diferentes.
**Importante:** conforme o artigo ["Saiba como preencher a tag <EXTIPI> no XML"](https://ajuda.sankhya.com.br/hc/pt-br/articles/12468307616151-Saiba-como-preencher-a-tag-EXTIPI-no-XML), para que o Sankhya gere a TAG <EXTIPI> é necessário que o cliente informe no cadastro do produto qual Cód. Exceção de NCM o mesmo está vinculado, baseado no cadastro das alíquotas de importação. 

![Imagem 23: Esse campo é utilizado para criar códigos de exceção das alíquotas de importação, ele é utilizado para criar variações…](https://ajuda.sankhya.com.br/hc/article_attachments/26518573217559)

### 3.1 Aba Geral

Nessa aba deverão ser informadas as Alíquotas dos Impostos e os CSTs dos mesmos.

**(1)** **Alíquotade ll**

Deverá ser informada a alíquota de Imposto de Importação (ll), que será utilizada no processo de importação, conforme o cabeçalho da "Alíquotas de Importação".

(1)** Alíquota de IPI**

Deverá ser informada a alíquota de IPI que será utilizada no processo de importação, conforme o cabeçalho da "Alíquotas de Importação".

(1)** Cód. Eng. Legal IPI Entrada**

Deverá ser informado o Cód. Eng. Legal IPI conforme a tabela de vínculo com o CST de IPI.

(1)** Cód. Sit. Trib. IPI**

Deverá ser informado Cód. Sit. Trib. IPI (CST IPI) conforme a classificação de operação do produto.

(1)** Alíquota de PIS**

Deverá ser informada a alíquota de PIS que será utilizada no processo de importação, conforme o cabeçalho da "Alíquotas de Importação".

**(1)** **Cód. Sit. Trib. PIS**

Deverá ser informado Cód. Sit. Trib. PIS (CST PIS) conforme a classificação de operação do produto.

(1)** Alíquota de COFINS**

Deverá ser informada a alíquota de COFINS que será utilizada no processo de importação, conforme o cabeçalho da "Alíquotas de Importação".

(1)** Cód. Sit. Trib. COFINS**

Deverá ser informado Cód. Sit. Trib. COFINS (CST COFINS) conforme a classificação de operação do produto.

(1)** Alíquota de PIS Créd.**

Essa opção deverá ser preenchida com a Alíquota de Crédito de PIS, caso ao nacionalizar os produtos pertencentes a essa regra, tenha geração de crédito de imposto.

(1)** Alíquota de COFINS Créd.**

Essa opção deverá ser preenchida com a Alíquota de Crédito de COFINS, caso ao nacionalizar os produtos pertencentes a essa regra, tenha geração de crédito de imposto.

### 3.2 Aba Exceções/TOP

Nessa aba deverão ser informados as Alíquotas dos Impostos de importação (I, IPI, PIS, COFINS) e os  seus respectivos Cód. Tributários (CSTs), vinculados a TOP de Pedido de embarque. Na qual o usuário poderá criar uma regra em que além da Empresa, NCM e Cód. Exceção NCM, será analisado qual a TOP o Pedido de Embarque está sendo lançado para buscar as alíquotas dos Impostos de Importação. Criando, assim, a possibilidade de gerar regras pelo Tipo de Operação.

**Observação:** a regra de preenchimento segue a mesma da aba geral.

![Imagem 24: Observação: a regra de preenchimento segue a mesma da aba geral.](https://ajuda.sankhya.com.br/hc/article_attachments/26748923242775)

**![Imagem 25: Alerta: Nas configurações de alíquota de importação por TOP, não é possível cadastrar mais de uma regra para mesma TOP,…](https://ajuda.sankhya.com.br/hc/article_attachments/26748886400791) Alerta:** Nas configurações de alíquota de importação por TOP, não é possível cadastrar mais de uma regra para mesma TOP, com os mesmos critérios de Empresa, NCM e Código de Exceção NCM.

### 3.3 Aba Exceções/Produto

Nessa aba deverão ser informadas as Alíquotas dos Impostos de importação (I, IPI, PIS, COFINS) e os seus respectivos Cód. Tributários (CSTs), e Dt. Fim da Vigência da Aliq. e Dt. Inicio da Vigência da Aliq. Vinculado ao produto. Na qual o usuário poderá criar uma regra em que além da Empresa, NCM e Cód. Exceção NCM, será analisado qual o produto está sendo lançado para buscar as alíquotas dos Impostos de Importação. Criando, assim, a possibilidade de gerar regras por produtos vinculados ao mesmo NCM.

**Observação:** a regra de preenchimento segue a mesma da aba geral.

![Imagem 26: Observação: a regra de preenchimento segue a mesma da aba geral.](https://ajuda.sankhya.com.br/hc/article_attachments/30034847096471)

**Alerta:** nas configurações de alíquota de importação por produtos não é possível cadastrar mais de uma regra para o mesmo produto, com os mesmos critérios de Empresa, NCM e Código de Exceção NCM.

## 4. Cadastro de Países

Configurações >> Cadastros >> Endereços >> Países
No cadastro de Países deve constar no campo de **“País Domicilio Fiscal”** o código com os **"4 números que constam na Tabela de Código de Países do BACEN".**
Segue abaixo um exemplo de cadastro de País:

![Imagem 27: Configurações >> Cadastros >> Endereços >> Países No cadastro de Países deve constar no campo de “País Domicilio…](https://ajuda.sankhya.com.br/hc/article_attachments/26748923251095)

## 5. Cadastro de Estados

Configurações >> Cadastros >> Endereços >> Estados
Para cada País cadastrado deve ter um Estado também cadastrado no sistema, onde na sigla de todos eles deve constar EX e no campo “Código IBGE” informar os 3 primeiros números do código do País da tabela do BACEN. 
Estado referente ao Pais Cadastrado:

![Imagem 28: Configurações >> Cadastros >> Endereços >> Estados Para cada País cadastrado deve ter um Estado também cadastrado no…](https://ajuda.sankhya.com.br/hc/article_attachments/26749168796183)

## 6. Cadastro de Cidades

Configurações » Cadastros » Endereços » Cidades
As cidades deverão ser cadastradas na tela Configurações » Cadastros » Endereços »Cidades e associadas ao estado cadastrado anteriormente. No campo Código Mun. Domicílio Fiscal deverá ser informado '9999999'. Uma sugestão seria a criação de uma Cidade para Cada País não necessitando cidades  estrangeiras diversas no sistema.

![Imagem 29: Configurações » Cadastros » Endereços » Cidades As cidades deverão ser cadastradas na tela Configurações » Cadastros »…](https://ajuda.sankhya.com.br/hc/article_attachments/26749168803991)

## 7. Cadastro de Parceiros

Configurações » Cadastros » Parceiros
Os parceiros deverão ser cadastrados obedecendo os seguintes parâmetros, informando os campos CNPJ = 00.000.000/0000-00, I.E = "Vazia" e Classificação I.E = "Vazia" e Classificação ICMS = Revendedor.

**Nota:** Se o parâmetro **"Aceita CGC/CPF repetido?-ACEITACGCREPET"** estiver ligado, será permitido o cadastro de mais de um parceiro com mesmo CNPJ/CPF. O contrário ocorre, caso o referido parâmetro esteja desativado.

Uma das regras do parâmetro ACEITACGCREPET é que, caso esteja desligado, será permitido cadastrar apenas um parceiro por CNPJ/ CPF. Porém, mesmo que ele esteja desligado e o parceiro **seja cadastrado com uma cidade ou unidade federativa do exterior**, o sistema permitirá a ação. Só não permitirá o cadastro de mais de um parceiro por CNPJ quando for do Brasil.

Um parceiro pode ser encaixado em diversos perfis, porém, no campo "Perfil Principal"  é possível definir um que o caracterize com mais expressividade, evidenciando também seu ramo de atuação.

Informe no campo **"Insc. Estadual/ Identidade”**, caso o Parceiro seja Pessoa Física, seu **"RG"** (Registro Geral) e caso seja Pessoa Jurídica, sua **"Inscrição Estadual"** referente ao local onde ele está estabelecido.

**Observação:** O campo Inscr. Estadual/ Identidade será de preenchimento obrigatório, apenas se o parâmetro **"Aceita Insc. Est. de Parceiro em branco? - ACEITAIEBRANCO"** estiver desligado. Atente-se para o parâmetro **"Código do País Brasil - CODPAISBRASIL"**, pois, se este for diferente de "0" ou "55" (este último, Código do Brasil), o sistema irá ignorar esses parâmetros.

## 8. Cadastro de Parceiros

Configurações » Cadastros » Valores de Moedas
Para realizar o cadastro de moedas é importante seguir o manual: [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754-Valores-de-Moedas)

![Imagem 30: Configurações » Cadastros » Valores de Moedas Para realizar o cadastro de moedas é importante seguir o manual: Valores…](https://ajuda.sankhya.com.br/hc/article_attachments/26761414928407)

![Imagem 31: Configurações » Cadastros » Valores de Moedas Para realizar o cadastro de moedas é importante seguir o manual: Valores…](https://ajuda.sankhya.com.br/hc/article_attachments/26761414946711)

### 8.1 Configuração de PTAX

Configurações >> Avançado >> Configuração para Importação PTAX
Acionar o botão **“Importar Agora”** e configurar e-mail para notificação caso de algum problema nas importações. As cotações aparecerão na tela **"Valores Moedas"** na aba de **"Cotação de Moeda"**. É importante saber que o Banco Central do Brasil libera o PTAX contendo os valores de moedas após as 13h10min de cada dia. Portanto, caso ocorra um agendamento antes desse horário, a atualização não será efetuada, sendo necessário realizar um novo agendamento.

Qualquer dúvida sobre o funcionamento da tela, confira o artigo: [Configuração para Importação PTAX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX).

![Imagem 32: Qualquer dúvida sobre o funcionamento da tela, confira o artigo: Configuração para Importação PTAX .](https://ajuda.sankhya.com.br/hc/article_attachments/26786334978583)

## 9. Cadastro de Naturezas de Receitas de Despesas

Configurações >> Cadastros >> Gerencial >> Natureza de Receitas e Despesas
As Naturezas de Receitas e Despesas são indispensáveis para o processo, pois deverão ser cadastradas nas Incoterms para as mesmas sofrerem o rateio devido conforme cada Incoterm configurado.

Levantar com o Cliente quais são as naturezas utilizadas por eles nas Operações de Importações e solicitar o cadastro das mesmas.

![Imagem 33: Levantar com o Cliente quais são as naturezas utilizadas por eles nas Operações de Importações e solicitar o cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/26786334980759)

![Imagem 34: Levantar com o Cliente quais são as naturezas utilizadas por eles nas Operações de Importações e solicitar o cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/26786334985751)

![Imagem 35: Levantar com o Cliente quais são as naturezas utilizadas por eles nas Operações de Importações e solicitar o cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/26786334990231)

## 10. Preferências

A partir da versão 4.12b272 os Parâmetros deverão seguir a seguinte configuração:

(1)** Parâmetros antigos:**
**IMPTAGEXCNOTNAC:** desligado
**PISCOFINSNACIO:** desligado
**SOMAIMPNFNAC:** desligado
**USAMGEIMPORT:** desligado
**VOUTNOTASEMICMS:** desligado
**VOUTITEMSEMICMS:** desligado, caso ICMS não vá para o valor destaque da nota
**DICMSDIFXMLNFE**: ligado
**CMX\_CONROUEFE:** ligado
**CMX\_CONICMSDIF:** ligado
**CMX\_ITEICMEFE:** ligado
**ACEITARVLRMEICM:** ligado

(1)** PS:** **Parâmetros válidos para composição de Nota de Nacionalização e comportamento dos impostos no DANFE:**

**SOMAICMSNFENAC**

- **Não se aplica:** não soma o ICMS ao total da Nota e não leva para o Valor Destaque;
- **Soma ICMS ao VIr Nota:** leva o ICMS somente para o Valor Total da Nota;
- **Soma ICMS ao vOutro do item no XML:** leva o ICMS para o valor destaque.

**SUMVLRIIOUTNOTA**

- **Não se Aplica:** valor do II fica no valor do produto;
- **Soma II ao vOutro do item no XML:** leva o valor do II para o Valor Destaque;
- **Soma II ao VIr Nota:** não leva o III para os itens somando apenas no total da NFE.

**SOMPISCOFNFENAC**

- **Soma PIS e COFINS ao vOutro do item no XML:** soma PIS e Cofins ao Valor Destaque;
- **Soma PIS e COFINS ao VIr Nota:** não leva o PIS e Cofins para o valor destaque, somente para o total da NFE.

**Outros Parâmetros importantes:**
**CUSTODEC:** decimais para custo. Informar de preferência 4 casas decimais;

**DECVLRMOEDA:** decimais p/ valores de Moeda. Informar de preferência 6 casas decimais;

**CODPAISBRASIL:** Código do País Brasil. Deverá ser informado o código 55;

**ACEITARVLRMEICM:** aceitar valor da nota menor que a base de ICMS. Ligado;

**DIVTOTQTDNFE:** divide VLRTOT do item pela QTDNEG no XML da NFE. Ligado;

**BH\_CALICMSDIFER:** aplica a redução de Base de cálculo do ICMS;

**BH\_ICMSDIFERIDO:** o mesmo deve ser ligado para o sistema calcular ICMS Diferido.

**CMX\_DECREDBASE:** número de casas decimais na aplicação de redução na alíquota de cálculo por dentro do ICMS de Importação.
