---
id: "16941845335063"
titulo: "[Erro 677]: Não pode existir qualquer evento para o vínculo trabalhista com data posterior a data do desligamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16941845335063--Erro-677-N%C3%A3o-pode-existir-qualquer-evento-para-o-v%C3%ADnculo-trabalhista-com-data-posterior-a-data-do-desligamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:17:58Z"
rotulos: ["Eventos", "eSocial", "Central do eSocial", "Erro 677: Eventos Pós-Desligamento", "Erro", "Desligamento", "RH"]
---

# [Erro 677]: Não pode existir qualquer evento para o vínculo trabalhista com data posterior a data do desligamento

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16941845289367) **MENSAGEM:**

[Erro 677]: Não pode existir qualquer evento para o vínculo trabalhista com data posterior a data do desligamento.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16941861283607)CAUSA:**

O erro indica que foi enviado algum evento com a data posterior ao desligamento, geralmente pode ser eventos de SST (S-2210, S-2220 e S-2240), eventos de alteração cadastral S-2205, alterações contratuais S-2206 ou Remunerações S-1200 então deve ser verificado no portal qual é o evento esta enviado com data posterior. 
Se for algum envio indevido ou com data incorreta fazer a exclusão ajustar no sistema as informações para que seja gerado o evento com as informações corretas a serem enviadas.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16941821639575)SOLUÇÃO:**

Identifique no portal eSocial  qual foi o envio realizado com data posterior ao desligamento.

Acesse: Empregado >> Gestão de Empregados >> no campo busca digitar o CPF completo >> Movimentações Trabalhistas

![Imagem 4: Acesse: Empregado >> Gestão de Empregados >> no campo busca digitar o CPF completo >> Movimentações Trabalhistas](https://ajuda.sankhya.com.br/hc/article_attachments/17294684419223)

Neste caso aqui observa-se que o desligamento do funcionário era 21/07/2023 e no portal do eSocial constava um S-2220 – Monitoramento da Saúde do Trabalhador com data do evento em 26/07/2023, ou seja posterior a data da demissão.

**Para o devido ajuste da data do evento S-2220 - Monitoramento da Saúde do Trabalhador**

Se o envio foi realizado pelo sistema Sankhya entre na rotina **Atestado de Saúde Ocupacional (ASO) -**
Pessoal+ » Cadastros » Atestado de Saúde Ocupacional (ASO):

Filtre Empresa  >> Clicar sobre o card do funcionário >>Clicar sobre  ASO >> clicar no ícone 'Lápis' para editar o ASO.

![Imagem 5: Se o envio foi realizado pelo sistema Sankhya entre na rotina Atestado de Saúde Ocupacional (ASO) - Pessoal+ »…](https://ajuda.sankhya.com.br/hc/article_attachments/17294708681623)

Feito o ajuste do ASO, gere os eventos na Central do esocial e envie o S-2220 de Retificação para eSocial.

Em seguida gere o evento S-2299 e enviar o desligamento para eSocial.

**Observação:** Se o envio NÃO foi realizado pelo sistema Sankhya, acione o responsável pelo envio dos eventos de SST da sua empresa e solicite os devidos ajustes, e só após o ajuste poderá fazer o envio do desligamento.
