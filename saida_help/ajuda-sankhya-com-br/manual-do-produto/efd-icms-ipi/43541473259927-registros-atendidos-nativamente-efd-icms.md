---
id: "43541473259927"
titulo: "Registros atendidos nativamente - EFD ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43541473259927-Registros-atendidos-nativamente-EFD-ICMS-IPI"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD ICMS/IPI"
atualizado_em: "2026-09-30T11:14:44Z"
---

# Registros atendidos nativamente - EFD ICMS/IPI

Este artigo apresenta o **mapa de registros da EFD ICMS/IPI**, organizado por bloco e na mesma sequência em que os registros aparecem no arquivo digital. Use-o como referência rápida para identificar a que informação cada registro corresponde, conferir se a escrituração do período contém os registros esperados e localizar a origem de uma inconsistência apontada na validação do arquivo.

A estrutura segue a ordem do layout: abertura, identificação e tabelas de referência (**Bloco 0**), escrituração e apuração do ISS (**Bloco B**), documentos fiscais de mercadorias e de serviços (**Blocos C e D**), apuração do ICMS e do IPI (**Bloco E**), crédito de ICMS do ativo permanente (**Bloco G**), inventário físico (**Bloco H**), controle da produção e do estoque (**Bloco K**), outras informações (**Bloco 1**) e controle e encerramento do arquivo (**Bloco 9**).

**Observação:** nem todos os registros abaixo são gerados em todas as escriturações. A presença de cada um depende das operações realizadas no período, do perfil de enquadramento (A, B ou C), da legislação da UF e das configurações da empresa.

