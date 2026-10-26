---
id: "42617290193943"
titulo: "Manual de Emissão do CIOT - Integradora Target"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42617290193943-Manual-de-Emiss%C3%A3o-do-CIOT-Integradora-Target"
trilha: "Sankhya Official Pack - SOP > SOP"
atualizado_em: "2026-09-08T11:28:10Z"
---

# Manual de Emissão do CIOT - Integradora Target

## 1. Visão geral

A Target é uma das integradoras homologadas pela ANTT para emissão de CIOT (Código Identificador da Operação de Transporte). Quando a integração está ativa, o SOP:

**1.** Cadastra/atualiza automaticamente o **transportador** (proprietário ANTT), o **motorista** e o **destinatário** na base da Target.

**2.** Consulta a situação do transportador na ANTT (RNTRC ativo e equiparação a TAC).

**3.** Envia a operação de transporte (viagem + valores + parcelas + veículos) e declara a operação, recebendo de volta o **número do CIOT**.

**4.** Opcionalmente compra o **vale-pedágio** no mesmo envio.

**5.** Grava o número do CIOT no afretamento e, quando o adiantamento é por cartão, baixa automaticamente o financeiro do adiantamento.

| **Importante:** o CIOT pela Target só é emitido quando o proprietário ANTT é **equiparado a TAC** (Transportador Autônomo de Cargas) e com RNTRC ativo. Isso é verificado on-line na ANTT no momento da emissão. |
| --- |

## Fluxo resumido

| # | Etapa | Onde |
| --- | --- | --- |
| 1 | Ativar a integração e informar credenciais | Configurações TMS, aba Target |
| 2 | Completar os cadastros de apoio | Parceiros, Cidades, Veículos, Composição, Produto, Rota |
| 3 | Registrar a viagem (origem, destino, veículo, motorista, proprietário ANTT, produto) | Viagem |
| 4 | Preencher o afretamento e confirmá-lo | Viagem, aba Afretamento > Pagamento |
| 5 | Emitir o contrato e receber o número do CIOT | Viagem, menu Target |
| 6 | Pagar o saldo depois de fechar a viagem | Fechamento de Viagem, menu Target |

## 2. Antes de começar

Providências fora do SOP:

| Item | Onde obter |
| --- | --- |
| Contrato ativo com a Target | Comercial Target |
| **Usuário** e **Senha** de acesso ao WebService | Suporte Target |
| Ambiente de homologação liberado (recomendado para testes) | Suporte Target |
| Tabela de **categorias de veículo** da Target | Documentação Target |
| Cartão de pedágio Target (se for usar pedágio Target) | Target |

## 3. Configuração inicial (feita uma vez)

### 3.1. Ativar a integração — tela Configurações TMS, aba Target

| Campo | O que informar |
| --- | --- |
| **Utiliza Pedágio/CIOT Target** | **Sim** — sem isso o menu **Target** não aparece na Viagem |
| **Usa Configuração por Empresa** | **Não** (padrão) ou **Sim** — veja 3.2 |
| **Usuário Target** | Usuário fornecido pela Target |
| **Senha Target** | Senha fornecida pela Target |
| **Ambiente** | **Homologação** durante os testes; **Produção** depois |
| **Imprimir XML no Log** | **Sim** só quando precisar diagnosticar erros (grava o XML enviado/recebido no log de integração) |
| **Parceiro Pag. Frete Target** | Parceiro que representa a Target — é gravado no afretamento como pagador do frete |

Ainda na aba **Target**, os dados usados na **baixa do financeiro do frete** (adiantamento pago por cartão):

| Campo | O que informar |
| --- | --- |
| **Tipo de Título** | Tipo de título usado na baixa do adiantamento |
| **Conta Bancária** | Conta bancária de saída do pagamento |
| **Tipo de Operação Baixa Target** | TOP de baixa do financeiro do frete |

E os dados usados na **baixa do financeiro do pedágio**:

| Campo | O que informar |
| --- | --- |
| **Tipo de Título Pedágio** | Tipo de título do pedágio |
| **Conta Bancária Pedágio** | Conta bancária de saída do pedágio |
| **Tipo Operação Baixa Pedágio** | TOP de baixa do pedágio |

