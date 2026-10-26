---
id: "39355571637143"
titulo: "Como funciona o apontamento de perdas ao apontar quantidade menor na produção do PA?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39355571637143-Como-funciona-o-apontamento-de-perdas-ao-apontar-quantidade-menor-na-produ%C3%A7%C3%A3o-do-PA"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-09-01T00:07:52Z"
rotulos: ["Perda", "Produção", "Artigo criado KCS", "Produção - KCS"]
---

# Como funciona o apontamento de perdas ao apontar quantidade menor na produção do PA?

No ERP Sankhya, quando você aponta uma quantidade menor do que o total previsto em uma ordem de produção, o sistema permite registrar essa diferença como perda de forma automática ou manual, cada uma tendo um comportamento diferente.

### Processo de Apontamento de Perdas

Para que as informações de perda sejam registradas corretamente no sistema, siga o procedimento abaixo em uma das telas **"Apontamento de Produção"** (Produção » Rotinas » Apontamento de Produção) ou **"Operações de Produção"** (Produção » Rotinas » Operações de Produção), em ambas as telas, o processo do apontamento é igual:

#### Automático:

No processo automático de apontamento de perdas, quando você aponta uma quantidade a menor do que deve ser produzida na atividade que gera a nota de produção e clica em confirmar, o sistema tem o comportamento abaixo:

**(1)** Acesse a tela específica e localize a ordem de produção desejada.

**(2)** Informe a quantidade produzida no campo **"Qtd. apontada"** que foi efetivamente concluída.

**(3)** Clique em **"Confirmar"** e é apresentado a mensagem abaixo:

**"Este será o último apontamento (Sim/Não)? Caso seja o último apontamento, este receberá o saldo das matérias-primas do tipo fixa e a diferença de quantidade será considerada com perda para estes produtos/controles.**

**Observação: Caso haja apontamento de matérias primas nessa atividade, a quantidade de matérias primas não será proporcionada de acordo com a 'Qtd. Perda' ao usar essa opção."**

Ao clicar em **"Sim"**, o sistema irá fixar a quantidade de matéria-primas proporcionalizando para a quantidade apontada. Entende-se que não houve perda de matérias-primas durante o processo de produção e perda daquele Produto Acabado.

#### Manual:

No processo manual de apontamento de perdas, quando você aponta uma quantidade a menor do que deve ser produzida na atividade que gera a nota de produção, é necessário indicar a perda manual no campo **"Qtd. Total de Perda"**, desta forma o sistema tem o comportamento abaixo:

**(1)** Acesse a tela específica e localize a ordem de produção desejada.

**(2)** Informe a quantidade produzida no campo **"Qtd. apontada"** que foi efetivamente concluída.

**(3)** No campo de **"Qtd. Total de Perda"**, informe manualmente a quantidade total de perda.

**(4)** Neste cenário, a quantidade de matéria-prima é proporcionalizada entre a quantidade apontada e a quantidade de perda, sendo devidamente considerado seu consumo na perda daquele processo de produção.
