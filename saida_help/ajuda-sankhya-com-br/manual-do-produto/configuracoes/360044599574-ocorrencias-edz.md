---
id: "360044599574"
titulo: "Ocorrências EDZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599574-Ocorr%C3%AAncias-EDZ"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:49:01Z"
rotulos: ["manual", "Configuração", "Parceiro", "Ocorrências", "Integração", "Aba Crédito", "Análise de Crédito EDZ", "Cadastro de Emitentes de Cheques sem Fundos", "Cadastro de Parceiros", "CCF", "Configuração EDZ", "crédito", "EDZ Consultoria", "FTP", "Ocorrências EDZ", "Parâmetros", "Receita Federal CNPJ", "Receita Federal CPF", "br.com.sankhya.cadastro.ocorrencia.edz", "Ocorrências EDZ manual", "Sintegra", "Gerenciamento de Ocorrências EDZ no Sankhya-Om"]
---

# Ocorrências EDZ

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310692138007) Módulo: Configurações > Avançado
```

---

Esta rotina aborda as ocorrências EDZ ligadas exclusivamente da Integração do Sankhya-Om com a EDZ Consultoria. Para mais informações sobre a EDZ Consultoria acesse <http://www.dez.com.br/edz/index.htm>.

As Ocorrências EDZ correspondem aos resultados das consultas realizadas e retornadas ao sistema. Através destas, o sistema executa suas próprias decisões, podendo bloquear a venda a prazo para o parceiro ou zerar seu limite. Estas ocorrências estão vinculadas a "Palavras chave", as quais correspondem ao resultado das consultas retornadas.

O campo **"Código"** permite efetuar uma busca mais precisa e rápida do(s) cadastro(s) desejado(s) através de vários critérios diferentes.

A identificação sobre o tipo de ocorrência será descrita no campo **"Descrição"**.

No campo **"Registro"** informe a qual documento essa consulta corresponde. São apresentadas as seguintes opções:

- R. Federal CNPJ;
- R. Federal CPF;
- Sintegra;
- CCF;
- Outros.

Por meio do campo **"Padrão"**, é definido se a ocorrência é padrão ou não para o tipo de registro.

Dessa forma, teremos abaixo as configurações necessárias para realizar o cadastro de uma ocorrência:

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599574-Ocorr%C3%AAncias-EDZ#abageral)                                                              [Aba Palavras chave](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599574-Ocorr%C3%AAncias-EDZ#abapalavraschave)

[Configuração EDZ](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025391013-Configura%C3%A7%C3%A3o-EDZ)

## Aba Geral

Essa aba apresenta as configurações relacionadas a cada tipo de ocorrência.

![Imagem 2: Essa aba apresenta as configurações relacionadas a cada tipo de ocorrência.](https://ajuda.sankhya.com.br/hc/article_attachments/360098579974)

O campo **"Situação"** descreve o resultado da consulta correspondente à ocorrência, são apresentadas as opções **"Inalterado"**, **"Regularizado"** e **"Negativado"**. A situação de cada parceiro será apresentada no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232674-Parceiros), aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232674-Parceiros#abacrdito), **"Seção EDZ"** através dos campos **"Situação na Receita Federal"**, **"Situação no CCF"** e **"Situação no Sintegra"** respectivamente.

O acionamento da opção **"Bloquear Parceiro"**, define se no **"Cadastro de Parceiros"**, aba **"Crédito"**, a opção **"Bloquear venda a prazo"** será ou não marcada.

Quando a opção **"Zerar limite de crédito"** estiver marcada, no **"Cadastro de Parceiros"**, aba **"Crédito"**, o campo **"Limite crédito mensal"** terá o valor zerado.

Tem-se casos em que os parceiros são também fornecedores ou clientes e possuem o mesmo CNPJ para ambas modalidades. O campo **"Tipo de parceiro"** tem a funcionalidade de filtrar os parceiros no momento do processamento da ocorrência. A regra dessa ocorrência deve valer para apenas uma modalidade do parceiro.

As informações indicadas no campo **"Alteração grupo autorização"**, irão preencher o campo **"Grupo de autorização"** no **"Cadastro de Parceiros"**, aba **"Crédito"**.

Ocorreram casos em que será necessário executar uma **"Stored Procedure"** durante o processamento da ocorrência. No campo **"Noma da Store Precedure"** deve ser alimentado com o nome da mesma. Ao chamar essa **"Stored Procedure"** o sistema passará como argumento o número do movimento.

**Nota:** uma **"Stored Procedure"** é um conjunto de comandos SQL que podem ser armazenados no servidor. Uma vez que isto tenha sido feito, os usuários não precisam reenviar os comandos individuais mas podem fazer referência as Stored Procedure.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599574-Ocorr%C3%AAncias-EDZ#top)

## Aba Palavras chave

As Palavras Chave cadastradas nesta aba tem a funcionalidade de casar com o resultado retornado de uma consulta EDZ. Pode-se cadastrar várias palavras chave e caso alguma faça combinação com o resultado a referida ocorrência será executada.

![Imagem 3: As Palavras Chave cadastradas nesta aba tem a funcionalidade de casar com o resultado retornado de uma consulta EDZ.…](https://ajuda.sankhya.com.br/hc/article_attachments/360100817353)

Para que a ocorrência corresponda por exemplo a uma consulta EDZ que tenha retornado como resposta a existência de pendências no Sintegra consultado como irregular, deve-se cadastrar a palavra chave **"Sintegra Irregular"**. Dessa forma, assim que o sistema verificar essa compatibilidade, ele executará os comandos cadastrados anteriormente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599574-Ocorr%C3%AAncias-EDZ#top)
