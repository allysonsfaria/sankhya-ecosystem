---
id: "40101409493271"
titulo: "Como emitir Nota de Crédito — Crédito Presumido na ZFM (Tipo 02)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40101409493271-Como-emitir-Nota-de-Cr%C3%A9dito-Cr%C3%A9dito-Presumido-na-ZFM-Tipo-02"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de crédito"
atualizado_em: "2026-08-06T11:18:05Z"
rotulos: ["Configuração", "NF-e", "Crédito", "Impostos", "IBS", "grupo gCredPresIBSZFM", "ZFM"]
---

# Como emitir Nota de Crédito — Crédito Presumido na ZFM (Tipo 02)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Compras`

---

## O que é e para que serve

Use a Nota Fiscal de Crédito (Tipo 02) exclusivamente se você for uma indústria incentivada localizada na Zona Franca de Manaus (ZFM) ou Áreas de Livre Comércio (ALC). Este documento serve para apropriar o crédito presumido de IBS incidente sobre o saldo devedor (Art. 450, § 1º da LC 214/2025). Neste processo, você apura o valor do benefício e emite esta nota de ajuste para que a apuração assistida abata o saldo devedor.

## Antes de começar

Garanta que sua empresa possua a classificação de indústria incentivada na ZFM para fins de subapuração e que esteja localizada em área abrangida. Em seguida, configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação.

| **Nota**  De acordo com a regra de validação do ambiente autorizador, este tipo de nota de crédito só poderá ser utilizado a partir de janeiro de 2029 (Art. 544 da LC 214/25). Além disso, a operação é permitida apenas para NF-e (modelo 55), sendo proibida para NFC-e (modelo 65). |
| --- |

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione C (Compra).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)**:** no campo **Financeiro**, selecione Não atualizar.
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** no campo **Atualização do Estoque**, selecione Nenhuma.
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Entrada. Informe o CFOP `1.949`.
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque a opção **Tem IBS** no grupo Reforma Tributária.
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 5 - Nota de Crédito. Em **Tipo de Nota de Crédito**, selecione 02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e configure a exceção com os parâmetros:

- **CST:** deve possuir o indicador que permita a geração do grupo de crédito presumido de IBS da ZFM na tabela do Comitê Gestor (ex.: 810).
- **Classificação Tributária (cClassTrib):** informe conforme a subapuração da indústria na ZFM (ex.: 810001).
- **Alíquotas:** informe as alíquotas vigentes.

## Como emitir a nota

1. Acesse o [**Portal de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953) ou a [**Central de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793).
2. Inclua uma nova nota utilizando a TOP configurada.
3. Informe a sua própria empresa como Emitente e Destinatário.
4. Adicione um item genérico de ajuste de imposto.
5. Na aba de itens, acesse [**Produtos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) **›** [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) **› Reforma tributária** para atrelar a classificação dos percentuais do benefício.
6. Clique em Grade de Itens > [**Outras Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) › [**Consultar/Alterar dados dos impostos dos itens**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#consultaralterardadosdoimpostodoitem) e informe o valor do crédito presumido apurado no campo de Valor de IBS (isso preencherá a tag `vCredPresIBSZFM`).
7. Preencha a competência do crédito através do campo **Data de movimento** (ou **Data de negociação**).
8. Salve a nota.

| **Atenção**  Não é permitido repetir o mesmo Tipo de Classificação de crédito presumido para itens diferentes no mesmo documento. A competência (tag `competApur`) não pode ser superior ao mês/ano atual da emissão. Esta operação não exige documento referenciado, pois se refere ao benefício sobre saldo. |
| --- |

## Pontos de atenção

### Estrutura do XML

Para validação correta, o XML conterá obrigatoriamente o Grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM (`gCredPresIBSZFM`):

```
<ide>
    <finNFe>5</finNFe>
    <tpNFCredito>02</tpNFCredito>
</ide>
<det nItem="1">
    <imposto>
        <IBSCBS>
            <gCredPresIBSZFM>
                <competApur>XXXX-XX</competApur>
                <tpCredPresIBSZFM>X</tpCredPresIBSZFM>
                <vCredPresIBSZFM>x.xx</vCredPresIBSZFM>
           </gCredPresIBSZFM>
        </IBSCBS>
    </imposto>
</det>
```
