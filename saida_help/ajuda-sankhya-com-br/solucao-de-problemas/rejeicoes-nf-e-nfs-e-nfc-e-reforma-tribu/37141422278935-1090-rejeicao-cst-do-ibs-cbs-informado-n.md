---
id: "37141422278935"
titulo: "1090 Rejeição: CST do IBS/CBS informado não permite informação de diferimento da CBS [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141422278935-1090-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-diferimento-da-CBS-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:19Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Alíquota de IBS", "Alíquotas de CBS", "CST (Código de Situação Tributária) do IBS/CBS", "Grupo de diferimento da CBS", "Mecanismo de diferimento da CBS"]
---

# 1090 Rejeição: CST do IBS/CBS informado não permite informação de diferimento da CBS [nItem: 999]

**MENSAGEM**

1090 Rejeição: CST do IBS/CBS informado não permite informação de diferimento da CBS [nItem: 999]

**SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e), o sistema está rejeitando o documento fiscal porque foi informado o grupo de diferimento da CBS para um CST (Código de Situação Tributária) do IBS/CBS que não permite a utilização deste mecanismo.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST configurado para o produto que está gerando a rejeição.

**(2)** Verifique se o CST configurado possui o **indicador de diferimento** (ind\_gDif) igual a 0, o que significa que este CST não permite a utilização do mecanismo de diferimento da CBS.

**(3)** Escolha uma das seguintes opções para corrigir o problema:

**Opção 1**

Remova o grupo de diferimento da CBS na configuração do produto ou operação fiscal:

- Acesse a tela "**Tipos de Operação**" (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP);
- Na aba **''Impostos''**, desmarque o campo **''Tem CBS''**.

**Opção 2**

Altere o CST do IBS/CBS para um código que permita o uso de diferimento:

- Acesse a tela **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS);
- Selecione um CST que possua o indicador de diferimento (ind\_gDif) igual a 1;
- Aplique esta configuração ao produto ou à operação fiscal

**CAUSA**

Esta rejeição ocorre devido a uma **incompatibilidade entre o CST do IBS/CBS informado e a utilização do mecanismo de diferimento da CBS**. Conforme a regra de validação UB59-20 da Sefaz, quando o CST possui indicador que não permite o uso de diferimento (ind\_gDif = 0), o grupo de Diferimento (gCBS/gDif) não deve ser informado no documento fiscal.

O diferimento é um mecanismo tributário que permite o adiamento do pagamento do tributo para um momento posterior na cadeia de comercialização. No entanto, nem todos os CSTs do IBS/CBS são compatíveis com este mecanismo, e a tentativa de utilizar o diferimento com um CST incompatível resulta nesta rejeição.
