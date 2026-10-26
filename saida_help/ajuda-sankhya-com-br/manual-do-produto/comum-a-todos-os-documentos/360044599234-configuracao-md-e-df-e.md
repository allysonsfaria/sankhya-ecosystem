---
id: "360044599234"
titulo: "Configuração MD-e/DF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599234-Configura%C3%A7%C3%A3o-MD-e-DF-e"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > Comum a todos os documentos"
atualizado_em: "2026-09-29T01:52:18Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "NF-e", "INTCONSULTAMDE", "br.com.sankhya.com.mov.configuracao.mde", "Configuração MD-e/DF-e manual", "Configuração MD-e", "XML", "SEFAZ", "MD-e", "Configuração de MD-e/DF-e: Automatização e Preferências", "Documentos Eletrônicos", "DF-e"]
---

# Configuração MD-e/DF-e

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311771591191) Módulo: Comercial > Rotinas
```

---

Através desta tela, configure algumas preferências para que o sistema execute os serviços da Manifestação do Destinatário de forma automática. Todas as alterações feitas na tela deverão ser gravadas por meio do botão **"Salvar"**.

**Observação:** Esta tela somente estará disponível no Sankhya OM, caso a empresa possua também os seguintes produtos:

- COMERCIAL /W
- PORTAL DE IMPORTAÇÃO DOC. ELETRÔNICOS/W
- MANIFESTO DO DESTINATÁRIO/W

**Importante:** No Jiva, esta tela só estará disponível se a empresa possuir os produtos:

- JIVA /W
- JIVA-MDe /W

Além disso, deve-se atentar para as informações passadas no link [MD-e - Manifestação do Destinatário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112353-MD-e-Manifesta%C3%A7%C3%A3o-do-Destinat%C3%A1rio).

![Imagem 2: Além disso, deve-se atentar para as informações passadas no link MD-e - Manifestação do Destinatário .](https://ajuda.sankhya.com.br/hc/article_attachments/4405789379607)

A marcação **"Baixar o XML ao dar ciência da operação"**, é utilizada para efetuar o download do XML da NF-e quando for realizado o evento de Ciência de Operação na tela [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML).

Através da marcação **"Realizar ciência automatizada"**, sempre que for feita uma consulta de notas, automaticamente também será realizada a ciência do documento. Ao habilitar essa marcação, a opção Baixar o XML ao dar ciência da operação será automaticamente assinalada.

No processo de consulta das notas fiscais emitidas para a empresa, as marcações Realizar ciência automatizada e Baixar o XML ao dar ciência da operação, caracterizam a automação existente no sistema que realiza a ciência da operação juntamente com o download do XML. Este procedimento, tem por objetivo agilizar o processo de conferência das notas de compra, sem a necessidade da empresa dar ciência e depois fazer o download do XML em momentos distintos; o download será realizado sempre ao final do processo de consulta da ciência automatizada.

Por meio do campo **"Versão de consulta"**, defina a versão de consulta do MD-e que deseja-se utilizar. Temos duas alternativas:

- Consulta de NF-e (NT 2012);
- Distribuição de DF-e (NT 2014).

**Atenção Implantadores:** Selecionando a opção Distribuição de DF-e (NT 2014), a Consulta é feita via webservice NFeDistribuicaoDFe, que visa disponibilizar os documentos para os autores interessados da NF-e, como emitentes, destinatários e transportadoras. Além da consulta dos documentos, a correspondente Baixa do XML da NF-e, será realizada por este webservice.

Informe no campo **"Qtd. dias para consulta de NSU faltantes"**, a quantidade de dias em que será possível proceder com a busca dos NSU's (Número Sequencial Único) faltantes, ou seja, números que não foram retornados pela SEFAZ até o momento que foram realizadas as buscas de dados sobre notas fiscais emitidas para a empresa.

**Observação:** Na realização da consulta dos documentos, a SEFAZ retorna uma resposta que possui o campo "maxNSU", que se refere ao último e maior NSU existente para o destinatário. Esta informação é gravada internamente pelo sistema, e será utilizada na próxima consulta de modo a evitar o consumo indevido do serviço de consulta de documentos.

Os campos **"Horário das consultas NF-e"** e **"Intervalo consulta NF-E em minutos"** são utilizados para que o sistema automaticamente busque as Notas Fiscais Eletrônicas emitidas para o destinatário em um intervalo de tempo determinado. Indique no campo Horário das consultas NF-e, o horário do dia em que as notas deverão ser buscadas. No campo Intervalo consulta em minutos, determine o intervalo em minutos para que o sistema busque as notas no dia. O valor do campo deverá ser entre 1 e 1439 (23 horas e 59 minutos), caso contrário será apresentada a seguinte mensagem:

**"O intervalo do download deve ser maior ou igual a 1 e menor ou igual a 1439."**

Não sendo inserida nenhuma informação sobre o intervalo de consulta em minutos, o sistema determinará o próximo horário de consulta de acordo com as informações presentes na última consulta realizada, utilizando o campo Horário das consultas por novas notas somando a este uma hora. Suponhamos, por exemplo, uma última consulta realizada em 07/11/2017 às 10:58hs; se for feita a tentativa de uma nova consulta, logo após esta última, será apresentada a seguinte mensagem:

**"Serviço de consulta não executado. Próxima execução permitida 07/11/2017 às 12:00hs."**

Os campos **"Horário de Download do XML"** e **"Intervalo de Download em minutos"**, possuem a mesma função dos campos Horário das consultas por novas notas e Intervalo consulta em minutos mencionados acima, porém ao invés do serviço de consulta, elas efetuam o serviço de download do XML automaticamente.

**Importante:** Vale ressaltar que, o download do XML somente ocorrerá caso a Nota Fiscal Eletrônica já possua o evento de Ciência de Operação registrado.

Os campos **"Horário das consultas CT-e"** e **"Intervalo consulta CT-E em minutos"** são utilizados para que o sistema automaticamente busque os Conhecimentos de Transporte Eletrônicos emitidos para o destinatário em um determinado intervalo de tempo. Informe no campo Horário das consultas CT-e o horário do dia em que ocorreram as buscas. No campo Intervalo consulta CT-e em minutos, determine o intervalo em minutos da busca no dia. O valor deste campo deverá ser entre 60 e 1439 (23 horas e 59 minutos), caso contrário será apresentada a seguinte mensagem:

**"O intervalo da consulta CT-e em minutos deve ser maior ou igual a 60 e menor ou igual a 1439."**

A marcação **"Gravar log de consultas"**, tem a finalidade que o sistema grave todos os serviços que o usuário executar manualmente ou, serviços executados automaticamente que estão relacionados com a manifestação do destinatário.

Quando a marcação for habilitada, todos os serviços feitos relacionados a manifestação do destinatário serão gravadas; quando desmarcada, somente serviços que retornarem rejeição serão gravados.

O campo **"Modelo de relatório Danfe"**, é utilizado para determinar qual modelo de impressão (relatório formatado) o sistema irá se basear para que o DANFE da Nota Fiscal importada seja visualizado.

Utilize o campo **"Modelo de relatório Dacte"**, para definir qual modelo de impressão (relatório formatado) o sistema irá se fundamentar para que o DACTE da Nota Fiscal importada seja visualizado.

O botão **"Consultar Documentos"** quando acionado, abrirá o pop-up denominado **"Selecione a empresa para consulta**". Ao informar a empresa desejada, será realizada a consulta junto a SEFAZ dos documentos fiscais emitidos pela mesma.

![Imagem 3: O botão "Consultar Documentos" quando acionado, abrirá o pop-up denominado " Selecione a empresa para consulta " . Ao…](https://ajuda.sankhya.com.br/hc/article_attachments/4405785945623)

**Observação:** No parâmetro **"Intervalo de consulta de notas MDe - INTCONSULTAMDE"**, informe o tempo (em milissegundos- 1000 (mil) milissegundos é equivalente a 1 (um) segundo.) que o sistema irá aguardar para consultar as notas MD-e junto a SEFAZ; é o intervalo de tempo respeitado pelo sistema para uma nova tentativa de obtenção de resposta (retorno das notas emitidas) junto a SEFAZ a respeito das notas MD-e emitidas por um mesmo CNPJ.

**Nota:** Ao ligar o parâmetro **"Imprimir processos DFE no log? - DFEMODODEBUG"**, as etapas do processo do DF-e serão gravadas no log do sistema.

---

**Seção Mensagens MD-e**

Na parte inferior da tela, temos a seção Mensagens MD-e que possibilita a verificação de todos os serviços realizados relacionados à manifestação do destinatário, conforme marcação do campo Gravar log de consultas citado anteriormente. Você pode visualizar a seção, em **"Modo grade"** ou **"Modo formulário"**.

![Imagem 4: Na parte inferior da tela, temos a seção Mensagens MD-e que possibilita a verificação de todos os serviços realizados…](https://ajuda.sankhya.com.br/hc/article_attachments/4405786697239)

É válido informar que o campo **"Motivo Resposta"**, também será alimentado com dados correspondentes às notas ou conhecimentos, no tocante à autorizações de documentos posteriores ou mesmo, resumo de eventos. Por exemplo, no caso de uma NF-e, se houver uma carta de correção, CT-e autorizado ou MDF-e autorizado, este campo irá registrar essa informação para o documento em questão.
