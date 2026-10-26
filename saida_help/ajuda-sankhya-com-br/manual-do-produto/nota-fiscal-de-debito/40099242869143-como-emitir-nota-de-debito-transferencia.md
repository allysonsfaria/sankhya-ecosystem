---
id: "40099242869143"
titulo: "Como emitir Nota de Débito — Transferência para Cooperativas (Tipo 01)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40099242869143-Como-emitir-Nota-de-D%C3%A9bito-Transfer%C3%AAncia-para-Cooperativas-Tipo-01"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de débito"
atualizado_em: "2026-07-29T16:12:28Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "Crédito", "IBS", "CBS", "Nota de Débito", "gTransfCred"]
---

# Como emitir Nota de Débito — Transferência para Cooperativas (Tipo 01)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Vendas`

---

## O que é e para que serve

Use a Nota Fiscal de Débito (Tipo 01) para transferir créditos acumulados de IBS e CBS para a sua cooperativa. Neste processo, você (cooperado) baixa os créditos na sua apuração e a cooperativa os recebe. Para que isso ocorra, você deve fornecer bens ou serviços à cooperativa, e ela deve fornecer bens ou serviços a associados sujeitos ao regime regular. A transferência alcança apenas os bens e serviços utilizados nesta produção específica; outros créditos não estão contemplados.

## Antes de começar

Antes de emitir a nota, configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação correspondente.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione V (Venda).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)**:** no campo **Financeiro**, selecione Não atualizar.
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** no campo **Atualização do Estoque**, selecione Nenhum.
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Saída. Informe os CFOPs `5949` (operações internas) ou `6949` (operações interestaduais).
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS** na seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF).
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 6 - Nota de Débito. Em **Tipo de Nota de Débito**, selecione 01 - Transferência de créditos para Cooperativas.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure uma exceção de imposto com os seguintes parâmetros:

- **CST:** 800
- **Classificação Tributária (cClassTrib):** 800002
- **Alíquotas:** informe as alíquotas vigentes para automatizar o cálculo e o registro no documento fiscal.

## Como emitir a nota

1. Acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) ou a [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).
2. Inclua uma nova nota utilizando a TOP configurada.
3. Informe a sua empresa (cooperado) como emitente e selecione a cooperativa como parceira destinatária.
4. Adicione um item genérico (produto ou serviço de ajuste).
5. Clique em Grade de Itens > [**Outras Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) › [**Consultar/Alterar dados dos impostos dos itens**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#consultaralterardadosdoimpostodoitem).
6. Informe o valor correspondente aos créditos disponíveis nos campos de valor do IBS (`vIBS`) e da CBS (`vCBS`).
7. Salve a nota.

| **Atenção**  O valor da nota deve considerar apenas os créditos efetivamente apropriados e não utilizados no período. A operação não deve gerar movimentações financeiras ou de estoque. |
| --- |

## Pontos de atenção

### Estrutura do XML

Apesar da configuração dos campos de IBS/CBS, eles não são enviados nas tags padrão do documento fiscal. O valor do crédito é gerado no grupo Transferência de Crédito (`gTransfCred`). Para validação correta, o XML apresentará a seguinte estrutura:

```
<ide>
    <finNFe>6</finNFe>
    <tpNFDebito>01</tpNFDebito>
</ide>
<det nItem="1">
    <imposto>
        <IBSCBS>
            <CST>800</CST>
            <cClassTrib>800002</cClassTrib>
            <gTransfCred>
                <vIBS>x.xx</vIBS>
                <vCBS>x.xx</vCBS>
            </gTransfCred>
        </IBSCBS>
    </imposto>
</det>
```
