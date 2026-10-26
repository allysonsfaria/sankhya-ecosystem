---
id: "360043659173"
titulo: "Empresa XXX é optante do 'Simples Nacional - excesso de sublimite de receita bruta' e o campo 'Tipo de Partilha SN' não pode estar preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043659173-Empresa-XXX-%C3%A9-optante-do-Simples-Nacional-excesso-de-sublimite-de-receita-bruta-e-o-campo-Tipo-de-Partilha-SN-n%C3%A3o-pode-estar-preenchido"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:23Z"
rotulos: ["Configuração", "Fiscal", "Simples Nacional", "Impostos", "CORE_E04172", "Verifique e atualize as alíquotas de ICMS conforme necessário", "Deixe o campo em branco na aba \"Naturezas\"", "Marque a opção de Simples Nacional - excesso de sublimite", "Receita Bruta"]
---

# Empresa XXX é optante do 'Simples Nacional - excesso de sublimite de receita bruta' e o campo 'Tipo de Partilha SN' não pode estar preenchido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16134803993879) MENSAGEM:**

[CORE\_E04172] Empresa XXX é optante do 'Simples Nacional - excesso de sublimite de receita bruta' e o campo

'Tipo de Partilha SN' não pode estar preenchido!

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16134803996951) SITUAÇÃO:**

Ao tentar alterar tipo de partilha da empresa, ocorre a mensagem.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16134817190295) CAUSA:**

A partir do momento que a empresa excedeu o limite do faturamento do Simples Nacional a marcação do Código do Regime Tributário será 'Simples Nacional - Excesso de Sublimite de Receita Bruta' e o campo Tipo de Partilha SN deve ficar em branco'.

O sistema não irá considerar mais a partilha e nesta faixa o cliente também não terá partilha, será necessário a configuração de regras de alíquotas tanto de ICMS quanto de PIS/COFINS. Desta forma não será utilizado o campo CSOSN e sim o campo CST do cadastro de alíquotas.

Para detalhes de como configurar Alíquotas de ICMS acesse o artigo: **"[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)"**

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16134817186327) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 5: Acesse: Configurações » Cadastros » Empresas, aba "Naturezas"](https://ajuda.sankhya.com.br/hc/article_attachments/16134803998231) Acesse: Configurações » Cadastros » Empresas, aba **"Naturezas"**

**(2)** Optante pelo SIMPLES: marcado

**(2)** Cód. Regime Tribut: Simples Nacional - excesso de sublimite de receita bruta

**(2)** Tipo de Partilha SN: Deixar em branco

![Imagem 6: (2) Tipo de Partilha SN: Deixar em branco](https://ajuda.sankhya.com.br/hc/article_attachments/14633792080535)
