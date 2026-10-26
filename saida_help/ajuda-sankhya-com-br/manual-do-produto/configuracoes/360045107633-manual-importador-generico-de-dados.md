---
id: "360045107633"
titulo: "Manual Importador Genérico de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107633-Manual-Importador-Gen%C3%A9rico-de-Dados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:54:23Z"
rotulos: ["#criadoRoger", "Configuração", "Parceiro", "Cidades", "Importação", "Agilizando Migração de Dados com Importador Genérico", "Documentos Eletrônicos"]
---

# Manual Importador Genérico de Dados

Este executável tem por finalidade facilitar a **migração de dados de tabelas básicas do sistema**, eliminando o tempo utilizado pela indústria e agilizando o processo de migração de dados de clientes Sankhya/Jiva.

![Imagem 1: Este executável tem por finalidade facilitar a migração de dados de tabelas básicas do sistema , eliminando o tempo…](https://ajuda.sankhya.com.br/hc/article_attachments/360060982554/mceclip2.png)

Primeiro escolhe-se o "**Tipo do Arquivo Origem**" que pode ser uma "**Planilha**" ou um "**Arquivo Texto**". Sendo do tipo “Texto”, ficam habilitadas as opções "**Arquivo Posicionado (Txt)**" e "**Arquivo Delimitado (Cvs)**". Sendo que quando o usuário optar por ‘Arquivo Delimitado’, deve-se informar o "**Delimitador**".

Seleciona-se o caminho do "**Arquivo Origem**" e a "**Tabela de Destino**" que é a aquela que irá receber os dados.

Clicando em "**Carregar Arquivo**" será aberta outra tela com a grade mostrando as informações de cada coluna da tabela a ser importada.

![Imagem 2: Clicando em " Carregar Arquivo " será aberta outra tela com a grade mostrando as informações de cada coluna da tabela a…](https://ajuda.sankhya.com.br/hc/article_attachments/360061912133/mceclip3.png)

**Valor Fixo**: Permitirá a inserção direta daquele valor na tabela.

Exemplo: para o **campo DTCAD** colocar o valor fixo "  **12/12/2010**  ". Assim todos os registros virão com esta data.

![Imagem 3: Exemplo: para o campo DTCAD colocar o valor fixo " 12/12/2010 ". Assim todos os registros virão com esta data.](https://ajuda.sankhya.com.br/hc/article_attachments/360060982594/mceclip4.png)

**Fórmula**: Através desta coluna podem-se usar outros campos para se chegar ao valor que se deseja incluir, com base nos dados de cada registro.

Exemplo: Fazendo **importação de parceiros** (**TGFPAR**) colocar para o campo "**ATIVO**" a fórmula "  **IF(CODVEND=0,'N','S')**  ". Desta forma os parceiros que forem importados e não tiverem um  **código de vendedor**   informado **serão importados como inativos**.

![Imagem 4: Exemplo: Fazendo importação de parceiros ( TGFPAR ) colocar para o campo " ATIVO " a fórmula " IF(CODVEND=0,'N','S') ".…](https://ajuda.sankhya.com.br/hc/article_attachments/360061912153/mceclip5.png)

**De Para**: coluna para a transformação de dados do arquivo importado para informações diferentes que sejam aceitas pelo sistema.

Exemplo: Fazendo um “**De Para**” na importação de produtos no campo **Unidade (CODVOL)**

Pode-se configurar:

"**Origem**"               "**Destino**"

Quilograma             KG
Caixa                       CX
Unidade                  UN

![Imagem 5: Quilograma KG Caixa CX Unidade UN](https://ajuda.sankhya.com.br/hc/article_attachments/360061912173/mceclip6.png)

Desta forma onde no arquivo tiver "**Quilograma**" o sistema colocará na tabela "**KG**".

![Imagem 6: Desta forma onde no arquivo tiver " Quilograma " o sistema colocará na tabela " KG ".](https://ajuda.sankhya.com.br/hc/article_attachments/360060982614/mceclip7.png)

E existem opções para tratamento de valores não previstos. Por exemplo, se no arquivo vier o volume "**Dúzia**", é possível **bloquear a entrada** deste dado ou **mandar gravar** do jeito que vier no arquivo ou **prever uma conversão** em um valor geral válido.

O tipo de arquivo ‘**Planilha**’ apresenta a coluna "**Coluna Origem**". O usuário indicará neste campo qual    **coluna da planilha** será gravada em qual **campo da tabela**.

![Imagem 7: O tipo de arquivo ‘ Planilha ’ apresenta a coluna " Coluna Origem ". O usuário indicará neste campo qual coluna da…](https://ajuda.sankhya.com.br/hc/article_attachments/360061912193/mceclip8.png)

A ‘Planilha’  **não deve conter**   **fórmulas nos campos**. Então, pode-se copiar os dados de uma planilha que tem fórmula para outra, usando o **'colar especial',** colando **apenas valores** ou **copiar os dados para um TXT**, depois **voltar para a planilha** ou ainda **salvar a planilha** em formato '**.csv'**.

O tipo de arquivo ‘Texto’ na opção “**Arquivo Posicionado (Txt)**” tem os campos "**Posição Inicial**" e "**Comprimento**". O conteúdo destes espaços será gravado na tabela.

Exemplo: linha do arquivo contendo "**J123AF**", configurando a "**Posição Inicial**" como  **“4”**   e o "**Comprimento**" igual a  **“2”**  , será importado para o campo o valor "  **3A**  ". **(J12**  **3A**  **F)**

O tipo de arquivo ‘Texto’ na opção “**Arquivo Delimitado (Cvs)**” apresenta a coluna "**Posição**". O conteúdo desta "**Posição**" será gravado na tabela.

Exemplo: com delimitador "-"  e linha do arquivo contendo "**J-35-AF-G5**", ao informar "**Posição**" igual a “  **3**  ” será importador para o campo o valor "  **AF**  ". **(J-35-**  **AF**  **-G5)**

![Imagem 8: Exemplo: com delimitador "-" e linha do arquivo contendo " J-35-AF-G5 ", ao informar " Posição " igual a “ 3 ” será…](https://ajuda.sankhya.com.br/hc/article_attachments/360060982634/mceclip9.png)

Na importação o sistema irá olhar primeiro o "**Valor Fixo**", se não estiver preenchido olhará a "**Fórmula**", se também não estiver preenchido irá olhar o "**De Para**". Se nenhuma dessas opções estiver preenchida o importador irá usar o **valor de origem** que vem do **arquivo importado**.

![Imagem 9: Na importação o sistema irá olhar primeiro o " Valor Fixo ", se não estiver preenchido olhará a " Fórmula ", se também…](https://ajuda.sankhya.com.br/hc/article_attachments/360060982654/mceclip10.png)

Clicando em "**Gravar Configurações**" o importador salvará as configurações para esta tabela. Desta forma quando for fazer **uma nova importação,**   **desta mesma tabela**  , o sistema oferecerá a opção de carregar as configurações salvas para que não seja preciso configurar tudo novamente. Ou pode-se negar o carregamento das configurações salvas e fazer uma nova configuração.

![Imagem 10: Clicando em " Gravar Configurações " o importador salvará as configurações para esta tabela. Desta forma quando for…](https://ajuda.sankhya.com.br/hc/article_attachments/360061912213/mceclip11.png)

As configurações ficam gravadas em um arquivo "**PreConfig.ini**" na pasta onde se encontra o ‘**Importador Genérico’**. As configurações do "**De Para**" ficam salvas em um arquivo "  **DePara.ini**  ".

Caso ocorra algum erro na importação, o sistema oferece opção de abrir o arquivo de log para verificação do motivo do erro. Se o campo de marcação "**Fazer Log Detalhado?**" estiver marcado, o log será apresentado com mais informações para uma análise mais detalhada.

![Imagem 11: Caso ocorra algum erro na importação, o sistema oferece opção de abrir o arquivo de log para verificação do motivo do…](https://ajuda.sankhya.com.br/hc/article_attachments/360060982674/mceclip12.png)

**Observação:** o Importador genérico ainda não está preparado para **importar planilhas do excel** com extensão ".**xlsx**".

Para o ‘**Cadastro de Parceiros**’ (**TGFPAR**) existem particularidades referentes ao ‘**Endereço do Parceiro’**  que está sendo importado.

Na coluna **CODEND**, no arquivo que está sendo importado, deve ter uma coluna **contendo à ‘Rua’**, para que o sistema já reconheça pelo **nome da ‘Rua’** um ‘**Endereço**’ cadastrado e caso não reconheça **cadastrar um novo**.

**Exemplos aceitáveis de endereço:**
Av Afonso Pena, 1524
 R Constelação 123
 Pca Clarimundo Carneiro 58
 Av. Rondon Pacheco
 Rua Pericles Vieira Mota

**Observação:** assim o sistema irá **ignorar os números** e comparar **apenas o nome das ‘Ruas’,** reconhecendo os tipos como Rua, Avenida, Praça...

O ‘Número’ do endereço deve ser colocado direto no campo **NUEND** da tabela **TGFPAR**.

O nome do ‘**Bairro**’ deve ser colocado no **CODBAI** para que o sistema já reconheça a partir do nome importado um ‘**Bairro**’ **cadastrado**.

Para ‘**Cidades**’ o campo deve ser colocado no campo **CODCID** da tabela e na planilha deve vir a informação do **nome da cidade** e a **UF** a que pertence a **cidade**, separados por um  **#**  .

**Observação:** uberlandia   **=**    UBERLANDIA, mas Uberlandia   **<>**   Uberlândia.

**Exemplos válidos**:

- Uberlândia   **#**   MG
- UBERLÂNDIA   **#**   MG
- São Paulo   **#**   SP

Se no campo não constar a informação "  **#UF**  ", o sistema buscará a **‘Cidade’** com o  **‘UF’ igual a “0”**   e caso não encontre irá cadastrar.

O campo **CODCID** permite no **máximo 20 caracteres**, então, qualquer informação que ultrapasse essa quantidade será **ignorada** na importação.

SANKHYA Central Business Partners -
Copyright © 2011 SANKHYA Tecnologia em Sistemas Ltda. Todos os direitos reservados.
Proibida a reprodução parcial ou total por qualquer meio, seja este eletrônico, mecânico, de fotocópia, de gravação, ou outros, sem prévia autorização, por escrito, da SANKHYA Gestão de Negócios.

 Clique abaixo para baixar o Executável do Importador Genérico:
