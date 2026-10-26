---
id: "43326564085399"
titulo: "Controle de Qualidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43326564085399-Controle-de-Qualidade"
trilha: "Sankhya Official Pack - SOP > SOP"
atualizado_em: "2026-09-09T17:38:55Z"
---

# Controle de Qualidade

## 1. Visão Geral do Produto

### O que é o Addon Controle de Qualidade?

O **Addon Controle de Qualidade** é uma solução integrada para gestão de qualidade, conformidade e melhoria contínua desenvolvida sobre a plataforma **Sankhya ERP**. Ele centraliza em um único sistema todos os processos críticos de qualidade que normalmente estão espalhados em planilhas Excel, e-mails e documentos físicos.

O produto é dividido em cinco módulos complementares:

| Módulo | Função Principal |
| --- | --- |
| **Gestão de Não Conformidade** | Tratamento estruturado de desvios de qualidade em 10 fases |
| **Gestão de Documentos** | Controle de ciclo de vida de documentos internos |
| **Qualificação de Fornecedores** | Avaliação e rastreamento de desempenho de fornecedores |
| **Gestão de Mudanças** | Avaliação estruturada de mudanças em processos e produtos |
| **Questionários** | Criação e coleta de formulários padronizados |

##

### Para quem é destinado?

O produto atende empresas industriais, de serviços e distribuição que:

- Precisam manter **certificação ISO 9001**, ISO 14001 ou similar
- Operam com **múltiplos fornecedores** e precisam rastrear qualidade de entrega
- Têm **processos de produção** com risco de não conformidade
- Desejam **substituir planilhas** por um sistema rastreável e auditável
- Precisam **demonstrar conformidade** em auditorias externas

## 2. Requisitos e Configuração Inicial

### Ordem de Configuração Recomendada

Antes de começar a usar o sistema, o administrador deve executar a configuração nesta sequência:

PASSO 1: Configuração e Parametrização
  ↓
PASSO 2: Cadastros Gerais (origens, tipipos, processos)
  ↓
PASSO 3: Questionários
  ↓
PASSO 4: Rotinas

#### Passo 1 — Configuração e Parametrização

Acesse: **Menu > Configuração e Parametrização**

| **Importante — Configuração por Empresa:** Cada empresa do grupo deve ter seu próprio registro de configuração. O campo **Empresa** identifica o cadastro. |
| --- |

