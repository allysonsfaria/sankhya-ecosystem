---
id: "42426976031767"
titulo: "Editor de Arquivos SPEDs"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426976031767-Editor-de-Arquivos-SPEDs"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Manuais Kolossus"
atualizado_em: "2026-08-03T12:42:07Z"
rotulos: ["asis", "sync_hc", "asis_52921034341139", "sync_hash_87bae5c11bbd"]
---

# Editor de Arquivos SPEDs

**Editor de Arquivos Sped**

Através do módulo é possível realizar ações corretivas nos arquivos SPED antes do envio para o FISCO, com velocidade e segurança nos dados. Ele automaticamente identifica as hierarquias  do layout para que você possa editar o dado específico. Disponível para SPED Fiscal (EFD ICMS  IPI) e EFD Contribuições.

O QUE COMPÕE O MÓDULO?  

**TELA – HOME –** Informações sobre o módulo

**TELA – EDIÇÕES –** Essa função é composta por outras 3:

**Todas as Edições**, histórico de todas as solicitações de edições feita dentro do módulo, **Minhas  Edições**, aparecem somente as edições do usuário, **Edições Finalizadas**, aquelas que foram  salvas.

**Importante:** Apenas os usuários começam o processo de edição pode salvar as alterações no  arquivo, caso contrário a plataforma não irá permitir que o arquivo seja salvo. Clique em **Sped** **Fiscal** ou **EFD Contribuições** para iniciar a edição de um arquivo processado

Passo a passo  

● Selecione o arquivo e cique em “Editar”.

![Imagem 1: ● Selecione o arquivo e cique em “Editar”.](https://ajuda.sankhya.com.br/hc/article_attachments/42427017672343)

Após processamento do arquivo no aplicativo de Edição, clique no nome do arquivo:

![Imagem 2: Após processamento do arquivo no aplicativo de Edição, clique no nome do arquivo:](https://ajuda.sankhya.com.br/hc/article_attachments/42427022479127)

Área de Edição 

Ao deslizar o cursor pelos ícones, será possível visualizar as funções de cada um conforme abaixo:

![Imagem 3: Ao deslizar o cursor pelos ícones, será possível visualizar as funções de cada um conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/42427003299095)

● **Consultar:** Após selecionar as condições, realize a consulta para verificar quantas linhas se enquadram nos parâmetros especificados.

● **Pré-visualizar:** Após visualizar as Condições e Escolher as Ações, esse botão permite que  você visualize o resultado antes de salvar. A Pré-visualização é obrigatória, para aplicar filtro  salvo.

● **Salvar:** Após realizar a conferência do resultado, clique aqui para gravar e proceder as  edições solicitadas.

● **Baixar arquivo:** Você poderá baixar o arquivo após as edições.

● **Finalizar Edição:** Após concluir todas as edições e salvar, você encerrará o processo clicando  aqui.

● **Salvar Filtro / Mostrar Filtros:** as condições a ações criadas poderão ser salvas como filtros  para edições futuras. Para visualizar o que está salvo, ir para “Mostrar Filtros”.

● **Limpar Filtro:** Clique aqui para limpar o filtro.

Condições e Ações 

![Imagem 4: Condições e Ações](https://ajuda.sankhya.com.br/hc/article_attachments/42427003410583)

**Condições:** Selecione os Registros e Campos que você deseja alterar; 

**Ações:** Indique a Ação que você quer realizar.

É possível inserir várias Condições e Ações, basta clicar no "+" para adicionar. Entretanto, quando uma  ação depende do ajuste de uma anterior, efetue separadamente. Exemplo: Fazer cálculo da base em um  primeiro momento e num segundo momento fazer o cálculo do tributo, pois percentual do tributo vai  sobre a base e esta deve estar previamente correta.

Utilização de Operadores 

**IGUAL** Função que localizará, no campo indicado do Registro, a informação desejada exatamente igual à inserida no campo “Valor”.

**MAIOR** Função que localizará, no campo indicado do Registro, todos os resultados com valores  maiores que o dado inserido no campo “Valor”.

**MENOR** Função que localizará, no campo indicado do Registro, todos os resultados com valores  menores que o dado inserido no campo “Valor”.

**MAIOR IGUAL** Função que localizará, no campo indicado do Registro, todos os resultados com  valores maiores ou iguais ao dado inserido no campo “Valor”.

**MENOR IGUAL** Função que localizará, no campo indicado do Registro, todos os resultados com  valores menores ou iguais ao dado inserido no campo “Valor”.

**DIFERENTE** Função que localizará, no campo indicado do Registro, todas as informações diferentes do dado inserido no campo “Valor”.

**CONTÉM** Função que localizará, no campo indicado do Registro, todas as informações que contêm (total ou parcialmente) o dado ou o valor inserido no campo “Valor”.

**ESTÁ EM** Função que localizará, no campo indicado do Registro, todos os resultados compreendidos na relação dos dados inseridos no campo “Valor” separados por vírgulas. Exemplo: Valor1,Valor2,Valor4.

**NÃO ESTÁ EM** Função que localizará, no campo indicado do Registro, todos os resultados não compreendidos na relação dos dados inseridos no campo “Valor” separados por vírgulas, ou seja, todos os dados diferentes da lista. Exemplo: Valor1,Valor2,Valor4.

**ESTÁ VAZIO** Função que localizará, no campo indicado do Registro, todos os resultados sem informação preenchida, ou seja, retornará nos casos que o campo estiver vazio.

![Imagem 5: ESTÁ VAZIO Função que localizará, no campo indicado do Registro, todos os resultados sem informação preenchida, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/42427003509143)

Nota: Função que localizará, no campo indicado do Registro, todos os resultados do intervalo compreendido entre os dados inseridos no campo “Valor”. Exemplo: Valor1 **e** Valor7, pode ser elaborada com maio igual a 1 e menor igual a 7.

Atribuição de Valores 

No campo Valor das Ações, há a possibilidade de preenchimento de diversos critérios para alteração nos campos dos registros indicados:

**CARACTERES** - dados em texto ou caracteres especiais. Ex: (A a ç,$ &: º ª § ; - /\_ ‘@%) **NUMÉRICOS** - dados com números (inteiros ou decimais). Ex: (100 17,00 18,00 7,6000) **EXPRESSÕES** - expressões matemáticas:

**DIRETAS:** Expressões básicas. Ex: =(A+A), =(A-A), =(A\*A), =(A/A), =(((A+B)/(A\*B))- A); **INDIRETAS:** Expressões com campos do mesmo registro.

Ex: =VL\_BC\_ICMS\*(ALIQ\_ICMS/100).

**FUNÇÕES** - funções específicas entre registros:

**SOMAFILHO:** Função para cálculo de valores de um campo no registro pai.

Ex: Para atualizar o campo VL\_ICMS do registro C100, somando o campo VL\_ICMS dos registros  C170 correspondentes: =SOMAFILHO(C170;VL\_ICMS).
