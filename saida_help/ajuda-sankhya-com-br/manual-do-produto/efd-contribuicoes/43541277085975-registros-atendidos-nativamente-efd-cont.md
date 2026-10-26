---
id: "43541277085975"
titulo: "Registros atendidos nativamente - EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43541277085975-Registros-atendidos-nativamente-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD Contribuições"
atualizado_em: "2026-09-30T11:14:49Z"
---

# Registros atendidos nativamente - EFD Contribuições

Este artigo apresenta o **mapa de registros da EFD-Contribuições**, organizado por bloco e na mesma sequência em que os registros aparecem no arquivo digital. Use-o como referência rápida para identificar a que informação cada registro corresponde, conferir se a escrituração do período contém os registros esperados e localizar a origem de uma inconsistência apontada na validação do arquivo.

A estrutura segue a ordem do layout: abertura e identificação da pessoa jurídica e tabelas de cadastro (**Bloco 0**), documentos fiscais de serviços e mercadorias (**Blocos A, C, D e F**), apuração das contribuições e dos créditos de PIS/PASEP e COFINS (**Bloco M**), outras informações (**Bloco 1**) e controle e encerramento do arquivo (**Bloco 9**).

**Observação:** nem todos os registros abaixo são gerados em todas as escriturações. A presença de cada um depende das operações realizadas no período, do regime de apuração adotado e das configurações da empresa.

| Tipo | Registro | Descrição |
| --- | --- | --- |
| **Abertura, Identificação e Referências** | **0000** | Abertura do Arquivo Digital e Identificação da Pessoa Jurídica |
| **0001** | Abertura do Bloco 0 |
| **0100** | Dados do Contabilista |
| **0110** | Regimes de Apuração da Contribuição Social e de Apropriação de Crédito |
| **0140** | Tabela de Cadastro de Estabelecimento |
| **0150** | Tabela de Cadastro do Participante |
| **0190** | Identificação das Unidades de Medida |
| **0200** | Tabela de Identificação do Item (Produtos e Serviços) |
| **0400** | Tabela de Natureza da Operação/Prestação |
| **0450** | Tabela de Informação Complementar do Documento Fiscal |
| **0500** | Plano de Contas Contábeis |
| **0990** | Encerramento do Bloco 0 |
| **Escrituração e Apuração do ISS** | **A001** | Abertura do Bloco A |
| **Encerramento do Bloco A** | **A990** | Encerramento do Bloco A |
| **Documentos Fiscais I – Mercadorias** | **C001** | Abertura do Bloco C |
| **C010** | Identificação do Estabelecimento |
| **C100** | Documento – Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04) e NF-e (código 55) |
| **C110** | Complemento do Documento – Informação Complementar da Nota Fiscal (códigos 01, 1B, 04 e 55) |
| **C170** | Complemento do Documento – Itens do Documento (códigos 01, 1B, 04 e 55) |
| **C990** | Encerramento do Bloco C |
| **Documentos Fiscais II – Serviços (ICMS)** | **D001** | Abertura do Bloco D |
| **Encerramento do Bloco D** | **D990** | Encerramento do Bloco D |
| **Abertura do Bloco F** | **F001** | Abertura do Bloco F |
| **Identificação do Estabelecimento** | **F010** | Identificação do Estabelecimento |
| **Demais Documentos e Operações Geradoras de Contribuição e Créditos** | **F100** | Demais Documentos e Operações Geradoras de Contribuição e Créditos |
| **Encerramento do Bloco F** | **F990** | Encerramento do Bloco F |
| **Abertura do Bloco M** | **M001** | Abertura do Bloco M |
| **Apuração da Contribuição e Crédito de PIS/PASEP e da COFINS** | **M100** | Crédito de PIS/Pasep Relativo ao Período Apenas com os dados/valores das devoluções de compras, quando tem ajuste. |
| **M110** | Ajustes do Crédito de PIS/Pasep Apurado |
| **M115** | Detalhamento dos Ajustes do Crédito de PIS/Pasep Apurado |
| **M500** | Crédito de Cofins Relativo ao Período |
| **M510** | Ajustes do Crédito de Cofins Apurado |
| **M515** | Detalhamento dos Ajustes do Crédito de Cofins Apurado |
| **Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, ou Sujeitas à Alíquota Zero (CST 04, 06, 07, 08 e 09)** | **M400** | Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou Substituição Tributária (PIS/PASEP) |
| **Detalhamento das Receitas Isentas/Não Alcançadas/Alíquota Zero** | **M410** | Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero (PIS/PASEP) |
| **Consolidação da Contribuição para o PIS/PASEP** | **M800** | Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou Substituição Tributária (COFINS) |
| **Consolidação da Contribuição para o PIS/PASEP – Detalhamento por Código de Recolhimento** | **M810** | Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero (COFINS) |
| **Encerramento do Bloco M** | **M990** | Encerramento do Bloco M |
| **Outras Informações** | **1001** | Abertura do Bloco 1 |
| **1990** | Encerramento do Bloco 1 |
| **Controle e Encerramento do Arquivo Digital** | **9001** | Abertura do Bloco 9 |
| **9900** | Registros do Arquivo |
| **9990** | Encerramento do Bloco 9 |
| **9999** | Encerramento do Arquivo Digital |
