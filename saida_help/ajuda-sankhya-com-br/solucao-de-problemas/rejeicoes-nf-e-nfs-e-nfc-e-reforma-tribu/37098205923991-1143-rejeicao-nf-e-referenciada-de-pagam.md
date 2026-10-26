---
id: "37098205923991"
titulo: "1143 Rejeição: NF-e referenciada de pagamento antecipado deve ser do tipo débito, pagamento antecipado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098205923991-1143-Rejei%C3%A7%C3%A3o-NF-e-referenciada-de-pagamento-antecipado-deve-ser-do-tipo-d%C3%A9bito-pagamento-antecipado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:13Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SEFAZ", "TOP", "Nota de Débito", "Tipo de Nota Fiscal de Débito", "NF-e de fornecimento vinculada a outra NF-e", "Pagamento antecipado", "Reforma Tributária (Lei Complementar 214/2025)", "NF-e de pagamento antecipado", "Documentos Eletrônicos"]
---

# 1143 Rejeição: NF-e referenciada de pagamento antecipado deve ser do tipo débito, pagamento antecipado

**MENSAGEM**

1143 Rejeição: NF-e referenciada de pagamento antecipado deve ser do tipo débito, pagamento antecipado

**SITUAÇÃO**

Ao emitir uma NF-e de fornecimento vinculada a outra NF-e, o sistema retorna uma rejeição relacionada à nota fiscal referenciada no vínculo de pagamento antecipado.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Localize o TOP utilizado para emissão da nota de débito de pagamento antecipado.

**(3)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e"** está configurado com a opção **"Nota de débito"**.

**(4)** No campo **"Tipo de Nota Fiscal de Débito"**, selecione a opção **"6-Pagamento Antecipado"**.

**(5)** Salve as alterações e emita novamente a nota fiscal.

**(6)** Ao vincular notas fiscais, certifique-se de que a NF-e referenciada como pagamento antecipado tenha sido emitida com o TOP corretamente configurado. 

**CAUSA**

Esta rejeição ocorre devido à implementação das regras da Reforma Tributária (Lei Complementar 214/2025), que exige que as notas fiscais de pagamento antecipado sejam corretamente identificadas no sistema. Quando uma NF-e de fornecimento faz referência a uma NF-e de pagamento antecipado, a nota referenciada deve obrigatoriamente ser do tipo débito (finalidade 6) e ter o tipo de nota fiscal de débito configurado como "6-Pagamento Antecipado". Caso contrário, o sistema da Sefaz rejeita a operação, pois o grupo **gPagAntecipado** no XML só pode referenciar notas que atendam a esses requisitos específicos.
