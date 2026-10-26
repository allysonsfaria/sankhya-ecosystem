---
id: "42644689226263"
titulo: "TMS Transportador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42644689226263-TMS-Transportador"
trilha: "Sankhya Official Pack - SOP > TMS"
atualizado_em: "2026-09-08T11:31:12Z"
---

# TMS Transportador

Este documento reúne, em linguagem de negócio, como os parâmetros de configuração do Transporte de Cargas governam a operação da tabela de frete ao manifesto — e mostra a jornada completa do frete, a correlação entre as telas e o catálogo de validações. Cada parâmetro definido na tela de Configuração vale para a empresa inteira e serve de padrão para as demais telas do processo.

### NESTE DOCUMENTO

| 1 | Acesso à Tela |
| --- | --- |
| 2 | Pré-Requisitos |
| 3 | Visão Geral |
| 4 | Jornada Operacional do Frete |
| 5 | Correlação entre as Telas |
| 6 | Fluxo — Tabela de Frete e Pedido |
| 7 | Fluxo — Ordem de Carregamento |
| 8 | Fluxo — Viagem, CT-e e Afretamento |
| 9 | Cálculos e Gerações Automáticas |
| 10 | Regras de Negócio |
| 11 | Catálogo de Validações |
| 12 | Parâmetros por Assunto |
| 13 | Boas Práticas |
| 14 | Glossário |
| 15 | Perguntas Frequentes |
| 16 | Go Live e Checklist |
| 17 | Telas Relacionadas |

### Acesso à Tela

Para abrir o painel de parâmetros, navegue pelo menu: Logística > Cadastros > Configurações TMS. A tela é organizada em abas por assunto — Geral, Afretamento, ANTT, Cheque, Cotação de Frete, Adiantamento de Motoristas, Pedido, Call Center, Subcontratação e as abas das operadoras de pagamento (Pamcard, Pagbem, Repom, Siga Fácil, e-Frete, Target, FF Cred, Strada), além de abas por Empresa e por Unidade.

