---
id: "39370900994327"
titulo: "Como resolver problemas com CFOP incorreto ou não convertido no sistema?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39370900994327-Como-resolver-problemas-com-CFOP-incorreto-ou-n%C3%A3o-convertido-no-sistema"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-09-08T19:44:21Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "CFOP", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# Como resolver problemas com CFOP incorreto ou não convertido no sistema?

**SITUAÇÃO:**

O **CFOP (Código Fiscal de Operações e Prestações)** é um dos principais elementos utilizados na definição da natureza das operações fiscais no ERP Sankhya. Sua configuração influencia a emissão dos documentos fiscais e o tratamento tributário aplicado às operações.

Problemas na definição ou conversão do CFOP podem ocorrer por diferentes motivos, como configurações da TOP, cadastro fiscal do produto, endereço utilizado para o cálculo do ICMS ou incompatibilidade entre CFOP e CST.

Este artigo apresenta **alguns cenários relacionados ao CFOP**, suas possíveis causas e os procedimentos recomendados para identificação e correção dos problemas.

#### **(1)**CFOP não é espelhado na devolução de compra

Quando o campo **"CFOP's para DENTRO do estado"** está em branco na TOP utilizada para a devolução, o sistema não consegue realizar a conversão automática do CFOP.

Nesse cenário, a configuração existente na TOP da nota de origem não determina o CFOP da devolução. O Sankhya considera a configuração da **TOP de devolução** para definir o CFOP que será utilizado na nova nota.

Os campos **"CFOP's para DENTRO do estado"** e **"CFOP's para FORA do estado"**, disponíveis na aba **Livro Fiscal** da TOP de devolução, são responsáveis por essa definição.

#### Atenção

Caso a TOP não possua CFOP configurado, é possível informá-lo manualmente na grade de itens das Centrais. Nesse caso, a conversão automática não será realizada. Para que ela ocorra, os CFOPs devem estar configurados na TOP.

#### **(1)**CFOP incorreto na entrada de nota fiscal

Quando o sistema não traz o CFOP correto na entrada de nota fiscal, geralmente o problema está relacionado à configuração do **Tipo de Substituição** no cadastro do produto.

Se no cadastro do produto estiver configurado **"Venda com Substituição Tributária (ST na venda)"**, o sistema não converterá o CFOP em movimentações de compra.

Da mesma forma, se estiver configurado **"Revenda com Substituição Tributária (ST na compra)"**, o sistema não converterá o CFOP em movimentações de venda.

#### Atenção

A alteração do **Tipo de Substituição** deve ser realizada de acordo com o tratamento tributário aplicável ao produto e à operação. Em caso de dúvida quanto ao enquadramento fiscal, consulte o responsável fiscal ou contador da empresa.

#### **(1)**CFOP incorreto quando endereço de entrega é diferente

Quando o parceiro possui seu endereço principal em um estado, mas a mercadoria é entregue em outro estado, o CFOP pode ser definido considerando o endereço utilizado para o cálculo do ICMS.

Nessa situação, é necessário verificar a configuração da preferência **"Endereço para cálculo de ICMS" (ENDICMS)**. Para consultar o procedimento detalhado sobre essa configuração, acesse: [Como configurar o sistema para considerar o endereço de entrega do parceiro no cálculo dos impostos em notas de vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/20140086062487-Como-configurar-o-sistema-para-considerar-o-endere%C3%A7o-de-entrega-do-parceiro-no-c%C3%A1lculo-dos-impostos-em-notas-de-vendas)

#### Importante

A utilização do endereço de entrega para definição do tratamento fiscal deve estar de acordo com as regras tributárias aplicáveis à operação. Em caso de dúvida, consulte o responsável fiscal ou contador da empresa.

#### **(1)**Boas práticas para evitar problemas com CFOP

Para reduzir ocorrências relacionadas ao CFOP:

- Mantenha as **TOPs** corretamente configuradas para as operações realizadas pela empresa.
- Verifique os CFOPs configurados na aba **Livro Fiscal** das TOPs de entrada, venda e devolução.
- Confira o **Tipo de Substituição** configurado no cadastro dos produtos.
- Valide o endereço utilizado para o cálculo do ICMS quando houver endereço de entrega diferente do endereço principal.
- Após alterações fiscais, valide se os impostos estão sendo calculados conforme esperado.
- Em caso de rejeição da **SEFAZ**, analise a combinação entre CFOP, CST e demais informações fiscais.
- Não defina um CFOP apenas para eliminar uma rejeição. O código deve representar corretamente a natureza da operação realizada.
- Quando houver dúvida sobre o enquadramento tributário, consulte o contador ou responsável fiscal da empresa.