| Se qualquer um desses seis campos ficar em branco, a emissão até acontece na Target, mas a baixa no financeiro falha e o usuário recebe aviso para baixar manualmente. |
| --- |

### 3.2. Configuração por empresa (multiempresa)

Se a operação usa **CNPJs diferentes com credenciais diferentes** na Target:

**1.** Em **Configurações TMS**, aba **Target**, marque **Usa Configuração por Empresa** = **Sim**.

**2.** Abra **TMS > Configurações > Configurações Empresas**.

**3.** Crie um registro **para cada empresa** que vai emitir CIOT e preencha a aba **Target** com os mesmos campos da tabela acima (Usuário, Senha, Ambiente, Tipo de Título, Conta Bancária, TOPs, Parceiro Pag. Frete Target).

| Com essa opção ligada, uma viagem de empresa sem registro cadastrado não emite CIOT — o sistema avisa que a empresa não foi configurada. |
| --- |

### 3.3. Categorias de Veículo Target

Abra **Categorias de Veículo Target** e cadastre as categorias conforme a tabela fornecida pela Target:

| Campo | Conteúdo |
| --- | --- |
| **Código Categoria** | Código numérico da categoria na Target |
| **Descrição** | Descrição de apoio (ex.: "Caminhão 3 eixos") |

Essa lista é usada depois na **Composição de Veículos** (item 4.6).

## 4. Cadastros que alimentam o CIOT

Os dados abaixo são lidos direto dos cadastros do ERP no momento da emissão. Cada ausência vira uma mensagem de bloqueio.

### 4.1. Parceiro — Proprietário ANTT (contratado)

É o dono do veículo / transportador contratado, informado na viagem.

**Dados principais**

| Campo | Obrigatório | Observação |
| --- | --- | --- |
| **CNPJ/CPF** | Sim | — |
| **Nº RNTRC** | Sim | Precisa estar **ativo** na ANTT |
| **Data de Nascimento / Fundação** | Sim | Pessoa física ou jurídica |
| **Razão Social** | Sim (PJ) | — |
| **Nome do Parceiro** | Sim | Em PF, é quebrado em nome e sobrenome |
| **Identidade / Inscrição Estadual** | Sim (PF) | Em PF é o **RG**, e deve conter **somente números** |
| **Órgão Emissor RG** | Recomendado (PF) | — |
| **Sexo** | Opcional | Sem preenchimento é enviado como "não informado" |

**Endereço** (todos obrigatórios)

| Campo | Observação |
| --- | --- |
| **Endereço** | — |
| **Número** | Somente números. Sem número, informe **0** |
| **Complemento** | Opcional |
| **Bairro** | — |
| **CEP** | — |
| **Cidade** | A cidade precisa ter o código IBGE preenchido (item 4.4) |

**Contato** (todos obrigatórios)

| Campo | Observação |
| --- | --- |
| **Telefone** | — |
| **Celular** | Preenchido no campo de fax/celular do cadastro |
| **E-mail** | — |

**Dados complementares (Pessoa Física)**

| Campo | Obrigatório |
| --- | --- |
| **Nº CNH** | Sim |
| **Categoria CNH** | Sim |
| **Vencimento CNH** | Sim |
| **Naturalidade** | Recomendado |
| **Nacionalidade** | Recomendado |

**Contatos (Pessoa Jurídica)**

Para PJ é obrigatório ter **ao menos um contato ativo** na aba de contatos, com:

- **Nome do contato**
- **Telefone**
- **Celular**
- **E-mail**

(Cargo, CPF e Data de nascimento do contato são opcionais.)

**Contas bancárias**

Se o pagamento (adiantamento ou saldo) for por **depósito em conta** e o favorecido for o **Contratado**, cadastre a conta na aba **Contas Bancárias** do parceiro (Banco, Agência, Dígito da Agência, Conta, Dígito da Conta, Tipo de Conta). No afretamento basta selecionar a sequência da conta.

### 4.2. Parceiro — Motorista

