---
id: "37230509815703"
titulo: "E0690 Rejeição: A alíquota do Cofins deve ser informada quando a base de cálculo deste imposto for informada."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37230509815703-E0690-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-Cofins-deve-ser-informada-quando-a-base-de-c%C3%A1lculo-deste-imposto-for-informada"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:47Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Alíquotas de COFINS", "Impostos", "alíquota do COFINS não foi preenchida", "Grupo COFINS", "base de cálculo do COFINS informada", "Produto sem tributação", "Alíquota de COFINS", "PIS/COFINS/CSLL"]
---

# E0690 Rejeição: A alíquota do Cofins deve ser informada quando a base de cálculo deste imposto for informada.

**MENSAGEM**

E0690 Rejeição: A alíquota do Cofins deve ser informada quando a base de cálculo deste imposto for informada.

**SITUAÇÃO**

Ao emitir uma NF-e (modelo 55) ou NFC-e (modelo 65), o sistema **calculou e informou a base de cálculo do COFINS** para um ou mais itens da nota fiscal, porém a **alíquota do COFINS não foi preenchida** ou está com valor zerado. Esta inconsistência entre ter base de cálculo sem a respectiva alíquota gera a rejeição do documento fiscal pela SEFAZ.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos).

**(2)** Localize o produto que está gerando a rejeição na emissão do documento fiscal.

**(2)** Na aba **"Impostos"**, sub-aba **''PIS/COFINS/CSLL''** no campo **''Grupo COFINS''**, verifique qual grupo está vinculado ao produto.

**(3)** Acesse a tela [**"Alíquotas de COFINS"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS) (Configurações » Impostos » Alíquotas de COFINS).

**(4)** Localize a regra de alíquota vinculada ao **Grupo COFINS** identificado no produto, utilizando os seguintes filtros:

- Empresa emissora da nota.
- TOP (Tipo de Operação) utilizado.
- Parceiro (se aplicável).
- Tipo de movimento (Entrada ou Saída).

**(5)** No campo ''**Alíquota''**, verifique se o percentual do **COFINS** está corretamente informado.

- Caso o campo esteja **em branco ou zerado**, informe o percentual correto conforme orientação do contador.

**(6)** Confirme que o campo **''Cód. sit. tributária''** foi preenchido de acordo com o tipo de operação (Entrada ou Saída):

- Para movimentos de **Saída**, utilize CST na faixa de **1 a 49**.
- Para movimentos de **Entrada**, utilize CST na faixa de **50 a 98**.

**(7)** Certifique-se de que o campo **''Produto sem tributação''** não esteja ativada indevidamente, pois isso zera automaticamente os campos de alíquota.

**(8)** Salve as alterações realizadas no cadastro de ''Alíquotas de COFINS''.

**(9)** Retorne à nota fiscal rejeitada e **redigite os itens** ou **refature a nota**, para que o sistema recalcule os impostos com as configurações corrigidas.

**(10)** Gere novamente o **lote de transmissão da NF-e ou NFC-e** e envie para autorização da SEFAZ.

**OBSERVAÇÕES:**

- Consulte sempre o contador responsável para confirmar o **percentual correto da alíquota de COFINS** e o **Código de Situação Tributária (CST)** adequado para cada operação;
- Recomenda-se criar **regras específicas** de alíquotas para cada tipo de movimento (Entrada/Saída);
- O cálculo de COFINS é **obrigatório para todas as movimentações de venda**, mesmo que a incidência seja zero.

**CAUSA**

A rejeição ocorre quando o documento fiscal eletrônico (NF-e ou NFC-e) possui **base de cálculo do COFINS informada** em um ou mais itens, mas a **alíquota correspondente não foi preenchida** ou está zerada. Esta situação pode acontecer devido a:

- Ausência de cadastro de **"Alíquotas de COFINS"** para o grupo vinculado ao produto;
- Regra de alíquota cadastrada com o campo **"Alíquota"** zerado ou em branco;
- Marcação indevida da opção **"Produto sem tributação"** no cadastro de alíquotas;
- Configuração incorreta do **"Código sit. tributária"** (CST) que não corresponde ao tipo de movimento (Entrada/Saída).

A SEFAZ exige que, **sempre que houver base de cálculo informada** para o COFINS, a **alíquota correspondente também seja preenchida**, garantindo a consistência das informações tributárias no documento fiscal.
