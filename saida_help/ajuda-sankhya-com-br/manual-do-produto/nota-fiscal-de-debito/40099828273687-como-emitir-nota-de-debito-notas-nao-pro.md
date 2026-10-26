---
id: "40099828273687"
titulo: "Como emitir Nota de Débito — Notas Não Processadas na Apuração (Tipo 03)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40099828273687-Como-emitir-Nota-de-D%C3%A9bito-Notas-N%C3%A3o-Processadas-na-Apura%C3%A7%C3%A3o-Tipo-03"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de débito"
atualizado_em: "2026-10-20T19:38:12Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "XML", "Impostos", "TOP", "CFOP", "gAjusteCompet"]
---

# Como emitir Nota de Débito — Notas Não Processadas na Apuração (Tipo 03)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Vendas`

---

## O que é e para que serve

Use a Nota Fiscal de Débito (Tipo 03) quando identificar, após a prévia da apuração assistida pelo Comitê Gestor do IBS (CG-IBS), que documentos fiscais que você emitiu não foram reconhecidos pelo sistema. Emitir esta nota garante que o saldo final do período reflita os débitos corretos, evitando que você sofra multas e juros futuros.

Esta nota produz efeitos apenas na sua apuração e não gera créditos automáticos para os clientes.

## Antes de começar

Verifique a integridade das informações na prévia da apuração assistida e configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação.

### Cadastro do produto genérico

Antes de configurar a TOP, cadastre o produto genérico que representará os itens da NF-e de origem. Você o seleciona depois no campo **Produto para agrupamento** da TOP.

1. Acesse o [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) em **Configurações › Cadastros › Produtos › Produtos**.
2. Inclua um novo produto, seguindo a codificação padrão da sua base. O código pode ser gerado automaticamente ou informado manualmente.
3. No **Painel Principal**, preencha o campo **Descrição**. Como sugestão, use **NOTA FISCAL NAO PROCESSADA**, sem acentos, para identificar o produto.
4. Na [**Aba Geral**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), preencha o campo **Referência** com **CFOP5949**.
5. Na **Aba Geral**, no campo **Unidade padrão**, selecione **UN**.
6. Na [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos), preencha o campo **NCM** com **00000000**.
7. Na **Aba Impostos**, no campo **Cód. Produto p/ NF-e/NFC-e/CF-e**, selecione **Referência**.
8. Na **Aba Impostos**, no campo **EAN/GTIN Produto p/ NF-e**, selecione **Não Informar**.
9. Salve o cadastro.

Com essa configuração, o código do produto enviado no XML passa a ser o texto do campo **Referência**, e não o código numérico do produto. Com **Não Informar** no campo **EAN/GTIN Produto p/ NF-e**, o XML envia `SEM GTIN`. Usando a descrição sugerida, o XML da nota fica assim:

```
<prod>
    <cProd>CFOP5949</cProd>
    <cEAN>SEM GTIN</cEAN>
    <xProd>NOTA FISCAL NAO PROCESSADA</xProd>
    <NCM>00000000</NCM>
    <CFOP>5949</CFOP>
    <uCom>UN</uCom>
    ...
</prod>
```

