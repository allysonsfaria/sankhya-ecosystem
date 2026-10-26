---
id: "34850740480151"
titulo: "Como é ajustado o estoque na rotina de Ajuste de Estoque por inventário com as opções ' Pela divergência do WMS' e  'Pela diferença entre MGE e WMS(Recomendável)?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34850740480151-Como-%C3%A9-ajustado-o-estoque-na-rotina-de-Ajuste-de-Estoque-por-invent%C3%A1rio-com-as-op%C3%A7%C3%B5es-Pela-diverg%C3%AAncia-do-WMS-e-Pela-diferen%C3%A7a-entre-MGE-e-WMS-Recomend%C3%A1vel"
trilha: "Dúvidas Frequentes > WMS"
atualizado_em: "2026-07-22T14:26:36Z"
rotulos: ["Produtos", "Configuração", "Inventário", "WMS", "Ocorrências", "Estoque", "Ajuste de Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Divergência do WMS", "Diferença entre MGE e WMS", "Consulta Estoque com Ocorrências", "Squad WMS"]
---

# Como é ajustado o estoque na rotina de Ajuste de Estoque por inventário com as opções ' Pela divergência do WMS' e  'Pela diferença entre MGE e WMS(Recomendável)?

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/34850740469399)SOLUÇÃO:**

O sistema permite o ajuste de estoque por duas formas: **"Pela divergência do WMS"** e **"Pela diferença entre MGE e WMS"**.

#### Divergência do WMS

##### O sistema avalia apenas o endereço onde o produto foi contado.

##### Caso haja divergência entre a quantidade contada e a registrada no sistema, será necessário emitir uma nota de ajuste, seja por sobra ou perda.

##### **(1)** Acesse a tela [''Consulta Estoque com Ocorrências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias) (WMS » Consultas » Consulta Estoque com Ocorrências),

##### **(2)** Verifique as divergências identificadas pelo inventário WMS.

**(3)** Caso seja necessário ajustar o estoque, acesse a tela **''Inventário''** (WMS » Inventário » Inventários).

**(4)** Realize o ajuste da nota.

(Após o ajuste da nota emitida, o estoque oficial é atualizado).

#### Diferença entre MGE e WMS (Recomendável)

##### O sistema considera todo o estoque registrado no WMS e o compara com o estoque do comercial, independentemente de a contagem ter sido feita em apenas um endereço.

- ##### O ajuste é aplicado globalmente, alinhando os dois estoques.
- ##### Se houver direfença entre o saldo do WMS e o saldo do Comercial, o sistema registra a ocorrência na tela ''Consulta Estoque com Ocorrências'' (WMS » Consultas » Consulta Estoque com Ocorrências), permitindo a emissão da nota de ajuste correspondente (sobra ou perda).

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/34850740472215)CAUSA:**

As diferenças no ajuste acontecem quando o saldo contado esta diferente do saldo logico.

Isso pode ocorrer por vários motivos, como movimentações não finalizadas, tarefas pendentes, contagens feitas pela metade ou registros que ainda não foram atualizados.

Por isso, o sistema oferece duas formas de cálculo para identificar e corrigir essas diferenças, garantindo que o estoque fique alinhado entre WMS e MGE.
