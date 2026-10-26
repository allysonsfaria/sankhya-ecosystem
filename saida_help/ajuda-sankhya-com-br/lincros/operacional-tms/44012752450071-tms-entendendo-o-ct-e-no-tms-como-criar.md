---
id: "44012752450071"
titulo: "[TMS] - Entendendo o CT-e no TMS: Como Criar, Importar, Validar e Gerenciar CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012752450071--TMS-Entendendo-o-CT-e-no-TMS-Como-Criar-Importar-Validar-e-Gerenciar-CT-e"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:38:11Z"
rotulos: ["sync_hc", "lincros", "lincros_13433249", "sync_hash_b5bdad11a4c5"]
---

# [TMS] - Entendendo o CT-e no TMS: Como Criar, Importar, Validar e Gerenciar CT-e

## 1. Problema Relatado pelo Cliente

O cliente necessita entender como criar, importar, validar e gerenciar Conhecimentos de Transporte Eletrônicos (CT-es) na plataforma, garantindo que os documentos fiscais relacionados ao transporte de cargas sejam corretamente registrados, validados e integrados ao sistema TMS. As dúvidas incluem desde os formatos de arquivos aceitos (XML, EDI), procedimentos de importação, ações disponíveis na plataforma, até informações importantes sobre status de importação e integração, além do entendimento completo sobre a tela de pesquisa de CT-e.

---

## 2. Importação e gerenciamento do CT-e

## 2.1. Formas de Criação do CT-e na Plataforma

Os CT-es podem ser criados na plataforma utilizando três métodos distintos:

- **Importação do arquivo XML:** versão digital do Conhecimento de Transporte.
- **Importação do arquivo EDI CONEMB:** arquivo em formato .txt contendo as informações do CT-e.
- **Criação manual:** realizada diretamente através do Portal do Transportador.

---

## 2.2. Envio de Arquivo XML

O arquivo XML pode ser importado:

- Por e-mail através do endereço padrão de importação.
- Manualmente pelo menu:
  **Operacional > Importação > CT-e > Importação**

---

## 2.3. Envio de Arquivo EDI

O arquivo EDI (Eletronic Data Interchange) CONEMB também pode ser importado:

- Por e-mail através do endereço padrão de importação.
- Manualmente pelo menu:
  **Operacional > Importação > EDI > Importação**

**Observação importante:**
A geração do arquivo EDI CONEMB é responsabilidade das transportadoras. Para que a importação seja bem-sucedida, o arquivo deve seguir um layout específico, que pode ser parametrizado no cadastro da transportadora, através do menu:
**Cadastros Gerais > Transportadoras > Transportadora (Empresa)**

**Layouts de arquivos EDI aceitos:**
A plataforma adota dois layouts padronizados pelo PROCEDA:

- PROCEDA 3.0
- PROCEDA 3.1

---

## 2.4. Criação Manual via Portal do Transportador

O Portal do Transportador é um módulo com acesso restrito a usuários com perfil específico, destinado às transportadoras parceiras.

**Funções disponíveis:**

- Importação de arquivos XML ou EDI.
- Criação de Conhecimentos de Frete através de Notas Fiscais de Serviço, especialmente para transportes realizados dentro da mesma cidade.

**Menu de acesso:**
**Operacional > Conhecimentos de Frete > CT-es**

---

## 2.5. Ações Disponíveis na Tela do CT-e

Na tela do CT-e, é possível executar diversas ações para ajuste e validação dos documentos:

- **Escriturar:**
  Envia o CT-e para o ERP do cliente, registrando-o oficialmente no sistema fiscal e contábil.
- **Validar:**
  Realiza a validação do CT-e na Secretaria da Fazenda (SEFAZ). Esse processo exige que o Certificado Digital esteja previamente configurado no ambiente do TMS.
- **Reprocessar:**
  Refaz o processamento do arquivo EDI ou XML que deu origem a este registro de CT-e, útil quando ajustes são realizados no layout ou nos dados do arquivo, ou para reprocessar um arquivo corrigido que havia dado erro de importação.
- **Anular:**
  Altera o status do CT-e para "Anulado" dentro da plataforma, sem impactar diretamente o status na SEFAZ.
- **Reabrir:**
  Reabre um CT-e que foi anteriormente anulado.
- **Tratar erro:**
  Ação específica para solucionar erros detectados no processamento ou integração do CT-e.
- **Forçar sucesso:**
  Força a alteração do status de integração para "Sucesso", geralmente utilizado após validações manuais garantindo que de fato o registro foi integrado ao ERP.
- **Download XML:**
  Permite o download do arquivo XML original do CT-e, geralmente gerado em um arquivo .zip, ou do arquivo EDI CONEMB, caso este tenha dado origem ao CT-e.
