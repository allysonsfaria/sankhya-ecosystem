---
id: "37097011600791"
titulo: "1173 Rejeição: Grupo de Estorno de Crédito não informado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097011600791-1173-Rejei%C3%A7%C3%A3o-Grupo-de-Estorno-de-Cr%C3%A9dito-n%C3%A3o-informado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-10T19:43:23Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Estoque", "CST", "Artigo atualizado KCS", "Estorno de Crédito", "Tipo de nota fiscal de débito", "Perda em estoque", "Grupo de estorno de crédito", "Grupo de Estorno de Crédito não informado", "Docs Eletrônicos - KCS"]
---

# 1173 Rejeição: Grupo de Estorno de Crédito não informado [nItem: 999]

**MENSAGEM**

1173 Rejeição: Grupo de Estorno de Crédito não informado [nItem: 999]

**SITUAÇÃO**

Rejeição apresentada na emissão de uma NF-e quando é utilizado um **CST** ou um **tipo de nota fiscal de débito “07 – Perda em estoque”** que exige a informação do grupo de **estorno de crédito**, sem que o grupo **gEstornoCred** esteja informado no documento fiscal.

### SOLUÇÃO

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP).
**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e"** está configurado com a finalidade **"Nota de Débito"**.
**(3)** Verifique se o campo **"Tipo de Nota Fiscal de Débito"** está configurado como **"07-Perda em estoque"**, se aplicável.
**(4)** Para verificar se o **CST** exige o preenchimento do grupo de **Estorno de Crédito**, consulte a **tabela de classificação tributária** disponível no [Portal da Conformidade Fácil](https://dfe-portal.svrs.rs.gov.br/CFF). Verifique se a classificação tributária correspondente ao CST possui o indicador `ind_gEstornoCred = 1`.
**(5)** Na tela de emissão da nota fiscal, certifique-se de preencher o grupo de **"Estorno de Crédito"** com os valores de IBS e/ou CBS correspondentes. Para isso:

- Informe o valor do IBS (gEstornoCred/vIBS) ou,
- Informe o valor da CBS (gEstornoCred/vCBS).

**OBSERVAÇÃO:** Pelo menos um dos valores (IBS ou CBS) deve ser maior que zero, exceto no caso de tipo de nota fiscal de débito "07-Perda em estoque".

Para mais informações, consulte o artigo: [Como emitir Nota de Débito — Perda em Estoque (Tipo 07)](https://ajuda.sankhya.com.br/hc/pt-br/articles/40100433570967-Como-emitir-Nota-de-D%C3%A9bito-Perda-em-Estoque-Tipo-07)

**(6)** Salve as alterações, recalcule a nota e realize a transmissão para a SEFAZ.

### CAUSA

A rejeição ocorre devido à regra de validação UB116-20 da Sefaz. Quando o CST ou a classificação tributária possuem o indicador **"ind\_gEstornoCred = 1"** ativo, ou em casos de perda em estoque, o sistema exige que o grupo **"gEstornoCred"** seja informado com os valores de IBS ou CBS a serem estornados, garantindo a conformidade com a Lei Complementar nº 214.