| **Atenção**  Se no campo **Cód. Produto p/ NF-e/NFC-e/CF-e** estiver selecionado **Código do Produto**, o XML envia o código numérico do produto no lugar de `CFOP5949`. |
| --- |

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione V (Venda).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro) **e** [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** selecione Não atualizar e Nenhum, respectivamente.
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Saída. Informe os CFOPs `5949` ou `6949`.
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS na seção** [**Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF). No campo **Cálculo de ICMS, IPI, ISS, IBS, CBS e IS**, selecione **Não calcula e digita**.
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 6 - Nota de Débito. Em **Tipo de Nota de Débito**, selecione 03 - Débitos de notas fiscais não processadas na apuração. Marque a opção **Buscar NF de origem p/referenciar na NFe** para que os documentos relacionados sejam gerados corretamente no XML do DFe. No subgrupo [**Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#h_REFORMATRIBUTARIANFE), marque **Agrupar itens em produto genérico** e informe o **Produto para agrupamento**. Esta é a boa prática para a Nota de Débito Tipo 03: a SEFAZ aceita cada documento de origem referenciado uma única vez, e o agrupamento evita a rejeição "1072 – Rejeição: DFe/Item referenciado em duplicidade [nItem: N]" quando a NF-e de origem tem mais de um item.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com os seguintes parâmetros:

- **CST:** 811
- **Classificação Tributária (cClassTrib):** 811002
- **Alíquotas:** informe as vigentes.

## Como emitir a nota

1. Acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas).
2. Utilize os filtros para localizar as notas não processadas pela apuração.
3. Selecione as notas que receberão o ajuste.
4. Clique Grade de Itens > [**Outras Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) › **Emissão de notas de ajuste e Complemento** › **Emitir nota de Débito**.
5. No pop-up, selecione a TOP configurada.
6. Selecione os itens a serem considerados (cada item corresponderá a um documento fiscal não processado).
   - Com a TOP configurada com **Agrupar itens em produto genérico**, o sistema lança um item genérico para cada NF-e de origem, independentemente de a origem ter um ou mais itens.
   - Se a marcação estiver desativada, o sistema replica os itens da NF-e de origem. Nesse caso, a SEFAZ rejeita a nota quando a NF-e de origem tiver mais de um item.
7. Confirme se a sua empresa e o destinatário estão exatamente iguais à nota original.
8. Salve a nota.

| **Dica**  O sistema recupera os impostos do documento de origem automaticamente. A data do documento referenciado é utilizada para informar o ajuste de competência de forma automática. |
| --- |

| **Nota**  O crédito do cliente só será liberado após o efetivo processamento da nota original pelo sistema do Comitê Gestor. |
| --- |

## Pontos de atenção

### Agrupamento de itens em produto genérico

Mantenha a marcação **Agrupar itens em produto genérico** ativa na TOP. Com ela, a nota é lançada com um item genérico por NF-e de origem selecionada. O produto vem do campo **Produto para agrupamento**, a quantidade é 1 e o valor unitário é o valor total da NF-e de origem. Nesse tipo de nota, cada documento de origem pode ser referenciado uma única vez. Se a mesma NF-e de origem for referenciada mais de uma vez, uma para cada item, a SEFAZ rejeita a nota.

O agrupamento automático ocorre quando você emite a nota pela rotina do **Portal de Vendas**. Você também pode lançar a nota manualmente na **Central de Notas**, com ou sem item genérico, desde que informe os vínculos respeitando essa regra de referência única.

O sistema bloqueia a emissão nestes casos:

- Produto para agrupamento não informado na TOP.
- Item da nota de débito sem NF-e de origem identificável, por vínculo inexistente, origem não autorizada ou documento de origem que não é NF-e/NFC-e.

### Estrutura do XML

Para validação correta, o XML conterá obrigatoriamente os grupos Ajuste de Competência (`gAjusteCompet`) e Documento Fiscal Eletrônico Referenciado (`DFeReferenciado`):

```
<ide>
    <finNFe>6</finNFe>
    <tpNFDebito>03</tpNFDebito>
</ide>
<det nItem="1">
    <imposto>
        <IBSCBS>
            <CST>811</CST>
            <cClassTrib>811002</cClassTrib>
            <gAjusteCompet>
                <competApur>xxxx-xx</competApur>
                <vIBS>x.xx</vIBS>
                <vCBS>x.xx</vCBS>
            </gAjusteCompet>
        </IBSCBS>
    </imposto>
    <DFeReferenciado>
        <chaveAcesso>44-CHAVE-DA-NOTA-ORIGINAL-NAO-PROCESSADA-44</chaveAcesso>
    </DFeReferenciado>
</det>
```

Com o agrupamento ativado, o XML contém um `<det>` genérico para cada NF-e de origem. As regras abaixo se aplicam a ele:

- `<qCom>` e `<qTrib>` valem 1. `<vUnCom>`, `<vProd>` e o valor do item são iguais ao valor total da NF-e de origem.
- `<cEAN>` e `<cEANTrib>` ficam como `SEM GTIN`. O CFOP é `5949` ou `6949`, conforme a TOP.
- `<vIBS>` e `<vCBS>` do grupo `<gAjusteCompet>` são a soma dos valores de todos os itens da NF-e de origem. `<competApur>` é o ano e mês da data de negociação da NF-e de origem.
- `<DFeReferenciado>` contém apenas `<chaveAcesso>`, com os 44 dígitos da NF-e de origem. Dentro de `<DFeReferenciado>`, o campo `<nItem>` não é gerado.
