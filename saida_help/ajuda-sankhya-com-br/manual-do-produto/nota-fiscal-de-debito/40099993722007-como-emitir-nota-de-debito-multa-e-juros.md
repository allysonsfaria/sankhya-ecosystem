---
id: "40099993722007"
titulo: "Como emitir Nota de Débito — Multa e Juros (Tipo 04)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40099993722007-Como-emitir-Nota-de-D%C3%A9bito-Multa-e-Juros-Tipo-04"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de débito"
atualizado_em: "2026-10-08T19:46:14Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "Impostos", "IBS", "CBS", "Nota de Débito"]
---

# Como emitir Nota de Débito — Multa e Juros (Tipo 04)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Vendas`

---

## O que é e para que serve

Use a Nota Fiscal de Débito (Tipo 04) para complementar a base de cálculo do IBS e da CBS quando você recebe acréscimos moratórios (multa e juros) por pagamentos atrasados do cliente. Emitir esta nota lança o imposto no período em que ocorre o recebimento.

Para o cliente (se for do regime regular), a extinção desse débito gera o direito ao crédito.

Esta nota fiscal possui efeito apenas de complemento de imposto e não duplica a saída de estoque.

## Antes de começar

Garanta que o registro do recebimento financeiro dos juros e multas esteja vinculado à nota de origem para viabilizar o cálculo. Configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação correspondente.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione V (Venda).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)**:** selecione Receitas (se desejar registrar a receita na nota) ou Não atualizar (se a multa e os juros já foram baixados no título original).
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** selecione Nenhum.
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Saída. Utilize o mesmo CFOP do item da nota fiscal original.
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS na seção** [**Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF)**.**
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 6 - Nota de Débito. Em **Tipo de Nota de Débito**, selecione 04 - Multa e Juros. Marque a opção **Buscar NF de origem p/referenciar na NFe** para que os documentos relacionados sejam gerados corretamente no XML do DFe.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com os seguintes parâmetros:

- **CST:** utilize o mesmo da operação original (ex: 000).
- **Classificação Tributária (cClassTrib):** utilize a mesma do fornecimento original.
- **Alíquotas:** informe as vigentes para o período de emissão deste documento.

## Como emitir a nota

1. Acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas).
2. Localize a nota que gerou a cobrança de juros e multas.
3. Selecione a nota e clique em [**Outras Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) › **Emissão de notas de ajuste e Complemento** › **Emitir nota de Débito**.
4. No pop-up, selecione a TOP configurada.
5. Selecione os itens a serem considerados (cada item deve referenciar o item correspondente da nota original).
6. Informe manualmente o valor de multa e juros de forma proporcional nos itens.
7. Confirme se o emitente e o destinatário são iguais aos da nota original.
8. Caso o sistema não recupere os impostos automaticamente, informe o valor proporcional no campo de base de cálculo.
9. Salve a nota.

| **Nota**  O complemento de IBS/CBS acompanha a tributação do produto. Se o produto da nota original não é tributado, não há valores de tributos a serem complementados. |
| --- |

## Pontos de atenção

### Estrutura do XML

Diferente das notas de anulação, o grupo essencial aqui é o referenciamento detalhado do item original, garantindo que a tributação do juro acompanhe a do produto que o gerou:

```
<ide>
    <finNFe>6</finNFe>
    <tpNFDebito>04</tpNFDebito>
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
    <dfeReferenciado>
        <chNFe>44-CHAVE-DA-NOTA-ORIGINAL-44</chNFe>
        <nItem>1</nItem>
    </dfeReferenciado>
</det>
```
