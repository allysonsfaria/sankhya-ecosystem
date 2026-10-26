---
id: "41605230701079"
titulo: "Processo DeRE — Declaração de Regimes Específicos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Comece por aqui > Processos do Portal da Reforma Tributária"
atualizado_em: "2026-10-21T14:36:39Z"
rotulos: ["Configuração", "XML", "Impostos", "Reforma Tributária", "br.com.sankhya.mgeliv.reforma.portal", "Documentos Eletrônicos", "DeRE"]
---

# Processo DeRE — Declaração de Regimes Específicos

**Módulo:** Portal da Reforma Tributária › DeRE
**Caminho de acesso:** Portal da Reforma Tributária › DeRE
**Versão mínima SankhyaOm 4.36:** 4.36b88 + erpcore-module 5.9.5
**Versão mínima SankhyaOm 4.35:** 4.35b777
**Versão mínima Livros:** 5.38.0
**Versão mínima Livros para envio em Produção:** 5.50

---

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#antes-de-comecar)
- [Habilitação de módulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#habilitacao-modulos)
- [Como funciona a estrutura de eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#estrutura-eventos)
- [Credenciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#credenciais)
- [Histórico de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#historico-eventos)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#faq)

## O que é e para que serve

O módulo DeRE no Portal da Reforma Tributária é o ponto central para cumprir a Declaração de Regimes Específicos (DeRE), obrigação acessória instituída pela Lei Complementar nº 214/2025 para apuração do IBS e CBS em setores com regras tributárias diferenciadas. Por meio dele, você gera, assina digitalmente e transmite os eventos obrigatórios à Receita Federal, além de acompanhar o status de cada envio com rastreabilidade completa dentro do Sankhya Om.

**💡 Dica**

Para mais informações sobre a DeRE, consulte o [site oficial da Declaração de Regimes Específicos](https://www.gov.br/sped/pt-br/assuntos/documentos-fiscais/dere).

## Antes de começar

Para que as empresas apareçam no módulo DeRE, o Administrador do sistema precisa habilitar o módulo DeRE para cada empresa na tela Portal da Reforma Tributária › Configurações › Empresas. Empresas sem habilitação não aparecem em nenhuma tela do módulo, independentemente do regime tributário cadastrado no ERP.

Para transmitir eventos, você também precisa configurar as credenciais do Receita Integra da empresa para o ambiente desejado, conforme descrito em [Credenciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#credenciais), e ter o certificado digital ICP-Brasil A1 do mesmo CNPJ. Para enviar eventos no ambiente **1 – Produção**, o Livros precisa estar na versão 5.50 ou superior.

**💡 Dica**

Para instruções completas sobre como habilitar o módulo DeRE por empresa, acesse [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#sumario)

## Habilitação de módulos

Além da DeRE, o Portal da Reforma Tributária reúne outros módulos que o Administrador do sistema pode habilitar conforme a necessidade da empresa, como a DeRE, Assistente de Configuração Integral e Assistente de Configuração de Exceções. Cada módulo possui sua própria tela e seu artigo de documentação específico, acessíveis a partir do Portal da Reforma Tributária.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#sumario)

## Como funciona a estrutura de eventos

A DeRE é transmitida por meio de eventos eletrônicos em formato XML, assinados digitalmente com certificado ICP-Brasil. Cada tipo de evento tem uma finalidade específica e segue uma ordem obrigatória de envio: nenhum evento periódico pode ser transmitido sem que o D-1001 esteja processado com sucesso para o mesmo CNPJ raiz.

No Sankhya Om, cada tipo de evento tem seu próprio artigo de documentação com o passo a passo completo. Confira abaixo os eventos disponíveis:

- [DeRE — Evento D-1001: Informações do Contribuinte](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#sumario)

## Credenciais

A tela **Credenciais do Receita Integra**, acessível em **Portal da Reforma Tributária › DeRE › Credenciais**, armazena o Client\_ID e o Client\_Secret fornecidos pelo Receita Integra para cada empresa e ambiente, e define o ambiente ativo: o ambiente da Receita Federal para onde os eventos da empresa são transmitidos. Configure as credenciais antes de transmitir os eventos.

### Colunas da grade

- **Cód. Empresa** — código interno da empresa no ERP.
- **Razão Social** — nome da empresa.
- **CNPJ** — CNPJ completo da empresa.
- **Ambiente Ativo** — ambiente para onde os eventos da empresa são transmitidos: **1 – Produção** ou **2 – Produção Restrita**.
- **Credencial (Produção)** — exibe **Configurada** quando a empresa tem credencial cadastrada para Produção.
- **Credencial (Produção Restrita)** — exibe **Configurada** quando a empresa tem credencial cadastrada para Produção Restrita.

### Filtros disponíveis

Você pode combinar os filtros **Empresa**, **Ambiente ativo** e **Credencial** para localizar empresas específicas na grade.

### Como configurar as credenciais

1. Marque na grade as empresas que deseja configurar. O sistema exibe a quantidade de empresas selecionadas e o botão **Configurar credenciais**.
2. Clique em **Configurar credenciais**.
3. Na etapa **Revisão**, confira os dados cadastrais da empresa: **CNPJ**, **CNPJ raiz (declarante)**, **Logradouro**, **Município** e **CEP**. Esses dados não são editáveis nesta tela; se algum estiver incorreto, corrija no cadastro da empresa no ERP. Clique em **Continuar**.
4. Na etapa **Credenciais**, selecione o **Ambiente DeRE** e preencha os campos **Client\_ID** e **Client\_Secret** com os dados fornecidos pelo Receita Integra.
5. Clique em **Salvar**. A coluna **Ambiente Ativo** passa a exibir o ambiente selecionado.

Em qualquer etapa, clique em **Voltar** para retornar à etapa anterior.

Campos da etapa **Credenciais**:

- **Client\_ID** — identificador da credencial fornecido pelo Receita Integra para o ambiente selecionado.
- **Client\_Secret** — chave secreta da credencial. Por segurança, o valor nunca é reexibido em tela; se você não alterar o campo, o sistema mantém o valor já cadastrado.

#### Ambiente DeRE

**O que faz**

Define o ambiente da Receita Federal para onde os eventos da DeRE da empresa são transmitidos.

**Quando usar**

Use **1 – Produção** para cumprir a obrigação acessória com validade fiscal. Use **2 – Produção Restrita** para homologar transmissões, sem validade fiscal.

**Como funciona**

Cada ambiente tem seu próprio par de Client\_ID e Client\_Secret. Ao selecionar um ambiente, informe as credenciais correspondentes a ele. Quando o ambiente selecionado já tem credencial configurada, o sistema mantém os dados cadastrados, a menos que você altere o Client\_Secret.

**Impacto no sistema**

O wizard do D-1001 transmite os eventos para o ambiente ativo da empresa. A coluna **Ambiente** do Histórico de Eventos registra o ambiente de cada evento, e o painel D-1001 exibe o status separadamente para cada ambiente.

**🚨 Risco operacional**

Eventos transmitidos com o ambiente **1 – Produção** têm validade fiscal perante a Receita Federal. Confira o ambiente ativo da empresa antes de concluir um envio.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#sumario)

## Histórico de Eventos

A tela Histórico de Eventos DeRE, acessível em [Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria) › DeRE › Histórico de Eventos, reúne todos os eventos transmitidos e permite acompanhar o status de cada envio, obter o recibo definitivo, baixar os XMLs gerados e excluir registros quando necessário.

### Colunas da grade

- **Cód. Empresa** — código interno da empresa no ERP.
- **Razão Social** — nome da empresa.
- **CNPJ** — CNPJ completo da empresa.
- **Evento** — código do evento transmitido (ex.: D-1001).
- **Operação** — tipo da operação realizada: Inclusão, Alteração ou Exclusão.
- **Status** — situação do evento: Enviado (verde), Processando (amarelo), Rejeitado (vermelho) ou Não enviado (cinza).
- **Ambiente** — ambiente para onde o evento foi transmitido: **1 – Produção** ou **2 – Produção Restrita (Homologação)**.
- **Data/Hora** — data e hora em que o evento foi gerado no sistema.

### Filtros disponíveis

Você pode combinar os filtros Empresa, Período, Status, Tipo do evento, Operação, Ambiente e Recibo para localizar eventos específicos na grade.

### Ações disponíveis

- **Atualizar** — consulta a Receita Federal para obter o resultado do processamento do evento. Disponível somente para eventos com status Processando. Quando a declaração é aceita, o sistema registra o recibo definitivo e o status muda para Enviado; quando é recusada, o status muda para Rejeitado.
- **Visualizar ocorrências** — exibe as ocorrências retornadas pela Receita Federal na resposta do envio.
- **Histórico de tentativas** — abre o pop-up **Histórico de tentativas**, que lista cada tentativa de envio do evento com informações como **Tentativa**, **ID Único**, **Lote** e **Protocolo (recebimento)**.
- **Baixar Envio** — faz o download do XML gerado no momento do envio do evento.
- **Baixar Retorno** — faz o download do XML de retorno recebido da Receita Federal, quando disponível.
- **Excluir** — remove o registro do histórico. Disponível somente para eventos sem recibo de processamento nesta versão.

**ℹ️ Nota**

Você consegue atualizar eventos transmitidos em **1 – Produção** e em **2 – Produção Restrita**, independentemente do ambiente ativo configurado para a empresa em [Credenciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#credenciais).

#### Limpar dados de teste

**O que faz**

Remove, na Receita Federal e no Sankhya Om, todos os eventos e lotes transmitidos em **2 – Produção Restrita** para a empresa.

**Quando usar**

Use quando quiser descartar os envios de homologação da empresa.

**Como funciona**

O botão só fica habilitado para eventos transmitidos em **2 – Produção Restrita**. Ao clicar, o sistema exibe "Esta operação remove, na Receita Federal E no Sankhya, todos os eventos de Produção Restrita desta empresa. É IRREVERSÍVEL. Deseja continuar?". Clique em **Sim** para confirmar ou em **Não** para cancelar. Após a remoção, o sistema informa a quantidade de eventos e lotes removidos, por exemplo: "2 evento(s) e 2 lote(s) de Produção Restrita removidos."

**Impacto no sistema**

Os eventos de 1 – Produção não são afetados.

**🚨 Risco operacional**

A remoção é permanente e não pode ser desfeita: todos os eventos de Produção Restrita da empresa são apagados, não apenas o evento selecionado.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#sumario)

## Perguntas frequentes

### Os eventos enviados em Produção Restrita têm validade fiscal?

Não. O ambiente **2 – Produção Restrita** serve para homologação e não cumpre a obrigação acessória. Para obter o recibo definitivo, configure **1 – Produção** em [Credenciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos#credenciais) e transmita os eventos nesse ambiente.

### Como obtenho o recibo definitivo de um evento?

Após a transmissão, o evento fica com status Processando. No Histórico de Eventos, selecione o evento e clique em **Atualizar**. Quando a Receita Federal aceita a declaração, o sistema registra o recibo e o status muda para Enviado.

### Por que uma empresa não aparece no módulo DeRE?

A empresa precisa ter o módulo DeRE habilitado pelo Administrador do sistema em Configurações › Empresas. Sem essa habilitação, a empresa não aparece em nenhuma tela do módulo, mesmo que tenha regime tributário cadastrado no ERP. Acesse [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria) para instruções.

### Quem está obrigado a transmitir a DeRE?

Estão obrigados os prestadores de serviços financeiros, as operadoras de planos de assistência à saúde (incluindo planos funerários e de saúde animal) e as entidades que explorem concursos de prognósticos. Empresas do Simples Nacional estão dispensadas, salvo opção pelo regime regular de IBS/CBS.
