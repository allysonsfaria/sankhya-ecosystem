---
id: "360044617333"
titulo: "A soma dos valores dos fatos contábeis deve ser igual ao saldo final do código de aglutinação menos o saldo inicial do código de aglutinação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617333-A-soma-dos-valores-dos-fatos-cont%C3%A1beis-deve-ser-igual-ao-saldo-final-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-menos-o-saldo-inicial-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:08Z"
rotulos: ["#criadoRoger", "Configuração", "ECD", "Fiscal", "Histórico", "Contabilidade", "Verificação de Saldos Contábeis", "Registrar históricos corretos", "Falta de históricos nos lançamentos contábeis", "Erro"]
---

# A soma dos valores dos fatos contábeis deve ser igual ao saldo final do código de aglutinação menos o saldo inicial do código de aglutinação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16595394803095) MENSAGEM:**

A soma dos valores dos fatos contábeis (somatório do campo 04 dos registros J215 filhos) deve ser igual ao saldo final do código de aglutinação (campo 07 do registro J210) menos o saldo inicial do código de aglutinação (campo 05 do registro J210).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16595394805143)SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD, aba: "Fatos DMPL / DLPA".](https://ajuda.sankhya.com.br/hc/article_attachments/16595405962519) Acesse: Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD, aba: **"Fatos DMPL / DLPA".**

Para cada registro de Fato contábil, registro um histórico na grade inferior.

![Imagem 4: Para cada registro de Fato contábil, registro um histórico na grade inferior.](https://ajuda.sankhya.com.br/hc/article_attachments/15184999901207)

**![Imagem 5: CAUSA](https://ajuda.sankhya.com.br/hc/article_attachments/16595405964823)CAUSA**

Todos os históricos utilizados nos lançamentos que fazem parte da DMPL (geralmente lançamentos de transferências para as contas de lucros/prejuízos) devem ter seu histórico devidamente informado, se houver lançamento sem histórico ou que o histórico por ventura não esteja configurado nesta aba, este erro será apresentado.
