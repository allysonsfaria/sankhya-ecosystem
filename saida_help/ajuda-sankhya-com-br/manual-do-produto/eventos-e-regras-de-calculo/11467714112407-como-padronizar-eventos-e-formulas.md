---
id: "11467714112407"
titulo: "Como padronizar eventos e fórmulas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11467714112407-Como-padronizar-eventos-e-f%C3%B3rmulas"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Eventos e Regras de Cálculo"
atualizado_em: "2026-10-07T15:39:36Z"
rotulos: ["Configuração", "Eventos", "Fórmulas", "Atualização", "Folha de Pagamento", "br.com.sankhya.rh.PadronizaEvtFormula", "Padronização de Eventos", "Pessoal+"]
---

# Como padronizar eventos e fórmulas

```
 Módulo: Pessoal+ > Rotinas Folha          Versão: a partir da 4.17
```

---

Nesta tela deve-se realizar o vínculo de características com os eventos personalizados, para que, assim, o sistema possa utilizá-los de maneira padronizada ou personalizada.

![Imagem 1: Nesta tela deve-se realizar o vínculo de características com os eventos personalizados, para que, assim, o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/26805380016407)

Então, ao abrir a tela, o sistema exibirá a mensagem:

**"ATENÇÃO!**

**O objetivo dessa tela é realizar a padronização de eventos e fórmulas do Pessoal+ para clientes que estão em processo de migração do MGE Pessoal para o Pessoal+, Antes de iniciarmos o processo é necessário definir se deseja copiar todas as fórmulas da tabela TFPFOR, hoje utilizadas nos cálculos do MGE Pessoal, para a tabela TFPNEWFORM. Se sim, a tabela TFPNEWFORM será excluída para receber os novos dados que estarão todos como "personalizados" para que não sofram modificações na atualização de eventos e fórmulas do Pessoal+. Do contrário, a tabela TFPNEWFORM terá apenas as fórmulas padrão Sankhya. Deseja realizar a cópia?"**

Caso acione a opção **"Sim"**, as tabelas de fórmulas do Pessoal+ serão limpas e as tabelas de fórmulas do **"MGE Pessoal"** serão migradas e quando concluído, as atualizações serão executadas logo depois. Dessa forma, as fórmulas serão ajustadas junto às características.

Mas, caso selecione a opção **"Não"**, o pop-up com a mensagem será fechado e a migração das fórmulas não acontecerá.

**Observação:** fórmulas criadas na tela [Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287) não serão duplicadas para o MGE Pessoal.

