---
id: "360043227613"
titulo: "CFOP de operação isenta para ZFM diferente do previsto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043227613-CFOP-de-opera%C3%A7%C3%A3o-isenta-para-ZFM-diferente-do-previsto"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:26Z"
rotulos: ["ERRONF", "#PUBLIFER", "#revisadohugo", "Configuração", "NF-e", "SEFAZ", "Impostos", "CFOP", "Rejeição CFOP 626", "CFOPs específicos para ZFM", "CFOP errado para Suframa", "ZFM"]
---

# CFOP de operação isenta para ZFM diferente do previsto

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16088348749719) MENSAGEM:**

626 - Rejeição: CFOP de operação isenta para ZFM diferente do previsto [nItem:X]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16088334274071) SOLUÇÃO:**

![Imagem 3: Quando uma operação é feita para a Zona Franca de Manaus (ZFM), ou seja, o parceiro possui 'Inscrição Suframa' (tag…](https://ajuda.sankhya.com.br/hc/article_attachments/16088334276503) Quando uma operação é feita para a Zona Franca de Manaus (ZFM), ou seja, o parceiro possui 'Inscrição Suframa' [tag <ISUF>] e o 'Motivo de Desoneração do ICMS' [tag motDesICMS] definido na alíquota de ICMS for igual a 7 - SUFRAMA, pode-se trabalhar apenas com os CFOP's:

- 1203, 1204, 1208, 1209, 2203, 2204, 2208, 2209,
- 5109, 5110,5120, 5151, 5152, 5651, 5652, 5654, 5655, 5658, 5659, 5910,
- 6109,6110, 6120, 6122, 6123, 6151, 6152,
- 6651, 6652, 6654, 6655,6658, 6659, 6910

![Imagem 4: Identificado o CFOP correto a ser utilizado, respeitando a lista citada, realize os devidos ajustes. Vale ressaltar que…](https://ajuda.sankhya.com.br/hc/article_attachments/16088334278295) Identificado o CFOP correto a ser utilizado, respeitando a lista citada, realize os devidos ajustes. Vale ressaltar que o CFOP será definido a partir das informações inseridas na aba **Livro Fiscal** da tela **"[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"**, campos **"CFOP'S"** para dentro do Estado/CFOP'S para fora do Estado.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16088348763927) CAUSA:**

Se informado tag:motDesICMS = 7 (desoneração Suframa) e inserido CFOP diferente dos listados abaixo:
1203, 1204, 1208, 1209, 2203, 2204, 2208, 2209, 5109, 5110,
5120, 5151, 5152, 5651, 5652, 5654, 5655, 5658, 5659, 5910, 6109,
6110, 6120, 6122, 6123, 6151, 6152, 6651, 6652, 6654, 6655,
6658, 6659, 6910 (NT 2012/003) (NT 2013/005 v1.10)

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16088348767383) OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)
