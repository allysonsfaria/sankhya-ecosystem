---
id: "40104842245527"
titulo: "Como emitir Nota de Crédito — Transferência na Sucessão (Tipo 05)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40104842245527-Como-emitir-Nota-de-Cr%C3%A9dito-Transfer%C3%AAncia-na-Sucess%C3%A3o-Tipo-05"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de crédito"
atualizado_em: "2026-08-06T11:17:43Z"
rotulos: ["Configuração", "NF-e", "XML", "Crédito", "Impostos", "TOP", "CFOP", "gTransfCred"]
---

# Como emitir Nota de Crédito — Transferência na Sucessão (Tipo 05)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Compras`

---

## O que é e para que serve

Use a Nota Fiscal de Crédito (Tipo 05) para transferir créditos não utilizados de uma empresa sucedida (fundida, cindida ou incorporada) para a sua empresa (sucessora), especificamente quando o CNPJ da sucedida já estiver inapto. Neste processo, a empresa sucessora emite a nota contra a sucedida para registrar o crédito na sua apuração. O crédito só é apropriado após manifestação de todas as sucessoras e deferimento expresso do Fisco.

## Antes de começar

Certifique-se de que o CNPJ da empresa sucedida está inapto (se estiver ativo, o processo deve ser feito via Nota de Débito Tipo 05 pela própria sucedida). Identifique o montante exato de créditos acumulados na sucedida e configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione C (Compra).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)**:** no campo **Financeiro**, selecione Não Atualizar.
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** no campo **Atualização do Estoque**, selecione Nenhuma.
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Entrada. Informe os CFOPs `1.949` ou `2.949`.
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS** **na seção** [**Reforma Tributária**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF).
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 5 - Nota de Crédito. Em **Tipo de Nota de Crédito**, selecione 05 - Transferência de Crédito na Sucessão.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com:

- **CST:** 800
- **Classificação Tributária (cClassTrib):** 800001
- **Alíquotas:** informe as alíquotas vigentes para automatizar o cálculo e o registro no documento.

## Como emitir a nota

1. Acesse o [**Portal de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953) ou a [**Central de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793).
2. Inclua uma nova nota utilizando a TOP configurada.
3. Informe a sua empresa (sucessora) como Emitente e a empresa sucedida como Parceiro/Destinatário.
4. Utilize um item genérico de ajuste.
5. Informe o valor do IBS/CBS correspondente ao crédito a ser transferido.
6. Salve a nota.

| **Atenção**  O somatório das notas de crédito emitidas pelas sucessoras está limitado ao saldo credor remanescente da sucedida. É obrigatório o evento de manifestação favorável das demais sucessoras e do Fisco. |
| --- |

## Pontos de atenção

### Estrutura do XML

Para validação correta, o XML conterá obrigatoriamente o grupo Transferências de Crédito (`gTransfCred`):

```
<ide>
    <finNFe>5</finNFe>
    <tpNFCredito>05</tpNFCredito>
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