| Campo | Obrigatório | Observação |
| --- | --- | --- |
| **CPF** | Sim | — |
| **Nome do Parceiro** | Sim | — |
| **Data de Nascimento** | Sim | — |
| **Cidade** | Sim | Com código IBGE preenchido |
| **Número do endereço** | Sim | Somente números; **0** se não houver |
| **Nome do Pai** e **Nome da Mãe** | Recomendado | Enviados como "Não Informado" quando vazios |
| **Identidade (RG)**, **Órgão Emissor**, **Telefone**, **Celular**, **E-mail**, **Nacionalidade** | Opcionais | Enviados quando preenchidos |

| Os dados complementares do motorista precisam existir — sem o registro complementar a emissão é bloqueada. |
| --- |

### 4.3. Parceiros de Remetente / Destinatário

O destinatário da carga é cadastrado como **participante** na Target, com as mesmas exigências de endereço, telefone, celular e e-mail descritas em 4.1.

Origem e destino são resolvidos nesta ordem:

| Sentido | 1ª opção | 2ª opção | 3ª opção |
| --- | --- | --- | --- |
| **Origem** | Parceiro Coleta | Parceiro Remetente | Cidade Origem |
| **Destino** | Parceiro Entrega | Parceiro Destinatário | Cidade Destino |

Além disso, precisa existir **CT-e ou NFS-e na viagem** cujo remetente esteja na Cidade de Origem e cujo destinatário esteja na Cidade de Destino. Caso contrário o sistema não consegue identificar os participantes.

### 4.4. Cidades

Para toda cidade usada (parceiros, origem, destino):

| Campo | Uso |
| --- | --- |
| **Mun. domicílio fiscal** | Código IBGE do município — obrigatório |
| **Latitude** e **Longitude** | Usadas na localização da operação; se não estiverem no parceiro, são buscadas na cidade |

### 4.5. Veículos

| Campo | Obrigatório | Observação |
| --- | --- | --- |
| **Placa** | Sim | — |
| **RNTRC do veículo** | Sim | — |
| **Tipo de Rodado** | Sim | É de onde vem a **quantidade de eixos** |

No cadastro de **Tipo de Rodado**, o campo **Nro. de Eixos** precisa estar preenchido (valor entre 1 e 10). Sem isso a emissão é bloqueada com aviso de que não foi possível determinar a quantidade de eixos.

Isso vale para o cavalo **e para cada carreta** da composição.

### 4.6. Composição de Veículos

Abra **Composição de Veículos** e, para cada cavalo usado em viagens com CIOT Target:

| Campo | Observação |
| --- | --- |
| **Cavalo** | Veículo tração |
| **Carreta 1 / 2 / 3** | Implementos, quando houver — todos vão no CIOT com placa, RNTRC e eixos |
| **Categoria do Veículo Target** | Obrigatório — selecione uma das categorias cadastradas no item 3.3 |

| Sem composição cadastrada para o veículo da viagem, a emissão é bloqueada. |
| --- |

### 4.7. Produto predominante

No cadastro do produto informado como **Produto Principal** da viagem:

| Campo | Obrigatório |
| --- | --- |
| **Natureza do Produto Receita Federal** | Sim |
| **Tipo de Carga MDF-e** | Sim |

### 4.8. Rotas (necessário apenas para vale-pedágio)

Se o pedágio for comprado pela Target, a rota da viagem precisa estar vinculada a um roteiro da Target.

Na tela **Rotas**, aba **Target**, use o menu **Target**:

- **Consultar Roteiro** — lista os roteiros que a Target já tem entre a origem e o destino da rota. Escolha um e o sistema preenche **Código Roteiro Target**, **Distância** e valor do pedágio por eixo.
- **Cadastrar Roteiro** — cria um roteiro novo na Target a partir da rota do SOP (origem, paradas e destino), gravando o **Código Roteiro Target** e a distância retornada.

| As cidades de origem, paradas e destino da rota precisam ter o **Mun. domicílio fiscal** (IBGE) preenchido. |
| --- |

## 5. Operação: da viagem ao CIOT

### 5.1. Preencher a Viagem

Abra a tela **Viagem** e preencha:

