---
id: "40100433570967"
titulo: "Como emitir Nota de Débito — Perda em Estoque (Tipo 07)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40100433570967-Como-emitir-Nota-de-D%C3%A9bito-Perda-em-Estoque-Tipo-07"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de débito"
atualizado_em: "2026-09-09T11:42:30Z"
rotulos: ["Configuração", "NF-e", "Impostos", "TOP", "CFOP", "Estoque", "IBS", "gEstornoCred"]
---

# Como emitir Nota de Débito — Perda em Estoque (Tipo 07)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Compras`

---

## O que é e para que serve

Use a Nota Fiscal de Débito (Tipo 07) para formalizar o estorno da apuração de créditos de IBS e CBS apropriados na aquisição de bens que sofreram perda (deterioração, quebra, extravio interno). Esta nota gera um lançamento a débito para anular o crédito indevido. Ela não se aplica a perdas durante o transporte (neste caso, observe os eventos da NT 2025.002).

## Antes de começar

Localize os documentos fiscais originais de aquisição dos bens perdidos e dos serviços vinculados a eles (como fretes) para realizar o devido referenciamento. Em seguida, configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação correspondente.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione V (Venda).
- [**Aba Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)**:** selecione Não atualizar.
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** selecione Baixar no campo **Atualização do Estoque**.
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Saída. Informe o CFOP `5927` (ou conforme orientação da sua contabilidade).
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS**.
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 6 - Nota de Débito. Em **Tipo de Nota de Débito**, selecione 07 - Perda em estoque. Marque a opção **Buscar NF de origem p/referenciar na NFe** para que os documentos relacionados sejam gerados corretamente no XML do DFe.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com os seguintes parâmetros:

- **CST:** 410 (ou conforme a tabela de CST do IBS para estornos).
- **Classificação Tributária (cClassTrib):** código de estorno por perda (ex: 410030).
- **Alíquotas:** informe as vigentes. Elas devem refletir o valor do crédito que está sendo estornado proporcionalmente à aquisição.

## Como emitir a nota

1. Acesse o [**Portal de Compras.**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras)
2. Localize o documento fiscal referente à aquisição do bem que sofreu perda.
3. Selecione a nota e clique em [**Dev/Est**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Tela-Portal-de-Vendas#devolucao-venda).
4. No pop-up, selecione a TOP configurada.
5. Selecione os itens que sofreram a perda.
6. Confirme que emitente e destinatário constam como sendo você mesmo (o próprio contribuinte - mesmo CNPJ base).
7. Informe o valor do imposto nos campos `Valor do IBS` e `Valor do CBS`.
8. Salve a nota.

## Pontos de atenção

### Estrutura do XML

Para validação correta, o XML conterá obrigatoriamente o grupo Estorno de Crédito (`gEstornoCred`) e Documento Fiscal Eletrônico Referenciado (`DFeReferenciado`):

```
<ide>
    <finNFe>6</finNFe>
    <tpNFDebito>07</tpNFDebito>
</ide>
<det nItem="1">
    <imposto>
        <IBSCBS>
            <CST>410</CST>
            <cClassTrib>410030</cClassTrib>
            <gEstornoCred>
                <vIBSEstCred>x.xx</vIBSEstCred>
                <vCBSEstCred>x.xx</vCBSEstCred>
            </gEstornoCred>
        </IBSCBS>
    </imposto>
    <DFeReferenciado>
        <chaveAcesso>44-CHAVE-DA-NOTA-DE-AQUISICAO-ORIGINAL-44</chaveAcesso>
    </DFeReferenciado>
</det>
```
