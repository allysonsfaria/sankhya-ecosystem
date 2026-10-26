---
id: "42427480771223"
titulo: "Como importar clientes ao Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427480771223-Como-importar-clientes-ao-Ploomes"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T18:04:36Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452147", "sync_hash_f6905c680ecc"]
---

# Como importar clientes ao Ploomes

A importação de clientes permite **criar e atualizar dados de forma massiva** a partir de uma planilha, evitando o cadastro manual cliente por cliente. Esse recurso é especialmente útil em cenários de **migração de dados de outras ferramentas para o Ploomes**.

Antes de realizar a importação, certifique-se de que sua planilha atende aos requisitos abaixo:

- O arquivo deve estar no formato **.xlsx (Excel)**;
- A planilha deve conter **apenas uma aba**;
- Não deve conter **fórmulas**;
- Evite **caracteres especiais** nos nomes das colunas;
- Garanta que os **campos obrigatórios estejam preenchidos**;
- Cada **linha** deve representar um cliente;
- Cada **coluna** deve representar um tipo de informação (ex.: nome, CPF/CNPJ, segmento, origem).

Se sua planilha definir um **responsável** para cada cliente, o nome deve estar **exatamente igual ao cadastrado no Ploomes**. Caso contrário, o cliente será importado **sem responsável**.

💡 Teste a importação com uma planilha reduzida antes de importar grandes volumes para entender se terá os preenchimentos esperados.

## Como importar

## Passo 1: Acesse a tela de Clientes

No menu lateral do Ploomes, clique em **Clientes**.

![Imagem 1: No menu lateral do Ploomes, clique em Clientes .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1370200916/0c5d86cb5d5a0e9325457b1029d4/image.png?expires=1786536000&signature=ad5f9e6062ed6549c0b44d98625829ba70bcbfb7a4a8bae72edffe4f2dd91ea4&req=dSMgFst%2BnYheX%2FMW3nq%2BgdoByfGnotgGo8f7%2FE20ndFOZeNH2dyNwkJqg%2BtZ%0AsR7Sq%2FyQRoNrKLhDxTSIHDAnGRg%3D%0A)

## Passo 2: Inicie a importação

Na tela de Clientes, clique em **Menu** e selecione **Importar clientes pelo Excel**.

![Imagem 2: Na tela de Clientes, clique em Menu e selecione Importar clientes pelo Excel .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1370205224/bb75a956b5f7e1b5473cbb8d8565/image.png?expires=1786536000&signature=2b5a81dac647c9b23799451cd7ed435f4159bccd0f35bf7707587456ea34900b&req=dSMgFst%2BmINdXfMW3nq%2BgTUKlSSOrRHbb9CmOvxBfTg9UIC%2BUd4YAcdNKtWe%0AGF8OlS%2FP%2BzBSNSyK0rlxdnzOBpk%3D%0A)

## Passo 3: Upload

Escolha o arquivo em seu computador e clique em **Avançar**.

[GIF animado: Imagem 3: Escolha o arquivo em seu computador e clique em Avançar .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1370213385/e86bbaa9e14751d4308053e1b1c1/NewGIF+%282%29.gif?expires=1786536000&signature=60a7f7b0f87b6d2209980c0c4f1916682108b4486ed51d5020e198d02e128dbd&req=dSMgFst%2FnoJXXPMW3nq%2BgRGnjaPoDh2kMFoqMz%2BANVP1kshGYrmRj0EJGIv3%0A81oMcRaSAHl94qKSXCP3HNHgb%2F4%3D%0A)

## Passo 4: Mapeamento

Nesta etapa, você deve informar ao Ploomes **a qual campo do sistema cada coluna da planilha corresponde**.

- Colunas com informações da **empresa** (ex.: nome da empresa, CNPJ) devem ser mapeadas como **Empresa**;
- Colunas com informações de **contato** (ex.: nome, e-mail, telefone) devem ser mapeadas como **Pessoa**.

Com esse mapeamento, o Ploomes criará corretamente as empresas e associará as pessoas aos respectivos registros.

**⚠️ Atenção**

- Caso a planilha tenha muitas colunas, será exibida uma barra de rolagem horizontal para facilitar a visualização;
- A opção “Detectar duplicado por este campo” evita a criação de registros duplicados. Normalmente, utiliza-se Nome da empresa ou CNPJ;
- Mesmo com os campos obrigatórios mapeados, linhas com células vazias nesses campos não serão importadas.

### Exemplo de mapeamento

Na imagem abaixo, as colunas A e B da planilha se referem ao contato, a coluna D é referente ao nome da empresa.