| Campo | Obrigatório | Observação |
| --- | --- | --- |
| **Empresa** | Sim | Define qual configuração Target será usada |
| **Cavalo / Veículo** | Sim | Precisa ter composição cadastrada |
| **Motorista** | Sim | — |
| **Proprietário ANTT** | Sim | É o contratado do CIOT |
| **Cidade Origem** | Sim | — |
| **Cidade Destino** | Sim | — |
| **Parceiro Coleta / Remetente** | Recomendado | Usados para resolver a origem |
| **Parceiro Entrega / Destinatário** | Recomendado | Usados para resolver o destino |
| **Produto Principal** | Sim | Com Natureza RF e Tipo de Carga MDF-e |
| **Peso Total** | Sim | Peso da carga enviado no CIOT |
| **Data Saída** | Sim | **Não pode ser anterior à data de hoje** |
| **Data Previsão Chegada** | Recomendado | Sem preenchimento o sistema usa hoje + 30 dias e é essa data que vira o vencimento da parcela de saldo |
| **Rota** | Sim, se houver pedágio Target | Precisa ter Código Roteiro Target |
| **Distância** | Recomendado | Se vazia, é buscada na Rota e, depois, na distância cadastrada entre origem e destino |

Vincule à viagem os **CT-e / NFS-e** da carga.

### 5.2. Consultar o valor do pedágio (quando aplicável)

No menu **Target** do cabeçalho da viagem:

- **Consultar Valor Pedágio** — retorna o valor do pedágio da rota para a categoria do veículo e atualiza a viagem.
- **Consultar Roteiros** — lista roteiros da Target entre origem e destino e permite atualizar o valor do pedágio na viagem.

| Se a configuração de validação de operadora de pedágio estiver ativa, o sistema **exige** que a consulta tenha sido feita pela Target antes da compra. Consultar por outra operadora e comprar pela Target é bloqueado. |
| --- |

### 5.3. Preencher o Afretamento

Na aba de afretamento da viagem, preencha a aba **Pagamento**.

**Dados da operação**

| Campo | O que informar |
| --- | --- |
| **Tipo Operação CIOT** | Carga Lotação, Carga Fracionada ou TAC-Agregado |
| **Retorno Vazio** | **Sim** quando o veículo retorna vazio |
| **Frete Motorista Total** | Valor total do frete |
| **Vlr. Adiantamento** | Valor do adiantamento (deixe zero se não houver) |
| **Saldo do frete** | Valor do saldo |
| **Vlr. Pedágio** | Valor do pedágio |
| **Vlr. Vale Abastecimento** | Valor de combustível, se houver |
| **Vlr. Desconto** | Despesas/descontos |
| **Vlr. SEST/SENAT**, **Vlr. IRRF**, **Vlr. INSS** | Impostos deduzidos |

**Grupo Adiantamento** (obrigatório quando há valor de adiantamento)

| Campo | O que informar |
| --- | --- |
| **Tipo Favorecido** | **Contratado** (proprietário ANTT) ou **Motorista** |
| **Forma de pagamento** | Depósito em conta ou **Cartão** |
| **Número cartão** | Quando a forma for Cartão |
| **Banco**, **Agência**, **Conta**, **Tipo conta** | Quando a forma for Depósito em conta |
| **Seq. Conta Adiantamento** | Alternativa: selecionar uma conta já cadastrada no parceiro |

**Grupo Saldo** (obrigatório quando há valor de saldo)

Mesmos campos do adiantamento: **Tipo Favorecido**, **Forma de pagamento**, **Número cartão** ou **Banco / Agência / Conta / Tipo conta**, ou **Seq. Conta Saldo**.

**Grupo Pedágio**

| Campo | O que informar |
| --- | --- |
| **Forma de pagamento** | **Target** para comprar o vale-pedágio junto com o CIOT. Também são aceitos Sem Parar, **Repom**, Move Mais, **Taggy** e **ConectCar** (TAG do cliente). Deixe em branco para não comprar pedágio |
| **Número cartão** | Número do cartão de pedágio, quando a forma for Target |

| **Atenção ao preenchimento da conta:** informe a **conta com o dígito, sem traço** — o sistema separa o último caractere como dígito verificador. O mesmo vale para a agência quando o cadastro é feito direto no afretamento. |
| --- |

