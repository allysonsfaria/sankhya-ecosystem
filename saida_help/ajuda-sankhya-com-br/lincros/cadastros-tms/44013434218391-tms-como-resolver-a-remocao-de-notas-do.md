---
id: "44013434218391"
titulo: "[TMS] - Como Resolver a Remoção de Notas do Embarque ao Importar o CT-e no Sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013434218391--TMS-Como-Resolver-a-Remo%C3%A7%C3%A3o-de-Notas-do-Embarque-ao-Importar-o-CT-e-no-Sistema"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:57:39Z"
rotulos: ["sync_hc", "lincros", "lincros_13432466", "sync_hash_15ebb20af9aa"]
---

# [TMS] - Como Resolver a Remoção de Notas do Embarque ao Importar o CT-e no Sistema

## 1 - Problema Relatado pelo Cliente

O cliente relatou que, ao realizar cotações spots com embarques, o sistema está removendo automaticamente notas do embarque assim que o CT-e é importado. Esse comportamento impacta diretamente o valor da cotação spot, causando inconsistências no processo. O problema ocorre sempre que o CT-e importado agrupa pré-conhecimentos, o que leva à remoção indevida das Notas associadas ao Embarque.

## 2 - Passo a Passo para Resolver o Problema

## Passo 1: Verificação do Parâmetro de Empresa

- Acesse o sistema e siga o caminho:

  Cadastros gerais > Configurações da empresa > Parâmetros > Empresa

- Localize o parâmetro **defineRegraCTeAgrupamentoEmbarque:**Define a regra padrão de vínculo/desvínculo das notas fiscais no Embarque nos casos em que os conhecimentos são agrupados na importação do CT-e. Podendo ser:

- 1 para vincular as demais notas
- 2 para desvincular as demais notas ou
- 3 para importar o Ct-e com erro

- Verifique o valor configurado para este parâmetro. Se o valor for '2', as notas estão sendo desvinculadas automaticamente após a importação do CT-e.

## Passo 2: Análise de alteração do Parâmetro para Resolver o Problema

- Para evitar que as notas sejam removidas, o parâmetro **defineRegraCTeAgrupamentoEmbarque** pode ser alterado para '3'.
- O valor '3' faz com que o CT-e seja importado com erro caso haja mais de um pré-conhecimento agrupado, impedindo que qualquer nota seja removida do embarque. O erro gerado será mostrado, permitindo a análise do que causou a falha.

## Passo 3: Solicitação de Alteração do Parâmetro

- Os parâmetros de empresa podem ser alterados apenas pela time de suporte ao cliente da Lincros. Caso seja necessário modificar o parâmetro, entre em contato com nosso time e informe a necessidade de alterar o valor do parâmetro **defineRegraCTeAgrupamentoEmbarque** para '3'.

## Passo 4: Teste Após Alteração

- Após a alteração do parâmetro, realize uma nova importação do CT-e para verificar se o problema foi resolvido e se as notas do embarque não estão mais sendo removidas.
