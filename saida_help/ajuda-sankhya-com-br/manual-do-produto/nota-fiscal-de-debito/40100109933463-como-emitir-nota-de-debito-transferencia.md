---
id: "40100109933463"
titulo: "Como emitir Nota de Débito — Transferência de Crédito na Sucessão (Tipo 05)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40100109933463-Como-emitir-Nota-de-D%C3%A9bito-Transfer%C3%AAncia-de-Cr%C3%A9dito-na-Sucess%C3%A3o-Tipo-05"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de débito"
atualizado_em: "2026-07-29T16:12:38Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Transferência de Crédito", "IBS", "CBS", "Nota de Débito", "gTransfCred"]
---

# Como emitir Nota de Débito — Transferência de Crédito na Sucessão (Tipo 05)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Vendas`

---

## O que é e para que serve

Use a Nota Fiscal de Débito (Tipo 05) para transferir créditos de IBS/CBS apropriados e não utilizados de uma empresa fundida, cindida ou incorporada (sucedida) para a empresa sucessora.

Neste processo, a empresa sucedida realiza a baixa dos créditos na apuração, e a sucessora recebe o direito de apropriação.

Este documento tem apenas efeito fiscal e não deve movimentar mercadorias ou gerar contas a receber.

## Antes de começar

Identifique o montante exato de créditos acumulados na apuração da empresa sucedida. A sucessora deve estar cadastrada como parceira. Em seguida, configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação correspondente.

| **Atenção**  Verifique se o CNPJ da empresa sucedida está apto. Caso esteja inapto, o processo muda: a sucessora deverá emitir uma Nota de Crédito (Tipo 05) e não uma Nota de Débito. |
| --- |

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione V (Venda).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro) **e** [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** selecione Não atualizar e Nenhum, respectivamente.
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Saída. Informe os CFOPs `5949` ou `6949`.
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS na seção** [**Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF).
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 6 - Nota de Débito. Em **Tipo de Nota de Débito**, selecione 05 - Transferência de crédito na sucessão.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com os seguintes parâmetros:

- **CST:** 800 (Transferências).
- **Classificação Tributária (cClassTrib):** 800001.
- **Alíquotas:** informe as vigentes. Embora o valor transferido seja nominal, a alíquota garante a integridade da nota.

## Como emitir a nota

1. Acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) ou a [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).
2. Inclua uma nova nota utilizando a TOP configurada.
3. Informe a empresa sucedida como emitente e a empresa sucessora como destinatária.
4. Adicione um item genérico de ajuste.
5. Clique em Grade de Itens > [**Outras Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) › [**Consultar/Alterar dados dos impostos dos itens**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#consultaralterardadosdoimpostodoitem).
6. Informe o valor do imposto a ser transferido nos campos `Valor do IBS` e `Valor do CBS`.
7. Salve a nota.

| **Nota**  A transferência está limitada ao saldo credor existente na empresa sucedida. Havendo mais de uma empresa sucessora, emita notas fiscais distintas para cada uma. |
| --- |

## Pontos de atenção

### Estrutura do XML

Para validação correta, o XML conterá obrigatoriamente o grupo Transferências de Crédito (`gTransfCred`):

```
<ide>
    <finNFe>6</finNFe>
    <tpNFDebito>05</tpNFDebito>
</ide>
<det nItem="1">
    <imposto>
        <IBSCBS>
            <CST>800</CST>
            <cClassTrib>800001</cClassTrib>
            <gTransfCred>
                <vIBS>x.xx</vIBS>
                <vCBS>x.xx</vCBS>
            </gTransfCred>
        </IBSCBS>
    </imposto>
</det>
```