**Tipos de conta aceitos:** Conta Corrente, **Poupança** e Conta Pagamento.

Ao final, **confirme o afretamento** (status precisa ficar **CONFIRMADO**) e **salve**.

### 5.4. Emitir o Contrato CIOT

**1.** Selecione o afretamento confirmado.

**2.** Menu **Target**, opção **Emitir Contrato CIOT**.

**3.** Confirme a pergunta "Deseja emitir o CIOT através da Target?".

O sistema então, em sequência:

**1.** Valida o afretamento (confirmado, sem contrato anterior, sem carta frete gerada, com Tipo Favorecido preenchido).

**2.** Consulta a ANTT: RNTRC ativo e proprietário equiparado a TAC.

**3.** Cadastra/atualiza transportador, motorista e destinatário na Target.

**4.** Envia a operação de transporte com parcelas, veículos e — se configurado — o vale-pedágio.

**5.** Declara a operação e recebe o **número do CIOT**.

**6.** Grava no afretamento: **Número CIOT**, contrato, parceiro pagador do frete e, quando houve compra de pedágio, o recibo do vale-pedágio.

**7.** Se o adiantamento for por **Cartão**, baixa automaticamente o financeiro do adiantamento usando o Tipo de Título, a Conta Bancária e a TOP configurados na aba Target.

Ao final aparece a mensagem **"Contrato de frete gerado com sucesso."**

| Se algo falhar depois que o CIOT já foi gerado na Target, o sistema **anula a operação** automaticamente ou, quando não consegue, exibe o número do CIOT na tela para anotação. **Anote o número** e acione o suporte antes de tentar emitir de novo. |
| --- |

### 5.5. Vale-pedágio: junto ou avulso?

| Situação | Como funciona |
| --- | --- |
| Proprietário **equiparado a TAC** (caso do CIOT) | O vale-pedágio é comprado **junto com o CIOT**. Basta preencher a Forma de pagamento do pedágio, o Número do cartão e ter a rota vinculada |
| Proprietário **não equiparado a TAC** | Não há CIOT. O pedágio é comprado avulso pelo menu **Target**, opção **Emitir Compra Vale Pedágio**, antes de qualquer contrato |

Outras ações de pedágio no menu **Target** da viagem:

- **Confirmar Compra Pedágio Sem Parar** — confirma a compra em TAG.
- **Cancelar Compra Pedágio** — cancela o vale-pedágio comprado.

## 6. Depois de emitir

### 6.1. Baixar o contrato

Menu **Target**, opção **Download de Contrato CIOT**. O documento abre em nova aba.

### 6.2. Pagar o saldo do frete

**1.** Feche a viagem na tela **Fechamento de Viagem** (status precisa ficar fechado).

**2.** Menu **Target**, opção **Pagar saldo CIOT**.

**3.** Confirme o valor apresentado.

O sistema encerra a operação na Target (informando peso de chegada e descontos), paga a parcela de saldo e baixa o financeiro correspondente.

### 6.3. Cancelar o contrato

Menu **Target**, opção **Cancelar Contrato CIOT**. O motivo registrado é "Cancelamento solicitado pelo usuário <nome>".

| Só é possível cancelar contratos emitidos pela Target. Contratos de outras integradoras precisam ser cancelados na integradora de origem. |
| --- |

### 7. Checklist rápido

Antes de clicar em **Emitir Contrato CIOT**, confirme:

| Configuração |
| --- |
| **Utiliza Pedágio/CIOT Target** = **Sim** |
| Usuário, Senha e Ambiente preenchidos (por empresa, se aplicável) |
| Tipo de Título, Conta Bancária e TOP de baixa preenchidos |
| Parceiro Pag. Frete Target preenchido |
| Categorias de Veículo Target cadastradas |

