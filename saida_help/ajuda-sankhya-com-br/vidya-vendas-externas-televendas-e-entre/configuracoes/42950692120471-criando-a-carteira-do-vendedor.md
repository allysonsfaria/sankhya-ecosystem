---
id: "42950692120471"
titulo: "Criando a carteira do vendedor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950692120471-Criando-a-carteira-do-vendedor"
trilha: "VIDYA: Vendas externas, televendas e entregas > Configurações"
atualizado_em: "2026-08-24T17:01:51Z"
rotulos: ["sync_hc", "vidya", "sync_hash_eb167cd49d47", "vidya_599499"]
---

# Criando a carteira do vendedor

Para criar a carteira de clientes/parceiros de um vendedor, existem duas formas de realizar o vínculo:

**1. Vendedor Preferencial:** informado diretamente no cadastro do parceiro, com o vínculo registrado na TGFPAR.

**2. Parceiros Vinculados ao Vendedor:** realizado diretamente no cadastro do vendedor, com o vínculo registrado na TGFRPV.

## 1. Vendedor Preferencial

**O Vendedor Preferencial** é utilizado para definir qual vendedor possui preferência para realizar vendas para determinado parceiro.

Esse vínculo é realizado na tela de **Parceiros**, na aba **Identificação**, por meio do campo **Vendedor Preferencial**, e fica registrado na TGFPAR.

**Como funciona?**

Ao informar um vendedor nesse campo, ele passa a ser o **Vendedor Preferencial daquele parceiro**.]

**Como realizar o cadastro?**

Para realizar o cadastro, siga o guia: [Cadastro de Vendedor Preferencial](https://drive.google.com/file/d/1pkCbCwZa4oHrBYRjumiaXNEham3rjDFu/view?usp=sharing)

##

## 2. Parceiros Vinculados ao Vendedor

**A opção de Parceiros Vinculados ao Vendedor** é utilizada para relacionar um parceiro diretamente à carteira de um vendedor.

Nesse caso, o vínculo é realizado no cadastro do vendedor, na tela de Vendedores/Compradores, na aba Parceiros, e fica registrado na TGFRPV.

**Como funciona?**

Ao vincular um parceiro nessa tela, ele passa a fazer parte da **carteira daquele vendedor**.

Essa opção permite que um mesmo parceiro esteja vinculado a **mais de um vendedor**.

**Como realizar o cadastro?**

Para realizar o cadastro, siga o guia: [Cadastro de Parceiros no vendedor](https://drive.google.com/file/d/1FAvcpGc1BqxqG9k8ijBuTGdoGStF32Y6/view?usp=sharing)

## Qual utilizar?

A diferença principal está no objetivo de cada vínculo:

| **Vendedor Preferencial** | **Parceiros Vinculados ao Vendedor** |
| --- | --- |
| Define o vendedor preferencial do parceiro | Relaciona o parceiro à carteira do vendedor |
| Cadastro realizado no parceiro | Cadastro realizado no vendedor |
| Vínculo registrado na TGFPAR | Vínculo registrado na TGFRPV |
| Um parceiro possui um Vendedor Preferencial | Um parceiro pode ser relacionado a mais de um vendedor |

## Como consultar os vínculos?

Os vínculos também podem ser consultados diretamente nas tabelas **TGFPAR** e **TGFRPV**, na tela de **DBExplorer**.

**TGFPAR — Vendedor Preferencial**

Utilize a consulta para verificar qual vendedor está definido como preferencial para cada parceiro.

| SELECT \* FROM TGFPAR |
| --- |

![Imagem 1: SELECT * FROM TGFPAR](https://ajuda.sankhya.com.br/hc/article_attachments/42957572179223)

**CODPARC** — informa o código do parceiro.

**CODVEND** — informa o código do vendedor preferencial vinculado ao parceiro.

![Imagem 2: CODVEND — informa o código do vendedor preferencial vinculado ao parceiro.](https://ajuda.sankhya.com.br/hc/article_attachments/42957558520727)

## TGFRPV — Parceiros Vinculados ao Vendedor

Utilize a consulta para verificar quais parceiros estão vinculados a cada vendedor pela TGFRPV:

| SELECT \* FROM TGFRPV |
| --- |

![Imagem 3: SELECT * FROM TGFRPV](https://ajuda.sankhya.com.br/hc/article_attachments/42957559164823)

![Imagem 4: SELECT * FROM TGFRPV](https://ajuda.sankhya.com.br/hc/article_attachments/42957620245527)
