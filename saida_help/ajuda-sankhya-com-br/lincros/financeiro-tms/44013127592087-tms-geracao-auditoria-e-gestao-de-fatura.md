---
id: "44013127592087"
titulo: "[TMS] - Geração, Auditoria e Gestão de Faturas no TMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013127592087--TMS-Gera%C3%A7%C3%A3o-Auditoria-e-Gest%C3%A3o-de-Faturas-no-TMS"
trilha: "Lincros > TMS > Financeiro - TMS"
atualizado_em: "2026-10-05T19:48:17Z"
rotulos: ["sync_hc", "lincros", "lincros_13432940", "sync_hash_fef63c350c0a"]
---

# [TMS] - Geração, Auditoria e Gestão de Faturas no TMS

**1 - Problema Relatado pelo Cliente:**
Este artigo explica como é a funcionalidade de Faturas do TMS, além de explicar situações onde a fatura enviada pela transportadora não é localizada na plataforma. Além disso, esclarece sobre o fluxo de auditoria de faturas, inclusão e remoção de CT-es da fatura, resolução de pendências da fatura, e funcionalidades disponíveis para gestão e conferência das faturas.

---

**2 - Passo a Passo para Resolver o Problema:**

## Como a fatura é criada na ferramenta

- A fatura pode ser criada de duas formas:

  - Pelo **Portal do Transportador**;
  - Pelo envio de **EDI (DOCCOB)**, que pode ser transmitido por e-mail, via Webservice ou manualmente pelo portal do embarcador.
- Para que uma fatura seja gerada na plataforma, é indispensável que os **Conhecimentos de Transporte (CT-es ou NFS-es)** estejam disponíveis no TMS.

---

## Fatura não localizada na ferramenta

**1. Validar a importação do arquivo EDI DOCCOB:**

- Acesse: **Operacional > Importação > EDI > Log**.
- Localize o arquivo enviado pela transportadora.
- Verifique a situação do arquivo, que pode ser:

  - **Importado**
  - **Não importado (se estiver nesse status, tente reprocessar o DOCCOB).**
  - **Importado com erros (se estiver nesse status, é necessário entrar nesse registro para verificar quais foram os erros de importação e tratá-los. Depois de ter os erros tratados, basta reprocessar o DOCCOB).**

**2. Ajustar os filtros na tela de Faturas:**

- A tela de faturas, por padrão, exibe apenas as situações: **Gerada, Aceita ou Conferida**.
- Para visualizar faturas em outras situações:

  - Clique no botão **Filtros**;
  - Selecione **todas as situações de faturas**.

---

## O que significam os valores exibidos na fatura

- **Valor calculado:** é a soma dos valores calculados pelo TMS em cada CT-e da fatura, de acordo com as tabelas de frete utilizadas em cada pré-conhecimento vinculado a seu respectivo CT-e, ou de acordo com a Cotação SPOT.
- **Valor realizado:** corresponde à soma dos valores que a transportadora informou nos CT-es ou NFS-es, considerando apenas documentos **não anulados, não cancelados e sem erros de importação**.
- **Valor do desconto:** quando há algum desconto concedido na fatura, este valor é informado no respectivo campo do arquivo DOCCOB.
- **Valor líquido:** resultado da subtração do **Valor realizado** menos o **Valor do desconto**.
- **Valor faturado:** total destacado no arquivo EDI como o valor global da fatura.

  - Observação: o valor faturado, caso esteja errado, só será alterado no sistema se o DOCCOB for corrigido e reimportado no sistema. Ou no Portal do Transportador caso a fatura tenha sido gerada de forma manual pela transportadora.

---

## Como localizar rapidamente CT-es com valores divergentes para auditoria

- Na aba **Conhecimentos eletrônicos**, são listados todos os CT-es vinculados à fatura.
- Para localizar rapidamente divergências:

  - Marque a opção **“Somente divergentes”** — exibe apenas fretes que precisam de auditoria.
  - Também é possível marcar **“Somente não calculados”** — exibe CT-es que não encontraram tabela para cálculo.

---

## Como incluir ou remover CT-es da fatura

- Acesse a aba **Conhecimentos eletrônicos**:

  - Para **remover** CT-es: marque os desejados e clique em **“Remover CT-es”**.
  - Para **adicionar** CT-es: clique em **“Adicionar CT-es”**, e inclua documentos com situação **não faturado** e da **mesma transportadora**.
  - Se a fatura estiver Aceita ou Paga, não será possível remover ou adicionar CT-es.
- Essas funções são úteis após a auditoria, quando é constatada sobra ou falta de CT-es no DOCCOB enviado.

---

## Como resolver pendências para permitir o aceite da fatura

- Se a fatura possui alguma **pendência**, ela não poderá ser aceita até que seja resolvida.
- Para resolver:

  - Acesse a aba **Pendências**;
  - Clique no número da pendência com a situação **“Não iniciada”**;
  - Modifique a situação para **“Resolvida”**;
  - Na aba **Providências**, inclua a justificativa da resolução.
- Todas as providências ficam registradas também na aba **Cadastro**, na opção **“Justificativa de ação”**.

---

## Função dos principais botões na tela de fatura

- **Aceitar:** encaminha a fatura, já conferida, para a fila de integração com o ERP.
- **Rejeitar:** usado para recusar uma fatura quando identificada cobrança indevida.
- **Conferir:** valida se todos os valores estão corretos.
- **Gerar espelho:** gera um relatório detalhado com todas as informações da fatura.
- **Reprocessar CT-es:** corrige possíveis erros de importação ao reprocessar os CT-es.
- **Reverter Integração:** utilizado quando ocorre erro na integração ou se a fatura foi integrada indevidamente; permite ajustar a fatura antes de nova tentativa de integração.
- **Reabrir:** após a reversão da integração, este botão libera a fatura para edição.

---

## Informações adicionais importantes

- **Data de Entrada:** indica a data em que o arquivo foi importado na plataforma.
- **Situação da Fatura:**

  - **Gerada:** DOCCOB processado com sucesso, fatura pronta para auditoria;
  - **Em geração:** DOCCOB ainda está sendo processado;
  - **Rejeitada:** fatura recusada após auditoria;
  - **Aceita:** fatura validada pelo responsável;
  - **Conferida:** fatura conferida e pronta para aceite;
  - **Paga:** fatura já quitada.
- **Responsáveis:** exibe o **CNPJ da Unidade da empresa** responsável pelo pagamento da fatura.
- **Dados Bancários:** contém as informações bancárias para pagamento da fatura.
- **Pré-Faturas:** permite criar um arquivo prévio com a relação de CT-es para que a transportadora emita a fatura.

  - Quando a fatura é criada com base nesse arquivo, a informação estará disponível na aba **Pré-Faturas**.