| Cadastros |
| --- |
| Proprietário ANTT com RNTRC ativo, endereço, telefone, celular e e-mail |
| Proprietário PF com RG numérico, CNH e vencimento da CNH |
| Proprietário PJ com pelo menos um contato ativo completo |
| Motorista com CPF, data de nascimento e cidade com IBGE |
| Cidades com **Mun. domicílio fiscal** preenchido |
| Veículo e carretas com RNTRC e Tipo de Rodado com nº de eixos |
| Composição do veículo com **Categoria do Veículo Target** |
| Produto principal com Natureza RF e Tipo de Carga MDF-e |
| Rota com **Código Roteiro Target** (se houver pedágio Target) |

| Viagem e afretamento |
| --- |
| Cidade Origem e Cidade Destino preenchidas |
| CT-e/NFS-e vinculados, com remetente na origem e destinatário no destino |
| **Data Saída** igual ou posterior a hoje |
| Peso total e produto principal preenchidos |
| Afretamento **CONFIRMADO** e salvo |
| Tipo Operação CIOT selecionado |
| Tipo Favorecido, Forma de pagamento e dados bancários / cartão preenchidos |
| Afretamento **sem** carta frete e **sem** contrato anterior |

### 8. Mensagens de erro e como resolver

###

#### Configuração

| Mensagem | O que fazer |
| --- | --- |
| Não foi configurada a empresa X para usar a Target... | Cadastrar a empresa em **Configurações Empresas**, aba **Target** |
| É necessário informar a Empresa para usar a configuração da Target por Empresa | Viagem sem empresa definida ou chamada fora de contexto de empresa |
| Conta bancária / TOP de Baixa / Tipo de Título para pagamento de pedágio não configurada na tela Configuração TMS, aba Target | Preencher os campos de baixa na aba **Target** |
| URL de acesso deve ser configurada | Ambiente (Homologação/Produção) não selecionado |

#### Parceiro / proprietário ANTT

| Mensagem | O que fazer |
| --- | --- |
| Viagem não possui Proprietário ANTT informado | Preencher **Proprietário ANTT** na viagem |
| Parceiro X não possui o campo RNTRC informado | Preencher **Nº RNTRC** no parceiro |
| Necessário informar o ANTT do Parceiro X para consultar a situação na ANTT | Idem acima |
| Não será possível emitir o pedágio ou CIOT para o parceiro X. RNTC consta como inativo | RNTRC irregular na ANTT — regularizar com o transportador |
| Parceiro X não é equiparado a TAC. Não será possível gerar vale pedágio | O CIOT pela Target exige proprietário equiparado a TAC |
| Parceiro X não possui Data de Nascimento/Fundação informada | Preencher a data no cadastro |
| Parceiro X não possui número do RG Informado | Preencher Identidade (PF) |
| Campo Número Identidade do Parceiro X deve possuir apenas números | Remover pontos, traços e letras do RG |
| Campo Número do Endereço do Parceiro X deve possuir apenas números. Caso não tenha número, informar 0 | Corrigir o número do endereço |
| Não foi informado o endereço / o bairro / a Cidade para o parceiro X | Completar o endereço |
| Número do telefone / Número do celular / Email deve ser informado para o parceiro X | Completar os contatos do parceiro |
| Dados complementares do parceiro X não cadastrados. Preencha os campos CNH, Naturalidade | Criar o registro complementar do parceiro (PF) |
| Parceiro X não possui a data de vencimento da CNH informada | Preencher o vencimento da CNH |
| Para parceiros PJ é necessário informar pelo menos um contato ativo | Cadastrar contato ativo |
| Para parceiros PJ é necessário informar o nome / telefone / celular / email do contato | Completar o contato |

#### Motorista

| Mensagem | O que fazer |
| --- | --- |
| Viagem não possui motorista informado | Preencher **Motorista** na viagem |
| Parceiro X não possui a data de nascimento informada | Preencher no cadastro do motorista |
| Dados complementares do parceiro X não cadastrados. Preencha os campos Nome do Pai e da Mãe | Criar o registro complementar do motorista |

#### Cidades, origem e destino

| Mensagem | O que fazer |
| --- | --- |
| Não foi informado a cidade de origem / destino na viagem | Preencher Cidade Origem e Cidade Destino |
| Não foi informado o campo 'Mun. domicílio fiscal' para a Cidade X | Preencher o código IBGE da cidade |
| Não foi localizado nenhum CT-e/NFS-e cujo remetente é na cidade X... | Conferir o remetente dos documentos ou a Cidade de Origem da viagem |
| Não foi localizado nenhum CT-e/NFS-e cujo destinatário é na cidade X... | Conferir os destinatários ou a Cidade de Destino |
| Latitude / Longitude não resolvida para origem/destino da ordem de carga | Preencher latitude e longitude no parceiro ou na cidade |