![Imagem 4: Na imagem abaixo, as colunas A e B da planilha se referem ao contato, a coluna D é referente ao nome da empresa.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1370217787/f1073e0ddab9a842743f12edef41/image.png?expires=1786536000&signature=378b6548bf3f49770c4a957a0d017120871ac35c8ee6ae0ce36b96fe5c55d4b1&req=dSMgFst%2FmoZXXvMW3nq%2BgU7Bv2pgUm6%2BLlHJuu0JQJ1%2F9G1p513iu2clPWSN%0AvqH%2BKx0p3GeVsis8Obd9dUdFU5s%3D%0A)

O mapeamento seria:

- Pessoa > Nome
- Pessoa > E-mail
- Cidade da empresa > Nome
- Empresa > Nome ("Detectar duplicado por este campo" marcado).

Demonstração em GIF:

[GIF animado: Imagem 5: Demonstração em GIF:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1370229267/04187ad5987fe9a145db83193c3a/NewGIF+%283%29.gif?expires=1786536000&signature=c9a85f3785b3b1a5942f03cb958579320bcd7ab47b6ff19c93ea23a0064ba5a7&req=dSMgFst8lINZXvMW3nq%2BgRNIRDJaYjeIQ%2B%2FOXL5Ha3OS5hVZh2XmE%2BJ%2FU7Sy%0Alu8iEU%2F0SoDUkDSGpOKh2vtM8I0%3D%0A)

Nesse exemplo, o sistema cria a empresa **“Nec Eleifend Non Inc.”**, localizada em **Maringá**, e vincula a ela a pessoa **Joseph Ribeiro**, com o e-mail **[phasellus.dapibus@yahoo.com.br](mailto:phasellus.dapibus@yahoo.com.br)**

## Passo 5: Resumo

Nesta tela, o sistema exibirá os registros com **erros ou inconsistências**, destacando quais não serão importados ou podem gerar problemas.

**Ações disponíveis nesta tela**

- **Confirmar**: prossegue com a importação;
- **Etapa anterior**: retorna ao mapeamento;
- **Cancelar importação**: cancela todo o processo para correção do arquivo, se necessário.

## Passo 6: Acompanhe a importação

Nesta etapa, é possível acompanhar o andamento do processo, com as seguintes informações:

- **Linhas processadas**: total de linhas processadas em relação ao arquivo;
- **Linhas processadas com sucesso**;
- **Linhas processadas com erro**;
- **Entidades criadas**;
- **Entidades atualizadas**.

A importação pode levar alguns minutos para iniciar, especialmente em **horários de pico**, devido ao limite de processos simultâneos.

![Imagem 6: A importação pode levar alguns minutos para iniciar, especialmente em horários de pico , devido ao limite de processos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1370234738/0c31c1b8e310f02c5f322ed0f27a/image.png?expires=1786536000&signature=70d7d9c14cb916ad17f92498e51b7f3be9d945fdc2da2274b6a02b296ebc8251&req=dSMgFst9mYZcUfMW3nq%2BgUdIX9NbNfkY8uC0NiKO5XhPmpYrj1kekIy2FHnT%0ADHfLQcS5G%2FEO2Bp%2BJy6X4LDtH9s%3D%0A)

**Ações disponíveis nesta tela**

- Minimizar
- Fechar
- Ver artigo de como importar
- Cancelar importação

Caso a tela de importação seja minimizada, você pode abrir novamente clicando no **ícone de importação** no menu superior.

Quando a importação for concluída, a barra de progresso ficará completa e será exibida a opção **“Clique aqui para baixar a planilha com os detalhes”**.

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 7: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1385555840/fb9d416a4a0af6aaca36fb26bec2/CRM.png?expires=1786536000&signature=b1a8f3a9c29e43c66a37dbefff5db5c77120ff5f12d6de9bd0a6706b5feb2961&req=dSMvE8x7mIlbWfMW3nq%2BgZmWGsmpDeMkKnkR9P3hu5dZq9gNl3QvFxGQTC2F%0AAumofAYr629D8%2Bbxnj6NRrFYazg%3D%0A)](https://universidade.ploomes.com/courses/trilha-adm-passo3-crm)

[![Imagem 8: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048769417/eec0a2fd90618e9fda80c00dce90/Teste+01.png?expires=1786536000&signature=f969cb5cd93cf4e1554686abbea90ec1c906385566499456a9dc845cefd4db90&req=diAjHs54lIVeXvMW3nq%2BgcCMbhk%2B9RBOuHJNtmDldv5NYmN7UxIBlsR3%2B4h4%0AcVR8oFd64BQuElgR5ZMxFM20p48%3D%0A)](https://universidade.ploomes.com/courses/boas-praticas-para-a-importacao-de-dados)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