![Imagem 1: Para abrir o painel de parâmetros, navegue pelo menu: Logística > Cadastros > Configurações TMS. A tela é organizada em…](https://ajuda.sankhya.com.br/hc/article_attachments/43164430088855)

Tela de Configurações do TMS — parâmetros gerais e abas por assunto.

As demais telas do processo ficam assim no menu:

| **TELA** | **CAMINHO NO MENU** |
| --- | --- |
| Tabela de Frete · Distribuição · ANTT (piso) | Logística › Cadastros › Tabela de Frete · Distribuição — e Movimentações › Tabela de Frete ANTT |
| Pedido (aba Roteiro) | Logística › Cadastros › Pedido |
| Ordem de Carregamento | Logística › Cadastros › Ordem de Carregamento |
| Viagem · Cotação · Formação de Cargas · MDF e | Logística › Movimentações › … |
| Fechamento · Acerto de Viagem · Call Center | Logística › Movimentações › … |

### Pré-Requisitos

**(1)** Licença do SOP Logística TMS Transportador ativa.

**(2)** Cadastros de apoio preenchidos: Parceiros (clientes, motoristas, proprietários), Veículos e Rotas.

**(3)** Tabelas de Frete cadastradas (inclusive a de Distribuição, com prazo de entrega).

**(4)** Produtos-serviço dos documentos (frete, pedágio, seguro, impostos) definidos.

**(5)** Naturezas, tipos de título e operações financeiras do adiantamento configuradas.

**(6)** Credenciais e contas de cada operadora de pagamento, quando utilizada.

**(7)** Permissão de acesso às telas atribuída aos perfis.

### Visão Geral

O painel concentra dezenas de parâmetros que padronizam o comportamento do sistema, agrupados em:

- Documentos e Serviços: quais serviços representam frete, pedágio, seguro e impostos no conhecimento; centro de resultado e tipo de negociação padrão.
- Validações e Bloqueios: regras que exigem informações ou impedem operações irregulares (crédito, saldo, canhotos, habilitação, CIOT).
- Afretamento e Adiantamento: como o pagamento ao motorista é calculado, com tetos, liberações e piso legal.
- Integrações de Pagamento e Pedágio: as operadoras utilizadas e suas credenciais.
- Padrões de Viagem e Ordem: exigências ao gerar viagens e ordens.

**Princípio geral**: a hierarquia manda de baixo para cima. A Tabela de Frete e o Roteiro do Pedido definem primeiro; a Configuração entra como padrão quando eles não trazem o valor. Padrão obrigatório em branco impede a emissão.

### Jornada Operacional do Frete

Do preço ao manifesto, o frete percorre uma sequência de telas. Em cada etapa, os parâmetros atuam como regra ou padrão. O fluxo abaixo resume o caminho completo:

A seguir, cada etapa em detalhe com o caminho da tela:

**(1)** Tabela de Frete Distribuição — define o custo por trecho (valor fixo + por distância + excedente) e o prazo de entrega. É onde o preço e o lead time nascem.

- Logística › Cadastros › Tabela de Frete Distribuição

**(2)** Tabela de Frete — calcula o valor por peso, rota ou valor da mercadoria; a variante ANTT guarda o piso mínimo legal.

- Logística › Cadastros › Tabela de Frete

**(3)** Pedido de Frete — aplica a tabela e registra o pedido; o roteiro define natureza, rota e cálculo de pedágio.

- Logística › Cadastros › Pedido (aba Roteiro)

**(4)** Ordem de Carregamento — consolida as notas a carregar. Valida crédito, saldo e teto do frete do motorista.

Logística › Cadastros › Ordem de Carregamento

**(5)** Viagem — reúne as ordens, calcula a previsão de entrega e consolida frete, pedágio e seguro; confere a habilitação.

- Logística › Movimentações › Viagem

**(6)** Emissão do Conhecimento (CT-e) — cada valor vira um item do documento, com centro de resultado e tipo de negociação.

- Logística › Movimentações › Formação de Cargas

**(7)** Afretamento — calcula o pagamento ao motorista, aplica tetos e liberações e gera o CIOT.

- Logística › Movimentações › Viagem › Afretamento

**(8)** Manifesto (MDF-e) — reúne os conhecimentos; exige o CIOT por categoria e usa o tipo de peso configurado.

- Logística › Movimentações › MDF-e

**(9)** Fechamento e Acerto — encerra a operação conferindo canhotos e financeiros antes de liquidar.

- Logística › Movimentações › Fechamento · Acerto de Viagem

### Correlação — Esclarecimento do Fluxo Operacional

Esta seção explica como as telas se conectam na prática, para que o time saiba onde cada informação nasce e para onde ela vai. A ideia central: o dado não é recriado a cada etapa — ele flui de uma tela para a próxima.

#### Como o fluxo funciona na prática

##### Tudo começa no preço. A tabela de frete calcula quanto custa transportar (por peso, rota ou valor da carga) e informa o prazo de entrega. Esse valor e esse prazo passam para o pedido, que registra o cliente, o remetente, o destinatário e o roteiro.

##### Quando a carga vai ser expedida, o pedido vira uma ordem de carregamento, que junta as notas a transportar. Nesse momento o sistema confere se o cliente tem crédito, se o peso cabe no pedido e se o pagamento ao motorista está dentro do teto. Aprovado, a ordem gera a viagem, que reúne a carga, calcula a previsão de entrega e confere se motorista, veículo e proprietário estão regulares.

##### Com a viagem pronta, o sistema emite o conhecimento (o documento de transporte). Cada valor — frete, pedágio, seguro e os impostos — aparece como um item do documento. Em paralelo, o afretamento calcula quanto o motorista recebe e gera a autorização de pagamento. Essa autorização é o que permite montar o manifesto, que declara a viagem para o transporte. Por fim, no fechamento e acerto, os documentos e valores são conferidos e tudo se liquida no financeiro.

#### Resumo da conexão entre as telas

##### O quadro abaixo mostra, para cada tela, o que ela entrega para a etapa seguinte:

| De (Tela) | Para (Tela) | O que é Transportado |
| --- | --- | --- |
| Tabela de Frete / Distribuição | Pedido | O valor do frete e o prazo de entrega. |
| Pedido (roteiro) | Ordem de Carregamento | Cliente, rota, parceiros, valores e classificação fiscal. |
| Ordem de Carregamento | Viagem | As notas consolidadas, o peso e o frete a carregar. |
| Viagem | Conhecimento (CT-e) | Frete, pedágio, seguro e impostos — cada um vira um item. |
| Viagem | Afretamento | A base do pagamento ao motorista. |
| Afretamento | Manifesto (MDF-e) | O CIOT e o vale-pedágio. |
| Afretamento | Financeiro | Os títulos de adiantamento, saldo e comissão, e as baixas. |
| Conhecimento (CT-e) | Call Center | Os canhotos gerados por documento. |

**Regra de leitura:** Um valor errado no conhecimento quase sempre nasce antes — na tabela de frete, no roteiro do pedido ou na viagem. Corrija na origem, não no documento.

### Fluxo Operacional — Tabela de Frete e Pedido

O valor do frete começa nas tabelas. A Tabela de Frete Distribuição guarda, por roteiro, o valor fixo, o valor por distância e o excedente, além do prazo de entrega (Lead Time), que alimenta a data prometida quando o parâmetro Calcular Data de Previsão de Entrega está ativo.

![Imagem 2: O valor do frete começa nas tabelas. A Tabela de Frete Distribuição guarda, por roteiro, o valor fixo, o valor por…](https://ajuda.sankhya.com.br/hc/article_attachments/43164430092055)

Tabela de Frete Distribuição — roteiro com faixas e o bloco de Lead Time (dias de previsão de entrega).

No Pedido, a aba Roteiro concentra remetente, destinatário, coleta e entrega, além da natureza, centro de resultado e tipo de negociação — com padrão vindo da Configuração quando não informados.

![Imagem 3: No Pedido, a aba Roteiro concentra remetente, destinatário, coleta e entrega, além da natureza, centro de resultado e…](https://ajuda.sankhya.com.br/hc/article_attachments/43164430093975)

Pedido de Frete — a aba Roteiro reúne parceiros, cidades e classificação do frete.

### Fluxo Operacional — Ordem de Carregamento

A Ordem de Carregamento consolida as notas a carregar e é um ponto forte de validação. Conforme os parâmetros ativos, o sistema confere o limite de crédito do cliente, o saldo do pedido e o teto do frete do motorista — abrindo pedido de liberação quando o valor excede a alçada.

![Imagem 4: A Ordem de Carregamento consolida as notas a carregar e é um ponto forte de validação. Conforme os parâmetros ativos, o…](https://ajuda.sankhya.com.br/hc/article_attachments/43164430096279)

Ordem de Carregamento — consolidação das notas e ponto de validação de crédito, saldo e teto de frete.

### Fluxo Operacional — Viagem, Conhecimento e Afretamento

A Viagem (Ordem de Carga) reúne as ordens, calcula a previsão de entrega e organiza o pagamento ao motorista. As abas Afretamento enFrete concentram o cálculo de adiantamento, saldo, pedágio, seguro e impostos, além do CIOT — onde atuam o piso ANTT, os tetos com liberação e o desconto de seguro por categoria.

![Imagem 5: A Viagem (Ordem de Carga) reúne as ordens, calcula a previsão de entrega e organiza o pagamento ao motorista. As abas…](https://ajuda.sankhya.com.br/hc/article_attachments/43164397902615)

###### Viagem / Ordem de Carga — abas de Afretamento, Frete e Motorista, onde o pagamento é calculado e o CIOT é gerado.

**IMPORTANTE**: na emissão do conhecimento, os serviços configurados (frete, pedágio, seguro, impostos e taxas do frete) determinam cada item do documento. Serviço obrigatório em branco interrompe a emissão com aviso.

### Cálculos e Gerações Automáticas

Além das travas, muitas regras acontecem automaticamente quando o operador confirma uma etapa:

- **Cálculo do afretamento:** apura os impostos e contribuições, o seguro por categoria, o adiantamento (percentual da rota) e o saldo; aplica os tetos de frete e adiantamento (abrindo liberação por alçada quando excede) e monta os valores a pagar. Veículo próprio pode ser isento dos lançamentos financeiros.
- **Validação de crédito:** no roteiro do pedido e na ordem, confere o limite/saldo de crédito do cliente e bloqueia se insuficiente.
- **Montagem automática do MDF-e:** ao vincular o conhecimento, monta as abas do manifesto — trajeto de UFs, CIOT (do afretamento), vale-pedágio e pagamento de frete — exigindo contratante, seguradora e fornecedor do vale.
- **Fechamento de terceiros:** puxa os valores do afretamento confirmado, calcula a quebra e o saldo e registra a quilometragem e a chegada da viagem.

### Regras de Negócio

- RN001 — Hierarquia do valor: Tabela de Frete e Roteiro têm precedência; a Configuração é o padrão de reserva.
- RN002 — Padrão obrigatório em branco: serviço, centro de resultado ou tipo de negociação sem valor impedem a emissão.
- RN003 — Crédito do cliente: não permite carregar para cliente sem limite/saldo de crédito.
- RN004 — Saldo do pedido: impede carregar peso além do saldo contratado.
- RN005 — Teto do frete do motorista: valor acima do máximo da rota abre pedido de liberação.
- RN006 — Habilitação obrigatória: CNH válida e situação regular de proprietário e veículo.
- RN007 — Transit point: exigido antes de emitir o conhecimento, quando parametrizado.
- RN008 — Piso ANTT: o frete pago não pode ficar abaixo do mínimo legal.
- RN009 — Frete × Conhecimento: pagamento acima da receita bloqueia ou exige liberação.
- RN010 — Seguro por categoria: o desconto do seguro é habilitado ou isento por categoria do transportador.
- RN011 — Financeiro da frota própria: veículo próprio exige o registro financeiro antes do pagamento.
- RN012 — CIOT no manifesto: obrigatório por categoria antes de criar o MDF-e.
- RN013 — Canhotos no fechamento: a quantidade deve corresponder aos documentos.
- RN014 — Financeiros no acerto: o acerto só fecha com os financeiros conciliados.
- RN015 — Configuração por empresa: filiais podem ter credenciais e contas próprias.

### Catálogo de Validações

Lista das validações que a empresa pode ligar ou desligar, com a tela em que atuam e o efeito.

| **VALIDAÇÃO** | **TELA ONDE ATUA** | **EFEITO** |
| --- | --- | --- |
| Valida limite de crédito | Pedido · Ordem de Carregamento | **bloqueia** |
| Valida saldo do pedido | Ordem de Carregamento | **bloqueia** |
| Valida viagens pendentes do veículo | Ordem de Carregamento | **bloqueia** |
| Valida frete máximo do motorista | Ordem de Carregamento | **gera liberação** |
| Liberação por tipo de veículo divergente | Ordem de Carregamento | **gera liberação** |
| Exige ordem ao gerar viagem | Viagem | **bloqueia** |
| Reutiliza ordem de carregamento | Viagem | **bloqueia reuso** |
| Exige tipo de viagem | Viagem | **bloqueia** |
| Exige transit point | Viagem · CT-e | **bloqueia** |
| Verifica CNH do motorista | Viagem · Ordem | **bloqueia** |
| Verifica situação de proprietário e veículo (ANTT) | Viagem · Ordem | **bloqueia** |
| Valida cidade origem × destino | Emissão do CT-e | **bloqueia** |
| Aceita mais de um conhecimento por viagem | Emissão do CT-e | **pode bloquear** |
| Valida frete mínimo (ANTT) | Afretamento | **bloqueia** |
| Valida valor do afretamento × conhecimento | Afretamento | **bloqueia ou libera** |
| Exige financeiro da frota própria | Afretamento | **bloqueia** |
| Valida proprietário ANTT do veículo | Afretamento | **bloqueia** |
| Usa liberação de adiantamento / frete máximo | Afretamento | **gera liberação** |
| Obriga CIOT no manifesto (por categoria) | MDF-e | **bloqueia** |
| Valida canhotos no fechamento | Fechamento de Viagem | **bloqueia** |
| Valida financeiros no acerto | Acerto de Viagem | **bloqueia** |
| Exige acerto vigente do agregado | Acerto de Viagem | **bloqueia** |
| Bloqueia efetivação por depósito | Pagamento / Efetivação | **bloqueia** |
| Critérios de aceite do documento (operadora) | Pagamento de frete | **lista enviada** |

### Parâmetros por Assunto

Referência rápida dos principais parâmetros de cada assunto e para que servem. Todos ficam em Logística › Cadastros › Configurações TMS, na aba indicada.

#### Documentos e Serviços (aba Geral)

| **PARÂMETRO** | **PARA QUE SERVE** |
| --- | --- |
| Serviços de Frete, Pedágio, Seguro e Impostos | Definem qual serviço representa cada valor no conhecimento. Obrigatórios para emitir. |
| Centro de Resultado e Tipo de Negociação | Padrão de classificação do documento para faturamento e apuração. |
| Casas Decimais do Valor de Frete | Precisão do arredondamento do frete. |
| Unidades Destacadas no Conhecimento | Quais medidas (peso bruto, líquido, quantidade) aparecem no documento. |
| Tabela de Pauta de Imposto | Aplica a base mínima de imposto quando exigida. |

#### Afretamento e Pagamento ao Motorista (aba Afretamento)

| **PARÂMETRO** | **PARA QUE SERVE** |
| --- | --- |
| Produto do Afretamento | Item base do pedido gerado no afretamento. Obrigatório. |
| Parceiro para os Financeiros | Define quem recebe (motorista, favorecido ou proprietário). |
| Percentual de Adiantamento sobre o Líquido | Base de cálculo do saldo do frete. |
| Usa Liberação de Adiantamento / Frete Máximo | Abre aprovação por alçada quando excede o teto. |
| Desconta Seguro por Categoria | Habilita ou isenta o desconto do seguro conforme o transportador. |
| Utiliza Carta Frete | Controla o uso e a numeração da carta frete. |

#### Adiantamento e Cheque (abas Adiantamento e Cheque)

| **PARÂMETRO** | **PARA QUE SERVE** |
| --- | --- |
| Natureza, Operações e Vencimento do Adiantamento | Como os títulos de adiantamento são classificados e quando vencem. |
| Fórmulas e Eventos de Comissão | Como as comissões (frete, estadia, média) são calculadas no acerto. |
| Utiliza Pagamento por Cheque (mínimo e limite) | Habilita o cheque e define os valores mínimo e máximo. |
| Data, Cópia e Numeração do Cheque | Padrões de impressão do cheque. |

#### Integrações de Pagamento e Pedágio (abas das operadoras)

| PARÂMETRO | PARA QUE SERVE |
| --- | --- |
| Utiliza (a operadora) | Liga a operadora de pagamento/pedágio no fluxo. |
| Ambiente e Credenciais | Ambiente (produção/homologação) e usuário/senha da operadora. |
| Conta, Tipo de Título e Parceiro de Pagamento | Como o título e a baixa do pagamento são gerados por operadora. |
| Baixa Automática do Adiantamento/Pedágio | Baixa o financeiro automaticamente após o pagamento. |
| Configuração por Empresa | Credenciais e contas próprias por filial. |

#### Pedágio e Vale-Pedágio (aba Geral)

| **PARÂMETRO** | **PARA QUE SERVE** |
| --- | --- |
| Sempre Destaca Pedágio no Conhecimento | Separa o pedágio do frete como item próprio. |
| Gerar Financeiro de Pedágio só para Roteirizado | Restringe o financeiro de pedágio às viagens roteirizadas. |
| Altera Valor de Pedágio no Afretamento | Soma o pedágio ao frete do motorista no cálculo. |

#### Cotação, Subcontratação e Atendimento (abas Cotação, Subcontratação e Call Center)

| **PARÂMETRO** | **PARA QUE SERVE** |
| --- | --- |
| Modelos de E-mail da Cotação | Assunto e conteúdo padrão do e-mail de cotação ao cliente. |
| Veículo Padrão e Prazo da Subcontratação | Padrões usados nos conhecimentos terceirizados. |
| Tipo de Call Center e Geração de Canhotos | Se o registro é por conhecimento ou por nota, e quais canhotos gerar. |
| Modelos de Relatório (Carta Frete, Recibos) | Layout dos documentos impressos. |

### Boas Práticas

**(1)** Revise serviços e centros de resultado antes do go-live — causa mais comum de bloqueio na emissão.

**(2)** Mantenha tabelas de frete e lead time atualizados; deles dependem preço e prazo prometido.

**(3)** Ative as validações de crédito e saldo em operações com risco financeiro.

**(4)** Defina as alçadas de liberação (frete máximo, adiantamento) com o financeiro.

**(5)** Confira o piso ANTT e as categorias de desconto de seguro conforme a frota.

**(6)** Teste cada operadora de pagamento em homologação antes de produção.

**(7)** Padronize as exigências de viagem (tipo, transit point, ordem) para evitar retrabalho.

### Perguntas Frequentes

- **Por que a emissão do conhecimento foi bloqueada com aviso de configuração?**

Algum serviço obrigatório (frete, pedágio, seguro ou imposto) está em branco. Preencha o serviço na aba Geral e tente novamente.

- **O sistema abriu um pedido de liberação em vez de barrar o frete. Por quê?**

O frete do motorista ultrapassou o teto da rota e o parâmetro de liberação está ativo. Segue para aprovação por alçada, sem travar o carregamento.

- **Não consigo criar o manifesto. O que falta?**

Para a categoria do transportador, o CIOT do afretamento é obrigatório. Gere o CIOT antes de criar o MDF-e.

- **Onde é definido o prazo de entrega prometido ao cliente?**

No Lead Time da Tabela de Frete Distribuição, aplicado quando o cálculo de previsão de entrega está ativo.

- **Um valor chegou errado no conhecimento. Onde corrijo?**

Quase sempre na origem — tabela de frete, roteiro do pedido ou viagem. Veja a seção de Correlação.

- **Cada filial pode ter uma configuração de pagamento diferente?**

Sim. Ative a Configuração por Empresa na operadora desejada e cadastre credenciais e contas por filial.

### Go Live e Checklist

Crítico: confirme todos os serviços obrigatórios do conhecimento — sem eles a emissão trava.

Crítico: valide naturezas, contas e operações do adiantamento antes do primeiro pagamento.

Crítico: defina as categorias de CIOT obrigatório conforme a frota (TAC, ETC, CTC).

Crítico: ajuste o piso ANTT e o desconto de seguro por categoria.

Crítico: teste cada operadora de pagamento em homologação.

Crítico: revise as alçadas de liberação com o time financeiro.

### Checklist de configuração

Parceiros, veículos e composições cadastrados e regulares.

Tabelas de frete e distribuição (com lead time) atualizadas.

Serviços, centros de resultado e tipos de negociação padrão preenchidos.

Parâmetros de adiantamento definidos.

Validações de crédito, saldo e canhotos ajustadas à política.

Categorias de CIOT e desconto de seguro configuradas.

Exigências de viagem e alçadas de liberação acordadas.

Operadoras de pagamento testadas em homologação.

Permissões de acesso e modelos de relatório configurados.

### Glossário

Termos usados no dia a dia do transporte, em linguagem simples:

| **TERMO** | **O QUE SIGNIFICA** |
| --- | --- |
| Conhecimento (CT-e) | Documento fiscal que formaliza o transporte da carga. |
| Manifesto (MDF-e) | Documento que reúne os conhecimentos de uma viagem para o transporte. |
| Roteiro | Trajeto do frete no pedido: origem, destino, coleta e entrega. |
| Lead Time | Prazo de entrega previsto, cadastrado na tabela de frete de distribuição. |
| Afretamento | O cálculo e o pagamento do frete ao motorista/terceiro. |
| CIOT | Autorização de pagamento do frete ao transportador autônomo (exigência legal). |
| Piso ANTT | Valor mínimo legal do frete definido pela agência reguladora de transporte. |
| Carta Frete | Documento de controle do pagamento entregue ao motorista. |
| Canhoto | Comprovante de entrega da carga, conferido no fechamento. |
| Transit Point | Ponto de transbordo/redespacho no meio do trajeto. |
| Liberação por alçada | Aprovação de um responsável quando um valor ultrapassa o teto. |
| Categoria do transportador | Perfil do prestador (autônomo, empresa, cooperativa), que muda regras de CIOT e seguro. |

### Telas Relacionadas

- **Tabela de Frete / Distribuição:** definição de preço e prazo do frete.
- **Pedido de Frete:** registro do pedido e do roteiro.
- **Ordem de Carregamento:** consolidação das notas para carregar.
- **Viagem:** execução, afretamento e emissão de documentos.
- **MDF-e:** manifesto dos conhecimentos da viagem.
- **Fechamento e Acerto de Viagem**: encerramento e liquidação.
- **Cotação de Frete:** geração de pedidos a partir de cotação.
- **Call Center:** registro de canhotos e ocorrências.