#### Veículo e composição

| Mensagem | O que fazer |
| --- | --- |
| Não foi localizada composição para o veículo X | Cadastrar o veículo em **Composição de Veículos** |
| Será necessário configurar a Categoria de veículo Target na tela Composição de veículos para a placa X | Preencher **Categoria do Veículo Target** |
| Não foi possível determinar a quantidade de eixos do Veículo X. Configure o Tipo de Reboque com a quantidade de eixos | Preencher **Nro. de Eixos** no Tipo de Rodado |
| Quantidade de eixos inválida (X)... deve estar entre 1 e 10 | Corrigir o número de eixos no Tipo de Rodado |

#### Produto e rota

| Mensagem | O que fazer |
| --- | --- |
| O campo 'Natureza Produto Receita Federal' no produto predominante X deve ser informado | Preencher no cadastro do produto |
| Rota não foi informada. Para emitir o pedágio é necessário informar a Rota na viagem | Preencher a **Rota** na viagem |
| Rota não vinculada com a Target. Para emitir o pedágio é necessário cadastrar a rota na Target antes | Usar **Consultar Roteiro** ou **Cadastrar Roteiro** na tela Rotas |
| Consulte o preço do pedágio pela operadora Target antes de realizar a compra | Usar **Consultar Valor Pedágio** no menu Target |
| O valor consultado pertence a operadora X. Consulte o preço do pedágio pela operadora Target | Refazer a consulta pela Target |

#### Afretamento e pagamento

| Mensagem | O que fazer |
| --- | --- |
| O afretamento deve estar confirmado | Confirmar o afretamento |
| Salve as informações antes / Selecione um afretamento antes | Salvar ou selecionar o registro |
| Contrato já emitido para este afretamento | Já existe CIOT — cancelar antes de reemitir |
| Não será possível emitir CIOT, pois já foi gerado a Carta Frete | Cancelar a carta frete |
| A Data de Saída é obrigatória / não pode ser menor que a data de hoje | Ajustar a Data Saída na viagem |
| Não foi configurado o Tipo Favorecido para pagar o adiantamento | Selecionar **Tipo Favorecido** |
| Afretamento possui adiantamento e não foi informado a Forma de pagamento | Selecionar Depósito em conta ou Cartão |
| Afretamento possui saldo e não foi informado a Forma de pagamento do saldo | Idem para o saldo |
| Não foi informado o banco / a agência / a conta / o tipo da conta para pagar o adiantamento (ou o saldo) | Completar os dados bancários |
| Não será possível realizar o pagamento do adiantamento, pois o financeiro X já está baixado | Conferir o financeiro do adiantamento |
| Não foi possível realizar a baixa do financeiro, pois foi solicitado liberação de limites | Liberar o limite no financeiro e baixar manualmente |

#### Retorno da Target

| Mensagem | O que fazer |
| --- | --- |
| Não foi possível incluir o contrato de frete. Mensagem retornada pela Target: ... | Ler a mensagem da Target — normalmente aponta o dado rejeitado |
| Falha ao cadastrar/atualizar parceiro ANTT / motorista / parceiro participante... | Corrigir o cadastro apontado e reemitir |
| Não foi possível consultar a situação do transportador... | Verificar credenciais, ambiente e disponibilidade do serviço |
| Foi realizado a geração do CIOT... mas não foi possível atualizar o afretamento. Segue o número do CIOT X para anotação | **Anotar o número do CIOT** e acionar o suporte — não reemitir |
| Erro ao processar URL Post (...) retorno inválido | Falha de comunicação — verificar rede/ambiente e tentar novamente |

| Para investigar erros de retorno da Target, ative temporariamente **Imprimir XML no Log** na aba Target e repita a operação. O XML enviado e recebido fica registrado no log de integração. |
| --- |
