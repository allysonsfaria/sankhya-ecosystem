---
id: "4410110448919"
titulo: "Como é formada a Chave de Acesso de uma NF-e/NFC-e?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4410110448919-Como-%C3%A9-formada-a-Chave-de-Acesso-de-uma-NF-e-NFC-e"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:21:21Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Identificação única da NF-e", "Evita duplicidades e facilita controle", "Detalhes como UF CNPJ modelo série e número", "Documentos Eletrônicos"]
---

# Como é formada a Chave de Acesso de uma NF-e/NFC-e?

#### Imagem 1: Introdução Introdução

A chave de acesso para uma NF-e  é uma sequência de números que é utilizada para identificar as notas fiscais eletrônicas. De tal modo, é possível que existam duas notas com números idênticos no arquivo .XML e no Documento Auxiliar da Nota Fiscal eletrônica (Danfe), mas jamais existirá duas chaves de acesso iguais.

Logo, é a chave que irá distinguir uma NF-e de outra. Essa funcionalidade foi criada para garantir mais segurança e agilidade para os registros das operações comerciais realizadas. Na caso concreto, ela funcionaria como uma identidade da nota trazendo a verdadeira face ao documento, evitando eventuais confusões no momento de identificação e facilitando a organização e o arquivamento.

#### Imagem 2: Formação da chave de acesso Formação da chave de acesso

A chave de acesso a nota fiscal eletrônica é composta pelas seguintes informações:

- **cUF -** Código da UF do emitente do Documento Fiscal;
- **AAMM -** Ano e Mês de emissão da NF-e;
- **CNPJ -** CNPJ do emitente;
- **mod -** Modelo do Documento Fiscal;
- **serie -** Série do Documento Fiscal;
- **nNF -** Número do Documento Fiscal;
- **tpEmis –** forma de emissão da NF-e;
- **cNF -** Código Numérico que compõe a Chave de Acesso;
- **cDV -** Dígito Verificador da Chave de Acesso.

|  | **Código da UF** | **AAMM da emissão** | **CNPJ do emitente** | **Modelo** | **Série** | **Número da NF-e** | **Forma de emissão da NF-e** | **Código numérico** | **DV** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Quantidade de** **caracteres** | 02 | 04 | 14 | 02 | 03 | 09 | 01 | 08 | 01 |
