---
id: "41605447288983"
titulo: "Processo D-1001 — Informações do Contribuinte"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Comece por aqui > Processos do Portal da Reforma Tributária"
atualizado_em: "2026-10-21T14:37:10Z"
rotulos: ["Configuração", "Impostos", "Reforma Tributária", "br.com.sankhya.mgeliv.reforma.portal", "DeRE", "D-1001", "Informações do Contribuinte"]
---

# Processo D-1001 — Informações do Contribuinte

**Módulo:** Portal da Reforma Tributária › DeRE
**Caminho de acesso:** Portal da Reforma Tributária › DeRE › D1001 — Inf. Contribuinte
**Versão mínima SankhyaOm 4.36:** 4.36b88 + erpcore-module 5.8.21
**Versão mínima Livros:** 5.38
**Versão mínima Livros para envio em Produção:** 5.50

---

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#antes-de-comecar)
- [Painel D-1001 — Informações do Contribuinte](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#painel)
- [Como enviar o D-1001](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#como-enviar)
- [Etapa 1 — Revisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#etapa-1)
- [Etapa 2 — Dados DeRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#etapa-2)
- [Etapa 3 — Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#etapa-3)
- [Etapa 4 — Revisão Final](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#etapa-4)
- [Tela de confirmação](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#confirmacao)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#pontos-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#faq)

## O que é e para que serve

O evento D-1001 — Informações do Contribuinte é o primeiro evento obrigatório da DeRE e identifica o contribuinte perante a Receita Federal: registra o regime tributário principal, os regimes secundários e as atividades exercidas conforme a legislação do IBS e CBS. Nenhum outro evento da DeRE pode ser transmitido sem que o D-1001 esteja processado com sucesso para o mesmo CNPJ raiz.

## Antes de começar

Para que uma empresa apareça no painel D-1001, o Administrador do sistema precisa habilitar o módulo DeRE para ela em Configurações › Empresas. Empresas sem habilitação não aparecem na grade, independentemente do regime tributário cadastrado no ERP.

Para transmitir o D-1001, a empresa também precisa ter as credenciais do Receita Integra configuradas para o ambiente desejado. Para enviar no ambiente **1 – Produção**, o Livros precisa estar na versão 5.50 ou superior. Para saber como configurar as credenciais, acesse [Processo DeRE — Credenciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#credenciais).

**💡 Dica**

Para instruções sobre como habilitar o módulo DeRE por empresa, acesse [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#sumario)

## Painel D-1001 — Informações do Contribuinte

Ao acessar DeRE › D1001 — Inf. Contribuinte, você vê a grade com todas as empresas habilitadas para DeRE e o status do último evento enviado para cada uma, separado por ambiente.

### Colunas da grade

- **Cód. Empresa** — código interno da empresa no ERP.
- **CNPJ Raiz** — CNPJ raiz da empresa, usado como declarante na DeRE.
- **Razão Social** — nome da empresa.
- **Ambiente Ativo** — ambiente para onde os eventos da empresa são transmitidos: **1 – Produção** ou **2 – Produção Restrita**, conforme configurado em Credenciais.
- **Status Produção** — situação do último evento D-1001 da empresa no ambiente **1 – Produção**.
- **Status Homologação** — situação do último evento D-1001 da empresa no ambiente **2 – Produção Restrita**.
- **Ocorrência** — exibe Erro ou Aviso quando o último evento retornou ocorrências; vazio se não houver.
- **Ações** — botões **Iniciar** e **Detalhes** da empresa.

As colunas de status exibem os seguintes valores, também descritos na legenda no rodapé da tela:

- **Não enviado** — nenhum D-1001 foi entregue à Receita Federal para o CNPJ raiz naquele ambiente: o evento foi criado e não enviado, ou nunca foi criado.
- **Processando** — o lote foi entregue e o recibo depende do resultado do processamento.
- **Rejeitado** — o evento foi processado e recusado pela Receita Federal. A ação **Corrigir e reenviar** fica disponível no Histórico de Eventos.
- **Enviado** — a declaração foi aceita pela Receita Federal, com recibo.

### Filtros disponíveis

Use os filtros **Status**, **Ambiente Ativo** e **Ocorrência** para localizar empresas específicas na grade.

### Ações disponíveis

- **Iniciar** — na coluna **Ações**, abre o wizard para enviar o D-1001 da empresa. Não disponível para empresas com status Processando.
- **Detalhes** — navega para o Histórico de Eventos filtrado pelo CNPJ da empresa selecionada.
- **Iniciar (N)** — no topo da tela, ao marcar múltiplas empresas na grade, inicia o wizard para todas as selecionadas simultaneamente.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#sumario)

## Como enviar o D-1001

O envio é feito por um wizard de 4 etapas. Clique em Iniciar na linha da empresa para abrir o wizard. Para enviar para várias empresas ao mesmo tempo, marque as empresas desejadas na grade e clique em Iniciar (N). O evento é transmitido para o ambiente ativo de cada empresa.

**ℹ️ Nota**

O wizard identifica automaticamente a operação correta: abre com Inclusão para empresas sem evento enviado e com Alteração para empresas que já possuem D-1001 com recibo. O badge da operação aparece ao lado do CNPJ e da Razão Social em cada etapa.

### Etapa 1 — Revisão

Revise os dados cadastrais da empresa antes de prosseguir. Nenhum campo é editável nesta etapa — as informações vêm do cadastro do ERP. Verifique se Razão Social, CNPJ, Regime Tributário, CNAE Principal, Logradouro, Município e CEP estão corretos.

Se algum dado estiver incorreto, corrija no cadastro da empresa no ERP antes de continuar. Clique em Continuar para avançar.

![Etapa Revisão do wizard D-1001 com os dados cadastrais da empresa](https://ajuda.sankhya.com.br/hc/article_attachments/41605502230423)

### Etapa 2 — Dados DeRE

Informe o regime tributário e a natureza tributária da empresa.

- **Regime Principal** — selecione o regime tributário principal da empresa para fins de IBS e CBS. Opções disponíveis no MVP: 9 — Normas Gerais (empresas em geral), 1 — Serviços Financeiros ou 2 — Planos de Saúde.
- **Regimes Secundários** — marque até 3 regimes adicionais, quando a empresa exercer atividades em mais de um regime. O regime selecionado como principal não aparece nas opções secundárias.
- **Indicador de natureza tributária** — selecione 0 — Tributação regular para empresas sujeitas ao IBS e CBS, ou 1 — Imunidade ou não incidência para empresas com tratamento diferenciado.

**⚠️ Atenção**

O regime secundário não pode ser igual ao regime principal. O wizard bloqueia o avanço se você tentar selecionar o mesmo valor nos dois campos.

Clique em Continuar para avançar.

![Etapa Dados DeRE do wizard D-1001 com regime principal, regimes secundários e indicador de natureza tributária](https://ajuda.sankhya.com.br/hc/article_attachments/41605447281815)

### Etapa 3 — Atividades

Esta etapa aparece somente quando a empresa tem Regime 1 — Serviços Financeiros ou Regime 2 — Planos de Saúde selecionado como regime principal ou secundário. Se nenhum dos dois for aplicável, o wizard pula esta etapa automaticamente.

Selecione as atividades exercidas pela empresa conforme os regimes informados na etapa anterior:

- **Serviços Financeiros** — obrigatório quando o Regime 1 estiver selecionado (principal ou secundário). Use o campo de busca para filtrar as atividades disponíveis e marque todas que se aplicam.
- **Planos de Saúde** — obrigatório quando o Regime 2 estiver selecionado (principal ou secundário). O wizard bloqueia o avanço se nenhuma atividade for selecionada para o regime correspondente.

Clique em Continuar para avançar.

![Etapa Atividades do wizard D-1001 com as atividades de Serviços Financeiros e Planos de Saúde](https://ajuda.sankhya.com.br/hc/article_attachments/41605447282711)

### Etapa 4 — Revisão Final

Confira o resumo do evento antes de transmitir: a tabela exibe a operação, o CNPJ, a Razão Social e a competência de cada empresa que será incluída no envio.

**ℹ️ Nota**

Nesta etapa, o sistema valida o XML gerado antes de permitir o envio. Se a validação falhar, o erro é exibido em tela e o evento fica com status Não enviado no Histórico. Corrija os dados indicados e reinicie o wizard.

Quando o evento estiver validado, a mensagem "O evento foi validado e está pronto para transmissão. Clique em 'Concluir' para enviar." é exibida. Clique em Concluir para transmitir.

![Etapa Revisão Final do wizard D-1001 com o resumo do evento validado](https://ajuda.sankhya.com.br/hc/article_attachments/41605502237079)

### Tela de confirmação

Após o envio, o sistema exibe a mensagem "Evento entregue à Receita Federal" e o **Protocolo** de recebimento do lote. O protocolo confirma a entrega do lote, não a aceitação do evento: o recibo, que comprova a quitação da obrigação, é devolvido quando a Receita Federal termina o processamento. Para obtê-lo, use a ação **Atualizar** no Histórico de Eventos. A partir daqui, você pode:

- **Consultar histórico** — acessa o Histórico de Eventos filtrado pelo envio que acabou de ser realizado.
- **Voltar para painel** — retorna à grade D-1001.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#sumario)

## Pontos de atenção

Em qualquer etapa do wizard, clicar em Cancelar exibe uma confirmação antes de descartar o preenchimento. Se confirmar o cancelamento, todos os dados informados nas etapas são perdidos e você retorna à grade D-1001.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte#sumario)

## Perguntas frequentes

### Por que o botão Iniciar não aparece para uma empresa?

O botão Iniciar não fica disponível para empresas com status Processando. Aguarde o processamento do evento atual antes de iniciar um novo envio. Acesse o Histórico de Eventos via botão Detalhes para acompanhar o andamento.

### Enviei o D-1001 e o status ficou Processando. O que faço?

Esse é o comportamento esperado logo após a entrega do lote. No Histórico de Eventos, selecione o evento e clique em **Atualizar** para consultar o resultado. Quando a Receita Federal aceita a declaração, o sistema registra o recibo e o status muda para Enviado.

### A etapa de Atividades não apareceu no meu wizard. É um erro?

Não. A Etapa 3 — Atividades só é exibida quando a empresa tem Regime 1 — Serviços Financeiros ou Regime 2 — Planos de Saúde selecionado (principal ou secundário) na Etapa 2. Para empresas com Regime 9 — Normas Gerais, o wizard pula essa etapa automaticamente e vai direto para a Revisão Final.

### O D-1001 enviado em Produção Restrita vale para Produção?

Não. O ambiente **2 – Produção Restrita** serve para homologação e não tem validade fiscal; por isso o painel exibe o status de cada ambiente em colunas separadas. Para cumprir a obrigação, configure **1 – Produção** em Credenciais e transmita o D-1001 nesse ambiente.

### Posso enviar o D-1001 para várias empresas ao mesmo tempo?

Sim. Marque as empresas desejadas na grade e clique em Iniciar (N). O wizard percorre as mesmas 4 etapas, mas cada empresa aparece como um card independente, com seu próprio badge de operação e seus próprios campos para preenchimento.
