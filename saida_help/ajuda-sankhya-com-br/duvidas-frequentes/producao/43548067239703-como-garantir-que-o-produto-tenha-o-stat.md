---
id: "43548067239703"
titulo: "Como garantir que o produto tenha o status alterado de quarentena para aprovado após o laudo?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548067239703-Como-garantir-que-o-produto-tenha-o-status-alterado-de-quarentena-para-aprovado-ap%C3%B3s-o-laudo"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-09-30T13:25:19Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Como garantir que o produto tenha o status alterado de quarentena para aprovado após o laudo?

Ao finalizar o ciclo de controle de qualidade no Sankhya, espera-se que o **Status do Lote** do Produto Acabado seja alterado de **"Quarentena"** para **"Aprovado"** ou **"Reprovado"**, conforme o resultado do ciclo. No entanto, em alguns casos, mesmo após a conclusão do laudo, o status pode permanecer como Quarentena.

Esse comportamento pode estar relacionado à configuração do ciclo de controle de qualidade, à configuração do Produto ou à forma como o processo foi executado. A seguir, veja como identificar e corrigir os principais pontos para garantir que o Status do Lote seja atualizado corretamente.

### Configurações do ciclo de controle de qualidade

Para que o Status do Lote seja alterado ao final do ciclo de controle de qualidade, é necessário que a atividade responsável pela conclusão do ciclo esteja configurada corretamente.

Acesse a tela **"Processo Produtivo - Nova"** (Produção » Cadastros » Processo Produtivo - Nova) e, na aba **"Controle de Qualidade"**, verifique se a marcação **"Conclui Ciclo de Controle de Qualidade"** está habilitada na atividade responsável pela finalização do ciclo.

Além disso, quando o objetivo for alterar o Status do Lote do Produto Acabado ao final do ciclo, verifique se a opção **"Aprova/Reprova 'Status do Lote' no final do Ciclo"** está marcada.

Essa opção somente fica disponível quando a atividade está configurada para **"Conclui Ciclo de Controle de Qualidade"**.

Também é necessário que o produto esteja configurado para trabalhar com **controle por lote e 'Usa Status de Lote'**, conforme as configurações do produto e do parâmetro **'UTILSTATUSLOTE - Utiliza Status do Lote?'**.

### Execução correta do processo de laudo

O ciclo de controle de qualidade só será finalizado corretamente se todas as amostras e laudos necessários forem lançados e concluídos. Siga o fluxo:

**(1)** Na tela **"Operações de Produção"** (Produção » Rotinas » Operações de Produção), inicie o ciclo de controle de qualidade e aprove as amostras.

**(2)** Preencha todos os itens de laudo, apontando os resultados das características analisáveis.

**(3)** Clique no botão **"Concluir Laudo"** para finalizar o ensaio.

**(4)** Finalize o ciclo de controle de qualidade na tela de operações de produção através do botão de finalizar a atividade.

Se a marcação **'Gerar Registro de Amostra e Laudo'** estiver realizada no processo produtivo, é possível fazer o processo fora da produção, ou seja, pelas telas **"Registros de Amostras"** e "**Controle de Laudos de Amostras"**.

### Outros pontos de atenção

• Se o produto não estiver configurado para controle por lote e utilização de **Status de Lote**, a alteração do Status do Lote não ocorrerá conforme esse fluxo.

• Caso o ciclo seja reprovado e seja escolhida a opção de **'Reprovando' ao Concluir Laudo**, o Status do Lote ficará como **R-Reprovado**, enquanto não iniciar um novo ciclo ou gerar novo laudo/amostra para **Aprovar.**

• A conclusão do **Laudo** não significa, necessariamente, a conclusão do **Ciclo de Controle de Qualidade**. Para que o Status do Lote seja tratado ao final do ciclo, é necessário que a atividade responsável esteja configurada para **Concluir o Ciclo de Controle de Qualidade** e, quando aplicável, para **Aprovar/Reprovar "Status do Lote" no final do Ciclo**.

Revise as configurações do Produto, do Processo Produtivo e a execução do ciclo de Controle de Qualidade para identificar em qual etapa o processo não foi concluído conforme o fluxo configurado.
