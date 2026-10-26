---
id: "1500000712122"
titulo: "Alíquota de ISS não encontrada para o serviço XX na cidade YY"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000712122-Al%C3%ADquota-de-ISS-n%C3%A3o-encontrada-para-o-servi%C3%A7o-XX-na-cidade-YY"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:26:09Z"
rotulos: ["#criadoRoger", "Configuração", "Alíquota de ISS", "Cidades", "Contrato", "Impostos", "CORE_E04489", "ISS alíquota não encontrada", "Ajuste cadastro de serviço/contrato", "Refaça nota após ajustes", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Alíquota de ISS não encontrada para o serviço XX na cidade YY

**MENSAGEM**

[CORE\_E04489]  Alíquota de ISS não encontrada para o serviço XX na cidade YY.

**SITUAÇÃO**

Esta mensagem ocorre ao tentar faturar um contrato ou emitir uma Nota Fiscal de Serviço Eletrônica onde o sistema identifica a necessidade de cálculo de ISS, mas não localiza a configuração de tributação ou alíquota correspondente.

**SOLUÇÃO**

**(1)Caso esteja lançando uma Nota Fiscal de Serviço Eletrônica:**
Acesse a tela **"Serviços"** (Configurações >> Cadastros >> Produtos >> Serviço). Na aba **"Alíquotas de ISS"**, informe o código da cidade tomadora do serviço e a % de **"Alíquota do Imposto de ISS"**. Preencha os demais campos obrigatórios.

**(2)Caso esteja lançando ou faturando um Contrato:**
1. Acesse a tela **"Alíquotas de ISS"** (Comercial >> Arquivo >> Cadastros >> Alíquotas >> Alíquotas de ISS). Preencha: **"Cidade"**, **"Empresa"**, **"Cód. Tributação ISS"** e **"Percentual de ISS"**.
2. No cadastro de contrato (Contratos e Serviços >> Arquivos >> Contratos), na aba **"Impostos"**, campo **"Cidade de Execução do Serviço"**, informe o código do imposto cadastrado anteriormente.

![Imagem 1: Após os ajustes, redigite o serviço na nota, ou exclua o documento e lance novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/39716629254935)

**(3)** Após os ajustes, redigite o serviço na nota, ou exclua o documento e lance novamente.

**OBSERVAÇÃO**
A mensagem também ocorre quando está gerando os Livros fiscais de ISS, portanto o ajuste é o mesmo.

**CAUSA**

Ocorre quando não foi determinado no cadastro de serviço ou no contrato as informações de cidade de prestação do serviços com seus respectivos dados de alíquotas e tipo de tributação de ISS.