Assim, tem-se na aba **"Eventos"**, as parametrizações dos padrões de fórmulas, onde será possível utilizar os filtros disponíveis no ícone ![Imagem 2: Assim, tem-se na aba "Eventos" , as parametrizações dos padrões de fórmulas, onde será possível utilizar os filtros…](https://ajuda.sankhya.com.br/hc/article_attachments/11535159784727) **"Filtrar"**, sendo eles:

- Todas;
- Características sem eventos;
- Características com eventos;
- Eventos padrão Sankhya;
- Eventos personalizados;
- Vinculações obrigatórias.

Pode-se também, reverter a última atualização realizada por meio do botão **"Reverter última atualização"**, desse modo, o sistema irá realizar uma busca pela última sequência existente e irá retornar esses dados para as tabelas originais. Após essa reversão, a data e hora da atualização anterior serão atualizadas nas telas [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767), [Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287) e Padronização de Eventos. 

**Observação:** caso seja identificado algum dado em um Evento, Fórmula ou Base, estes serão alterados na atualização, de forma que será realizada uma cópia armazenada em uma tabela histórica antes da efetiva alteração para ser revertida, quando necessário.

Tem-se também, o botão ![Imagem 3: Tem-se também, o botão "Conferir alterações" que irá verificar se existem características sem evento vinculado e caso…](https://ajuda.sankhya.com.br/hc/article_attachments/18860632396695) **"Conferir alterações"** que irá verificar se existem características sem evento vinculado e caso encontre no repositório da Sankhya, ele será criado também na base de dados do cliente e ainda, vinculado à característica na tela de migração.

Além disso, quando houver eventos personalizados que forem padronizados ou ainda, padronizados que forem personalizados, você poderá conferir o histórico dessas modificações ao pressionar o botão indicado acima. 

Porém, quando a marcação **"Padrão Sankhya"** estiver com o ícone ao utilizar o botão, indicará que a referida característica é um padrão do sistema e por isso, não poderá ser editada. Então, o sistema irá manter as informações do evento personalizado vinculado a uma tabela e suas configurações com as características padrões serão copiadas para o evento personalizado.

Quando houver a possibilidade de selecionar a marcação **"Reverter"**, as características que tiveram o evento vinculado com a marcação Padrão Sankhya, sendo este identificado pelo ícone terão as suas configurações dos eventos personalizados a ser consideradas novamente ao evento, revertendo assim, a padronização e o ícone será identificado como .

Tem-se ainda que, quando um evento de Base personalizado for relacionado a uma característica, o mesmo não poderá ser editado, ou seja, as marcações Padrão Sankhya e Reverter ficarão desabilitadas. 

Além disso, quando você desejar mudar o evento através do campo **"Código"**, ao clicar no botão Conferir alterações o sistema irá salvar o novo registro inserido e ativá-lo. 

Por fim, após realizar o processo de vínculo de eventos às características e utilizar o referido botão, o sistema irá verificar a coluna **"Características"** dessa tela para preencher as tabelas de bases.

Dessa forma, ao conferir todas as alterações, a tabela de bases será atualizada conforme as configurações feitas e poderão ser visualizadas na aba [Bases de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#ababasesdecalculo) da tela Eventos.

**Observação:** após a realização das parametrizações, pode indicar se o evento irá utilizar as configurações aqui realizadas como base para os cálculos através da marcação **"É base?"** da aba [Básico](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#ababasico) da tela Eventos.

Quando as características do evento forem preenchidas, as informações destas serão apresentadas no log do cálculo das folhas de pagamentos realizadas na tela [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031). Nela, será encontrado um resumo das modificações realizadas ao utilizar o botão Conferir alterações, e após verificar essas modificações, clique no botão ![Imagem 4: Quando as características do evento forem preenchidas, as informações destas serão apresentadas no log do cálculo das…](https://ajuda.sankhya.com.br/hc/article_attachments/18860607577751) **"Concluir"** para executar todas as ações conforme definidas, ou clique em **"Voltar"** para fechar o detalhamento e retornar para a tela Padronização de Eventos:

![Imagem 5: Quando as características do evento forem preenchidas, as informações destas serão apresentadas no log do cálculo das…](https://ajuda.sankhya.com.br/hc/article_attachments/26805558104855)

**Nota:** quando a tela atualizar os eventos e fórmulas, apenas os eventos padrões e ativos serão considerados.

Caso queira, pode-se também expandir os eventos de uma só vez por meio do botão **"Abrir todos"**:

[GIF animado: Imagem 6: Caso queira, pode-se também expandir os eventos de uma só vez por meio do botão "Abrir todos" :](https://ajuda.sankhya.com.br/hc/article_attachments/26805558106263)

Além disso, por meio do botão ![Imagem 7: Além disso, por meio do botão "Pausar Padronização" é possível interromper o processo de padronização para retornar a…](https://ajuda.sankhya.com.br/hc/article_attachments/18860632424215) **"Pausar Padronização"** é possível interromper o processo de padronização para retornar a tabela TFPEVE ao estado anterior à utilização de qualquer funcionalidade da tela Padronização de Eventos.

Assim, não será possível realizar nenhum processo nessa tela até que o processo seja retomado através do botão ![Imagem 8: Assim, não será possível realizar nenhum processo nessa tela até que o processo seja retomado através do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/18860607608343) **"Continuar Padronização"**. 

Porfim, pode-se também ![Imagem 9: Porfim, pode-se também "Descartar Alterações" realizadas nos Eventos .](https://ajuda.sankhya.com.br/hc/article_attachments/26805596769943) **"Descartar Alterações"** realizadas nos Eventos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/11467714112407-Como-padronizar-eventos-e-f%C3%B3rmulas#top)
