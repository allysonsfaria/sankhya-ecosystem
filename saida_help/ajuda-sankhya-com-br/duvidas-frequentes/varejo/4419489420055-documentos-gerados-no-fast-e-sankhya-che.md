---
id: "4419489420055"
titulo: "Documentos gerados no Fast e Sankhya Checkout e Geração no Sped e Sintegra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4419489420055-Documentos-gerados-no-Fast-e-Sankhya-Checkout-e-Gera%C3%A7%C3%A3o-no-Sped-e-Sintegra"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:19:56Z"
rotulos: ["ECF", "SPED", "Fast Service", "Sintegra", "NFC-e", "Sankhya Checkout", "Fast Service: ECF CFe NFC-e", "SPED Blocos: ECF: C400-C495 SAT: C800-C990 NFC-e: C100-C101", "Sankhya Checkout: CFe NFC-e", "Documentos Eletrônicos"]
---

# Documentos gerados no Fast e Sankhya Checkout e Geração no Sped e Sintegra

#### **(1)** Que tipos de documentos são gerados pelo Fast Service e Sankhya Checkout?

| **Produto** | **Documento** |
| --- | --- |
| **Fast Service** | ECF (Cupom Fiscal)   CFe (SAT)   NFC-e |
| **Sankhya Checkout** | CFe (SAT) \*\*MFe  NFCe |

#### **(1)** O que é um ECF (Cupom Fiscal)?

Trata-se de um equipamento automatizado que emite cupons fiscais, calcula o imposto devido na comercialização de cada produto, armazena a numeração e os valores dos cupons fiscais, de forma sumarizada, em totalizadores e contadores de sua Memória Fiscal, armazena os dados de cupons fiscais, em sua totalidade, na Memória de Fita-Detalhe e emite relatórios fiscais consolidados.

O  ECF não emite somente cupons fiscais, mas documentos de diversas naturezas, como os relatórios fiscais (Leitura X, Redução Z. Leitura de Memória Fiscal), e documentos não fiscais (Relatório Gerencial, Comprovante Não Fiscal, Cupom Vinculado ao Cartão de Crédito, dentre outros), sendo que todos os documentos possuem uma numeração de Contador de Ordem de Operação (COO).

#### **(1)** Quais blocos no Sped é gerado o Cupom Fiscal? E Qual Registro Gero no Sintegra?

| **EFD (SPED Fiscal)** | **Sintegra** |
| --- | --- |
| - C400 / C405  Redução Z - C420 Registro dos Totalizadores Parciais da Redução Z - C425 RESUMO DE ITENS DO MOVIMENTO DIÁRIO - C460 DOCUMENTO FISCAL EMITIDO POR ECF - C465 COMPLEMENTO DO CUPOM FISCAL ELETRÔNICO EMITIDO POR ECF – CF-e-ECF - C470 : ITENS DO DOCUMENTO FISCAL EMITIDO POR ECF ( - C490 : REGISTRO ANALÍTICO DO MOVIMENTO DIÁRIO - C495 – RESUMO MENSAL DE ITENS DO ECF POR ESTABELECIMENTO | - Registro 60 |

#### **(1)** Como é feita a importação desses registros para o sistema no Fast Service?

Para que os Registros de Redução Z sejam inseridos no EFD ou Sintegra é necessário que os lançamentos tenham sido importados 

#### **(1)**  Caminho para importação no Fast Service:

| FastService>>Menu>>Utilitários>>Impressora Fiscal> Importar dados da Redução Z |
| --- |

![Imagem 1: FastService>>Menu>>Utilitários>>Impressora Fiscal> Importar dados da Redução Z](https://ajuda.sankhya.com.br/hc/article_attachments/15745987041303)

#### **(1)** E no Sankhya como gero o Sped e Sintegra?

| **Geração do Sped** | - Livros Fiscais> Arquivos >  Geração ICMS/IPI - Livros Fiscais> Conexão >  EFD- Escrituração Fiscal Digital -ICMS/IPI |
| --- | --- |
| **Geração Sintegra** | - 60- Item - 60-Diário - 60-Resumo Mensal - 61-Resumo Mensal |

#### **(1)** O que é CFe SAT?

Modelo 59 é um documento fiscal eletrônico, emitido, armazenado e transmitido automaticamente pelo equipamento SAT, de existência apenas digital.

#### **(1)**  Quais blocos no Sped é gerado o SAT?

| **EFD (SPED Fiscal)  > Bloco C** |
| --- |
| - **C800:** CUPOM FISCAL ELETRÔNICO (CÓDIGO 59) - **C850:** REGISTRO ANALÍTICO DO CF-E (CODIGO 59) - **C860:** IDENTIFICAÇÃO DO EQUIPAMENTO SAT-CF-E - **C890:** RESUMO DIÁRIO DO CF-E (CÓDIGO 59) POR EQUIPAMENTO SAT-CF-E - **C990:** ENCERRAMENTO DO BLOCO C |

#### **(1)** O que é NFC-e ?

A "NFC-e - Nota Fiscal de Consumidor Eletrônica" é um documento de existência apenas digital, emitido e armazenado eletronicamente com o intuito de registrar as operações comerciais de venda presencial ou venda para entrega em domicílio a consumidor final (pessoa física ou jurídica), em operação interna e sem geração de crédito de ICMS ao adquirente.

A NFC-e (modelo 65) substitui a nota fiscal de venda a consumidor (modelo 2), assim como o cupom fiscal emitido por ECF (Emissor de Cupom Fiscal). 

#### **(1)** Quais blocos no Sped é gerada a NFCe?

| **EFD (SPED Fiscal)  > Bloco C** |
| --- |
| - **C100:**  Documento  Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código 55) e Nota Fiscal Eletrônica para Consumidor Final (código 65) - **C101:** Informação complementar dos documentos fiscais quando das operações interestaduais destinadas a consumidor final não contribuinte EC 87/15 |
