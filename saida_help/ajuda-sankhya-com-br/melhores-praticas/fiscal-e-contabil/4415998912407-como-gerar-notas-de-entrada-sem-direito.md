---
id: "4415998912407"
titulo: "Como gerar notas de entrada sem direito a crédito no arquivo EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4415998912407-Como-gerar-notas-de-entrada-sem-direito-a-cr%C3%A9dito-no-arquivo-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-09-22T13:04:11Z"
rotulos: ["Configuração", "Fiscal", "Crédito", "Impostos", "Preferências", "EFD Contribuições", "Notas de entrada sem direito a crédito", "Parâmetro CSTSEMCREDEFDCT controla", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Como gerar notas de entrada sem direito a crédito no arquivo EFD Contribuições

### Causa da divergência

A divergência na escrituração de notas fiscais no arquivo SPED Contribuições (EFD PIS/COFINS) ocorre quando notas lançadas no sistema não são incluídas no arquivo digital. Além de questões cadastrais e de configuração geral, é fundamental compreender a regra de geração do registro C100.

### Regra de geração (Registro C100)

Ao gerar o arquivo EFD Contribuições, o registro C100 considera, por padrão, as notas de entrada nas quais haja o cálculo do crédito de PIS e COFINS na operação. O sistema verifica nos lançamentos se os dados de PIS e COFINS estão calculados nos itens e se a CST do PIS/COFINS está entre: 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66.

### Notas sem direito a crédito

Para os casos em que há a necessidade de gerar no registro C100 as entradas sem o crédito de PIS e COFINS, foi criado o parâmetro **"CSTSEMCREDEFDCT - Gerar reg. que não geram créd. PIS/COFINS no EFD"**. Com este parâmetro ativado em **"Preferências"** (Configurações >> Avançado >> Preferências), o sistema passa a considerar no registro C100 os lançamentos com CST de PIS/COFINS entre: 70, 71, 72, 73, 74, 75, desde que tenham os valores calculados na TGFDIN.

![Como gerar notas de entrada sem direito a crédito](https://ajuda.sankhya.com.br/hc/article_attachments/16251955117463)

###
