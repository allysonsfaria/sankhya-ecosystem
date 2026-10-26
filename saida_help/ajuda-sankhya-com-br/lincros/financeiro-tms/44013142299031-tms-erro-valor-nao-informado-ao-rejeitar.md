---
id: "44013142299031"
titulo: "[TMS] - Erro “Valor não informado” ao Rejeitar ou Aceitar Fatura no TMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013142299031--TMS-Erro-Valor-n%C3%A3o-informado-ao-Rejeitar-ou-Aceitar-Fatura-no-TMS"
trilha: "Lincros > TMS > Financeiro - TMS"
atualizado_em: "2026-10-05T19:48:16Z"
rotulos: ["sync_hc", "lincros", "lincros_13432942", "sync_hash_08197744f64d"]
---

# [TMS] - Erro “Valor não informado” ao Rejeitar ou Aceitar Fatura no TMS

## 1 - Problema Relatado pelo Cliente:

O cliente reportou a exibição da mensagem de erro "Valor não informado" ao tentar realizar a ação de 'Rejeitar' ou 'Aceitar' uma fatura na aba Financeiro> Faturas, do sistema TMS. O erro impede a continuidade do processo de aceite ou rejeição da fatura.

## 2 - Passo a Passo para Resolver o Problema

## a. Verifique a Fatura no Sistema:

- Acesse o módulo Financeiro> Faturas.
- Localize a fatura que está apresentando o erro pesquisando pelo seu número.
- Acesse a aba 'Valores' da fatura.

## b. Identifique o Campo com Valor Faturado:

- No campo 'Valor faturado', verifique se o valor está definido como '0,00'.
- A mensagem de erro “Valor não informado” será exibida sempre que este campo estiver zerado.

## c. Orientação ao Responsável pela Fatura:

- Caso o valor esteja incorreto ou zerado, entre em contato com o responsável pelo preenchimento da fatura, que é a transportadora emissora da fatura.
- Solicite à transportadora dona da fatura, a correção do valor faturado, informando o valor real da fatura.
- Se a fatura foi gerada no TMS através de um arquivo EDI DOCCOB, a transportadora deve corrigir o arquivo DOCCOB informando nele o valor faturado correto, e enviar o DOCCOB novamente ao TMS, para que o arquivo seja reprocessado e corrigir automaticamente o valor faturado da fatura em questão.
- Se a fatura foi gerada de forma manual pelo Portal do Transportador, a transportadora deve entrar no Portal do Transportador e corrigir manualmente o valor faturado, e salvar a alteração.

## d. Reprocessamento da Ação:

- Com o valor faturado corrigido, via portal do transportador ou via reimportação do DOCCOB, retorne à aba Financeiro> Faturas.
- Tente novamente realizar o Aceite ou Rejeição da fatura.
- A mensagem de erro não será mais exibida e o processo seguirá normalmente.