![Imagem 1: Importante — Configuração por Empresa: Cada empresa do grupo deve ter seu próprio registro de configuração. O campo…](https://ajuda.sankhya.com.br/hc/article_attachments/43326564067607)

| Parâmetro | Descrição |
| --- | --- |
| Empresa | Identifica a qual empresa esta configuração pertence |
| Qtde. Dias para Notificação | Antecedência com que o sistema avisa vencimentos de documentos |
| Usuário Notificação | Quem recebe avisos internos de documentos a vencer |
| E-mail Notificação | E-mail que recebe alertas de documentos |
| Bloqueia Compras para Fornecedores com Qualificação Vencida | Impede pedidos de compra para fornecedores com qualificação expirada |
| Índice Qualificação Padrão | Índice de qualificação utilizado como padrão para novos fornecedores |
| Notificar Fornecedor | Envia e-mail individual ao fornecedor com qualificação próxima de vencer |
| E-mail Notificação para Qualificação Vencida | Recebe tabela consolidada de qualificações a vencer |
| Dias para Retorno do Fornecedor | Prazo que o fornecedor tem para responder ao questionário de qualificação |

**Como funciona a rotina automática:**

O job ValidadeDocumentosSP executa automaticamente a cada 4 horas. Para cada empresa que possui um registro na tela de Configuração e Parametrização, são realizadas duas verificações **usando os parâmetros daquela empresa**:

**1 - Documentos a vencer**

Consulta documentos cuja data de validade está dentro da janela de **Qtde. Dias para Notificação** configurada. Para cada documento encontrado: - Gera aviso interno no painel de notificações do **Usuário Notificação** configurado - Envia e-mail para o **E-mail Notificação** (se preenchido)

| Os documentos são globais (compartilhados entre empresas). A configuração por empresa define apenas **quem é notificado** e **com quantos dias de antecedência** — cada empresa recebe as notificações de acordo com seus próprios parâmetros. |
| --- |

**2 - Qualificações de fornecedores a vencer**

Consulta qualificações (exceto canceladas) cuja data de validade está dentro da janela de dias configurada. Para cada fornecedor encontrado: - Inclui o fornecedor na tabela consolidada enviada ao **E-mail Notificação para Qualificação Vencida** (se preenchido) - Se **Notificar Fornecedor = S**: envia e-mail individual para o fornecedor usando o e-mail cadastrado no Sankhya

| **Atenção:** Se “Notificar Fornecedor = S” mas o parceiro não tiver e-mail cadastrado no Sankhya, a notificação individual é ignorada silenciosamente. Verifique o cadastro do parceiro (campo E-mail) caso o fornecedor informe não ter recebido a notificação. |
| --- |

**Empresa sem configuração cadastrada não recebe notificações.** O job ignora empresas que não possuem registro na tela de Configuração e Parametrização.

**Exemplo de configuração recomendada (por empresa):**

| Campo | Valor exemplo | Efeito |
| --- | --- | --- |
| Empresa | 1 | Configuração válida para a empresa 1 |
| Qtde. Dias para Notificação | 30 | Avisa 30 dias antes do vencimento de documentos |
| Usuário Notificação | 42 | Usuário 42 recebe aviso interno no painel |
| E-mail Notificação | qualidade@empresa.com | Recebe alertas de documentos |
| E-mail Notificação para Qualificação Vencida | qualidade@empresa.com | Recebe tabela de qualificações |
| Notificar Fornecedor | S | Fornecedor também recebe e-mail individual |

#### Passo 2 — Cadastros Gerais

Acesse: **Menu > Cadastros > Cadastros Gerais**

Cadastre os registros de cada tipo antes de começar a operar. O campo **Tipo Cadastro** define a categoria, e o campo **Descrição** é o nome que aparecerá nas seleções do sistema.

**Tipo: Origem RNC** — de onde veio o problema detectado:

| Descrição (exemplo) | Quando usar |
| --- | --- |
| Recebimento de Material | Problema identificado na inspeção de recebimento |
| Processo Produtivo | Desvio detectado durante a produção |
| Pós-venda / Reclamação de Cliente | Cliente reportou problema após entrega |
| Auditoria Interna | Não conformidade encontrada em auditoria |
| Auditoria Externa | Não conformidade apontada por auditor externo (ISO, cliente) |
| Desvio de Fornecedor | Entrega com quantidade, prazo ou qualidade fora do acordado |

**Tipo: Processo** — área ou processo da empresa envolvido na RNC:

| Descrição (exemplo) | Quando usar |
| --- | --- |
| Produção | Linha de fabricação, montagem |
| Logística / Expedição | Separação, embalagem, transporte |
| Qualidade | Inspeção, laboratório, controle de qualidade |
| Compras | Negociação, pedidos, fornecedores |
| Engenharia | Projeto, especificações técnicas |
| Comercial / Vendas | Relacionamento com cliente, pedidos |

**Tipo: Tipo RNC** — categoria da não conformidade:

| Descrição (exemplo) | Quando usar |
| --- | --- |
| Produto Não Conforme | Item físico fora de especificação |
| Desvio de Processo | Procedimento não foi seguido |
| Falha de Documentação | Documento incorreto, desatualizado ou ausente |
| Desvio de Entrega | Entrega fora do prazo, quantidade ou local incorretos |
| Reclamação de Cliente | Insatisfação ou falha reportada pelo cliente |
| Reincidência | Problema que já ocorreu antes e voltou |

**Tipo: Gestão de Mudanças** — categoria da mudança proposta:

| Descrição (exemplo) | Quando usar |
| --- | --- |
| Mudança de Fornecedor | Troca ou inclusão de fornecedor |
| Alteração de Equipamento | Compra, substituição ou modificação de equipamento |
| Mudança de Processo | Alteração em fluxo produtivo ou procedimento operacional |
| Alteração de Produto / Especificação | Mudança em especificação técnica ou desenho |
| Reorganização de Área | Mudança de layout, estrutura ou responsabilidades |
| Alteração de Sistema / Software | Atualização ou troca de sistema de gestão |

| **Aviso:** Alterar cadastros depois que RNCs estão em aberto pode causar inconsistências. Planeje bem antes de começar. |
| --- |

![Imagem 2: Aviso: Alterar cadastros depois que RNCs estão em aberto pode causar inconsistências. Planeje bem antes de começar.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564067991)

## 3. Descrição das Rotinas

### 3.1 Gestão de Não Conformidade

[Evento de Qualidade Detectado]
        |
        ▼
  01. Registro de RNC
  (quem detectou preenche)
        |
        ▼
  02. Ações Imediatas
  (conter o problema)
        |
        ▼
  03. Causa Raiz
  (investigar o porquê)
        |
        ▼
  04. Abrangência
  (verificar impactos)
        |
        ▼
  05. Ações Corretivas
  (definir soluções)
        |
        ▼
  06. Revisão de Documentos
  (atualizar procedimentos)
        |
        ▼
  07. Riscos e Oportunidades
  (avaliar riscos residuais)
        |
        ▼
  08. Implementação
  (executar e comprovar)
        |
        ▼
  09. Liberação de Produto
  (decidir sobre lote afetado)
        |
        ▼
  10. Verificação de Eficácia
  (confirmar que problema não voltou)
        |
        ▼
      [RNC FECHADA]

**Ações disponíveis:**

| Botão | Função |
| --- | --- |
| Avançar Fase | Move para Fase 02 (somente se todos os campos obrigatórios estiverem preenchidos) |
| Cancelar RNC | Encerra a Não Conformidade (ação irreversível) |
| Enviar Notificação | Notifica por e-mail o responsável da fase |

**Comportamentos esperados:** - O campo Parceiro mostra o campo Percentual de Desvio apenas para origens que exigem desvio - Após avançar fase, a Não Conformidade fica disponível apenas na tela da próxima fase - Após cancelar, a Não Conformidade fica travada para novas alterações

#### Tela: 01. Registro de Não Conformidade

**Acesso:** Menu > Gestão de Não Conformidade > 01. Registro de Não Conformidade

![Imagem 3: Acesso: Menu > Gestão de Não Conformidade > 01. Registro de Não Conformidade](https://ajuda.sankhya.com.br/hc/article_attachments/43326564068503)

**Finalidade:** Formalizar o registro de um desvio de qualidade com todas as informações necessárias para tratamento.

**Aba Responsáveis por Fase:**

Na aba são registradas no mínimo 9 linhas (uma para cada fase, a partir da fase 2). Em cada linha, selecione o usuário responsável.

Ao avançar para a Fase 2, o sistema deve notificar automaticamente via email, todos os usuários/parceiros vinculados às fases de Não Conformidade.

| **Importante:** Somente o usuário vinculado à fase poderá ver a respectiva Não Conformidade. |
| --- |

#### Tela: 02. Ações Imediatas

**Acesso:** Menu > Gestão de Não Conformidade > 02. Ações Imediatas

**Finalidade:** Registrar as ações de contenção tomadas para interromper o impacto imediato do problema.

![Imagem 4: Finalidade: Registrar as ações de contenção tomadas para interromper o impacto imediato do problema.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564069399)

#### Tela: 03. Causa Raiz

**Acesso:** Menu > Gestão de Não Conformidade > 03. Causa Raiz

**Finalidade:** Identificar e documentar a causa raiz real do problema (não apenas o sintoma superficial).

![Imagem 5: Finalidade: Identificar e documentar a causa raiz real do problema (não apenas o sintoma superficial).](https://ajuda.sankhya.com.br/hc/article_attachments/43326576416535)

#### Tela: 04. Abrangência de Não Conformidade

**Acesso:** Menu > Gestão de Não Conformidade > 04. Abrangência de Não Conformidade

**Finalidade:** Avaliar se a causa raiz identificada pode ter afetado outros lotes, produtos ou períodos além do caso registrado.

![Imagem 6: Finalidade: Avaliar se a causa raiz identificada pode ter afetado outros lotes, produtos ou períodos além do caso…](https://ajuda.sankhya.com.br/hc/article_attachments/43326576417047)

#### Tela: 05. Ações Corretivas

**Acesso:** Menu > Gestão de Não Conformidade > 05. Ações Corretivas

**Finalidade:** Definir as ações permanentes que eliminam a causa raiz identificada, impedindo reincidência.

![Imagem 7: Finalidade: Definir as ações permanentes que eliminam a causa raiz identificada, impedindo reincidência.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564070935)

**Campos por ação (tabela expansível — adicione quantas ações forem necessárias):**

| **Dica:** Nesta fase você **define** as ações. A **execução com evidências** acontece na Fase 08. |
| --- |

#### Tela: 06. Revisão de Documentos

**Acesso:** Menu > Gestão de Não Conformidade > 06. Revisão de Documentos

**Finalidade:** Identificar e atualizar todos os documentos internos afetados pelo problema ou pela solução.

![Imagem 8: Finalidade: Identificar e atualizar todos os documentos internos afetados pelo problema ou pela solução.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564071191)

#### Tela: 07. Riscos e Oportunidades

**Acesso:** Menu > Gestão de Não Conformidade > 07. Riscos e Oportunidades

**Finalidade:** Avaliar riscos residuais após a implementação das correções e identificar oportunidades de melhoria.

![Imagem 9: Finalidade: Avaliar riscos residuais após a implementação das correções e identificar oportunidades de melhoria.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564071959)

###

#### Tela: 08. Implementação

**Acesso:** Menu > Gestão de Não Conformidade > 08. Implementação

**Finalidade:** Registrar e comprovar a execução de cada ação corretiva planejada na Fase 05.

![Imagem 10: Finalidade: Registrar e comprovar a execução de cada ação corretiva planejada na Fase 05.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564072087)

**Exemplos de evidências:**

| Tipo de Ação | Evidência Esperada |
| --- | --- |
| Calibração de equipamento | Certificado de calibração emitido por laboratório |
| Treinamento de equipe | Lista de presença + foto + resultado de quiz |
| Atualização de procedimento | Documento com aprovação assinada e data |
| Manutenção preventiva | Ordem de serviço e foto do equipamento |
| Mudança de fornecedor | Nota fiscal ou contrato com novo fornecedor |

###

#### Tela: 09. Liberação de Produto

**Acesso:** Menu > Gestão de Não Conformidade > 09. Liberação de Produto

**Finalidade:** Registrar a decisão sobre o lote ou produto que estava segregado desde a Fase 02.

![Imagem 11: Finalidade: Registrar a decisão sobre o lote ou produto que estava segregado desde a Fase 02.](https://ajuda.sankhya.com.br/hc/article_attachments/43326576419223)

**Campos disponíveis:** Produto, Lote e Quantidade envolvidos, além de um campo de texto livre (Detalhe da Ação) onde a decisão é registrada por escrito (ex: liberar, liberar com restrição, descartar, devolver).

#### Tela: 10. Verificação de Eficácia

**Acesso:** Menu > Gestão de Não Conformidade > 10. Verificação de Eficácia

**Finalidade:** Confirmar, após período de observação, que o problema não voltou a ocorrer.

![Imagem 12: Finalidade: Confirmar, após período de observação, que o problema não voltou a ocorrer.](https://ajuda.sankhya.com.br/hc/article_attachments/43326576419351)

**Se resultado = Não Eficaz:** - O sistema não permite encerrar a RNC - Recomenda-se abrir nova RNC referenciando esta como reincidência - Ou voltar à Fase 03 para aprofundar análise de causa raiz

#### Tela: Consulta Não Conformidade

**Acesso:** Menu > Gestão de Não Conformidade > Consulta Não Conformidade

**Finalidade:** Pesquisar, filtrar e consultar o histórico completo de RNCs.

![Imagem 13: Finalidade: Pesquisar, filtrar e consultar o histórico completo de RNCs.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564073111)

## 3.2 Gestão de Documentos

[Documento criado externamente (Word/PDF)]
        |
        ▼
Cadastrar no Controle de Documentos
  (título, tipo, versão, validade)
        |
        ▼
 Anexar arquivo digital
        |
        ▼
 Marcar como Revisado
  (quando revisor validar)
        |
        ▼
 Marcar como Aprovado
  (quando aprovador assinar)
        |
        ▼
 [Documento ativo e rastreável]
        |
        ▼
 Sistema monitora validade
 (avisa antes de vencer)

#### Tela: Controle de Documentos

**Acesso:** Menu > Gestão de Documentos > Controle de Documentos

**Finalidade:** Registrar, versionar e controlar o ciclo de vida de documentos internos.

![Imagem 14: Finalidade: Registrar, versionar e controlar o ciclo de vida de documentos internos.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564073495)

**Aba Controle de Impressão:**

Quando o documento é impresso fisicamente, registrar aqui: - Data de impressão - Responsável - Cópia número (para controle de cópias físicas) - Localização (Setor)

![Imagem 15: Quando o documento é impresso fisicamente, registrar aqui: - Data de impressão - Responsável - Cópia número (para…](https://ajuda.sankhya.com.br/hc/article_attachments/43326564074647)

**Aba Lista de Arquivos:**

Aba com uploads do documento digital. Permite múltiplos arquivos por documento (ex: versão PDF + versão Word editável).

![Imagem 16: Aba com uploads do documento digital. Permite múltiplos arquivos por documento (ex: versão PDF + versão Word editável).](https://ajuda.sankhya.com.br/hc/article_attachments/43326564075159)

**Aba Histórico de Status:** (» Roadmap)

Registro automático de cada mudança de status com data, hora e usuário responsável.

## 3.3 Gestão de Fornecedores

[Novo fornecedor identificado]
        |
        ▼
 Abrir Qualificação de Fornecedor
  (cadastrar dados do fornecedor)
        |
        ▼
 Enviar Questionário por E-mail
 (fornecedor responde online)
        |
        ▼
 Avaliar respostas e certificados
        |
        ▼
 Registrar resultado (Qualificado/Reprovado)
        |
        ▼
 [Fornecedor qualificado - aparece no Dashboard]

#### Tela: Qualificação de Fornecedor

**Acesso:** Menu > Gestão de Fornecedores > Qualificação de Fornecedor

**Finalidade:** Avaliar e qualificar fornecedores com base em critérios definidos pela empresa.

**Aba Questionário:** - Botão “Enviar Questionário por E-mail” envia formulário online para o fornecedor responder - Respostas ficam registradas automaticamente ao serem submetidas pelo fornecedor

![Imagem 17: Aba Questionário: - Botão “Enviar Questionário por E-mail” envia formulário online para o fornecedor responder -…](https://ajuda.sankhya.com.br/hc/article_attachments/43326576423575)

**Aba Certificados:** - Upload de certificados (ISO, qualidade, etc.) com data de validade - Sistema monitora vencimento e alerta antes da data

#### 3.4 Gestão de Mudanças

[Proposta de mudança identificada]
        |
        ▼
01. Cadastro da Mudança
(descrever estado atual vs. proposto)
        |
        ▼
02. Questionário de Avaliação
(impactos estruturados)
        |
        ▼
03. Ações da Mudança (5W2H)
(plano de implementação)
        |
        ▼
04. Avaliação de Riscos
(identificar e mitigar)
        |
        ▼
05. Aprovação da Proposta
(aprovador formal decide)
        |
        ▼
[Mudança aprovada ou reprovada]

#### Tela: Cadastro de Gestão de Mudanças (Fase 1)

**Acesso:** Menu > Gestão de Mudanças > Cadastro de Gestão de Mudanças

**Finalidade:** Registrar uma proposta de mudança descrevendo o estado atual e o estado desejado.

![Imagem 18: Finalidade: Registrar uma proposta de mudança descrevendo o estado atual e o estado desejado.](https://ajuda.sankhya.com.br/hc/article_attachments/43326576424087)

#### Tela: Questionário de Avaliação (Fase 2)

**Acesso:** Menu > Gestão de Mudanças > Questionário de Avaliação

**Finalidade:** Responder perguntas estruturadas que ajudam a avaliar o impacto da mudança proposta.

As perguntas são configuradas no módulo de Questionários e podem variar conforme o tipo de mudança.

**Estrutura típica:** - Perguntas sobre impacto em cliente - Perguntas sobre impacto regulatório - Perguntas sobre impacto em processos relacionados - Perguntas sobre necessidade de treinamento - Perguntas sobre custos estimados

![Imagem 19: Estrutura típica: - Perguntas sobre impacto em cliente - Perguntas sobre impacto regulatório - Perguntas sobre impacto…](https://ajuda.sankhya.com.br/hc/article_attachments/43326576424471)

#### Tela: Ações de Mudança (Fase 3)

**Acesso:** Menu > Gestão de Mudanças > Ações de Mudança

**Finalidade:** Definir o plano de ação 5W2H para implementação da mudança.

**Campos por ação:**

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| O Quê (What) | Texto | Sim | Qual ação será executada |
| Quem (Who) | Usuário | Sim | Responsável pela execução |
| Onde (Where) | Texto | Sim | Local ou sistema onde acontece |
| Por Quê (Why) | Texto | Sim | Motivo desta ação específica |
| Quando (When) | Data | Sim | Prazo de conclusão |
| Como (How) | Texto | Sim | Método de execução |
| Quanto Custa (How Much) | Valor | Não | Custo estimado |

![Imagem 20: Custo estimado](https://ajuda.sankhya.com.br/hc/article_attachments/43326564077591)

#### Tela: Avaliação de Riscos (Fase 4)

**Acesso:** Menu > Gestão de Mudanças > Avaliação de Riscos

**Finalidade:** Identificar e mitigar riscos antes de aprovar a mudança.

Funciona da mesma forma que a Fase 2 (Questionário de Avaliação): perguntas de Sim/Não configuradas no módulo de Questionários, voltadas para riscos da mudança proposta (ex: “Esta mudança pode gerar risco à segurança do operador?”).

![Imagem 21: Funciona da mesma forma que a Fase 2 (Questionário de Avaliação): perguntas de Sim/Não configuradas no módulo de…](https://ajuda.sankhya.com.br/hc/article_attachments/43326564078999)

#### Tela: Aprovação da Proposta (Fase 5)

**Acesso:** Menu > Gestão de Mudanças > Aprovação da Proposta (ou Avaliação Pós-Mudança)

**Finalidade:** Decisão formal do aprovador sobre a proposta de mudança.

**Registro da decisão:**

| Campo | Tipo | Descrição |
| --- | --- | --- |
| Aprovador | Usuário | Quem está decidindo (usuário logado) |
| Aprovado? | Sim/Não | Marca a aprovação da mudança |
| Reprovado? | Sim/Não | Marca a reprovação da mudança |
| Assinatura | Texto | Identificação de quem assina a decisão |
| Motivo da Reprova | Texto longo | Preenchido quando Reprovado = Sim |
| Data da Aprovação | Data | Data em que a decisão foi registrada |

Esta é a última fase (não existe fase 6). O botão “Avançar Fase” não aparece nesta tela — só “Voltar Fase”.

![Imagem 22: Esta é a última fase (não existe fase 6). O botão “Avançar Fase” não aparece nesta tela — só “Voltar Fase”.](https://ajuda.sankhya.com.br/hc/article_attachments/43326564079639)

## 3.5 Questionários

#### Tela: Cadastro de Questionários

**Acesso:** Menu > Questionários > Cadastro de Questionários

**Finalidade:** Criar modelos de questionário reutilizáveis para qualificação de fornecedores ou avaliação de mudanças.

**Aba Perguntas:**

Para cada pergunta, configure:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| Pergunta | Texto | Enunciado da questão |
| Tipo de Resposta | Seleção | Texto / Número / Data / Seleção Única / Múltipla Escolha |
| Obrigatória | Sim/Não | Se pode ser pulada |
| Peso | Número | Para cálculo de pontuação |

**Para perguntas do tipo “Seleção”:** - Sub-grid de opções de resposta - Cada opção tem um texto e uma pontuação associada

![Imagem 23: Para perguntas do tipo “Seleção”: - Sub-grid de opções de resposta - Cada opção tem um texto e uma pontuação associada](https://ajuda.sankhya.com.br/hc/article_attachments/43326564080535)

#### Tela: Formulário de Qualidade

**Acesso:** Via link enviado por e-mail ou Menu > Formulário de Qualidade

**Finalidade:** Interface simplificada para que terceiros (fornecedores, parceiros) respondam questionários com um usuário compartilhado.

**Comportamento:** - Usuário compartilhado, que tem acesso apenas ao formulário enviado por e-mail. - Ao enviar, respostas ficam registradas automaticamente na qualificação do fornecedor

![Imagem 24: Comportamento: - Usuário compartilhado, que tem acesso apenas ao formulário enviado por e-mail. - Ao enviar, respostas…](https://ajuda.sankhya.com.br/hc/article_attachments/43326564080919)![Imagem 25: Comportamento: - Usuário compartilhado, que tem acesso apenas ao formulário enviado por e-mail. - Ao enviar, respostas…](https://ajuda.sankhya.com.br/hc/article_attachments/43326576426263)![Imagem 26: Comportamento: - Usuário compartilhado, que tem acesso apenas ao formulário enviado por e-mail. - Ao enviar, respostas…](https://ajuda.sankhya.com.br/hc/article_attachments/43326576426903)

## 4. Exemplos de Uso Prático

### Exemplo 1 — Lote Recebido Fora de Especificação

**Cenário:** Uma indústria alimentícia recebe do fornecedor “Embalagens ABC” um lote de 5.000 potes. Na inspeção de recebimento, 12% dos potes apresentam tampa com vedação deficiente.

**Como registrar e tratar no sistema:**

**Passo 1 — Abrir a RNC**

```
Menu > Gestão de Não Conformidade > 01. Registro

- Origem: Recebimento de Material
- Tipo: Produto Não Conforme
- Processo: Inspeção de Recebimento
- Parceiro: Embalagens ABC
- Detalhamento: "Lote 2024-847 com 5.000 potes recebidos em
  15/01/2024. Inspeção identificou 600 unidades (12%) com
  vedação da tampa abaixo do padrão mínimo definido no
  contrato (tolerância máxima: 2%)"
- Nota Fiscal: NF-12847
- Quantidade: 5000
- Prioridade: Alta (fornecedor com histórico de problemas)
- Prazo Total: 45 dias

Responsáveis:
  Fase 02: João Souza (Supervisor de Qualidade)
  Fase 03: Maria Lima (Engenheira de Qualidade)
  Fase 04-10: [definir por área]
```

**Passo 2 — Ações Imediatas (Fase 02)**

```
Ação: "Segregar imediatamente as 600 unidades suspeitas em
área de quarentena (Galpão 3, Setor Q). Lote 2024-847 não
deve ser usado em produção até liberação formal."

Data de Execução: 15/01/2024
Responsável: João Souza

Evidências anexadas:
- Foto da etiqueta de quarentena
- Relatório da inspeção de recebimento (PDF)
```

**Passo 3 — Causa Raiz (Fase 03)**

```
Metodologia: 5 Porquês

Por que as tampas têm vedação deficiente?
  → Porque o material da junta de borracha está fora de espessura

Por que o material está fora de espessura?
  → Porque o lote de borracha usado pelo fornecedor era de um
    novo fornecedor deles, sem qualificação completa

Por que o fornecedor usou borracha não qualificada?
  → Porque não têm processo de aprovação de novos materiais

Causa Raiz: "Embalagens ABC não tem processo estruturado de
aprovação de novos fornecedores de matéria-prima, permitindo
uso de material não qualificado em produção."
```

**Passo 4 — Avançar pelas fases 04–10**

Cada fase é executada pelo responsável designado. Ao final, na Fase 10, após 30 dias sem reincidência, a RNC é encerrada como “Eficaz”.

## Exemplo 2 — Reclamação de Cliente por Produto Entregue Errado

**Cenário:** Um cliente da distribuidora liga reportando que recebeu 50 caixas do produto X quando havia pedido o produto Y. O erro está no picking do armazém.

**Como tratar:**

```
Menu > Gestão de Não Conformidade > 01. Registro

- Origem: Pós-venda / Reclamação de Cliente
- Tipo: Falha de Processo
- Processo: Expedição e Logística
- Parceiro: [nome do cliente]
- Detalhamento: "Cliente reportou no dia 18/01/2024 recebimento
  incorreto. Pedido 44892 solicitava produto Y (Ref 847-B),
  mas foram expedidas 50 caixas do produto X (Ref 839-A).
  Divergência identificada no picking."

Ações Imediatas (Fase 02):
- Enviar representante para coleta do produto errado
- Priorizar entrega do produto correto via transportadora urgente
- Contatar cliente com prazo de solução: 24h

Causa Raiz (Fase 03):
- Análise revelou que as referências 847-B e 839-A têm
  embalagem visualmente semelhante e estavam armazenadas
  no mesmo corredor
- Causa raiz: ausência de código de barras diferenciador
  visível no facing da prateleira

Ações Corretivas (Fase 05):
- Instalar etiquetas de cor diferente por família de produto
- Implementar leitura obrigatória de código de barras no picking
- Reposicionar os dois produtos em corredores distintos
```

##

## Exemplo 3 — Auditoria Interna Identifica Procedimento Desatualizado

**Cenário:** Auditoria interna anual identificou que o procedimento POP-023 (Controle de Temperatura) não foi atualizado após a compra de novos equipamentos de refrigeração em 2022.

**Como tratar:**

```
Menu > Gestão de Não Conformidade > 01. Registro

- Origem: Auditoria Interna
- Tipo: Falha de Documentação
- Processo: Controle de Qualidade
- Parceiro: [não aplicável]
- Detalhamento: "Auditoria interna (18/01/2024) identificou
  que POP-023 referencia equipamentos modelo RF-2019,
  substituídos em março/2022 por equipamentos RF-2022 com
  faixa de temperatura operacional diferente. Operadores
  estão seguindo procedimento desatualizado."

Ações Imediatas (Fase 02):
- Comunicar equipe imediatamente que POP-023 está suspenso
- Distribuir versão anotada com parâmetros corretos até
  revisão formal

Causa Raiz (Fase 03):
- Procedimento de troca de equipamento não inclui etapa
  de atualização de POPs relacionados
- Causa raiz: lacuna no processo de gestão de mudança de
  equipamentos

Revisão de Documentos (Fase 06):
- POP-023: atualizar parâmetros e referenciar RF-2022
- Formulário de troca de equipamento: incluir campo
  "POPs afetados"
```

##

## Exemplo 4 — Qualificação de Novo Fornecedor de Componentes

**Cenário:** A empresa precisa qualificar um novo fornecedor de componentes eletrônicos antes de utilizá-lo.

**Como tratar:**

```
Menu > Gestão de Fornecedores > Qualificação de Fornecedor

1. Criar novo registro:
  - Fornecedor: Componentes Tech Ltda
  - Tipo de Fornecimento: Componentes Eletrônicos
  - Forma de Qualificação: Questionário + Certificado
  - Responsável: Engenheira Ana Costa

2. Enviar questionário por e-mail:
  - Selecionar questionário "Qualificação de Fornecedores
    de Componentes - v2"
  - Clicar em "Enviar Questionário por E-mail"
  - Sistema envia link para fornecedor responder online

3. Aguardar resposta (prazo: 5 dias úteis)

4. Avaliar respostas e solicitar certificados:
  - ISO 9001 válida
  - Certificado de conformidade RoHS

5. Registrar resultado:
  - Pontuação: 87/100
  - Situação: Qualificado
  - Validade: 12 meses
```

##

## Exemplo 5 — Avaliação de Mudança de Processo Produtivo

**Cenário:** O gerente de produção propõe mudar a temperatura do forno de cura de 180°C para 195°C para reduzir o tempo de ciclo.

**Como tratar:**

```
Menu > Gestão de Mudanças > Cadastro de Gestão de Mudanças
1. Cadastrar mudança:
  - Processo: Mudança de Processo
  - Situação Atual: "Temperatura: 180°C, tempo de ciclo: 8min"
  - Mudança Proposta: "Temperatura: 195°C, tempo estimado: 6min"
  - Justificativa: "Redução de 25% no tempo de ciclo aumenta
    capacidade produtiva sem investimento em equipamento"

2. Questionário de Avaliação (Fase 2):
  - "A mudança afeta especificações de produto?" → Sim
  - "Requer validação de cliente?" → Não
  - "Há impacto em certificação ISO?" → Não
  - "Requer treinamento?" → Sim (operadores devem saber nova temp)

3. Ações 5W2H (Fase 3):
  - O quê: Ajustar set point do forno de 180 para 195°C
  - Quem: Técnico de Manutenção Paulo Mendes
  - Quando: Após aprovação, no próximo turno de manutenção
  - Como: Acesso ao painel de controle do forno, código 4422
  - Quanto custa: R$ 0 (ajuste de parâmetro)

4. Avaliação de Riscos (Fase 4):
  - "Esta mudança pode gerar risco à segurança do operador?" → Não
  - "Esta mudança pode afetar a qualidade do produto?" → Sim

5. Aprovação (Fase 5):
  - Aprovador: Diretor Industrial Carlos Ferreira
  - Aprovado: Sim
  - Assinatura: "Carlos Ferreira - Diretor Industrial"
```