- **DACTE:**
  Gera o Documento Auxiliar do Conhecimento de Transporte Eletrônico (DACTE) em PDF, abrindo para visualização e download. Este DACTE é um arquivo gerado dentro da estrutura do TMS, e não é o DACTE original da SEFAZ.
- **Reverter integração:**
  Desfaz a integração do CT-e com o ERP, permitindo uma nova tentativa ou correção de algum dado.

---

## 2.6. Informações Importantes Disponíveis na Aba “Cadastro” do CT-e

- A aba **Cadastro** reúne todos os dados essenciais relacionados ao CT-e (Conhecimento de Transporte Eletrônico).

  ## Geral

  - **Número:**
    → Número sequencial do CT-e, gerado automaticamente pelo sistema.
  - **Série:**
    → Identificação da série do documento fiscal.
  - **Chave:**
    → Chave de acesso do CT-e, composta por 44 dígitos, utilizada para consulta e validação do documento.
  - **Tipo:**
    → Tipo de CT-e emitido, como Normal e Complementar.
  - **Alíquota ICMS:**
    → Percentual de ICMS aplicado na operação.
  - **Base Cálculo ICMS:**
    → Valor sobre o qual foi calculado o ICMS.
  - **Valor do ICMS:**
    → Total do ICMS apurado na operação.
  - **CST:**
    → Código de Situação Tributária (CST)..
  - **CFOP:**
    → Código Fiscal de Operações e Prestações.
  - **Protocolo:**
    → Número do protocolo de autorização do CT-e, atribuído pela SEFAZ.
  - **Tipo Tomador:**
    → Indica quem é o responsável pelo pagamento do frete
  - **Tipo Sefaz:**
    → Indica a natureza específica do documento perante a SEFAZ, se Normal ou de Complemento de Valores, por exemplo.
- ---

  ## Transporte

  - **Conhecimento:**
    → Número do pré-conhecimento em que o CT-e está vinculado.
  - **Transportadora:**
    → Razão social da transportadora emissora deste CT-e.
  - **Filial:**
    → CNPJ e nome da filial da transportadora emissora deste CT-e.
  - **Emissão:**
    → Data e horário em que o CT-e foi emitido junto a SEFAZ.
  - **Tipo:**
    → eletrônico: Indica se o CT-e foi emitido eletronicamente. → serviço: Indica que este registro se trata de uma Nota Fiscal de Serviço (NFS).
  - **Situação:**
    → Status atual do faturamento do CT-e (Faturado, Não Faturado).
- ---

  ## Fatura

  - **Código:**
    → Número da fatura em que este CT-e está vinculado
  - **Situação:**
    → Situação atual da fatura (gerada, conferida, aceita, paga)
- ---

  ## Importação

  - **Situação:**
    → Status da importação do XML do CT-e ou do CONEMB.
  - **Data importação:**
    → Data e horário em que a importação foi efetuada no sistema.
  - **Mensagem importação:**
    → Alerta indicando se foi identificado algum problema ou divergência no momento da importação do CT-e no TMS.
- ---

  ## Validação Legal

  - **Versão XML do CT-e:**
    → Versão do layout XML utilizada para gerar o CT-e.
  - **Situação:**
    → Situação da consulta legal do registro na SEFAZ (requer Certificado Digital da empresa cadastrado na plataforma).
- ---

  ## Integração

  - **Situação:**
    → Informa se este registro foi integrado ou não ao ERP.
- ---

  ## Notas Fiscais Vinculadas
- ## → Indica qual ou quais notas fiscais estão vinculadas a este CT-e.

---

## 3. Filtros e Colunas de Pesquisa

Facilita a localização de CT-es específicos por critérios como:
**Chave, Número, Série, Emissão, CNPJ, Transportadora, Remetente, Destinatário, Pré-conhecimento, Situação, Fatura, Situação Conhecimento, Tipo, Importação, Integração.**

Cada campo pode ser preenchido ou selecionado para refinar a busca.

---

## 4. Descrição das Colunas Apresentadas na Tela de Pesquisa do CT-e

