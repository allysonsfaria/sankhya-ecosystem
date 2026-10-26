---
id: "360043102353"
titulo: "CSOSN não permitido para a UF(NT2015/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102353-CSOSN-n%C3%A3o-permitido-para-a-UF-NT2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:23Z"
rotulos: ["ERRONF", "Configuração", "SEFAZ", "Impostos", "384", "CSOSN rejeitado para UF", "Ajustar CSOSN na alíquota", "Verificar normas estaduais"]
---

# CSOSN não permitido para a UF(NT2015/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16444245468951) MENSAGEM:**

[384-Rejeição]: CSOSN não permitido para a UF.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16444270327575) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Identifique a alíquota de ICMS que incidiu na nota (a identificação se dá através do item da nota, no campo " Cód. Alíq…](https://ajuda.sankhya.com.br/hc/article_attachments/16444245477655) Identifique a alíquota de ICMS que incidiu na nota (a identificação se dá através do item da nota, no campo "**Cód. Alíq ICMS"**).

**(2)**Acesse a tela "[**Alíquotas de ICMS**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)" (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS)

**(2)** Aba: "**Simples Nacional"**, campo: "**Código de Situação da Operação no Simples Nacional -    CSOSN."**

![Imagem 4: Efetue o ajuste do CSOSN e, em seguida, faça o relançamento dos itens da nota, ou então, o refaturamento do pedido.…](https://ajuda.sankhya.com.br/hc/article_attachments/16444270334103) Efetue o ajuste do CSOSN e, em seguida, faça o relançamento dos itens da nota, ou então, o refaturamento do pedido. Atentar-se em cada item da nota se o campo CSOSN foi devidamente preenchido e ajustado.

Gere o lote novamente.

**(2)** Exemplo XML com CSOSN incorreto:

...

<imposto>
   <ICMS>
      <ICMSSN102>
          <orig>0</orig>
          **<CSOSN>400</CSOSN> /\*CSOSN inválido para a UF \*/**
     </ICMSSN102>

 Após ajuste:

**(2)**Exemplo XML com CSOSN correto:

...

<imposto>
   <ICMS>
      <ICMSSN102>
          <orig>0</orig>
          **<CSOSN>900</CSOSN> /\*CSOSN válido para a UF \*/**
     </ICMSSN102>

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16444270334871) CAUSA:**

Quando for emitida uma NFC-e com o Código de Situação da Operação – Simples Nacional (CSOSN) igual a 103 ou 400 e o uso desses Códigos não forem permitidos para o estado de origem, será retornado a rejeição "384 - CSOSN não permitido para a UF". Os CSOSN 103 e 400 podem ser aceitos a critério da UF.

Fica a critério do Estado a utilização do  CSOSN 103 e 400. Nos estados que estes códigos de tributação não forem aceitos, deve-se utilizar os disponibilizados pela SEFAZ:

- **102** - Tributada pelo Simples Nacional sem permissão de crédito;
- **300**- Imune;
- **500**- ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação;
- **900**- Outros (a critério da UF);

![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16444245480343) **OBSERVAÇÃO:**

1- (NT2015/002) Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hDS5co/qWOc=>
