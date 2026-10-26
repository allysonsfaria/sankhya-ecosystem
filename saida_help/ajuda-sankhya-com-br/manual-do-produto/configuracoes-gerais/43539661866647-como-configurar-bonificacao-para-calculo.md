---
id: "43539661866647"
titulo: "Como configurar bonificacao para calculo de IBS e CBS na mesma nota de venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43539661866647-Como-configurar-bonificacao-para-calculo-de-IBS-e-CBS-na-mesma-nota-de-venda"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Configurações gerais"
atualizado_em: "2026-09-17T10:07:00Z"
---

# Como configurar bonificacao para calculo de IBS e CBS na mesma nota de venda

## Caminhos de acesso

- Livros Fiscais > Cadastros > Alíquotas de IBS
- Livros Fiscais > Cadastros > Alíquotas de CBS
- Comercial > Rotinas > Central de Vendas
- Comercial > Rotinas > Central de Compras

---

## O que é e para que serve

A configuração de bonificação para IBS e CBS permite que, em uma mesma nota de venda, itens concedidos como bonificação tenham tributação diferenciada para o Imposto sobre Bens e Serviços (IBS) e a Contribuição sobre Bens e Serviços (CBS). O vínculo entre a finalidade de operação **Bonificada** e as alíquotas cadastradas instrui o sistema a aplicar as regras corretas de cálculo para esses itens.

Essa configuração não altera o comportamento dos demais tributos — PIS, COFINS, ICMS, IPI e outros —, que continuam seguindo as parametrizações já existentes no sistema.

## Antes de começar

Verifique se a finalidade de operação **Bonificada** já está cadastrada no sistema. Caso não esteja, realize o cadastro na tela **Finalidade de Operação** antes de seguir os próximos passos.

**Nota**

O cadastro de [finalidades de operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599434-Finalidade-da-Opera%C3%A7%C3%A3o) está fora do escopo deste artigo.

## Configure a tributação de IBS e CBS para bonificação

Cadastre nas telas de alíquotas a tributação que será aplicada às operações de bonificação e vincule-a à finalidade de operação **Bonificada**. O processo é idêntico para as telas de IBS e CBS.

1. Acesse **Livros Fiscais > Cadastros >** [**Alíquotas de IBS**.](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199)
2. Cadastre a tributação que deverá ser aplicada às operações de bonificação.
3. Vincule o registro à finalidade de operação **Bonificada**.
4. Repita os passos 1 a 3 em **Livros Fiscais > Cadastros >** [**Alíquotas de CBS**](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895).

[Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43539661866647-Como-configurar-bonificacao-para-calculo-de-IBS-e-CBS-na-mesma-nota-de-venda#antes)

## Emita a nota com item bonificado

Na emissão da nota pela Central de Vendas ou pela Central de Compras, informe a finalidade de operação **Bonificada** no item concedido como bonificação. O sistema identificará essa configuração e aplicará automaticamente as alíquotas de IBS e CBS cadastradas.

1. Acesse **Comercial > Rotinas > Central de Vendas** ou **Comercial > Rotinas > Central de Compras**, conforme a operação.
2. Lance os itens da nota normalmente.
3. No item concedido como bonificação, informe a finalidade de operação como **Bonificada**.
4. Prossiga com a emissão da nota normalmente.

**Atenção**

Essa configuração impacta exclusivamente o cálculo do IBS e da CBS. O comportamento dos demais tributos permanece inalterado e continuará seguindo as regras e parametrizações já existentes no sistema.

[Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43539661866647-Como-configurar-bonificacao-para-calculo-de-IBS-e-CBS-na-mesma-nota-de-venda#antes)