- **Chave:** Chave de acesso do CT-e, código numérico único de identificação fiscal do documento.
- **Número:** Número sequencial do CT-e, conforme informado no documento fiscal.
- **Série:** Série numérica que compõe, junto com o número, a identificação do CT-e.
- **Emissão:** Data de emissão do CT-e, conforme consta no arquivo XML ou EDI.
- **CNPJ Emissor:** Número do CNPJ da transportadora ou empresa que emitiu o CT-e.
- **Transportadora:** Nome da transportadora responsável pela emissão ou transporte da carga.
- **Remetente:** Empresa ou pessoa física responsável pelo envio da mercadoria.
- **Destinatário:** Empresa ou pessoa física que receberá a mercadoria transportada.
- **Pré-conhecimento:** Código interno que vincula o CT-e a um pré-conhecimento, utilizado para rastreio e conferência de processos.
- **Situação:** Estado atual de faturamento do CT-e. Exemplo: Não Faturado, Faturado.
- **Fatura:** Número da fatura gerada para o CT-e, vinculado ao processo financeiro.
- **Situação Conhecimento:** Status logístico do pré-conhecimento vinculado a este CT-e. Exemplo: Transportado, Em transporte.
- **Tipo:** Se Eletrônico ou Serviço (NFS-e).
- **Importação:** Indicador visual da situação da importação do CT-e no TMS.
- **Integração:** Indicador visual da situação de integração com o ERP ou outro sistema.
- **Valor Calculado:** Valor do frete calculado pelo TMS, de acordo com a tabela de frete vinculada ao pré-conhecimento deste CT-e.
- **Valor Realizado:** Valor do frete informado no CT-e pela transportadora.

---

## 5. Linhas de CT-es

Cada linha corresponde a um CT-e individual, com todas as informações associadas. É possível selecionar múltiplas linhas utilizando as caixas de seleção à esquerda para executar ações em lote (como Escriturar ou Validar), além de exportar os registros em arquivo PDF ou Excel/CSV.

---

## 6. Filtros Avançados e Visão

No canto superior direito:

- **Filtros:**
  Permite ativar ou ocultar filtros adicionais, facilitando a segmentação dos CT-es na tela.
- **Colunas:**
  Permite personalizar a exibição, ocultando ou mostrando colunas conforme a necessidade do usuário.
- **Visão:**
  Permite salvar configurações de filtros e colunas como "visões" personalizadas, úteis para diferentes perfis de operação (ex.: Faturamento, Logística, Controladoria).

---

## 6.1. Filtros Avançados - Explicação de Cada Campo

- **Unidade:**
  Filtra os CT-es vinculados a uma unidade específica da empresa, conforme estrutura organizacional cadastrada no sistema.
- **Grupo de unidades:**
  Permite buscar CT-es considerando um agrupamento de unidades, útil para empresas com múltiplos CNPJs ou filiais.
- **Remetente:**
  Filtro para localizar CT-es associados a um remetente específico, seja pessoa jurídica ou física.
- **Destinatário:**
  Permite localizar CT-es destinados a uma empresa ou pessoa específica.
- **Segmento do remetente:**
  Define o critério de busca para o segmento do remetente:
  ➔ Contido em: busca parcial dentro do nome ou segmento.
  ➔ Igual a: busca exata pelo segmento.
  ➔ Começa com: busca pelo início do nome ou código.
- **Segmento do destinatário:**
  Idêntico ao campo anterior, mas referente ao destinatário. Útil para buscar CT-es de destinatários pertencentes a um mesmo segmento de mercado.
- **Transportadora:**
  Filtra CT-es emitidos ou transportados por uma transportadora específica. Pode ser preenchido com nome ou código da transportadora.
- **Emissão:**
  Permite filtrar CT-es por um intervalo de datas de emissão. Ex.: De 25/05/2025 até 26/05/2025. Por padrão, o sistema sempre vai listar os CT-es do dia anterior em diante.
- **Data da última importação:**
  Filtra os CT-es conforme a data da última importação do arquivo XML ou EDI. Muito utilizado para monitorar importações recentes.
- **Data de pagamento:**
  Filtra os CT-es pela data de pagamento relacionada à fatura.
- **Chave:**
  Filtro para buscar pela chave de acesso do CT-e, com critérios:
  ➔ Começa com
  ➔ É igual a
  ➔ Contém
- **Número:**
  Filtra os CT-es pelo número específico atribuído no momento da emissão.
- **Série:**
  Permite filtrar por série do CT-e, com as mesmas opções de critério (começa com, igual a etc.).
- **CNPJ Emissor:**
  Filtra os CT-es emitidos por um CNPJ específico. Critérios de busca: começa com, igual a etc.
- **Pré-conhecimento:**
  Permite buscar CT-e vinculado a um pré-conhecimento específico, identificando facilmente documentos relacionados a processos internos ou embarques.
- **Número da fatura:**
  Filtra pela fatura gerada para aquele CT-e, útil para conciliações financeiras.
- **Data de integração:**
  Filtra CT-es conforme a data em que foram integrados com o ERP.
- **Natureza da operação:**
  Permite buscar CT-es segundo a natureza de operação cadastrada.
- **Somente divergências:**
  Checkbox que, quando marcado, exibe apenas os CT-es que apresentam divergências entre o valor calculado pelo TMS e o valor informado no CT-e pela transportadora.
