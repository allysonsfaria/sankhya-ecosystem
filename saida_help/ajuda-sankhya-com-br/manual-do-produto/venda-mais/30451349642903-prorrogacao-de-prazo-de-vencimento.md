---
id: "30451349642903"
titulo: "Prorrogação de prazo de vencimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30451349642903-Prorroga%C3%A7%C3%A3o-de-prazo-de-vencimento"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Venda Mais"
atualizado_em: "2026-07-29T13:12:45Z"
rotulos: ["Parceiro", "Crédito", "Financeiro", "Configurações Venda Mais", "Venda Mais", "Status Venda Mais", "prorrogação de títulos", "prorrogação por prazo de vencimento", "Prorrogação"]
---

# Prorrogação de prazo de vencimento

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42309642210199) Versão disponível: A partir da 4.32b90 e 4.33b38
```

Após a emissão, é possível prorrogar o vencimento do boleto, enviando os dados da nova data de vencimento ao parceiro de crédito.

### Configurações da prorrogação

Para garantir que a prorrogação ocorra corretamente, é necessário que na tela **Configurações Venda Mais** > **aba Processos** > **Configurar rotinas** > **Financeiro - despesas**, preencha os campos correspondentes à geração de eventuais taxas adicionais, que serão inseridos no título de despesa:

- **Centro de Resultado:** deve-se utilizar um cadastro **Ativo** e **Analítico**;
- **Tipo de Título:** determina a classificação do título de despesa relacionado à prorrogação;
- **Conta Bancária:** define a conta bancária para o registro da despesa;
- **Natureza:** deve ser do tipo **Despesa**, com cadastro **Ativo** e **Analítico**;
- **Projeto:** identifica o projeto vinculado ao título de despesa, é necessário estar **Ativo**.

![Imagem 2: Projeto: identifica o projeto vinculado ao título de despesa, é necessário estar Ativo .](https://ajuda.sankhya.com.br/hc/article_attachments/30474079221655)

**Importante:** mesmo que nem todas as prorrogações gerem despesas, é essencial configurar essas opções para casos em que sejam necessárias.

### Realizando a prorrogação

O sistema poderá prorrogar o vencimento do boleto tanto através do título renegociado (título em nome do parceiro de crédito), quanto através do título original (parceiro original da venda/boleto). Em ambos serão lidos os dados do título original, visto que é nele que contém os dados do vencimento do boleto ao qual se deseja executar a prorrogação. 

1. Acesse a tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) e selecione o título a ser prorrogado.

2. No botão **Outras opções**, escolha a opção **Venda Mais** > **Prorrogar Vencimento**.

![Imagem 3: 2. No botão Outras opções , escolha a opção Venda Mais > Prorrogar Vencimento .](https://ajuda.sankhya.com.br/hc/article_attachments/30474412315287)

3. Informe a nova data de vencimento. O parceiro de crédito Trademaster exige um prazo mínimo de dois dias a partir da data original.

![Imagem 4: 3. Informe a nova data de vencimento. O parceiro de crédito Trademaster exige um prazo mínimo de dois dias a partir da…](https://ajuda.sankhya.com.br/hc/article_attachments/30474480091031)

4. Confirme o processo. O sistema irá validar e enviar a solicitação ao parceiro de crédito. Aqui, é apresentado o retorno de **Sucesso** ou **Falha**;

![Imagem 5: 4. Confirme o processo. O sistema irá validar e enviar a solicitação ao parceiro de crédito. Aqui, é apresentado o…](https://ajuda.sankhya.com.br/hc/article_attachments/30474477237271)

5. Se aprovado, a nova data de vencimento será registrada na seção **Prorrogação de vencimento** presente na aba **Venda Mais** dentro da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

**Observação:** a nova data não será atualizada no título original, pois ele já foi renegociado. A data atualizada pode ser consultada na aba Venda Mais.

### Falhas na prorrogação

Caso a prorrogação não seja realizada, o sistema apresentará uma mensagem indicando o motivo. As principais restrições são:

![Imagem 6: Mensagens de validação conforme regras do parceiro de crédito Trademaster:](https://ajuda.sankhya.com.br/hc/article_attachments/30451380468119) Mensagens de validação conforme regras do parceiro de crédito Trademaster:

**"A prorrogação não é permitida para títulos vencidos a mais de 60 dias. Para mais informações, entre em contato com o parceiro de crédito."**

---

**"Não é possível prorrogar o mesmo título mais de uma vez ao dia. Para mais informações, entre em contato com o parceiro de crédito."**

---

Nos casos acima, a prorrogação não pode ser realizada. Caso haja dúvidas nesta validação, o parceiro de crédito Trademaster deverá ser acionado.

![Imagem 7: Ao selecionar o título a ser prorrogado e, no momento dessa prorrogação houver indisponibilidade nos serviços do…](https://ajuda.sankhya.com.br/hc/article_attachments/30451380468887) Ao selecionar o título a ser prorrogado e, no momento dessa prorrogação houver indisponibilidade nos serviços do parceiro de crédito ou serviços Sankhya, será apresentada uma das seguintes mensagens:

**"Não foi possível realizar a prorrogação! Sistema do parceiro de crédito indisponível no momento. Reenvie a solicitação de prorrogação de vencimento novamente em alguns minutos."**

---

**"Não foi possível realizar a prorrogação! Sistema Venda Mais Indisponível no momento. Reenvie a solicitação de prorrogação de vencimento novamente em alguns minutos."**

---

Nesses casos, aguarde alguns minutos, e tente novamente, ou seja, feche o pop-up de prorrogação e acesse-o novamente, inserindo os dados e repetindo o processo.

![Imagem 8: Ao escolher vários títulos para prorrogação simultaneamente:](https://ajuda.sankhya.com.br/hc/article_attachments/30451349634583) Ao escolher vários títulos para prorrogação simultaneamente:

**"Selecione apenas um título para visualizar essa opção. Não é possível prorrogar o vencimento de múltiplos títulos simultaneamente."**

---

Selecione apenas um título por vez para realizar o processo de prorrogação.

![Imagem 9: Mensagem enviada pelo parceiro de crédito Trademaster através do retorno: Billet not found](https://ajuda.sankhya.com.br/hc/article_attachments/30451349635095) Mensagem enviada pelo parceiro de crédito Trademaster através do retorno: **Billet not found**

**"Não foi possível realizar a prorrogação! Boleto não encontrado ou já liquidado. Para mais informações, acione o parceiro de crédito."**

---

Caso haja dúvidas nesta validação, o parceiro de crédito Trademaster deverá ser acionado.

![Imagem 10: Mensagem é enviada pelo parceiro de crédito Trademaster através do retorno: sale not eligible for this operation](https://ajuda.sankhya.com.br/hc/article_attachments/30451380470423) Mensagem é enviada pelo parceiro de crédito Trademaster através do retorno: **sale not eligible for this operation**

**"Não foi possível realizar a prorrogação! Venda não elegível para esta operação. Para mais informações, acione o parceiro de crédito."**

---

Em caso de dúvidas nesta validação, o parceiro de crédito Trademaster deverá ser acionado.

### Acerto financeiro na prorrogação

Dependendo do contrato, pode ser necessário gerar uma despesa para cobrir custos adicionais.

(1)** Contratos com antecipação**

Um título de **despesa em aberto** será criado para ajustar os valores adicionais referentes à prorrogação.

(1)** Contratos sem antecipação**

- **sem taxa adicional**: nenhuma despesa é gerada;
- **com repasse realizado**: a despesa é criada para ajuste financeiro, pois, neste caso, quando o título de receita original da prorrogação já tiver sido baixado, entende-se que o repasse já foi realizado, e a negociação com o parceiro de crédito sobre os dias adicionais acontecerá por meio de uma despesa;
- **com repasse não realizado**: a taxa adicional é somada à **taxa Venda Mais** da receita original, visto que, se o título da receita original não tiver sido baixado, entende-se que o repasse não foi realizado.

### Geração do título de despesa

Se uma despesa for necessária, ela será criada após a confirmação da prorrogação:

1. O sistema exibirá a opção de gerar o título de despesa.
2. Se bem-sucedido, a mensagem de confirmação exibirá o **Nro Único** da despesa.
3. O título pode ser consultado na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) pelo **Nro Único** ou pelo **Nro da Nota** que originou essa prorrogação.

![Imagem 11: O título pode ser consultado na Movimentação Financeira pelo Nro Único ou pelo Nro da Nota que originou essa…](https://ajuda.sankhya.com.br/hc/article_attachments/30474582389015)

#### Cálculo do valor da despesa

- **Com antecipação:**

```
Valor desdobramento = [(Dias Operacionais * (Taxa/30)) * Valor do Título] / 100]
```

Onde:

Dias Operacionais = Nova data de vencimento - Dt. Vencimento (do título original)

Taxa = Taxa de Antecipação da aba Dados Contratuais, tela Configurações Venda Mais do produto Venda Mais **com** antecipação

- **Sem antecipação:**

```
Valor desdobramento = [(Dias Prorrogados * (Taxa Variável/30)) * Valor do Documento] / 100
```

Onde: 

Dias Operacionais Prorrogados = Nova data de vencimento - Dt. Vencimento (do título original)

Taxa Variável = Taxa Variável da aba Dados Contratuais, tela Configurações Venda Mais do produto Venda Mais sem antecipação

**Importante:** se houver falha na geração da despesa, o título ainda assim será prorrogado. 

![Imagem 12: Importante: se houver falha na geração da despesa, o título ainda assim será prorrogado.](https://ajuda.sankhya.com.br/hc/article_attachments/30474648474519)

Nesse caso, corrija os dados e tente novamente, acessando a opção **Gerar Título de Despesa** **da prorrogação** na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

![Imagem 13: Nesse caso, corrija os dados e tente novamente, acessando a opção Gerar Título de Despesa da prorrogação na…](https://ajuda.sankhya.com.br/hc/article_attachments/30474706222103)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30451349642903-Prorroga%C3%A7%C3%A3o-de-prazo-de-vencimento#top)
