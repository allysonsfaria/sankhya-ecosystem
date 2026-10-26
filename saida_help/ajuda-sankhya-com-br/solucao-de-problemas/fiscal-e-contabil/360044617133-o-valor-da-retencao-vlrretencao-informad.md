---
id: "360044617133"
titulo: "O valor da retenção {vlrRetencao} informado não pode ser maior que 11% da Base de cálculo da retenção da contribuição previdenciária {vlrBaseRet}"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617133-O-valor-da-reten%C3%A7%C3%A3o-vlrRetencao-informado-n%C3%A3o-pode-ser-maior-que-11-da-Base-de-c%C3%A1lculo-da-reten%C3%A7%C3%A3o-da-contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-vlrBaseRet"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:21Z"
rotulos: ["#criadoRoger", "#revisadojunior", "Configuração", "Impostos", "Preferências", "Erro de retenção: Valor da retenção não pode exceder 11% da base de cálculo.", "Correção: Ajuste a configuração \"TIPCALCLVLRRET\" para somar valores e aplicar alíquota corretamente.", "Causa: Retenções totais superam o valor permitido pela base de cálculo e alíquota", "Alíquotas de CBS", "Alíquotas de IBS", "Reinf"]
---

# O valor da retenção {vlrRetencao} informado não pode ser maior que 11% da Base de cálculo da retenção da contribuição previdenciária {vlrBaseRet}

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16942820667415) MENSAGEM:**

[Erro MS1183]: O valor da retenção {vlrRetencao} informado não pode ser maior que 11% da Base de cálculo da retenção da contribuição previdenciária {vlrBaseRet}.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16942820672919) SOLUÇÃO:**

 Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela "Preferências": Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16942867086743) Acesse a tela **"Preferências":** Configurações » Avançado » Preferências

Chave: **"TIPCALCLVLRRET"**
Descrição: **"Tipo do cálculo do valor da retenção para o Reinf"**

- Considere a soma dos impostos dos movimentos;
- Considere base dos movimentos e aplique a alíquota.

Considere marcar a segunda opção:

Pois, desta forma, em um mesmo documento não haverá diferença de centavos ocasionadas por arredondamentos nos valores de retenções, uma vez que o sistema irá somar o valor das base de cálculo dos itens e aplicar a alíquota.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16942867091607) CAUSA:**

Na geração dos eventos R-2010 e R-2020 o sistema soma os valores de retenções dos diferentes itens de serviço. Caso este somatório seja superior ao cálculo obtido pela aplicação da alíquota sobre a base de calculo, o erro é retornado.
