---
id: "40101194562583"
titulo: "Como emitir Nota de Crédito — Multa e Juros (Tipo 01)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40101194562583-Como-emitir-Nota-de-Cr%C3%A9dito-Multa-e-Juros-Tipo-01"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de crédito"
atualizado_em: "2026-10-21T18:05:25Z"
rotulos: ["Configuração", "NF-e", "Crédito", "Impostos", "IBS", "CBS", "Nota de Crédito", "gIBSCBS"]
---

# Como emitir Nota de Crédito — Multa e Juros (Tipo 01)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Compras`

---

## O que é e para que serve

Use a Nota Fiscal de Crédito (Tipo 01) como um instrumento de regularização quando você (adquirente) pagar acréscimos moratórios (multa e juros) por atraso e o seu fornecedor for omisso (não emitir a Nota de Débito Tipo 04). Neste processo, você registra o crédito do IBS e da CBS sobre o valor dos acréscimos pagos. Esta nota gera um débito de igual valor na apuração do fornecedor e exige o aceite dele para produzir efeitos.

## Antes de começar

Garanta que você possui o comprovante do pagamento dos juros/multa vinculado à nota fiscal de aquisição original e confirme que o fornecedor não emitiu a nota de débito prevista. Em seguida, configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione C (Compra).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)**:** selecione Despesas (para registrar a despesa na nota) ou Não atualizar (se o juro já foi baixado no título original).
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** no campo **Atualização do Estoque**, selecione Nenhuma (para evitar entrada duplicada de mercadorias).
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Entrada. Informe o CFOP de entrada correspondente à operação original (ex.: `1.102` ou `2.102`).
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS** no grupo Reforma Tributária.
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 5 - Nota de Crédito. Em **Tipo de Nota de Crédito**, selecione 01 - Multa e Juros. Marque a opção **Buscar NF de origem p/referenciar na NFe** para que os documentos relacionados sejam gerados corretamente no XML do DFe.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com:

- **CST:** utilize o mesmo da operação de aquisição original (ex.: 000).
- **Classificação Tributária (cClassTrib):** a mesma utilizada no fornecimento original.
- **Alíquotas:** aplique a mesma tributação da nota original.

## Como emitir a nota

1. Acesse o [**Portal de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras).
2. Utilize os filtros para localizar a nota fiscal de aquisição original que sofreu os acréscimos.
3. Selecione a nota e clique em [**Outras Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598054-Portal-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) › [**Emissão de notas de ajuste e Complemento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598054-Portal-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#h_01HCMREQF3RRV941W3DSNHPC9T) › **Emitir nota de Crédito**.
4. No pop-up, selecione a TOP configurada.
5. Selecione os itens do documento original que tiveram incidência de juros e multa.
6. Na Central, informe o valor dos itens de forma proporcional ao valor de multa/juros pago (os impostos serão registrados sobre este acréscimo).
7. Confirme as informações do emitente (você, pagador) e do parceiro (fornecedor recebedor).
8. Salve a nota. O referenciamento da nota original e de seus itens ocorre automaticamente.

| **Atenção**  O crédito só será efetivado na sua apuração após o fornecedor emitir um evento de "Aceite de débito na apuração por emissão de nota de crédito". |
| --- |

## Pontos de atenção

### Estrutura do XML

Diferente de notas de anulação, o Tipo 01 exige concordância da outra parte. Para validação correta, o XML conterá obrigatoriamente o grupo Informação de Documentos Fiscais referenciados (`NFref`) da nota original e o destaque proporcional do imposto no grupo (`gIBSCBS`):

```
<ide>
    <finNFe>5</finNFe>
    <tpNFCredito>01</tpNFCredito>
    <NFref>
        <refNFe>44-CHAVE-DA-NOTA-ORIGINAL-44</refNFe>
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
