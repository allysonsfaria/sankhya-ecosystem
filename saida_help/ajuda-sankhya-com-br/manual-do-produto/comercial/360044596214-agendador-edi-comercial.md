---
id: "360044596214"
titulo: "Agendador EDI Comercial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:20:29Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Layout", "Agendamento", "EDI", "br.com.sankhya.com.cfg.agendadoredicomercial", "Agendador EDI Comercial manual", "Agendador EDI Comercial", "Envio por E-mail ou FTP: Opções para disponibilização dos arquivos gerados", "Comercial"]
---

# Agendador EDI Comercial

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311730347927) Módulo: Comercial > Avançado > Agendadores
```

---

Esta tela permite que seja realizada a definição de agendamentos para a geração de arquivos de remessa por layout. Assim, tem-se a geração automática dos arquivos de remessa EDI Comercial, como no envio por e-mail ou FTP.

Inicialmente, insira o **"Nro. agendamento"** que corresponde à identificação do agendamento, sendo que ele pode ser gerado de forma automática ou manual.

Em **"Descrição agendamento"**, informe o nome do agendamento a ser executado.

A marcação **"Ativo"** determina se o agendamento está ativo ou não, ou seja, se pode ou não ser utilizado.

Para conhecer as funcionalidades dessa tela, clique nos links abaixo:                 

| Funcionalidades da Tela | |
| --- | --- |
| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#abageral) | [Aba Horários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#abahorrios) |
| [Aba Frequência Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#abafrequnciaagendamento) | [Aba Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#abaconfiguraes) |

---

### Aba Geral

Por meio desta aba pode-se acompanhar o status da última execução do agendador através do campo **"Status Última Execução"**.

![Imagem 2: Por meio desta aba pode-se acompanhar o status da última execução do agendador através do campo "Status Última…](https://ajuda.sankhya.com.br/hc/article_attachments/21045099800343)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#top)

### Aba Horários

Nesta aba será possível configurar o período que a próxima geração de arquivos será realizada no campo **"Próxima execução em"**, assim como a data final dessa execução, que será definida em **"Data Final de Execução"**.

![Imagem 3: Nesta aba será possível configurar o período que a próxima geração de arquivos será realizada no campo "Próxima…](https://ajuda.sankhya.com.br/hc/article_attachments/21045099812375)

Visto que a geração do arquivo é automática, o sistema disponibiliza três possibilidades, sendo elas:

- Disponível no repositório de arquivo;
- Pode ser enviado por e-mail;
- Disponibilizado em um FTP.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#top)

### Aba Frequência Agendamento

Tem-se nesta aba, as configurações referentes à frequência do agendamento, sendo elas:

**1)** Pode-se intercalar o agendamento dentre uma ou várias execuções, em um horário específico;

**2)** Indicar em qual mês ocorrerá o agendamento, podendo ser em um determinado mês, acima de um, ou em todos os meses;

**3)** Conforme a configuração executada no item acima, será configurada a frequência do agendamento de acordo com as seguintes formas:

- **Diário:** ao selecionar essa opção, a frequência será efetuada diariamente durante a semana;
- **Semanal:** nessa opção de frequência, determina-se um dia da semana, acima de um ou todos os dias da semana;
- **Mensal:** configura-se através dessa opção, um dia específico do mês para realizar o agendamento, acima de um, ou diariamente durante o mês.

![Imagem 4: Mensal: configura-se através dessa opção, um dia específico do mês para realizar o agendamento, acima de um, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/21045099829271)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#top)

### Aba Configurações

O **"Layout"** é a base para se chegar aos dados do arquivo que serão executados na geração do mesmo, sendo que, será um único layout por agendamento.

**Observação:** o campo Layout só trará informação de grau 1, ou seja, não incluirá os incidentes filhos.

![Imagem 5: Observação: o campo Layout só trará informação de grau 1, ou seja, não incluirá os incidentes filhos.](https://ajuda.sankhya.com.br/hc/article_attachments/21045099839383)

Após a geração do arquivo, ele poderá ser enviado para um diretório no Repositório de arquivos, por e-mail ou para um servidor FTP. Abaixo, tem-se sobre cada um deles:

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#top)

#### Repositório de arquivos

Insira no campo **"Caminho"** o endereço do diretório que foi previamente cadastrado na tela [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos).

---

#### E-mail

A **"Conta** **SMTP"** deve ser previamente cadastrada na tela [Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP). Além disso, nos campos **"E-mail(s) do(s) destinatário(s)"** e **"E-mail(s) para informar erros"** pode-se apontar um ou vários endereços de e-mail pertencentes aos destinatários e informar um ou mais endereços de e-mail responsáveis pelo recebimento de mensagens de problemas que podem ocorrer na geração do(s) arquivo(s), respectivamente.

---

#### FTP

Aqui será possível inserir os dados de conexão por meio do campo **"Endereço"**. É possível também utilizar o Assistente para definir os parâmetros de acesso Endereço, Usuário, Senha e Porta.

**Nota:** poderá ser configurado os três tipos de disponibilizações simultaneamente.

Por meio da marcação **"Usa SFTP"** será indicado ao sistema se agendamento utilizará o SFTP. Assim, ao selecioná-la o campo **"Porta"** ficará disponível para preenchimento, uma vez que, quando a marcação for selecionada, a Porta deve ser informada.

Dessa forma, poderá ser configurado o protocolo FTP ou SFTP e a Porta, além do **"Endereço"**, **"Usuário"** e **"Senha"**. Então, quando o sistema executar o agendamento serão gerados os arquivos no endereço configurado.

No campo Endereço poderá ser preenchido, por exemplo: 192.168.1.218//home/mgeweb/EDI.

---

#### Filtros para execução do agendamento

Os layouts possuem consultas que são executadas a fim de obter os dados a serem inseridos no arquivo gerado, essas consultas podem conter condições (filtros). Portanto, aqui pode configurar os filtros que serão empregados na execução da consulta. Assim, temos:

O campo **"Data inicial"**, que contém as seguintes opções:

- Hoje;
- Última execução;
- 1° dia do mês;
- Últ. dia do Mês.

No campo **"Data final"** tem-se as opções **"Hoje"** e **"Últ. dia do Mês"**.

**Nota:** os únicos parâmetros de consulta que o layout poderá utilizar serão o DTINICIO e DTFIM.

Através dos campos **"Dias p/ somar dt. inicial"** e **"Dias p/ somar dt. inicial"**, pode-se indicar a quantidade de dias que será inserida na data inicial e final do filtro.

**Observação:** o filtro deverá ser preenchido manualmente. Assim, considere o exemplo abaixo:

( :CODEMP: = 1 ) .E.
( :DTNEG: >= [DTINICIO] ) .E.
( :DTNEG: <= [DTFIM] )

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596214-Agendador-EDI-Comercial#top)
