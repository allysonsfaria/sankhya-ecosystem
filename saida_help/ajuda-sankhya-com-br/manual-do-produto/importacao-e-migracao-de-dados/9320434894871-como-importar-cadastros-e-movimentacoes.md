---
id: "9320434894871"
titulo: "Como importar cadastros e movimentações com o Importador Folha?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9320434894871-Como-importar-cadastros-e-movimenta%C3%A7%C3%B5es-com-o-Importador-Folha"
trilha: "Manual do Produto > Pessoas+ > Implantação e Acessos do Pessoas+ > Importação e Migração de Dados"
atualizado_em: "2026-09-27T14:05:09Z"
rotulos: ["Configuração", "Funcionários", "Importação", "br.com.sankhya.rh.ImportadorFolha", "importador folha", "Cadastro", "Revisão correções confirmação", "Planilhas correções configurações", "Colunas títulos correspondências", "Ajuste colunas títulos modelo", "Correções confirmação importação", "Automação cadastros movimentações", "Pessoal+"]
---

# Como importar cadastros e movimentações com o Importador Folha?

```
 Módulo: Pessoal+ > Configurações
```

---

Por meio desta tela é possível realizar as importações de planilhas referente às diversas tabelas no Pessoal+. Dessa forma, é eliminada a necessidade de input manual de cadastros e movimentações,  podendo direcionar tempo para possíveis correções de inconsistências dos dados e configurações específicas para o cliente, bem como, a entrada dos dados que não é possível tratar via importação.

Antes de importar os dados, é preciso organizá-los em uma planilha, de forma que permita identificar as respectivas colunas nas tabelas do Sankhya Om.

Uma forma de se obter um modelo para preenchimento é por meio do [DBExplorer](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603894). Em uma consulta simples é possível obter a estrutura de várias tabelas, como, por exemplo, do cadastro de funcionários.

![Imagem 1: Uma forma de se obter um modelo para preenchimento é por meio do DBExplorer . Em uma consulta simples é possível obter…](https://ajuda.sankhya.com.br/hc/article_attachments/9332984701847)

Como nas diversas grades do sistema, é possível usar o botão ![Imagem 2: Como nas diversas grades do sistema, é possível usar o botão "Exportar para planilha" para exportar o resultado da…](https://ajuda.sankhya.com.br/hc/article_attachments/25609545123351) **"Exportar para planilha"** para exportar o resultado da consulta.

Logo após, ajuste a planilha para que a primeira linha contenha o nome das colunas e as demais linhas contenham os valores que serão importados. Outra possibilidade é gerar essa planilha a partir da sua solução atual, ajustando os títulos das colunas às suas correspondências em nosso banco, facilitando a identificação automática dos dados.

![Imagem 3: É importante garantir que as colunas da planilha de importação correspondam aos campos da tabela TFPMOV, pois, em caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16591139635351) É importante garantir que as colunas da planilha de importação correspondam aos campos da tabela TFPMOV, pois, em caso de erro na importação, será necessário excluir manualmente as movimentações e refazer o processo de importação.

---

Para realizar a importação de dados da tabela por meio de planilhas, acesse a tela Importador Folha e acione o botão **"Insira a planilha da tabela a ser importada aqui"**. Em seguida, localize no dispositivo o arquivo salvo em formato XLSX e selecione o card que contenha a tabela que deseja importar. No nosso exemplo, a tabela TFPFUN, que é a tabela de funcionários.

**Nota:** utilize a lupa disposta na parte superior da tela para localizar a tabela que deseja.

![Imagem 4: Nota: utilize a lupa disposta na parte superior da tela para localizar a tabela que deseja.](https://ajuda.sankhya.com.br/hc/article_attachments/9333410627095)

Após selecionar o card, clique nele e serão exibidos todos os dados contidos na planilha importada.

Você poderá importar dados de endereços na tabela TFPFUN (Funcionários), que exibirá a seção **"Como deseja importar endereços?"** contendo as seguintes opções:

- **Utilizar somente planilha:** esta opção não irá utilizar o serviço de Correios e importará apenas o que consta na planilha.
- **Buscar CEP nos Correios, priorizando planilha:** o sistema irá buscar os dados dos Correios para as linhas que contenham apenas o CEP informado.
- **Buscar CEP nos Correios, priorizando Correios:** esta opção utilizará os dados dos Correios para todas as linhas, independente se o restante do endereço foram informados ou não.

No canto direito da tela, tem-se a grade de **"Revisão (Planilha e Tabela Oficial)"** onde são apresentados todos os campos cuja relação entre a planilha e o banco de dados foi identificada automaticamente.

![Imagem 5: No canto direito da tela, tem-se a grade de "Revisão (Planilha e Tabela Oficial)" onde são apresentados todos os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/9348808997527)

**Importante:** os campos da planilha que não estão conforme a tabela oficial correspondente, serão apresentados na seção de grade **"Observe a coluna abaixo..."**, na qual poderá ignorar a coluna, acionando o **"X"**. Prossiga quando não mais houver inconsistências apontadas nessa área.

Caso identifique alguma relação incorreta, é possível excluir uma coluna da planilha utilizando o botão **"Remover item para nova associação"**.

![Imagem 6: Caso identifique alguma relação incorreta, é possível excluir uma coluna da planilha utilizando o botão "Remover item…](https://ajuda.sankhya.com.br/hc/article_attachments/9348932899479)

| ![Imagem 7: Caso identifique alguma relação incorreta, é possível excluir uma coluna da planilha utilizando o botão "Remover item…](https://ajuda.sankhya.com.br/hc/article_attachments/16591139635351) | O sistema identifica automaticamente as colunas que, na planilha, possuem o mesmo nome de campos existentes na tabela de destino em nosso banco de dados. |
| --- | --- |

Alguns cards que representam as colunas em nosso banco, são sinalizados como obrigatórios pelo ícone . Diante disso, deve haver uma correspondência na planilha para os mesmos. Caso esses campos não estejam preenchidos, será apresentada uma mensagem informando que o campo está nulo.

![Imagem 8: Alguns cards que representam as colunas em nosso banco, são sinalizados como obrigatórios pelo ícone . Diante disso,…](https://ajuda.sankhya.com.br/hc/article_attachments/9349060931479)

Finalizada a revisão, acione o botão **"Importar para Tabela"**, será aberto um pop-up para confirmar a importação, após clicar em **"SIM"** as informações serão carregadas na tabela selecionada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9320434894871-Como-importar-cadastros-e-movimenta%C3%A7%C3%B5es-com-o-Importador-Folha#top)
