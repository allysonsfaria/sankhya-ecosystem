---
id: "41605814716695"
titulo: "Processo Assistente de Exceções IBS/CBS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Comece por aqui > Processos do Portal da Reforma Tributária"
atualizado_em: "2026-10-15T16:34:03Z"
rotulos: ["Configuração", "Livros Fiscais", "Impostos", "IBS", "CBS", "Reforma Tributária", "br.com.sankhya.mgeliv.reforma.portal"]
---

# Processo Assistente de Exceções IBS/CBS

**Módulo:** Livros Fiscais › Cadastros › Portal da Reforma Tributária
**Caminho de acesso:** Menu Principal › Livros Fiscais › Cadastros › Portal da Reforma Tributária › Assistente de Exceções IBS/CBS
**Versão mínima SankhyaOm 4.36:** 4.36b88 + erpcore-module 5.9.5
**Versão mínima SankhyaOm 4.35:** 4.35b777
**Versão mínima Livros:** 5.38.0

---

Neste artigo

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#antes-de-comecar)
- [Como usar o assistente](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#como-usar)
- [Painel de Diagnóstico](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#painel-diagnostico)
- [Etapa 1 — UF/Município de destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#etapa-1)
- [Etapa 2 — Seleção de](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#etapa-2)
- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#etapa-2)
- [Etapa 3 — Tipo de](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#etapa-3)
- [Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#etapa-3)
- [Etapa 4 — Finalidade da Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#etapa-4)
- [Etapa 5 — Parceiro / Grupo](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#etapa-5)
- [de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#etapa-5)
- [Resultado da configuração](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#resultado-config)
- [Painel de revisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#painel-revisao)
- [Resultado da gravação](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#resultado-gravacao)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#pontos-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605814716695-Processo-Assistente-de-Exce%C3%A7%C3%B5es-IBS-CBS#faq)

## O que é e para que serve

O Assistente de Exceções IBS/CBS guia você, passo a passo, na configuração das exceções tributárias do Imposto sobre Bens e Serviços (IBS) e da Contribuição sobre Bens e Serviços (CBS) para os produtos e serviços da sua empresa. Ele analisa o histórico real de documentos fiscais emitidos, identifica automaticamente quais NCMs e NBS precisam de atenção e sugere a classificação tributária correta com base nas tabelas oficiais do governo — permitindo concluir a configuração dos principais produtos em menos de 15 minutos. O assistente não realiza o cálculo do IBS/CBS nas notas fiscais, não substitui a parametrização de alíquotas gerais e não cobre créditos presumidos.

## Antes de começar

Verifique os seguintes pré-requisitos antes de acessar o assistente:

- Seu perfil de usuário precisa ter permissão de parametrização tributária. Sem essa permissão, o assistente não exibe o fluxo de configuração. Solicite o acesso em Controle de Acessos.
- O módulo fiscal do Sankhya Om deve estar ativo no seu contrato.
- Os dois indicadores de sincronização exibidos no painel — **Tabela CFF** e **Análise DFe** — devem estar com o status **"Atualizado"**. Caso algum deles exiba o status **"Desatualizado"** ou **"Falha"**, verifique se os Jobs responsáveis pelas atualizações automáticas estão ativos e sendo executados normalmente antes de prosseguir com a configuração.

O CNPJ usado pelo Job -22005 na comunicação com o CFF/SVRS é determinado automaticamente pelo Sankhya Om: o sistema busca no cadastro de empresas (`TSIEMP`) a empresa configurada como matriz (`CODEMPMATRIZ` nulo ou igual ao próprio `CODEMP`). Se houver mais de uma matriz, usa a empresa definida no parâmetro Empresa padrão para utilização do certificado digital (`EMPPADCERTDIG`).

**⚠️ Atenção**

A atualização das informações é feita automaticamente pelos Jobs (agendadores) do sistema. Para o correto funcionamento da Reforma Tributária, certifique-se de que os Jobs -22005 (Agendador Update Tabelas Reforma) e -22008 (Agendador Análise DFe – Exceção de Alíquotas) estejam ativos e sem falhas recentes. Para saber mais sobre os Jobs, suas funções e como acompanhar a execução, consulte a seção [Controle de Jobs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594634-Controle-de-Jobs).

O Job -22005 se comunica com o CFF/SVRS via mTLS e exige um certificado digital válido (e-CNPJ/e-NF) cadastrado no **Console NFe**. Sem o certificado, o job falha com a mensagem "CFF: certificado nao encontrado para CNPJ=XXXXXXXXXX" e o indicador **Tabela CFF** nunca alcança o status **Atualizado**, bloqueando o assistente antes mesmo de abrir. Antes de iniciar, confirme no **Console NFe** que o certificado da empresa responsável está válido, dentro do prazo de validade e com senha correta.

## Como usar o assistente

O assistente é composto por um painel de diagnóstico e um fluxo guiado de 5 etapas. Acesse pelo menu Livros Fiscais › Cadastros › Portal da Reforma Tributária › Assistente de Exceções IBS/CBS.

### Painel de Diagnóstico

Ao abrir o assistente, você vê o painel de diagnóstico. Ele cruza o histórico de documentos fiscais da sua empresa — NF-e, NFC-e, CT-e, CT-eOS, NFS-e e NF-Com — com a tabela oficial de elegibilidade do governo e exibe apenas os NCMs e NBS que realmente precisam de configuração.

- **Seletor de período** — escolha o período de análise: 30 dias (padrão ativo), 60 dias ou 90 dias. O painel recarrega automaticamente ao alterar o período.
- **Cards de resumo** — quatro cards clicáveis no topo mostram, respectivamente: total de produtos elegíveis, já configurados, aguardando configuração e volume financeiro total no período. Clique em qualquer card para aplicar o filtro correspondente na tabela.
- **Tabela de NCMs/NBS** — exibe código, descrição, volume em R$, quantidade de documentos e status de configuração atual para cada item. A ordenação padrão é por maior volume financeiro; você pode reordenar por qualquer coluna.

Filtros de status disponíveis:

- **Todos** — exibe todos os itens elegíveis.
- **Sem exceção** — itens sem nenhuma regra configurada.
- **Exceção parcial** — itens com configuração incompleta.
- **Configurado** — itens totalmente parametrizados.
- **Aguardando** — agrupa "Sem exceção" e "Exceção parcial" para priorização rápida.

**💡 Dica**
Use o filtro Aguardando para focar nos itens que ainda precisam de atenção e iniciar pelo de maior volume financeiro — esse costuma ser o de maior risco fiscal.

Para iniciar a configuração, selecione um ou mais NCMs/NBS na tabela (seleção múltipla disponível para configuração em lote) e clique em Configurar. O assistente abre o fluxo guiado de 5 etapas com os itens pré-carregados.

Para consultar as configurações anteriores, clique em Visualizar Logs no dashboard. O histórico de sessões exibe ID de execução, usuário, data/hora e total de regras gravadas sem necessidade de iniciar um novo fluxo.

### Etapa 1 — UF/Município de destino

Defina a jurisdição de destino da regra tributária. O IBS tem competência subnacional — a alíquota de exceção varia por estado e município de destino, e a regra gravada no motor fiscal precisa dessa dimensão para ser válida em operações interestaduais.

Escolha uma das três modalidades:

- **Todas as UFs/Municípios sem restrição** — opção padrão recomendada. A regra se aplica a qualquer destino.
- **UFs específicas** — busque por sigla ou nome entre as 27 unidades federativas. A lista exibe apenas UFs com documentos no período de análise.
- **Municípios específicos** — busque por nome ou código IBGE. A lista exibe apenas municípios presentes no histórico de documentos do período, evitando uma lista com os 5.570 municípios brasileiros.

Clique em Próximo para avançar.

![Imagem 1: Clique em Próximo para avançar.](https://ajuda.sankhya.com.br/hc/article_attachments/41605814711703)

### Etapa 2 — Seleção de Empresa

Selecione quais empresas do grupo terão a regra aplicada. A lista exibe apenas as empresas que emitiram documentos com os NCMs/NBS selecionados no período, mostrando nome, CNPJ e volume de documentos.

Use o toggle Selecionar todas as empresas do grupo para marcar todas em um clique. Para filtrar, use a busca por CNPJ ou razão social.

Clique em Próximo para avançar.

![Imagem 2: Clique em Próximo para avançar.](https://ajuda.sankhya.com.br/hc/article_attachments/41605814711959)

### Etapa 3 — Tipo de Operação (TOP)

Defina a qual Tipo de Operação (TOP) a regra se aplica.

Selecione uma ou mais TOPs da lista. Para criar uma regra geral que abranja todas as operações, marque a opção 0 - <Sem Descrição>.

**ℹ️ Nota**
Marcar 0 - <Sem Descrição> cria uma regra sem restrição de TOP — ela se aplica a qualquer tipo de operação. Marcar TOPs específicas restringe a regra apenas àquelas operações selecionadas.

Clique em Próximo para avançar.

![Imagem 3: Clique em Próximo para avançar.](https://ajuda.sankhya.com.br/hc/article_attachments/41605851861655)

### Etapa 4 — Finalidade da Operação

Defina a qual finalidade da operação a regra se aplica.

Selecione uma ou mais finalidades da lista. Para criar uma regra geral que abranja todas as finalidades, marque a opção 0 - <Sem Descrição>.

**💡 Dica**
As finalidades exibidas nesta etapa são as que estão previamente cadastradas na tela Finalidade da Operação. Para cadastrar ou gerenciar finalidades, acesse Comercial › Arquivo › Cadastros › Finalidade da Operação.

Marcar 0 - <Sem Descrição> cria uma regra sem restrição de finalidade — ela se aplica a qualquer finalidade de operação. Marcar finalidades específicas restringe a regra apenas às finalidades selecionadas.

Clique em Próximo para avançar.

![Imagem 4: Clique em Próximo para avançar.](https://ajuda.sankhya.com.br/hc/article_attachments/41605851862935)

### Etapa 5 — Parceiro / Grupo de Parceiros

Defina para quais parceiros a regra se aplica.

Escolha uma das três modalidades:

- **Todos os parceiros (sem restrição)** — opção padrão recomendada. A regra se aplica a qualquer parceiro.
- **Parceiros específicos** — busque por nome. A lista é paginada para ambientes com alto volume de clientes.
- **Grupo de parceiros** — selecione entre os grupos fiscais disponíveis. Os grupos exibidos aqui refletem os valores cadastrados no campo Grupo IBS/CBS, localizado na aba Fiscal da tela Parceiros. Para cadastrar ou ajustar os grupos, acesse Configurações › Cadastros › Parceiros.

Clique em Finalizar. O assistente executa a rotina de configuração e exibe o resultado.

![Imagem 5: Clique em Finalizar. O assistente executa a rotina de configuração e exibe o resultado.](https://ajuda.sankhya.com.br/hc/article_attachments/41605851863319)![Imagem 6: Clique em Finalizar. O assistente executa a rotina de configuração e exibe o resultado.](https://ajuda.sankhya.com.br/hc/article_attachments/41605851863831)

## Resultado da configuração

Ao finalizar a Etapa 5, o assistente exibe um painel de revisão com todas as regras que serão geradas a partir das seleções realizadas. Nenhuma gravação ocorre antes da sua confirmação explícita.

### Painel de revisão

O painel exibe o impacto global da configuração — total de NCMs/NBS, empresas impactadas e estimativa de documentos futuros afetados — seguido do detalhamento de cada regra: NCM/NBS, empresa, TOP, finalidade, parceiro, classificação atual, classificação nova e ação (INCLUIR ou ATUALIZAR).

**⚠️ Atenção**
Se qualquer classificação tributária (cClassTrib) selecionada não for aceita pela SEFAZ para o tipo de documento, o assistente bloqueia a confirmação e indica o item com problema. Corrija antes de prosseguir.

Clique em Editar em qualquer item para retornar à etapa correspondente sem perder as demais seleções. Quando estiver satisfeito com a revisão, clique em Confirmar e Gravar.

**🚨 Risco operacional**
A gravação é definitiva e tem efeito imediato no cálculo de IBS/CBS das notas fiscais emitidas a partir deste momento. Não é possível desfazer a configuração pelo assistente após a confirmação. Revise o painel com atenção antes de clicar em Confirmar e Gravar.

### Resultado da gravação

Após a confirmação, a rotina grava as regras no motor fiscal e exibe o resultado:

- Tabela com status individual por NCM/NBS: INCLUÍDA, ATUALIZADA ou ERRO.
- Log de execução expansível com: ID de execução, usuário, versão das tabelas CFF, versão da NT ENCAT vigente no momento da gravação e registros gravados.
- Indicativo de NCMs/NBS restantes ainda aguardando configuração.

**ℹ️ Nota**
Em caso de falha parcial — quando algumas regras são gravadas e outras não — as regras com sucesso são mantidas e os erros são reportados individualmente. Você decide como tratar os itens que falharam.

Clique em Voltar ao Diagnóstico para retornar ao painel e configurar os itens restantes.

## Pontos de atenção

- O assistente funciona com dados locais sincronizados em background — não requer conectividade com o Portal da Conformidade Fácil (SVRS) no momento do uso. Se qualquer uma das fontes ultrapassar 24 horas sem sincronização bem-sucedida, um alerta é exibido no painel antes de qualquer ação.
- O ID de execução gerado em cada sessão (formato EXC-AAAA-NNNNN) é o principal instrumento de diagnóstico para o time de suporte. Em caso de dúvida sobre uma configuração realizada, informe esse ID ao acionar o suporte.

## Perguntas frequentes

**O assistente vai configurar todos os produtos da minha empresa automaticamente?**

Não. O assistente exibe apenas os NCMs e NBS que sua empresa efetivamente operou no período selecionado e que são elegíveis para exceção conforme as tabelas oficiais do governo. A confirmação e a gravação das regras dependem sempre da sua aprovação explícita no painel de revisão.

**O que acontece se o governo atualizar as tabelas de classificação tributária depois que eu configurar?**

As configurações já gravadas permanecem ativas com a classificação vigente no momento da gravação — essa informação fica registrada no log de execução com a versão da NT ENCAT utilizada. Quando uma nova NT for detectada na próxima sincronização, o assistente exibe um alerta recomendando que você revise as regras afetadas.

**Posso configurar mais de um NCM ao mesmo tempo?**

Sim. Selecione múltiplos NCMs/NBS no painel de diagnóstico antes de clicar em Configurar. Todos os itens selecionados percorrem o mesmo fluxo guiado com as mesmas definições de jurisdição, empresa, TOP, finalidade e parceiro.

O assistente não suporta a configuração simultânea de NCMs/NBS com CSTs e classificações tributárias (cClassTrib) distintas em uma mesma execução — todos os itens selecionados recebem a mesma regra. Se os NCMs/NBS do seu diagnóstico exigirem regras diferentes, execute o assistente mais de uma vez, selecionando em cada execução apenas os itens que compartilham a mesma regra. As execuções são independentes e não interferem entre si, desde que as regras configuradas sejam distintas das anteriores.

**Por que meu Assistente de Exceções IBS/CBS está com os valores zerados?**

A atualização das informações é feita automaticamente pelos Jobs (agendadores) do Sankhya Om. Para o correto funcionamento da Reforma Tributária, certifique-se de que os Jobs `-22005` (**Agendador Update Tabelas Reforma**) e `-22008` (**Agendador Análise DFe – Exceção de Alíquotas**) estejam ativos e sem falhas recentes. Para saber mais sobre os Jobs, suas funções e como acompanhar a execução, acesse [Controle de Jobs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594634-Controle-de-Jobs).

Caso os Jobs já tenham sido executados e os valores continuem zerados, verifique se os NCMs e NBS utilizados nos documentos fiscais possuem, de fato, alguma exceção tributária. Este assistente não lista NCMs ou NBS com tributação integral (`cClassTrib 000001`). Para configurar a tributação integral desses itens, acesse o [Assistente de Configuração da Tributação Integral (IBS e CBS)](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria).
