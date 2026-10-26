---
id: "40104576502039"
titulo: "Como emitir Nota de Crédito — Redução de Valores (Tipo 04)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40104576502039-Como-emitir-Nota-de-Cr%C3%A9dito-Redu%C3%A7%C3%A3o-de-Valores-Tipo-04"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de crédito"
atualizado_em: "2026-09-09T11:45:09Z"
rotulos: ["Configuração", "NF-e", "TOP", "Financeiro", "IBS", "CBS", "Nota de Crédito"]
---

# Como emitir Nota de Crédito — Redução de Valores (Tipo 04)

Módulo: Comercial › Rotinas

Caminho de acesso: `Menu Principal › Comercial › Rotinas › Portal de Compras`

---

## O que é e para que serve

Use a Nota Fiscal de Crédito (Tipo 04) quando houver necessidade de reduzir o valor do IBS destacado por erro a maior ou entrega parcial, e não for mais possível cancelar o documento original, emitir nota complementar ou carta de correção. Esta nota reduz o débito na sua apuração e, se o cliente já houver apropriado o crédito, exige que ele emita o evento de aceite para gerar o débito correspondente na apuração dele.

## Antes de começar

Localize a nota fiscal original que possui o valor a ser reduzido e configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação correspondente.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione D (Devolução de Venda) ou C (Compra).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)**:** selecione Despesas (para gerar o abatimento no título do cliente).
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** selecione Entrar (para casos de mercadoria não entregue) ou Nenhuma (para correções apenas de valor).
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Entrada. Informe o CFOP de entrada correspondente à operação original (ex.: `1.102` ou `2.102`).
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS** **na seção** [**Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF).
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 5 - Nota de Crédito. Em **Tipo de Nota de Crédito**, selecione 04 - Redução de Valores. Marque a opção **Buscar NF de origem p/referenciar na NFe** para que os documentos relacionados sejam gerados corretamente no XML do DFe.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção com:

- **CST e Classificação Tributária (cClassTrib):** utilize os mesmos da operação de aquisição original.
- **Alíquotas:** utilize a mesma tributação aplicada na nota original.

## Como emitir a nota

1. Acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) ou a [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) e localize a nota com erro.
2. Clique em [**Outras Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) › **Emissão de notas de ajuste e Complemento** › **Emitir nota de Crédito**.
3. No pop-up, selecione a TOP configurada e os itens originais.
4. Informe a quantidade como `0` se a correção for apenas de valor, ou a quantidade faltante se for erro de volume.
5. Confirme a empresa e o parceiro.
6. Caso o sistema não recupere automaticamente, preencha apenas o valor que será reduzido da nota original.
7. Salve a nota. O referenciamento ocorrerá automaticamente.

| **Nota**  Enquanto não houver legislação clara, emita este documento apenas para corrigir valores de IBS/CBS. Ajustes de ICMS devem seguir regras estaduais específicas. |
| --- |

## Pontos de atenção

### Estrutura do XML

Para validação correta, o XML conterá obrigatoriamente a tag de referência (`NFref`) e o destaque proporcional do imposto a ser reduzido (`gIBSCBS`):

```
<ide>
    <finNFe>5</finNFe>
    <tpNFCredito>04</tpNFCredito>
    <NFref>
        <refNFe>44-CHAVE-DA-NOTA-DE-VENDA-ORIGINAL-44</refNFe>
    </NFref>
</ide>
<det nItem="1">
    <imposto>
        <IBSCBS>
            <CST>xxx</CST>
            <cClassTrib>xxxxxx</cClassTrib>
            <gIBSCBS>
                <vBC>xx.xx</vBC>
                <vIBS>x.xx</vIBS>
                <vCBS>x.xx</vCBS>
            </gIBSCBS>
        </IBSCBS>
    </imposto>
</det>
```
