---
id: "44010143169431"
titulo: "[TMS] - Pré-notas fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010143169431--TMS-Pr%C3%A9-notas-fiscais"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:31:21Z"
rotulos: ["sync_hc", "lincros", "lincros_13433386", "sync_hash_46f961d8a73c"]
---

# [TMS] - Pré-notas fiscais

**Menu**: Operacional > Documentos de despacho > Pré-notas fiscais

**Objetivo**: A pré-nota fiscal serve como um rascunho do que será faturado posteriormente.

**Considerações**:
- Para que a nota fiscal seja vinculada com a pré-nota fiscal, é necessário seguir um dos passos apresentados em “Vínculo da pré-nota com a nota fiscal”;
- A criação da pré-nota não é obrigatória, sendo uma escolha da empresa. A nota fiscal poderá ser importada mesmo não havendo pré-nota cadastrada.

## Criação

A pré-nota fiscal pode ser criada manualmente ou via webservice. O webservice utilizado atualmente é o /prenota/criarSync ou Async (assíncrono permite o envio de mais de uma pré-nota).

![Imagem 1: A pré-nota fiscal pode ser criada manualmente ou via webservice. O webservice utilizado atualmente é o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010147384343)

A pré-nota pode ser criada via webservice sem informar transportadora, para que seja definida posteriormente em simulação de frete e definição no sistema. Nesse caso, a pré-nota é criada sem um pré conhecimento atrelado e fica com a situação “Criada”.

Quando for realizada simulação e definida a transportadora, o conhecimento será criado.
Se necessário e a empresa desejar que seja criado conhecimento mesmo sem ter a transportadora vinculada, isto é possível através da configuração empresa “criarPreconhecimentoPreNota”.
Caso seja informada a transportadora na requisição, a pré-nota é criada com pré conhecimento atrelado e com situação “Transportadora definida”.

## Definição de transportadora

A transportadora pode ser definida por tela, na aba “Simulação”, que traz as tabelas de frete, sendo possível selecionar a desejada, ou então por simulação e definição via webservice.
Também é possível realizar cotação spot para a pré-nota. Caso sejam selecionadas mais de uma pré-nota na tela de listagem e então criada cotação, automaticamente é criado um embarque com estes documentos.
Tendo a transportadora definida, é possível criar uma ordem de coleta a partir da pré-nota.

![Imagem 2: A transportadora pode ser definida por tela, na aba “Simulação”, que traz as tabelas de frete, sendo possível…](https://ajuda.sankhya.com.br/hc/article_attachments/44010188937239)

## Vínculo da pré-nota com a nota fiscal

Há diferentes maneiras de realizar o vínculo:
1. Manualmente, informando ou na tela de cadastro da PNF ou na de NF qual o documento em que deve vincular;
2. Via webservice /nota/vincularPreNotaFiscal (vincularPreNotaFiscal - WS NotaFiscal);
3. Via tags TF\_NUM\_PNF\_REF e TF\_SER\_PNF\_REF, onde deve vir na nota fiscal o número e a série da pré nota, e no momento da importação da nota a mesma é vinculada automaticamente na pré-nota;

Feito o vínculo, a pré-nota é alterada para a situação Faturada.

**Obs:** Tendo sido vinculada a PNF com a NF, o pré conhecimento da PNF passa para a NF, e a PNF fica sem pré conhecimento.

## Cancelamento da nota fiscal vinculada

Cancelar a nota fiscal (seja pelo ERP, seja via evento de cancelamento na SEFAZ) **não desvincula automaticamente a pré-nota**, que permanece com a situação "Faturada" mesmo após o cancelamento da NF — esse é o comportamento esperado do sistema atualmente, não uma falha pontual. Hoje não existe forma de desfazer esse vínculo, nem por tela nem por integração/API.

Na prática, isso significa que a pré-nota original vinculada a uma NF cancelada fica indisponível para reprogramação. Caso seja necessário dar sequência à programação de coleta, o caminho é gerar um novo pedido/pré-nota.

## Cancelamento

Por tela é possível cancelar caso a ação permitirCancelarPrenota estiver habilitada para o perfil do usuário. Também é possível cancelar via webservice.

**Obs**.: pré-notas fiscais vinculadas a alguma ordem de coleta que esteja com situação igual à “Enviado à transportadora”, não será possível cancelar. Será exibida uma mensagem informando o código da ordem que impossibilita o cancelamento.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
