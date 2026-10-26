---
id: "360044597214"
titulo: "Histórico de Cheques"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597214-Hist%C3%B3rico-de-Cheques"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:37:49Z"
rotulos: ["AJUDA DO SKW", "manual", "Consulta", "Contas", "Parceiro", "Movimentação Financeira", "br.com.sankhya.historicocheques", "Histórico de Cheques manual", "Financeiro", "Cheque", "Permite verificar status e destino dos cheques", "Busca por CMC7 data status tipo parceiros e contas", "Registra e exibe eventos como recebimento baixa estorno e devolução"]
---

# Histórico de Cheques

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312260396951) Módulo: Financeiro > Consultas
```

---

![Imagem 2: Esta tela será apresentada para uso, caso o parâmetro "Usa rastreabilidade de cheques? - USARASTCHEQUE" esteja…](https://ajuda.sankhya.com.br/hc/article_attachments/16286885898135) Esta tela será apresentada para uso, caso o parâmetro **"Usa rastreabilidade de cheques? - USARASTCHEQUE"** esteja habilitado.

Esta rotina permite realizar a consulta dos cheques que foram gerados no financeiro. Assim, você pode verificar qual foi o destino dado para um cheque recebido, se o mesmo ainda está em poder da empresa, se já foi depositado em algum banco ou se foi utilizado para pagar algum título da empresa.

Localizado no lado esquerdo da tela, o quadrante Filtros é composto por campos que auxiliarão na localização dos cheques. A pesquisa poderá ser realizada pelas entidades do parceiro e do financeiro ou pelos filtros rápidos, informando a **"Banda CMC7 ou n° do cheque"**, a **"Data do cheque"**, o seu **"Status"**, o **"Tipo do cheque"**, os **"Parceiros"** e as **"Contas"**.

Depois de definidos os filtros desejados, acionando botão ![Imagem 3: Depois de definidos os filtros desejados, acionando botão "Aplicar" localizado no alto da tela, fará com que sejam…](https://ajuda.sankhya.com.br/hc/article_attachments/16286892808855)**"Aplicar"** localizado no alto da tela, fará com que sejam apresentados os cheques que foram localizados.

![histórico](https://ajuda.sankhya.com.br/hc/article_attachments/15499171041431)

Ao lado superior direito da tela, temos a grade **"Relação de cheques"** que comporta as informações relacionadas ao título. Já na parte inferior, a grade **"Histórico do cheque"** apresenta os dados pertinentes os eventos.

Através do botão ![Imagem 5: Através do botão "Detalhes" localizado na grade Histórico do cheque , teremos a exibição de um pop-up de mesma…](https://ajuda.sankhya.com.br/hc/article_attachments/16286952392343)**"Detalhes"** localizado na grade Histórico do cheque, teremos a exibição de um pop-up de mesma nomenclatura, contendo as informações detalhadas sobre cada evento:

![Imagem 6: Através do botão "Detalhes" localizado na grade Histórico do cheque , teremos a exibição de um pop-up de mesma…](https://ajuda.sankhya.com.br/hc/article_attachments/15499171049111)

Em cada movimentação do cheque, devemos registrar principalmente, a conta de origem e qual foi a conta de destino, além dos campos listados acima que é importante para cada situação. A partir do momento em que o sistema registrar o cheque, sempre que eventos acontecerem a este cheque, deverão ser gravados para serem exibidos na tela Histórico de Cheques.

Abaixo, temos uma lista dos eventos e seus respectivos status:

O ato de preencher o CMC7 de um título cria o evento **"Recebimento/Emissão"** com status **"Registrado"**.

Quando o título for baixado, será salvo o evento de **"Baixa"**. Caso o título esteja em uma conta do tipo **"Conta Corrente"**, seu status será **"Em depósito"**; caso contrário, terá o status **"Aguardando depósito"**.

Se houver um evento de **"Estorno"** da baixa, o cheque voltará ao status de Registrado.

Toda **"Transferência"** de títulos deverá gerar um evento; assim, se a conta de destino for uma Conta Corrente, seu status irá para Em depósito, caso contrário, para Aguardando depósito, conforme o evento da Baixa.

Quando o título passar para **"Conciliado = Não"**, o status será alterado para o status anterior à Conciliação.

Todo **"Pagamento de despesas"** registrará o status **"Pago à terceiro"** e, quando estornado o pagamento, o status permanecerá como **"Pago à terceiro"**.

Toda **"Devolução de cheques"** registrará o status **"Devolvido"**, sendo que, esta opção não existe um estorno.

A **"Renegociação de títulos"** possuirá o status **"Renegociado"** e para esta opção também não existe um estorno.

Quando você remover manualmente o CMC7 de um título, o Sankhya Om registrará o evento como **"Excluído"**, fazendo com que o título deixe de ser reconhecido como um cheque.

Por fim, quando você realizar o procedimento de **"Desconto de Títulos"**, o status do cheque será registrado como **"Antecipado"**.
