---
id: "38865034649111"
titulo: "Cartão inteligente - Diagnóstico do Serviço(Boleto Rápido)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:00:59Z"
rotulos: ["Configuração", "Contas", "Financeiro", "Cartões Inteligentes", "Boleto Rápido", "Diagnóstico"]
---

# Cartão inteligente - Diagnóstico do Serviço(Boleto Rápido)

Este artigo explica como interpretar o **Cartão Inteligente de Diagnóstico do Serviço Boleto Rápido**.

O cartão utiliza **indicadores de cores** para demonstrar a saúde da operação e indicar quando é necessário realizar verificações ou ajustes na configuração do serviço.

Tópicos deste artigo:

| Tópico | Tópico | Tópico |
| --- | --- | --- |
| [Como interpretar o cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS57EJASA7CHTT12VFZYW) | [Erro crítico — Status vermelho](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS57M14RVHJFK7KZC825T) | [Avisos e pendências — Status amarelo](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS57SWS3NGKVTYGCXVPWV) |
| [Parâmetro indevido — SERVERHOSTSCHED](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS57S6V7B9DCES3EMKCFX) | [Jobs sem execução recente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS57WS7W6B2A1APRBAZPF) | [Contas sem ocorrência de remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS57Z9H4KT6X0MK495XNH) |
| [Boletos não enviados para o serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS58369ENFQJB2FK46V9B) | [Conta com credenciamento incompleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS58B61RAFHVMPRW0SGP9) | [Status normal — Verde](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS58C3K19SZ0VW44TZQ93) |
| [Inatividade / sem uso — Cinza](https://ajuda.sankhya.com.br/hc/pt-br/articles/38865034649111-Cart%C3%A3o-inteligente-Diagn%C3%B3stico-do-Servi%C3%A7o-Boleto-R%C3%A1pido#h_01KK9DS58D3DMCXVTYCZR36T40) |  |  |

---

# Como interpretar o cartão

As cores exibidas no cartão indicam o estado do serviço e o nível de atenção necessário.

| Cor | Status | O que significa | Ação sugerida |
| --- | --- | --- | --- |
| 🟢 Verde | Funcionando normalmente | O serviço está operando sem problemas | Nenhuma ação necessária |
| 🟡 Amarelo | Avisos / Pendências | Existem configurações ou processos que precisam de verificação | Verificar configurações |
| 🔴 Vermelho | Erro crítico | O serviço está inoperante | Ação imediata necessária |
| ⚪ Cinza | Sem uso / Inativo | Não houve utilização recente do serviço | Nenhuma ação necessária |

(Inserir imagem do cartão aqui)

---

# 🔴 Erro crítico (Status Vermelho)

O status vermelho ocorre quando o serviço está ativo, porém **não existe nenhuma conta bancária credenciada** para operar o Boleto Rápido.

Sem uma conta credenciada, o sistema não consegue:

- enviar boletos
- registrar títulos
- processar baixas automáticas

Mesmo sem funcionamento, **o contrato do serviço continua ativo**.

![Captura de tela do cartão de diagnóstico com cabeçalho vermelho, exibindo o status "Crítico" e o alerta "Contas não…](https://ajuda.sankhya.com.br/hc/article_attachments/38865063651351)

O status **Crítico** indica que o serviço está parado por falta de contas credenciadas ativas.

---

## Impacto no serviço

Quando esse status ocorre:

- o serviço fica totalmente inoperante
- nenhum boleto é enviado
- as baixas automáticas não são processadas

---

## Como resolver

1. Acesse **Boleto Rápido → Contas**
2. Verifique se existe alguma conta com status **Credenciada / Ativa**
3. Caso não exista, realize o **credenciamento da conta**
4. Após credenciar, reteste o envio ou registro de boletos

---

# 🟡 Avisos e pendências (Status Amarelo)

O cartão amarelo indica que o serviço **não está totalmente bloqueado**, mas existem situações que exigem verificação.

A seguir estão os cenários mais comuns.

![Cartão de diagnóstico com cabeçalho amarelo e status "Atenção", listando pendências como "Jobs sem execução recente",…](https://ajuda.sankhya.com.br/hc/article_attachments/38865034637335)

O status de **Atenção** detalha falhas parciais ou configurações pendentes que exigem ajuste.

---

## Parâmetro indevido — SERVERHOSTSCHED

Indica uma configuração que pode impedir a execução automática de tarefas do sistema.

### Como resolver

1. Acesse **Preferências → Parâmetros**
2. Pesquise pelo parâmetro **SERVERHOSTSCHED**
3. Limpe o campo **Texto**
4. Salve as alterações
5. Reinicie o servidor de aplicação

---

## Jobs sem execução recente

Um ou mais processos automáticos essenciais estão atrasados ou não foram executados.

### Checklist de verificação

- verificar se o parâmetro **SERVERHOSTSCHED** está vazio
- verificar se o servidor de aplicação está funcionando corretamente
- confirmar se as contas estão credenciadas e ativas
- caso persista, acionar o suporte técnico para análise de logs

---

## Contas sem ocorrência de remessa

A conta não possui a configuração mínima de ocorrências necessária para operar o Boleto Rápido.

Isso pode impedir:

- envio de boletos
- alterações de títulos
- cancelamentos

### Como configurar

Acesse **Ocorrências de Remessa → Incluir Conta** e configure as ocorrências conforme necessidade.

| Código | Finalidade |
| --- | --- |
| 01 | Entrada |
| 02 | Baixa |
| 03 | Exclusão |
| 99 | Valor de desconto |
| 99 | Abatimento |
| 99 | Abatimento cancelado |
| 99 | Data de vencimento |

![Interface do sistema Sankhya na tela de Ocorrências de Remessa, mostrando o formulário de inclusão de conta e a grade…](https://ajuda.sankhya.com.br/hc/article_attachments/38865034643863)

Exemplo de configuração das **Ocorrências de Remessa**, essencial para habilitar o envio e baixa de boletos.

---

## Boletos não enviados para o serviço

Ocorre quando títulos no ERP não entram corretamente no fluxo do Boleto Rápido.

### Situações mais comuns

#### Título com boleto gerado, mas sem registro no sistema

O boleto possui:

- Nosso Número
- Código de Barras
- Linha Digitável

Porém não existe registro correspondente no sistema.

**O que fazer**

- confirmar se a conta está credenciada
- confirmar se existem ocorrências configuradas
- se necessário, renegociar o título e gerar um novo boleto

---

#### Registro pendente de envio

O registro foi criado, mas ainda não foi enviado ao banco.

Onde verificar:

**Acompanhamento do Boleto → painel de status**

**Ação recomendada**

- validar credenciamento da conta
- confirmar execução dos jobs
- reprocessar o registro

---

#### Aguardando processamento

O envio foi solicitado e está na fila de processamento.

**Ação recomendada**

- aguardar o processamento
- confirmar execução dos jobs
- caso permaneça parado por muito tempo, acionar suporte

---

#### Erro retornado pelo banco

O banco retornou uma rejeição ou erro técnico.

### Como tratar

1. Acesse **Acompanhamento do Boleto**
2. Abra os detalhes do registro
3. Consulte a mensagem de retorno do banco
4. Ajuste a inconsistência indicada
5. Reprocesse o registro

---

## Conta com credenciamento incompleto

O credenciamento foi iniciado, mas não foi concluído.

**Ação recomendada**

- repetir o credenciamento
- confirmar o status **Ativa / Credenciada**

---

# 🟢 Status normal (Verde)

Indica que o serviço está operando normalmente.

O sistema valida automaticamente:

- contas bancárias credenciadas
- envio e registro de boletos
- retornos bancários
- execução de jobs
- processamento de baixas automáticas

**Nenhuma ação é necessária.**

![Ícone de check branco dentro de um círculo verde sólido, indicando que o diagnóstico do serviço está saudável e sem…](https://ajuda.sankhya.com.br/hc/article_attachments/38865034645399)

O status **Saudável** confirma que todos os processos automáticos estão operando conforme o esperado nos últimos 30 dias.

---

# ⚪ Inatividade / sem uso (Cinza)

Esse status indica ausência de utilização recente do serviço.

Pode ocorrer quando:

- o cliente nunca utilizou o Boleto Rápido
- o credenciamento inicial ainda não foi iniciado
- não houve emissão ou registro de boletos nos últimos 30 dias

Isso **não representa um erro**, apenas ausência de uso.

![Ilustração de um rosto triste em tons de cinza com a mensagem "Serviço não contratado", indicando ausência de atividade…](https://ajuda.sankhya.com.br/hc/article_attachments/38865063656855)

O status **Cinza** é exibido quando não há registros de uso ou o credenciamento ainda não foi iniciado

---

**Dica:** Para informações sobre modelos de contratação e custos, consulte o artigo [Detalhes de cobrança de serviço do Boleto rápido](https://ajuda.sankhya.com.br/hc/pt-br/articles/14550240434839-Detalhes-de-cobran%C3%A7a-de-servi%C3%A7o-do-Boleto-r%C3%A1pido).

---

> 📌Conheça mais [Cartões Inteligentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044355393-Cart%C3%B5es-Inteligentes#h_01KK2GB7X9R8E27DYCHM2NEY81)!