| Tipo | Registro | Descrição |
| --- | --- | --- |
| **Abertura, Identificação e Referências** | **0000** | Abertura do Arquivo Digital e Identificação da entidade |
| **0001** | Abertura do Bloco 0 |
| **0002** | Classificação do Estabelecimento Industrial ou Equiparado a Industrial |
| **0005** | Dados Complementares da entidade |
| **0015** | Dados do Contribuinte Substituto ou Responsável pelo ICMS Destino |
| **0100** | Dados do Contabilista |
| **0150** | Tabela de Cadastro do Participante |
| **0175** | Alteração da Tabela de Cadastro de Participante |
| **0190** | Identificação das unidades de medida |
| **0200** | Tabela de Identificação do Item (Produtos e Serviços) |
| **0205** | Alteração do Item |
| **0206** | Código de produto conforme Tabela ANP |
| **0210** | Consumo Específico Padronizado |
| **0220** | Fatores de Conversão de Unidades |
| **0221** | Correlação entre Códigos de Itens Comercializados |
| **0300** | Cadastro de bens ou componentes do Ativo Imobilizado |
| **0305** | Informação sobre a Utilização do Bem |
| **0400** | Tabela de Natureza da Operação/Prestação |
| **0450** | Tabela de Informação Complementar do documento fiscal |
| **0460** | Tabela de Observações do Lançamento Fiscal |
| **0500** | Plano de contas contábeis |
| **0600** | Centro de custos |
| **0990** | Encerramento do Bloco 0 |
| **Escrituração e Apuração do ISS** | **B001** | Abertura do Bloco B |
| **B020** | Nota Fiscal (código 01), NF de Serviços (código 03), NF de Serviços Avulsa (código 3B), NF de Produtor (código 04), CT Rodoviário de Cargas (código 08), NF-e (código 55) e NFC-e (código 65) |
| **B025** | Detalhamento por combinação de alíquota e item da lista de serviços da Lei Complementar nº 116/2003 |
| **B420** | Totalização dos valores de serviços prestados por combinação de alíquota e item da lista de serviços da Lei Complementar nº 116/2003 |
| **B440** | Totalização dos valores retidos |
| **B460** | Deduções do ISS |
| **B470** | Apuração do ISS |
| **B990** | Encerramento do Bloco B |
| **Documentos Fiscais I – Mercadorias (ICMS/IPI)** | **C001** | Abertura do Bloco C |
| **C100** | Documento - Nota Fiscal (código 01), NF Avulsa (código 1B), NF de Produtor (código 04), NF-e (código 55) e NF-e para Consumidor Final (código 65) |
| **C101** | Informação complementar dos documentos fiscais quando das operações interestaduais destinadas a consumidor final não contribuinte EC 87/15 (código 55) |
| **C110** | Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55) |
| **C111** | Complemento de Documento - Processo referenciado |
| **C112** | Complemento de Documento - Documento de Arrecadação Referenciado |
| **C113** | Complemento de Documento - Documento Fiscal Referenciado |
| **C114** | Complemento de Documento - Cupom Fiscal Referenciado |
| **C115** | Local de coleta e/ou entrega (códigos 01, 1B e 04) |
| **C116** | Cupom Fiscal Eletrônico - CF-e referenciado |
| **C120** | Complemento de Documento - Operações de Importação (código 01 e 55) |
| **C130** | Complemento de Documento - ISSQN, IRRF e Previdência Social |
| **C140** | Complemento de Documento - Fatura (código 01) |
| **C141** | Complemento de Documento - Vencimento da Fatura (código 01) |
| **C160** | Complemento de Documento - Volumes Transportados (código 01 e 04), exceto combustíveis |
| **C170** | Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55) |
| **C172** | Complemento de Item - Operações com ISSQN (código 01) |
| **C173** | Complemento de Item - Operações com Medicamentos (código 01, 55) |
| **C176** | Complemento de Item - Ressarcimento de ICMS em operações com Substituição Tributária (código 01, 55) |
| **C177** | Complemento de Item – Outras informações (códigos 01 e 55) – válido a partir de 01/01/2019 |
| **C178** | Complemento de Item - Operações com Produtos Sujeitos a Tributação de IPI por Unidade ou Quantidade de produto |
| **C180** | Informações complementares das operações de entrada de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55) |
| **C181** | Informações complementares das operações de devolução de saídas de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55) |
| **C185** | Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55) |
| **C186** | Informações complementares das operações de devolução de entradas de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55) |
| **C190** | Registro Analítico do Documento (código 01, 1B, 04, 55 e 65) |
| **C191** | Informações do Fundo de Combate à Pobreza – FCP – na NF-e (código 55) |
| **C195** | Complemento do Registro Analítico - Observações do Lançamento Fiscal (código 01, 1B, 04 e 55) |
| **C197** | Outras Obrigações Tributárias, Ajustes e Informações provenientes de Documento Fiscal |
| **C300** | Documento - Resumo Diário das Notas Fiscais de Venda a Consumidor (código 02) |
| **C310** | Documentos Cancelados de Nota Fiscal de Venda a Consumidor (código 02) |
| **C320** | Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02) |
| **C321** | Itens dos Resumos Diários dos Documentos (código 02) |
| **C350** | Nota Fiscal de Venda a Consumidor (código 02) |
| **C370** | Itens do documento (código 02) |
| **C390** | Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02) |
| **C400** | Equipamento ECF (código 02, 2D e 60) |
| **C405** | Redução Z (código 02, 2D e 60) |
| **C410** | PIS e COFINS Totalizados no Dia (código 02 e 2D) |
| **C420** | Registro dos Totalizadores Parciais da Redução Z (código 02, 2D e 60) |
| **C425** | Resumo de itens do movimento diário (código 02 e 2D) |
| **C430** | Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (código 02, 2D e 60) |
| **C460** | Documento Fiscal Emitido por ECF (código 02, 2D e 60) |
| **C470** | Itens do Documento Fiscal Emitido por ECF (código 02 e 2D) |
| **C490** | Registro Analítico do movimento diário (código 02, 2D e 60) |
| **C495** | Resumo Mensal de Itens do ECF por Estabelecimento (código 02, 2D e 2E) |
| **C500** | NF/Conta de Energia Elétrica (código 06), NF de Energia Elétrica Eletrônica (código 66), NF/Conta de fornecimento de água canalizada (código 29) e NF/Conta Fornecimento de Gás (código 28) |
| **C510** | Itens do Documento - NF/Conta de Energia Elétrica (código 06), NF/Conta de fornecimento de água canalizada (código 29) e NF/Conta Fornecimento de Gás (código 28) |
| **C590** | Registro Analítico do Documento - NF/Conta de Energia Elétrica (código 06), NF de Energia Elétrica Eletrônica (código 66), NF/Conta de fornecimento de água canalizada (código 29) e NF/Conta Fornecimento de Gás (código 28) |
| **C591** | Informações do Fundo de Combate à Pobreza – FCP na NF3e (código 66) |
| **C595** | Observações do Lançamento Fiscal (códigos 06, 28, 29 e 66) |
| **C597** | Outras obrigações tributárias, ajustes e informações de valores provenientes de documento fiscal |
| **C800** | Registro Cupom Fiscal Eletrônico - CF-e (código 59) |
| **C850** | Registro Analítico do CF-e (código 59) |
| **C855** | Observações do Lançamento Fiscal (código 59) |
| **C857** | Outras Obrigações Tributárias, Ajustes e Informações de Valores Provenientes de Documento Fiscal |
| **C860** | Identificação do equipamento SAT-CF-e (código 59) |
| **C890** | Resumo diário de CF-e (código 59) por equipamento SAT-CF-e |
| **C895** | Observações do Lançamento Fiscal (código 59) |
| **C897** | Outras Obrigações Tributárias, Ajustes e Informações de Valores Provenientes de Documento Fiscal |
| **C990** | Encerramento do Bloco C |
| **Documentos Fiscais II – Serviços (ICMS)** | **D001** | Abertura do Bloco D |
| **D100** | NF de Serviço de Transporte (código 07), CT Rodoviário de Cargas (código 08), CT de Cargas Avulso (código 8B), Aquaviário de Cargas (código 09), Aéreo (código 10), Ferroviário de Cargas (código 11), Multimodal de Cargas (código 26), NF de Transporte Ferroviário de Carga (código 27), CT Eletrônico – CT-e (código 57), CT Eletrônico para Outros Serviços - CT-e OS (código 67) e Bilhete de Passagem Eletrônico (código 63) |
| **D101** | Informação complementar dos documentos fiscais quando das prestações interestaduais destinadas a consumidor final não contribuinte EC 87/15 (código 57 e 67) |
| **D110** | Itens do documento - Nota Fiscal de Serviços de Transporte (código 07) |
| **D120** | Complemento da Nota Fiscal de Serviços de Transporte (código 07) |
| **D130** | Complemento do Conhecimento Rodoviário de Cargas (código 08) e Conhecimento de Transporte de Cargas Avulso (código 8B) |
| **D140** | Complemento do Conhecimento Aquaviário de Cargas (código 09) |
| **D150** | Complemento do Conhecimento Aéreo de Cargas (código 10) |
| **D160** | Carga Transportada (códigos 08, 8B, 09, 10, 11, 26 e 27) |
| **D161** | Local de Coleta e Entrega (códigos 08, 8B, 09, 10, 11 e 26) |
| **D170** | Complemento do Conhecimento Multimodal de Cargas (código 26) |
| **D180** | Modais (código 26) |
| **D190** | Registro Analítico dos Documentos (códigos 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 67) |
| **D195** | Observações do lançamento (códigos 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 67) |
| **D197** | Outras obrigações tributárias, ajustes e informações de valores provenientes do documento fiscal |
| **D500** | Nota Fiscal de Serviço de Comunicação (código 21) e Serviço de Telecomunicação (código 22) |
| **D510** | Itens do Documento - Nota Fiscal de Serviço de Comunicação (código 21) e Serviço de Telecomunicação (código 22) |
| **D530** | Terminal Faturado |
| **D590** | Registro Analítico do Documento (códigos 21 e 22) |
| **D600** | Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código 21) e de Serviço de Telecomunicação (código 22) |
| **D610** | Itens do Documento Consolidado (códigos 21 e 22) |
| **D690** | Registro Analítico dos Documentos (códigos 21 e 22) |
| **D695** | Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código 21) e de Serviço de Telecomunicação (código 22) |
| **D696** | Registro Analítico dos Documentos (códigos 21 e 22) |
| **D700** | Nota Fiscal Fatura Eletrônica de Serviços de Comunicação (código 62) |
| **D730** | Registro analítico da Nota Fiscal Fatura Eletrônica de Serviços de Comunicação - NFCom (código 62) |
| **D731** | Informações do Fundo de Combate à Pobreza - FCP (código 62) |
| **D735** | Observações do lançamento fiscal (código 62) |
| **D737** | Outras obrigações tributárias, ajustes e informações de valores provenientes do documento fiscal |
| **D750** | Escrituração consolidada da Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom (código 62) |
| **D760** | Registro analítico da escrituração consolidada da Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom (código 62) |
| **D761** | Informações do Fundo de Combate à Pobreza – FCP (código 62) |
| **D990** | Encerramento do Bloco D |
| **Apuração do ICMS e do IPI** | **E001** | Abertura do Bloco E |
| **E100** | Período de Apuração do ICMS |
| **E110** | Apuração do ICMS - Operações Próprias |
| **E111** | Ajuste/Benefício/Incentivo da Apuração do ICMS |
| **E112** | Informações Adicionais dos Ajustes da Apuração do ICMS |
| **E113** | Informações Adicionais dos Ajustes da Apuração do ICMS - Identificação dos documentos fiscais |
| **E115** | Informações Adicionais da Apuração do ICMS - Valores Declaratórios |
| **E116** | Obrigações do ICMS Recolhido ou a Recolher - Obrigações Próprias |
| **E200** | Período de Apuração do ICMS - Substituição Tributária |
| **E210** | Apuração do ICMS - Substituição Tributária |
| **E220** | Ajuste/Benefício/Incentivo da Apuração do ICMS - Substituição Tributária |
| **E230** | Informações Adicionais dos Ajustes da Apuração do ICMS Substituição Tributária |
| **E240** | Informações Adicionais dos Ajustes da Apuração do ICMS Substituição Tributária - Identificação dos documentos fiscais |
| **E250** | Obrigações do ICMS a Recolher - Substituição Tributária |
| **E300** | Período de Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15 |
| **E310** | Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15 |
| **E311** | Ajuste/Benefício/Incentivo da Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15 |
| **E312** | Informações Adicionais dos Ajustes da Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15 |
| **E313** | Informações Adicionais da Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15 - Identificação dos Documentos Fiscais |
| **E316** | Obrigações do ICMS recolhido ou a recolher – Diferencial de Alíquota – UF Origem/Destino EC 87/15 |
| **E500** | Período de Apuração do IPI |
| **E510** | Consolidação dos Valores de IPI |
| **E520** | Apuração do IPI |
| **E530** | Ajustes da Apuração do IPI |
| **E531** | Informações Adicionais dos Ajustes da Apuração do IPI – Identificação dos Documentos Fiscais (01 e 55) |
| **E990** | Encerramento do Bloco E |
| **Controle do Crédito de ICMS do Ativo Permanente – CIAP** | **G001** | Abertura do Bloco G |
| **G110** | ICMS – Ativo Permanente – CIAP |
| **G125** | Movimentação de Bem do Ativo Imobilizado |
| **G126** | Outros créditos CIAP |
| **G130** | Identificação do documento fiscal |
| **G140** | Identificação do item do documento fiscal |
| **G990** | Encerramento do Bloco G |
| **Inventário Físico** | **H001** | Abertura do Bloco H |
| **H005** | Totais do Inventário |
| **H010** | Inventário |
| **H020** | Informação complementar do Inventário |
| **H030** | Informações complementares do inventário das mercadorias sujeitas ao regime de substituição tributária |
| **H990** | Encerramento do Bloco H |
| **Controle da Produção e do Estoque** | **K001** | Abertura do Bloco K |
| **K010** | Informação sobre o Tipo de Layout (Simplificado/Completo) |
| **K100** | Período de Apuração do ICMS/IPI |
| **K200** | Estoque Escriturado |
| **K210** | Desmontagem de mercadorias – Item de Origem |
| **K215** | Desmontagem de mercadorias – Item de Destino |
| **K220** | Outras Movimentações Internas entre Mercadorias |
| **K230** | Itens Produzidos |
| **K235** | Insumos Consumidos |
| **K250** | Industrialização Efetuada por Terceiros – Itens Produzidos |
| **K255** | Industrialização em Terceiros – Insumos Consumidos |
| **K260** | Reprocessamento/Reparo de Produto/Insumo |
| **K265** | Reprocessamento/Reparo – Mercadorias Consumidas e/ou Retornadas |
| **K280** | Correção de Apontamento – Estoque Escriturado |
| **K290** | Produção Conjunta – Ordem de Produção |
| **K291** | Produção Conjunta – Itens Produzidos |
| **K292** | Produção Conjunta – Insumos Consumidos |
| **K990** | Encerramento do Bloco K |
| **Outras Informações** | **1001** | Abertura do Bloco 1 |
| **1010** | Obrigatoriedade de registros do Bloco 1 |
| **1100** | Registro de Informações sobre Exportação |
| **1105** | Documentos Fiscais de Exportação |
| **1110** | Operações de Exportação Indireta - Mercadorias de terceiros |
| **1200** | Controle de Créditos Fiscais - ICMS |
| **1210** | Utilização de Créditos Fiscais - ICMS |
| **1250** | Informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS |
| **1255** | Informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS por motivo |
| **1400** | Informação sobre Valor Agregado |
| **1600** | Total das operações com cartão de crédito e/ou débito |
| **1601** | Operações com Instrumentos de Pagamentos Eletrônicos |
| **1900** | Indicador de sub-apuração do ICMS |
| **1910** | Período da sub-apuração do ICMS |
| **1920** | Sub-apuração do ICMS |
| **1921** | Ajuste/benefício/incentivo da sub-apuração do ICMS |
| **1922** | Informações adicionais dos ajustes da sub-apuração do ICMS |
| **1923** | Informações adicionais dos ajustes da sub-apuração do ICMS - Identificação dos documentos fiscais |
| **1925** | Informações adicionais da sub-apuração do ICMS - Valores declaratórios |
| **1926** | Obrigações do ICMS a recolher - Operações referentes à sub-apuração do ICMS |
| **1960** | GIAF 1 - Guia de informação e apuração de incentivos fiscais e financeiros: indústria (crédito presumido) |
| **1990** | Encerramento do Bloco 1 |
| **Controle e Encerramento do Arquivo Digital** | **9001** | Abertura do Bloco 9 |
| **9900** | Registros do Arquivo |
| **9990** | Encerramento do Bloco 9 |
| **9999** | Encerramento do Arquivo Digital |
