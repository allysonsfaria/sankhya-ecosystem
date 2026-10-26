---
id: "42426865254423"
titulo: "Manual Editor de Arquivos SPEDs"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426865254423-Manual-Editor-de-Arquivos-SPEDs"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Manuais Kolossus"
atualizado_em: "2026-08-03T12:36:13Z"
rotulos: ["asis", "sync_hc", "asis_52941211622035", "sync_hash_b7e5600c48aa"]
---

# Manual Editor de Arquivos SPEDs

Sumário

[O que compõe o módulo?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426865254423-Manual-Editor-de-Arquivos-SPEDs#h1702slt5teshv68th2jkt1kqi1a5p0xg)

[Passo a passo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426865254423-Manual-Editor-de-Arquivos-SPEDs#h1733slt5tey32pc7v2o2rtd7q1svrpme)

[Área de Edição](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426865254423-Manual-Editor-de-Arquivos-SPEDs#h1809slt5tfccc78r73ai9jebv12h72jm)

[Condições e Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426865254423-Manual-Editor-de-Arquivos-SPEDs#h1830slt5tfk0h1l0su3915vvhpwvzec7k)

[Utilização de Operadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426865254423-Manual-Editor-de-Arquivos-SPEDs#h1846slt5tfry61uoiso53g6a5xn5ayf4)

[Atribuição de Valores](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426865254423-Manual-Editor-de-Arquivos-SPEDs#h1855slt5tfyauzuj9d714y7ckbtwg06q)

[Função Edit Express](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426865254423-Manual-Editor-de-Arquivos-SPEDs#h1862slt5tg8ucu05grv12fga2h1r77jm2)

Status de Processamento

EDITOR DE ARQUIVOS SPEDs 

Através do módulo é possível realizar ações corretivas nos arquivos SPED antes do envio para o FISCO, com velocidade e segurança nos dados. Ele automaticamente identifica as hierarquias do layout para que você possa editar o dado específico. Disponível para SPED Fiscal (EFD ICMS IPI) e EFD Contribuições. 

### O que compõe o módulo?

TELA – HOME – Informações sobre o módulo

TELA – EDIÇÕES – Essa função é composta por outras 3: 

Todas Edições, histórico de todas as solicitações de edições feita dentro do módulo, Minhas Edições, aparecem somente as edições do usuário, Edições Finalizadas, aquelas que foram salvas. 

TELA – EDIT EXPRESS – É composto por 2 outras funções: 

Home: Transforma arquivo TXT em Excel e Excel em arquivo TXT. Processos: Visualização das suas transformações. 

Importante: Apenas os usuários que começam o processo de edição podem salvar as alterações no arquivo, caso contrário a plataforma não irá permitir que o arquivo seja salvo. 

Clique em [Sped Fiscal](https://kolossus.asisprojetos.com.br/processos?produto=1) ou [EFD Contribuições](https://kolossus.asisprojetos.com.br/processos?produto=4) para iniciar a edição de um arquivo processado pelo Auditor, selecione o Protocolo: Marque para ver as opções através de um clique, e selecione a opção ![Imagem 1: Clique em Sped Fiscal ou EFD Contribuições para iniciar a edição de um arquivo processado pelo Auditor, selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/42426844051223) então será direcionado para a tela de edições de arquivos, e aparecerá o ícone quando ele estiver disponível para edição. 

## Passo a passo

- Selecione o arquivo e clique em “Editar”.

![Imagem 2: Selecione o arquivo e clique em “Editar”.](https://ajuda.sankhya.com.br/hc/article_attachments/42426859189271)

- Após processamento do arquivo no aplicativo de Edição, clique no nome do arquivo:

![Imagem 3: Após processamento do arquivo no aplicativo de Edição, clique no nome do arquivo:](https://ajuda.sankhya.com.br/hc/article_attachments/42426848352151)

## Área de Edição

Ao deslizar o cursor pelos ícones, será possível visualizar as funções de cada um conforme abaixo: 

![Imagem 4: Ao deslizar o cursor pelos ícones, será possível visualizar as funções de cada um conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/42426848462999)

- Consultar: Após selecionar as condições, realize a consulta para verificar quantas linhas se enquadram nos parâmetros especificados.

- Pré-visualizar: Após visualizar as Condições e Escolher as Ações, esse botão permite que você visualize o resultado antes de salvar. A Pré-visualização é obrigatória, para aplicar filtro salvo.
- Salvar: Após realizar a conferência do resultado, clique aqui para gravar e proceder as edições solicitadas.
- Baixar arquivo: Você poderá baixar o arquivo após as edições.
- Finalizar Edição: Após concluir todas as edições e salvar, você encerrará o processo clicando aqui.
- Salvar Filtro / Mostrar Filtros: as condições a ações criadas poderão ser salvas como filtros para edições futuras. Para visualizar o que está salvo, ir para “Mostrar Filtros”.
- AEQL: você poderá clicar aqui para alterar o método de criação de condições e ações para a linguagem SQL.
- Limpar Filtro: Clique aqui para limpar o filtro.

Passando o mouse em cima as figuras é possível identificar o que cada uma faz.

## Condições e Ações

![Imagem 5: Condições e Ações](https://ajuda.sankhya.com.br/hc/article_attachments/42426832875415)

Condições: Selecione os Registros e Campos que você deseja alterar;

Ações: Indique a Ação que você quer realizar.

É possível inserir várias Condições e Ações, basta clicar no "+" para adicionar. Entretanto, quando uma ação depende do ajuste de uma anterior, efetue separadamente. Exemplo: Fazer cálculo da base em um primeiro momento e num segundo momento fazer o cálculo do tributo, pois percentual do tributo vai sobre a base e esta deve estar previamente correta. 

## Utilização de Operadores

IGUAL Função que localizará, no campo indicado do Registro, a informação desejada exatamente igual à inserida no campo “Valor”.

MAIOR Função que localizará, no campo indicado do Registro, todos os resultados com valores maiores que o dado inserido no campo “Valor”.

MENOR Função que localizará, no campo indicado do Registro, todos os resultados com valores menores que o dado inserido no campo “Valor”.

MAIOR IGUAL Função que localizará, no campo indicado do Registro, todos os resultados com valores maiores ou iguais ao dado inserido no campo “Valor”.

MENOR IGUAL Função que localizará, no campo indicado do Registro, todos os resultados com valores menores ou iguais ao dado inserido no campo “Valor”.

DIFERENTE Função que localizará, no campo indicado do Registro, todas as informações diferentes do dado inserido no campo “Valor”.

CONTÉM Função que localizará, no campo indicado do Registro, todas as informações que contêm (total ou parcialmente) o dado ou o valor inserido no campo “Valor”.

ESTÁ EM Função que localizará, no campo indicado do Registro, todos os resultados compreendidos na relação dos dados inseridos no campo “Valor” separados por vírgulas. Exemplo: Valor1,Valor2,Valor4.

NÃO ESTÁ EM Função que localizará, no campo indicado do Registro, todos os resultados não compreendidos na relação dos dados inseridos no campo “Valor” separados por vírgulas, ou seja, todos os dados diferentes da lista. Exemplo: Valor1,Valor2,Valor4.

ESTÁ VAZIO Função que localizará, no campo indicado do Registro, todos os resultados sem informação preenchida, ou seja, retornará nos casos que o campo estiver vazio.

![Imagem 6: ESTÁ VAZIO Função que localizará, no campo indicado do Registro, todos os resultados sem informação preenchida, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/42426827740055)

Nota: Função que localizará, no campo indicado do Registro, todos os resultados do intervalo compreendido entre os dados inseridos no campo “Valor”. Exemplo: Valor1 e Valor7, pode ser elaborada com maio igual a 1 e menor igual a 7.

## Atribuição de Valores

No campo Valor das Ações, há a possibilidade de preenchimento de diversos critérios para alteração nos campos dos registros indicados:

CARACTERES - dados em texto ou caracteres especiais. Ex: (A a ç,$ &: º ª § ; - /\_ ‘@%)

NUMÉRICOS - dados com números (inteiros ou decimais). Ex: (100 17,00 18,00 7,6000)

EXPRESSÕES - expressões matemáticas:

DIRETAS: Expressões básicas. Ex: =(A+A), =(A-A), =(A\*A), =(A/A), =(((A+B)/(A\*B))-A);

INDIRETAS: Expressões com campos do mesmo registro.

Ex: =VL\_BC\_ICMS\*(ALIQ\_ICMS/100).

FUNÇÕES - funções específicas entre registros:

SOMAFILHO: Função para cálculo de valores de um campo no registro pai.

Ex: Para atualizar o campo VL\_ICMS do registro C100, somando o campo VL\_ICMS dos registros C170 correspondentes: =SOMAFILHO(C170;VL\_ICMS).

## Função Edit Express

Em home do Edit Express, selecione o arquivo que quer realizar a conversão, e defina os seguintes critérios:

![Imagem 7: Em home do Edit Express, selecione o arquivo que quer realizar a conversão, e defina os seguintes critérios:](https://ajuda.sankhya.com.br/hc/article_attachments/42426866131991)

![Imagem 8: Em home do Edit Express, selecione o arquivo que quer realizar a conversão, e defina os seguintes critérios:](https://ajuda.sankhya.com.br/hc/article_attachments/42426833141783)

Ao importar um arquivo txt, podemos selecionar se será convertido em uma única aba do excel (padrão), ou se será demonstrado por registros ou blocos. Na opção por registro cada um estará um em uma aba, e por blocos cada bloco estará em uma aba do arquivo xlsx.

Exemplo excel separado por registros:

![Imagem 9: Exemplo excel separado por registros:](https://ajuda.sankhya.com.br/hc/article_attachments/42426878296983)

Exemplo excel separado por blocos:

 ![Imagem 10: Exemplo excel separado por blocos:](https://ajuda.sankhya.com.br/hc/article_attachments/42426866467735)

Na separação por REGISTROS, é possível alterar dados e excluir linhas.

Na separação por BLOCOS, é possível alterar dados, incluir e excluir linhas.

 Linhas incluídas: para a contagem de campos da linha, caso seja preenchida com campos vazios, incluir na última campo a palavra “vazio” sem aspas para que a ferramenta consiga identificar a realizar a contagem de campos.

Exemplo:

Linha incluída no excel:

![Imagem 11: Linha incluída no excel:](https://ajuda.sankhya.com.br/hc/article_attachments/42426895578903)

Linha com a contagem correta no txt:

![Imagem 12: Linha com a contagem correta no txt:](https://ajuda.sankhya.com.br/hc/article_attachments/42426859949847)

Se não selecionar nenhuma das opções, o txt é convertido para o excel conforme o padrão já existente, em uma única aba.

Ao finalizar as correções necessárias, importar o excel novamente na ferramenta para converter em txt.

Importante: Essa nova funcionalidade está disponível dentro do Editor de Arquivos Sped para os clientes da base. Ou seja, NÃO está disponível ao realizar o donwload gratuito do edist express.

 Status de Processamento 

![Imagem 13: Status de Processamento](https://ajuda.sankhya.com.br/hc/article_attachments/42426833686295)
