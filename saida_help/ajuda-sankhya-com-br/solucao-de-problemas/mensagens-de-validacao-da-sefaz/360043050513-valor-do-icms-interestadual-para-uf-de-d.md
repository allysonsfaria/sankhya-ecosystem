---
id: "360043050513"
titulo: "Valor do ICMS Interestadual para UF de Destino difere do calculado [nItem:999] (Valor Informado: XXX, Valor Calculado:XXX) (NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050513-Valor-do-ICMS-Interestadual-para-UF-de-Destino-difere-do-calculado-nItem-999-Valor-Informado-XXX-Valor-Calculado-XXX-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:47Z"
rotulos: ["ERRONF", "Alíquotas", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "815", "Divergência no Valor do ICMS Interestadual para UF de Destino"]
---

# Valor do ICMS Interestadual para UF de Destino difere do calculado [nItem:999] (Valor Informado: XXX, Valor Calculado:XXX) (NT2015/003)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16475259258391) MENSAGEM:**

[815 - Rejeição]: Valor do ICMS Interestadual para UF de Destino difere do calculado [nItem:999] (Valor Informado: XXX, Valor Calculado:XXX).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16475302030487) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 3: Verifique o cálculo do DIFAL, se está devidamente configurado.](https://ajuda.sankhya.com.br/hc/article_attachments/16475259265687) Verifique o cálculo do DIFAL, se está devidamente configurado.

- - Configurações » Cadastros » Partilhas DIFAL
  - Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
  - Aba "**Impostos"** - campo "**Calcular DIFAL Partilhado**"
  - Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS » campo **"Aliq. Interna Destino"**

![Imagem 4: Alíquota Interna Destino](https://ajuda.sankhya.com.br/hc/article_attachments/16475259267479) Alíquota Interna Destino

- Insira o percentual da alíquota interna de destino estipulada pela CONFAZ¹.

![Imagem 5: Acesse a nota novamente após os ajustes e redigite o item.](https://ajuda.sankhya.com.br/hc/article_attachments/16475259270295) Acesse a nota novamente após os ajustes e redigite o item.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16475259274519) CAUSA:**

Quando for emitida uma NF-e com o Valor do ICMS Interestadual para a UF de Destino (vICMSUFDest) diferente do Calculado pela Sefaz, será retornado a rejeição.

**![Imagem 7: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16475302049815) OBSERVAÇÕES:**

**(1)** Como as alíquotas variam de estado para estado e a legislação sempre avança, recomendamos que você faça uma consulta rápida no [portal do Conselho Nacional de Política Fazendária](https://www.confaz.fazenda.gov.br/legislacao/aliquotas-icms-estaduais) (Confaz) para sempre validar esta informação. Lá, é possível revisar o ICMS de cada tipo de mercadoria.

**(1)** (**NT2015/003**) - Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=>
