---
id: "40100269106839"
titulo: "Como emitir Nota de Débito — Pagamento Antecipado (Tipo 06)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40100269106839-Como-emitir-Nota-de-D%C3%A9bito-Pagamento-Antecipado-Tipo-06"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de débito"
atualizado_em: "2026-09-25T12:03:40Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "Impostos", "TOP", "Nota de Débito", "gIBSCBS", "Pagamento Antecipado"]
---

# Como emitir Nota de Débito — Pagamento Antecipado (Tipo 06)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Vendas`

---

## O que é e para que serve

Emita uma **Nota Fiscal Eletrônica (modelo 55)** com **Finalidade de Emissão** igual a **Débito** (Tipo 06) para destacar os tributos devidos no momento em que você recebe valores relativos a um fornecimento futuro. Essa finalidade deve ser utilizada apenas quando já souber exatamente qual bem ou serviço será entregue posteriormente. Este registro permite que você compute o débito na apuração e o seu cliente aproprie o crédito de forma antecipada.

## Antes de começar

Identifique a classificação tributária e a alíquota do bem que será efetivamente entregue no futuro. Em seguida, configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação correspondente.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione V (Venda).
- [**Campo Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)**:** selecione Receitas, na aba Geral e, no campo **Atualização do financeiro**, selecione Incluir.
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** selecione Nenhum (o bem não foi entregue, logo não há baixa física).
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Saída. Informe os CFOPs `5922` ou `6922`.
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS na seção** [**Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF)
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 6 - Nota de Débito. Em **Tipo de Nota de Débito**, selecione 06 - Pagamento antecipado.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com os seguintes parâmetros:

- **CST e Classificação Tributária (cClassTrib):** utilize os mesmos que serão aplicados no fornecimento efetivo.
- **Alíquotas:** informe as mesmas alíquotas que incidirão sobre o bem/serviço no futuro.

## Como emitir a nota

1. Acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) ou a [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).
2. Inclua uma nova nota utilizando a TOP configurada.
3. Informe a sua empresa como emitente e o cliente que realizou o pagamento como destinatário.
4. Adicione o item exato que será vendido no futuro.
5. Informe o valor bruto recebido como base de cálculo para o destaque do imposto.
6. Salve a nota.

| **Risco operacional**  É obrigatório referenciar a nota fiscal de antecipação nas futuras notas de fornecimento efetivos para que o sistema de apuração deduza o valor já pago.  Ao emitir a nota de fornecimento, para que a nota fiscal de antecipação seja vinculada na nota fiscal de fornecimento, acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), selecione a nota de antecipação, clique no botão **Dev./Est.** e siga com a emissão pela [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), isso garante que você não pague o imposto duas vezes. |
| --- |

## Pontos de atenção

### Estrutura do XML

Para validação correta, o XML conterá obrigatoriamente o destaque completo dos tributos no grupo de Informações do IBS e CBS (`gIBSCBS`):

```
<ide>
    <finNFe>6</finNFe>
    <tpNFDebito>06</tpNFDebito>
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
