---
id: "9935875684503"
titulo: "Para o Modelo do Documento '55-Nota Fiscal Eletrônica', o Indicador de Presença para NFC-e não aceita a opção: 4-NFC-e com entrega em domicílio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9935875684503-Para-o-Modelo-do-Documento-55-Nota-Fiscal-Eletr%C3%B4nica-o-Indicador-de-Presen%C3%A7a-para-NFC-e-n%C3%A3o-aceita-a-op%C3%A7%C3%A3o-4-NFC-e-com-entrega-em-domic%C3%ADlio"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:05:13Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "NF-e (Modelo 55) aceita 0 1 2 3 ou 9", "Indicador de Presença inválido (4) para NF-e", "Verifique \"Modelo do Documento\" e \"Indicador de Presença"]
---

# Para o Modelo do Documento '55-Nota Fiscal Eletrônica', o Indicador de Presença para NFC-e não aceita a opção: 4-NFC-e com entrega em domicílio

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17267110135959) SOLUÇÃO:**

![Imagem 2: Acesse a tela "Tipos de Operação - TOP" e revise os campos abaixo relacionados ao Tipo de Operação utilizado no…](https://ajuda.sankhya.com.br/hc/article_attachments/17267110137239) Acesse a tela **"Tipos de Operação - TOP"** e revise os campos abaixo relacionados ao Tipo de Operação utilizado no respectivo lançamento.

- Aba **"NF-e/NFC-e"**: **"Campo 'Modelo do Documento"**
- Aba NF-e/NFC-e: **"Campo 'Indicador de Presença para NF-e/NFC-e/CF-e"**

![Imagem 3: Aba NF-e/NFC-e : "Campo 'Indicador de Presença para NF-e/NFC-e/CF-e"](https://ajuda.sankhya.com.br/hc/article_attachments/12292554312471)

Considerando as regras abaixo:

**Sendo uma "NF-e (Modelo = 55)", são válidos os indicadores de presença "0", "1", "2", "3" ou "9".**

![Imagem 4: Realizados os ajustes, considerando a regra acima, refaça o faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/17267110144663) Realizados os ajustes, considerando a regra acima, refaça o faturamento.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17267110147479) CAUSA:**

Mensagem apresentada quando emitida uma Nota Fiscal Eletrônica (Modelo 55), utilizando um Indicador de Presença = 4 - NFC-e com entrega em domicílio.
