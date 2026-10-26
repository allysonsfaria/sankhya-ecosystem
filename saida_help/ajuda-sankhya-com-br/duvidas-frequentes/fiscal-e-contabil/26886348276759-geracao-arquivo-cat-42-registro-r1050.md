---
id: "26886348276759"
titulo: "Geração Arquivo CAT 42 - Registro R1050"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26886348276759-Gera%C3%A7%C3%A3o-Arquivo-CAT-42-Registro-R1050"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:40:36Z"
rotulos: ["Relatórios", "Fiscal", "SEFAZ", "ICMS", "Impostos", "Estoque", "Geração Arquivo CAT 42", "Registro R1050"]
---

# Geração Arquivo CAT 42 - Registro R1050

A Obrigação acessória CAT 42 trabalha com alguns registros particulares. Confira abaixo alguns detalhes a respeito do registro R1050 e sobre dois campos que podem causar dúvidas durante o uso da rotina:

**Vlr. ICMS + ST Inicial**

**Vlr. ICMS + ST Final**

Explicação sobre o cálculo:

**(1)** **Vlr. ICMS + ST Inicial**: o cálculo realizado sobre esse campo se dá sobre o que foi encontrado pelo sistema na aba **"Notas q/ Amparam Estoque",** pegando o que está no campo **"Vlr. ICMS + ST Unitário",** das linhas que estiverem no **mês anterior** **(campo "DT. Entrada da Mercadoria")** à referência de geração da CAT 42, e multiplicando pelo valor que estiver presente no campo **"Qtd. Inicial"** da grade superior do registro R1050.

**(1)** **Vlr. ICMS + ST Final:** o cálculo realizado sobre esse campo se dá sobre o que foi encontrado pelo sistema na aba Notas q/ Amparam Estoque, pegando o que está no campo **"Vlr. ICMS + ST Unitário",** das linhas que estiverem **dentro do mês** **(campo "DT. Entrada da Mercadoria")** da referência de geração da CAT 42, e multiplicando pelo valor que estiver presente no campo Qtd. Final da grade superior do registro R1050.
