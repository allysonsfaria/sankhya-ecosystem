---
id: "25025633093783"
titulo: "Como cadastrar exames toxicológicos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25025633093783-Como-cadastrar-exames-toxicol%C3%B3gicos"
trilha: "Manual do Produto > Pessoas+ > SST – Saúde e Segurança do Trabalho > Saúde Ocupacional"
atualizado_em: "2026-10-02T17:44:16Z"
rotulos: ["Transporte", "eSocial", "Ambiente de trabalho", "Central do eSocial", "evento S-2190", "evento S-2200", "Médico", "Exame Toxicológico", "CAT", "ID: br.com.sankhya.rh.ExameToxicologico", "Pessoal+", "SESMT", "Motorista Profissional"]
---

# Como cadastrar exames toxicológicos

```
 Módulo: Pessoal+ > Rotinas Folha > SESMT   Versão disponível: A partir da 5.17.1
                                                                                                                                          MGE - 4.59.0.5
```

---

O Exame Toxicológico é obrigatório para o motorista profissional empregado de transporte rodoviário coletivo de passageiros e de transporte rodoviário de cargas. 

Este exame deve ser realizado na admissão, periodicamente (cada 2 anos e 6 meses) e, no desligamento. Lembrando que, o prazo de envio ao eSocial é até o dia 15 do mês subsequente ao da admissão/realização do exame, com o respectivo vínculo empregatício confirmado.

Desse modo, após [cadastrar o funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639) e enviar o evento S-2190 ou S-2200, acesse a tela Exames Toxicológicos e informe os dados do exame desse funcionário.

![Imagem 1: Desse modo, após cadastrar o funcionário e enviar o evento S-2190 ou S-2200, acesse a tela Exames Toxicológicos e…](https://ajuda.sankhya.com.br/hc/article_attachments/25271610205591)

Ao lado esquerdo da tela têm-se os filtros para facilitar a busca dos exames cadastrados, que pode ser por **"Empresa"**, **"Funcionário"**, **"Departamento"** ou **"Situação"** do funcionário.

Para cadastrar um novo exame, basta acionar o botão ![Imagem 2: Para cadastrar um novo exame, basta acionar o botão "Cadastrar Exame Toxicológico" e preencher os campos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/25026017248151) **"Cadastrar Exame Toxicológico"** e preencher os campos abaixo:

Indique a **"Empresa"** contratante e o **"Funcionário"** que realizou o exame.

Preencha a **"Data do exame"** lembrando que, apenas os exames realizados após o início da obrigatoriedade de envio do evento S-2221 serão registrados no eSocial, ou seja, exames cadastrados a partir de 01/08/2024. Além disso, o sistema não permitirá o cadastro do exame caso tenha alguma [CAT](https://ajuda.sankhya.com.br/hc/pt-br/articles/7067272406807) com indicação de óbito registrada para esse funcionário com data anterior ao exame.

O **"Cód. do exame"** deve ser composto por 2 letras iniciais seguidas por 9 números.

Exemplo: AB123456789

Informe o **"CNPJ do laboratório"** onde o exame foi feito e o **"Nome do médico"** responsável, preenchendo manualmente ou utilizando o ícone de pesquisa localizado a frente do campo para buscar o nome já cadastrado na tela [Cadastro de Profissionais Responsáveis pelo Ambiente de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/14716151130647).

Indique também o **"Número do CRM"** e **"UF do CRM"** desse médico, lembrando que, esses campos serão preenchidos automaticamente quando o Nome do médico for pesquisado pela tela Cadastro de Profissionais Responsáveis pelo Ambiente de Trabalho.

Finalizado o cadastro, clique no botão ![Imagem 3: Finalizado o cadastro, clique no botão "Anexo" para arquivar a imagem do exame e, em seguida em "Salvar (F7)" .](https://ajuda.sankhya.com.br/hc/article_attachments/25271693147159) **"Anexo"** para arquivar a imagem do exame e, em seguida em ![Imagem 4: Finalizado o cadastro, clique no botão "Anexo" para arquivar a imagem do exame e, em seguida em "Salvar (F7)" .](https://ajuda.sankhya.com.br/hc/article_attachments/25026716212631) **"Salvar [F7]"**.

Em seguida, deve-se enviar essas informações ao eSocial através do evento S-2221 - Exame Toxicológico Motorista Profissional Empregado.

![Imagem 5: Caso realize qualquer alteração no CNPJ do laboratório ou nos dados do médico, deve ser enviado ao eSocial o evento…](https://ajuda.sankhya.com.br/hc/article_attachments/25076750275223) Caso realize qualquer alteração no CNPJ do laboratório ou nos dados do médico, deve ser enviado ao eSocial o evento S-2221 de retificação. Se alterar qualquer outra informação, é necessário gerar o evento de exclusão do cadastro e enviar o evento de inclusão do novo cadastro.

Considere ainda que, a exclusão de exames nessa tela deve ser feita de modo decrescente, ou seja, do último para o primeiro. Além disso, deve-se gerar e enviar o evento de exclusão do S-2221 na [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175).
