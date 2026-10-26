---
id: "40099589288599"
titulo: "Como emitir Nota de Débito — Anulação de Crédito por Saídas Imunes/Isentas (Tipo 02)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40099589288599-Como-emitir-Nota-de-D%C3%A9bito-Anula%C3%A7%C3%A3o-de-Cr%C3%A9dito-por-Sa%C3%ADdas-Imunes-Isentas-Tipo-02"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de débito"
atualizado_em: "2026-07-29T16:12:30Z"
rotulos: ["Configuração", "NF-e", "Impostos", "CFOP", "IBS", "CBS", "Nota de Débito", "gAjusteCompet"]
---

# Como emitir Nota de Débito — Anulação de Crédito por Saídas Imunes/Isentas (Tipo 02)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Vendas`

---

## O que é e para que serve

Use a Nota Fiscal de Débito (Tipo 02) para formalizar o estorno proporcional de créditos vinculados a aquisições que você utilizou em operações subsequentes sem incidência do imposto ou amparadas por imunidade. Emitir esta nota garante que o valor seja efetivamente lançado na sua apuração assistida, promovendo a regularização do saldo.

## Antes de começar

Antes de emitir a nota, configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação correspondente.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione V (Venda).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro) **e** [**Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** selecione Não atualizar e Nenhum, respectivamente.
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Saída. Informe os CFOPs `5949` ou `6949`.
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS**.
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 6 - Nota de Débito. Em **Tipo de Nota de Débito**, selecione 02 - Anulação de Crédito por Saídas Imunes/Isentas.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com:

- **CST:** 811
- **Classificação Tributária (cClassTrib):** 811001
- **Alíquotas:** informe as alíquotas vigentes.

## Como emitir a nota

1. Acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) ou a [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).
2. Inclua uma nova nota utilizando a TOP configurada.
3. Informe a sua própria empresa como emitente e como destinatária (trata-se de um ajuste na sua própria apuração).
4. Adicione um item genérico (produto ou serviço de ajuste) com um valor simbólico.
5. Clique em Grade de Itens > [**Outras Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) › [**Consultar/Alterar dados dos impostos dos itens**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#consultaralterardadosdoimpostodoitem) e informe os valores segregados por tipo de tributo (utilize os valores sugeridos pelo sistema de apuração assistida).
6. No cabeçalho da nota, informe a data correspondente ao ajuste no campo **Data do Movimento** (ou deixe em branco para o sistema considerar a **Dt. de negociação**). Isso gera o ano e mês do período de apuração na tag de competência.
7. Salve a nota.

| **Nota:**  A emissão desta nota é condição obrigatória para que o valor seja lançado como débito na apuração assistida. Acompanhe os prazos de ajuste no regulamento do IBS/CBS para realizar a emissão no momento correto. |
| --- |

## Pontos de atenção

### Estrutura do XML

Para validação correta, o XML conterá o grupo Ajuste de Competência (`gAjusteCompet`):

```
<ide>
    <finNFe>6</finNFe>
    <tpNFDebito>02</tpNFDebito>
</ide>
<det nItem="1">
    <imposto>
        <IBSCBS>
            <CST>811</CST>
            <cClassTrib>811001</cClassTrib>
            <gAjusteCompet>
                <competApur>xxxx-xx</competApur>
                <vIBS>x.xx</vIBS>
                <vCBS>x.xx</vCBS>
            </gAjusteCompet>
        </IBSCBS>
    </imposto>
</det>
```
