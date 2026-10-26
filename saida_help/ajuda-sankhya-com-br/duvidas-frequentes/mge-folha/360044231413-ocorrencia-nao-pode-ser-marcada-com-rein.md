---
id: "360044231413"
titulo: "Ocorrência não pode ser marcada com reincidência (60 dias)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044231413-Ocorr%C3%AAncia-n%C3%A3o-pode-ser-marcada-com-reincid%C3%AAncia-60-dias"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:03Z"
rotulos: ["#RevisadoLorrana", "Ocorrências", "eSocial", "Configuração Funcionários", "Central do eSocial", "Erro ao Marcar Reincidência em Ocorrência", "Erro"]
---

# Ocorrência não pode ser marcada com reincidência (60 dias)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16421934145047) MENSAGEM:**

Ocorrência não pode ser marcada com reincidência (60 dias). Não existem ocorrências no período de 60 dias para relacionar.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16421934148503) SITUAÇÃO:**

Mensagem apresentada ao tentar lançar um registro de ocorrência de afastamento (atestados, auxilio doença, acidente de trabalho, etc.) na tela **"Registros de Ocorrências"**, marcando a opção **"Reincidência (60 dias)?".**

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16421905773335) SOLUÇÃO:**

**Situação 1** **-** Já existe um afastamento (atestados, auxilio doença, acidente de trabalho, etc) com data inferior a 60 dias.

Confira as informações abaixo:

![Imagem 4: MGEPessoal » Lançamentos » Histórico do Funcionário » Histórico de Ocorrências](https://ajuda.sankhya.com.br/hc/article_attachments/16421934154263) MGEPessoal » Lançamentos » Histórico do Funcionário » Histórico de Ocorrências

Selecione o tipo de Ocorrência do primeiro afastamento lançado e no campo **"Situação do Funcionário"** certifique se está devidamente preenchido. Exemplo: Se for um atestado, o campo deverá ser preenchido com **"Atestado em Dias"**.

![Imagem 5: MGEPessoal » Lançamentos » Histórico do Funcionário » Registro de Ocorrências](https://ajuda.sankhya.com.br/hc/article_attachments/16421905775895) MGEPessoal » Lançamentos » Histórico do Funcionário » Registro de Ocorrências

Efetue o lançamento novamente e será permitido a marcação da opção Reincidência (60 dias).

**Situação 2 -** Não existe um afastamento anterior (atestados, auxilio doença, acidente de trabalho, etc) com data inferior a 60 dias. Para esse exemplo, não marque a opção Reincidência (60 dias).

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16421934159767) CAUSA:**

Ocorre quando o tipo de Ocorrência para atestados médicos está com o campo Situação do Funcionário configurado de forma incorreta, ou não existem afastamentos com data anterior de até 60 dias.
