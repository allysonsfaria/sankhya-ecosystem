---
id: "360044617613"
titulo: "Natureza da Receita inválida. O valor informado no campo deverá existir em uma das tabelas de acordo com o Código de Situação Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617613-Natureza-da-Receita-inv%C3%A1lida-O-valor-informado-no-campo-dever%C3%A1-existir-em-uma-das-tabelas-de-acordo-com-o-C%C3%B3digo-de-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:42Z"
rotulos: ["Produtos", "Configuração", "Impostos", "Natureza", "EFD Contribuições", "Erro devido à configuração incorreta do campo 'Cód. Natureza'", "Natureza da Receita inválida; verificar tabelas tributárias", "Preencha o campo correto e gere o arquivo novamente"]
---

# Natureza da Receita inválida. O valor informado no campo deverá existir em uma das tabelas de acordo com o Código de Situação Tributária

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18612220641175) MENSAGEM:**

Natureza da Receita inválida. O valor informado no campo deverá existir em uma das tabelas de acordo com o Código de Situação Tributária: Tabela 4.3.10: Produtos Sujeitos à Incidência Monofásica da Contribuição Social - Alíquotas Diferenciadas (CST 04); Tabela 4.3.12: Produtos Sujeitos à Substituição Tributária da Contribuição Social (CST 05); Tabela 4.3.13: Produtos Sujeitos à Alíquota Zero da Contribuição Social (CST 06); Tabela 4.3.14: Operações com Isenção da Contribuição Social (CST 07); Tabela 4.3.15: Operações sem Incidência da Contribuição Social (CST 08).

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18612196184471) SITUAÇÃO:**

Erro na Geração de Arquivo - EFD-Contribuições.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18612196188951) CAUSA:**

Ocorre quando há tributação especial para produtos que se enquadra na Tabela Outros Produtos e Operações Sujeitos a Alíquotas Diferenciadas e no cadastro do produto não foi configurado corretamente o campo 'Cód. Natureza (PIS/COFINS M410/M810)'.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18612220655895) SOLUÇÃO:**

![Imagem 5: Acesse Configurações » Cadastros » Produtos:](https://ajuda.sankhya.com.br/hc/article_attachments/18612196225943) Acesse Configurações » Cadastros » Produtos:

- Aba: Impostos
- Campo: Cód. Natureza (PIS/COFINS M410/M810): [Preencher com o Código correspondente]

No relatório de erro, mostra detalhes sobre o produto que está com a falta de informação. Acesse o sistema no cadastro de produto e preencha com valor de 1 a 999, de acordo com o Manual do EFD-Contribuições.

Buscar orientação com o Contador e no site da Receita: <http://sped.rfb.gov.br/projeto/show/268>

![Imagem 6: Após os ajustes, gere novamente o arquivo EFD-Contribuições e validar no PVA.](https://ajuda.sankhya.com.br/hc/article_attachments/18612220675607) Após os ajustes, gere novamente o arquivo EFD-Contribuições e validar no PVA.
