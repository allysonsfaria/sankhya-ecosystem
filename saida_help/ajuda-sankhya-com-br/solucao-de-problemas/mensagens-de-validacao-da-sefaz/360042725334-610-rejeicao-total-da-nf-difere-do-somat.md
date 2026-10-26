---
id: "360042725334"
titulo: "610 Rejeição: Total da NF difere do somatório dos Valores compõe o valor Total da NF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042725334-610-Rejei%C3%A7%C3%A3o-Total-da-NF-difere-do-somat%C3%B3rio-dos-Valores-comp%C3%B5e-o-valor-Total-da-NF"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-21T17:59:13Z"
rotulos: ["ERRONF", "#Naves", "Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "TOP", "610", "Divergência no Total da NF", "Erro", "Rejeição 610", "610 Rejeição:", "Total da NF difere do somatório dos Valores compõe o valor Total da NF", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Fiscal/Contábil - KCS"]
---

# 610 Rejeição: Total da NF difere do somatório dos Valores compõe o valor Total da NF

**MENSAGEM**

610 Rejeição: Total da NF difere do somatório dos valores que compõe o valor total da NF

**SITUAÇÃO**

Esta rejeição ocorre durante a emissão de NF-e ou NFC-e, quando o sistema identifica divergência entre o valor total da nota fiscal e o somatório dos valores que compõem esse total (produtos, impostos como ICMS, IPI, ISS e despesas acessórias). É comum em vendas com produtos tipo kit, notas de devolução de compra, notas complementares com produtos zerados, operações com ICMS-ST, DIFAL, ICMS desonerado, descontos aplicados nos itens, produtos com matéria-prima e empresas do Simples Nacional com configurações tributárias inadequadas. Em específico, o erro pode ser causado pela tag <vIPIDevol> em notas de devolução.

**SOLUÇÃO**

**Verifique o imposto IPI:**

Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize a nota desejada. Em seguida, dê duplo clique sobre a nota para abrir a tela **Central de Vendas**. Por fim, confirme se o IPI está sendo corretamente incluído no total da NF-e.

![Imagem 1: Acesse a tela ''Portal de Vendas'' (Comercial » Consulta » Portal de Vendas) e localize a nota desejada. Em seguida, dê…](https://ajuda.sankhya.com.br/hc/article_attachments/14639515392279)

**Verifique imposto ST e PIS/COFINS:**

Caso a nota possua ST, valide o campo **"Indica se o valor do PIS/COFINS ST compõe o valor total da NF-e"** (SOMARPISCOFINSST) na tela **"Impostos Item de nota"** (Comercial >> Arquivo >> Cadastros >> Impostos >> Impostos por item de nota).

![Imagem 2: Caso a nota possua ST, valide o campo "Indica se o valor do PIS/COFINS ST compõe o valor total da NF-e"…](https://ajuda.sankhya.com.br/hc/article_attachments/14639556898199)

**Configuração da TOP (Devolução):**

Acesse a tela **"TOP - Tipo de Operação"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP). No campo **"Cálculo de ICMS, IPI e ISS"**, selecione **"Não calcula e digita"**. Marque o campo **"Devolver sem IPI"** caso a devolução não deva calcular IPI. Na aba **"NF-e / NFC-e / CF-e"**, marque o campo **"NF-e"** como **"Devolução"**.

**(4)** **Destaque de IPI em devoluções:**

Na tela **"Documentos Fiscais Eletrônicos"** (Comercial >> Arquivo >> Documentos Fiscais Eletrônicos) » **"NF-e"**, marque a opção **"Destacar o IPI na tag <vIPIDevol> em devolução"**.

**Recálculo e unidades alternativas:**

Recalcule os valores total da nota. Verifique se existem unidades alternativas cadastradas incorretamente nos produtos; se houver, exclua ou corrija a unidade problemática.

**(6)** **Verificação de descontos:**

Verifique se há descontos na nota de origem que não foram incluídos na nota de devolução. Caso existam, inclua manualmente o valor do desconto na nota de devolução para garantir a correspondência entre os valores totais.

**Atualização e conferência:**

Se o problema persistir, atualize o sistema para a versão **4.35b393** ou superior. Utilize o **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas) » **"Botão NF-e"** » **"Gerar XML da NF-e em arquivo para conferência"** para validar os somatórios no XML. Consulte a **Nota Técnica 2013.005 v1.22** para detalhes das regras de cálculo.

**Verificações gerais importantes:**

- Conforme a **Nota Técnica 2013.005 v1.22**, a rejeição não deve ocorrer caso não tenha sido subtraído o valor de ICMS desonerado (vICMSDeson) do valor total.
- Para vendas de kits, verifique se todos os componentes do kit estão com cálculos tributários corretos.
- Empresas não contribuintes do IPI realizando devolução: consulte o artigo: [Geração NF-e de devolução de compra por empresas não contribuintes do IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044531353).
- Verifique a correlação **"Tributação"** x **"CSOSN"** para optantes do Simples Nacional.

**CAUSA**

A Rejeição 610 ocorre por divergência no cálculo: vNF = vProd + vFrete + vSeg + vOutro + vII + vIPI + vIPIDevol - vDesc - vICMSDeson. Causas comuns:

- Configuração incorreta do IPI ou IPI não somado ao total.
- Tag IPI incorreta em devolução (<vIPIDevol> ausente ou errada).
- TOP mal configurada para o tipo de operação.
- Descontos da nota de origem não sendo incluídos na nota de devolução.
- ICMS desonerado não tratado no total.
- Campo **"SOMARPISCOFINSST"** ou **"INDTOT"** configurados incorretamente.
- Unidade alternativa de produto causando erro.
- Erros de arredondamento ou versão do sistema desatualizada.
- Inconsistências em produtos do tipo kit ou com matéria-prima que possuem descontos aplicados.
