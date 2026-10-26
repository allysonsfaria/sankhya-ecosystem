---
id: "360043194873"
titulo: "GTIN (cEAN) com prefixo inválido [nItem:999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043194873-GTIN-cEAN-com-prefixo-inv%C3%A1lido-nItem-999"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:56Z"
rotulos: ["ERRONF", "#criadoRoger", "#RevisadoBraga", "Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "Estoque", "882", "Erro: GTIN inválido", "Solução: Verificar código de barras", "Ajuste: Redigitar itens gerar novo lote"]
---

# GTIN (cEAN) com prefixo inválido [nItem:999]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15862770605847) MENSAGEM:**

882-Rejeição: GTIN (cEAN) com prefixo inválido [nItem:999].

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/15862770608791) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/15862818691095) Acesse: Configurações » Cadastros » Produtos

Aba: **"Impostos"**

Campo "**EAN/GTIN produto p/ NF-e":**

- Código de Barras Estoque: Caso esteja esta opção, verifique o campo "**Cód. de Barras"** da aba: **"ESTOQUE"**;
- Cód. Barras da Unid.Alternativa ou a Referencia: Caso esteja esta opção, verifique o campo Código de Barras da aba: **"Unidades Alternativas"**;
- Referência: Caso esteja esta opção, verifique o campo **"Referencia da aba: Geral";**
- Código do Produto: Caso esteja esta opção, nada a fazer.

  Após a correção, o XML será gerado:

<prod>
     <cProd>802133</cProd>
      <cEAN>7892193036998</cEAN>
      <xProd>COMEDOURO PLAST JAMBO PRETO CAVEIRINHA-M</xProd>
      <NCM>39269090</NCM>
      <CFOP>5202</CFOP>
      <uCom>UN</uCom>
      <qCom>1</qCom>
      <vUnCom>24.74</vUnCom>
      <vProd>24.74</vProd>
      <cEANTrib>**794**2193036998</cEANTrib>
      <uTrib>UN</uTrib>
      <qTrib>1</qTrib>
      <vUnTrib>24.74</vUnTrib>
      <indTot>1</indTot>
      <xPed>669</xPed>
      <nItemPed>25</nItemPed>
 </prod>

Validação efetuada conforme prefixos e orientações constantes na “Tabela Prefixo GS1” publicada no Portal Nacional da NF-e.

- Tabela Prefixo GS1: <https://www.gs1.org/standards/id-keys/company-prefix>

 Para Brasil os prefixos (inicias) aceitos são: **789**-**790** - GS1 Brasil

![Imagem 4: Após os ajustes, redigite os itens na nota e gere lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/15862818692759) Após os ajustes, redigite os itens na nota e gere lote novamente.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15862770613143) CAUSA:**

Quando for emitida uma NF-e/NFC-e e o GTIN (antigo código EAN ou código de barras - tag: cEAN) contiver o prefixo inválido, haverá a rejeição.
