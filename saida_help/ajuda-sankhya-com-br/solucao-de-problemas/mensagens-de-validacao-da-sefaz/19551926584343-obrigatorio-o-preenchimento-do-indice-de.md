---
id: "19551926584343"
titulo: "Obrigatório o preenchimento do índice de mistura do Biodiesel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/19551926584343-Obrigat%C3%B3rio-o-preenchimento-do-%C3%ADndice-de-mistura-do-Biodiesel"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:51:35Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "CFOP", "908", "Preenchimento obrigatório do índice de mistura do Biodiesel"]
---

# Obrigatório o preenchimento do índice de mistura do Biodiesel

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19551885594263) **MENSAGEM:**

Rejeição 908 - Rejeição: Obrigatório o preenchimento do índice de mistura do Biodiesel [nItem:1]

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19605332255127) SITUAÇÃO:**

Se produto <cProdANP> existe na Tabela de Combustíveis Sujeitos à Tributação Monofásica (coluna “Código ANP”) e coluna “Percentual do Biodiesel” igual a 1

É obrigatório o preenchimento do índice de mistura do Biodiesel tag <pBio>

**Exceção 1:** Regra de validação não se aplica quando:

- NF-e Complementar tag <finNFe> =2) ou NF-e de Devolução <finfe> =4 e - AnoMes da ChaveReferenciada tag <refNFe> < ‘2307’ (em Homologação) e < ‘2309’ (em Produção)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19551868882711)SOLUÇÃO:**

![Imagem 4: Tela: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/19551900596759) Tela: Configurações » Cadastros » Produtos » Produtos

Aba>> Combustível
Campo>> Percentual do Índice de Mistura ( Preencha de acordo com orientação de sua contabilidade )

![Imagem 5: Aba>> Combustível Campo>> Percentual do Índice de Mistura ( Preencha de acordo com orientação de sua contabilidade )](https://ajuda.sankhya.com.br/hc/article_attachments/19605377611415)

![Imagem 6: Tela: Comercial » Preferências » Empresa Aba: Documentos Fiscais Eletrônico Sub Aba>> NF-e/NFC-e Sub Aba >> Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/19551885604503) Tela: Comercial » Preferências » Empresa
Aba: Documentos Fiscais Eletrônico
Sub Aba>> NF-e/NFC-e
Sub Aba >> Nota Técnica (última do ano regente)

![Imagem 7: Tela: Comercial » Preferências » Empresa Aba: Documentos Fiscais Eletrônico Sub Aba>> NF-e/NFC-e Sub Aba >> Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/19605332258199)

Após ajuste e ao gerar o lote da nota novamente a TAG <pBio> é alimentada com a informação previamente preenchida no cadastro do produto

![Imagem 8: Após ajuste e ao gerar o lote da nota novamente a TAG <pBio> é alimentada com a informação previamente preenchida no…](https://ajuda.sankhya.com.br/attachments/token/jyQmk8vdpeK1tAGbxeDMrFZpx/?name=image.png)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19551868888471)CAUSA:**

Será apresentada a rejeição quando o produto estiver presente na Tabela de Combustíveis Sujeitos à Tributação Monofásica e não foi informado o índice de mistura do Biodiesel referente a CST (02, 15, 53 ou 61). 

**Observação 1:**

**Exceção 2:** Regra de validação não se aplica quando <indIEDest>=9

**Exceção 3:** Regra de validação não se aplica quando CFOP 5.922 ou 6.92

**Observação 2:**

Tabela de Combustíveis Sujeitos à Tributação Monofásica publicada na aba “Documentos”, opção “Diversos” do Portal Nacional da Nota
Fiscal Eletrônica.

**Observação 3:**

Regra implantada até 25/09/2023 em homologação e em 30/10/2023 em produção.
