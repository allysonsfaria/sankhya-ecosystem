---
id: "37097647214999"
titulo: "1119 Rejeição: Total de IBS e CBS não informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097647214999-1119-Rejei%C3%A7%C3%A3o-Total-de-IBS-e-CBS-n%C3%A3o-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-07T13:50:28Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Passos para resolver", "Erro", "CST (Código de Situação Tributária)", "Nota Fiscal Eletrônica (NF-e)", "Nota Fiscal de Consumidor Eletrônica (NFC-e)", "Como resolver", "Total de IBS e CBS"]
---

# 1119 Rejeição: Total de IBS e CBS não informado

**MENSAGEM**

1119 Rejeição: Total de IBS e CBS não informado

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) com tributação de IBS e CBS, o documento foi rejeitado pela SEFAZ porque o valor total dos impostos IBS e CBS não foi informado no documento fiscal, mesmo tendo sido informados os grupos de tributação correspondentes nos itens.

**SOLUÇÃO**

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o tipo de operação utilizado na nota fiscal rejeitada.

**(2)** Na aba **''Impostos''**, verifique os campos **''Tem IBS''** e **''Tem CBS''** estão habilitados.

**(3)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS), e verifique se os produtos da nota fiscal possuem o CST do IBS/CBS configurados corretamente.

**(4)** Certifique-se de que os **CSTs utilizados** nos itens da nota fiscal exigem a informação dos grupos de IBS e CBS, conforme a tabela de indicadores de CST do IBS e da CBS.

**(5)** Verifique se o **parâmetro de sistema** que habilita o cálculo dos impostos da Reforma Tributária está ativado.

- Caso não esteja, entre em contato com o administrador do sistema para ativá-lo.

**(6)** Após realizar as configurações necessárias, tente emitir a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando o documento fiscal possui itens com grupos de tributação de IBS e CBS informados, mas o **valor total desses impostos** não foi calculado ou informado no documento. De acordo com as regras de validação da SEFAZ, quando há itens com tributação de IBS e CBS, é obrigatório que o valor total desses impostos seja informado no documento fiscal.

O problema pode ocorrer devido a configurações incorretas no tipo de operação, onde a opção de cálculo de IBS/CBS está desabilitada, ou devido a inconsistências nas configurações de CST do IBS/CBS nos produtos. Também pode ser causado pela falta de ativação dos parâmetros do sistema relacionados à Reforma Tributária.
