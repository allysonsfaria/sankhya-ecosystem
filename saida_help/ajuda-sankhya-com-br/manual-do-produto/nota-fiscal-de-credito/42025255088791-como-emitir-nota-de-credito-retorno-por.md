---
id: "42025255088791"
titulo: "Como emitir Nota de Crédito — Retorno por Recusa Parcial na Entrega (Tipo 06)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42025255088791-Como-emitir-Nota-de-Cr%C3%A9dito-Retorno-por-Recusa-Parcial-na-Entrega-Tipo-06"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão > Nota fiscal de crédito"
atualizado_em: "2026-09-09T11:45:16Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "IBS", "CBS", "Nota de Crédito"]
---

# Como emitir Nota de Crédito — Retorno por Recusa Parcial na Entrega (Tipo 06)

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** Menu Principal › Comercial › Rotinas › Portal de Vendas

---

## O que é e para que serve

Use a Nota Fiscal de Crédito (Tipo 06) quando apenas parte dos bens de um fornecimento não for recebida pelo destinatário por recusa durante a entrega. Neste processo, a nota desfaz automaticamente o débito de IBS/CBS destacado na nota original, proporcionalmente aos itens recusados. Este documento não se aplica a devoluções de mercadorias já recebidas — nesse caso, utilize a devolução padrão (Finalidade 4). A nota gera um débito de igual valor na apuração do fornecedor (recebedor) e exige o aceite dele para produzir efeitos.

## Antes de começar

Garanta que você possui a comprovação dos itens recusados durante a entrega da nota fiscal de venda original e confirme a necessidade de ajuste do crédito de IBS/CBS. Em seguida, configure o Tipo de Operação - TOP e a tributação.

## Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- **Tipo de Movimento:** selecione D (Devolução de Venda).
- [**Campo Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)**:** selecione Despesas, na aba Geral (para registrar o estorno do valor dos itens recusados no contas a receber) ou Não atualizar (se preferir não alterar os registros financeiros).
- [**Aba Estoque**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** no campo Atualização do Estoque, selecione Entrar (para registrar a entrada física dos bens que retornaram).
- [**Aba Livro Fiscal**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo Atualização de Livro ICMS, selecione Livro de Entrada. Informe o CFOP contrário ao da operação de fornecimento original.
- [**Aba Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções Tem IBS e Tem CBS no grupo Reforma Tributária.
- [**Aba NF-e / NFC-e / CF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em NF-e, selecione 5 - Nota de Crédito. Em Tipo de Nota de Crédito, selecione 06 - Retorno por recusa parcial na entrega. Marque a opção **Buscar NF de origem p/referenciar na NFe** para que os documentos relacionados sejam gerados corretamente no XML do DFe.

## Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Tela-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção de imposto com:

- **CST:** utilize o mesmo da operação de venda original (ex.: 000).
- **Classificação Tributária (cClassTrib):** a mesma utilizada no fornecimento original.
- **Alíquotas:** aplique a mesma tributação da nota original.

## Como emitir a nota

1. Acesse o [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas).
2. Utilize os filtros para localizar a nota fiscal de venda original que sofreu o retorno parcial.
3. Selecione a nota e clique em[Dev/Est](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Tela-Portal-de-Vendas#devolucao-venda).
4. No pop-up, selecione a TOP configurada para o Tipo 06.
5. Selecione **apenas os itens recusados** durante a entrega.
6. Na [Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), informe o valor dos itens de forma proporcional aos itens recusados (os impostos serão registrados sobre este valor de IBS/CBS recusado).
7. Confirme as informações do emitente (você, fornecedor) e do parceiro (destinatário recebedor).
8. Salve a nota. O referenciamento da nota original e de seus itens ocorre automaticamente.

| **Atenção**  O crédito será efetivado na apuração do destinatário apenas após aceitar a operação mediante evento correspondente. |
| --- |

## Pontos de atenção

- **Referenciamento obrigatório:** a chave de acesso da NF-e de fornecimento original deve ser informada no grupo NFref.
- **Destinatário:** o emitente da nota de crédito é o próprio fornecedor; o destinatário é o mesmo constante na NF-e de saída original.
- **Valor do crédito:** limitado ao IBS/CBS correspondente aos itens recusados, não ao total da nota.
- **Eventos exigidos:** o destinatário deve registrar Operação Não Realizada ou Desconhecimento da Operação; o transportador deve registrar Insucesso de Entrega, quando aplicável.
- **ICMS:** este documento não contempla, por ora, ajustes de ICMS. Devem coexistir os procedimentos estaduais aplicáveis ao retorno de mercadoria não entregue.
- **Diferença em relação ao Tipo 03:** a única distinção funcional é o campo tpNFCredito = 06 (parcial) versus tpNFCredito = 03 (total). Toda a parametrização, escrituração e estrutura XML é idêntica.

## Estrutura do XML

Diferente de notas de anulação, o Tipo 06 exige concordância da outra parte. Para validação correta, o XML conterá obrigatoriamente o grupo Informação de Documentos Fiscais referenciados (NFref) da nota original e o destaque proporcional do imposto no grupo (gIBSCBS):

```
<ide>
<finNFe>5</finNFe>
<tpNFCredito>06</tpNFCredito>
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
<gIBSUF>
<pIBSUF>x.xxxx</pIBSUF>
<vIBSUF>x.xx</vIBSUF>
</gIBSUF>
<gIBSMun>
<pIBSMun>x.xxxx</pIBSMun>
<vIBSMun>x.xx</vIBSMun>
</gIBSMun>
<vIBS>x.xx</vIBS>
<gCBS>
<pCBS>x.xxxx</pCBS>
<vCBS>x.xx</vCBS>
</gCBS>
</gIBSCBS>
</IBSCBS>
</imposto>
</det>
```

###

### Confira os outros artigos

- [Como emitir Nota de Débito — Multa e Juros (Tipo 04)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42025255088791-Como-emitir-Nota-de-Cr%C3%A9dito-Retorno-por-Recusa-Parcial-na-Entrega-Tipo-06)
- [Como emitir Nota de Crédito — Retorno por recusa ou não localização (Tipo 03)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42025255088791-Como-emitir-Nota-de-Cr%C3%A9dito-Retorno-por-Recusa-Parcial-na-Entrega-Tipo-06)
- [Como emitir Nota de Crédito — Crédito Presumido na ZFM (Tipo 02)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42025255088791-Como-emitir-Nota-de-Cr%C3%A9dito-Retorno-por-Recusa-Parcial-na-Entrega-Tipo-06)
- [Processo Notas Fiscais de Crédito (Finalidade 5)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42025255088791-Como-emitir-Nota-de-Cr%C3%A9dito-Retorno-por-Recusa-Parcial-na-Entrega-Tipo-06)
- [Introdução às Notas Fiscais de Ajuste (Débito e Crédito)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42025255088791-Como-emitir-Nota-de-Cr%C3%A9dito-Retorno-por-Recusa-Parcial-na-Entrega-Tipo-06)
