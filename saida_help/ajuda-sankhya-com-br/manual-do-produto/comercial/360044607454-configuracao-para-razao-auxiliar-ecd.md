---
id: "360044607454"
titulo: "Configuração para Razão Auxiliar - ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607454-Configura%C3%A7%C3%A3o-para-Raz%C3%A3o-Auxiliar-ECD"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:25:29Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "ECD", "Fiscal", "Auxiliar", "Razão", "br.com.sankhya.contab.configuracaorazaoauxiliarecd", "Configuração para Razão Auxiliar - ECD manual", "Configuração da Razão Auxiliar na ECD", "Comercial"]
---

# Configuração para Razão Auxiliar - ECD

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311890912279) Módulo: Comercial > Rotinas
```

---

A tela Configuração para Razão Auxiliar - ECD tem como função possibilitar a configuração dos campos do relatório Razão Auxiliar, representado pelos registros: I500, I510, I550 e I555; estes são utilizados exclusivamente para escriturações do tipo **"Z"**.

![Imagem 2: A tela Configuração para Razão Auxiliar - ECD tem como função possibilitar a configuração dos campos do relatório Razão…](https://ajuda.sankhya.com.br/hc/article_attachments/22212535892119)

Informa-se inicialmente o **"Cód. Razão Auxiliar"**; o preenchimento deste campo pode ser feito de forma manual ou automática; esta definição é feita por meio do botão ![Imagem 3: Informa-se inicialmente o "Cód. Razão Auxiliar" ; o preenchimento deste campo pode ser feito de forma manual ou…](https://ajuda.sankhya.com.br/hc/article_attachments/360061935773) **"Configuração da Tela"**.

Determina-se, obrigatoriamente, o **"Tamanho da Fonte"** a ser utilizado na geração do arquivo ECD com relação ao livro Razão Auxiliar.

No campo **"Natureza do Livro"** informa-se o nome da Natureza do livro associado; sua finalidade, é a que se destina o instrumento. Esta é uma informação utilizada para preencher o 3º campo do registro I012.

Informa-se no campo **"Lista de Campos p/ Ordenação"**, os campos que deseja-se que sejam ordenados na instrução a ser salva no espaço SQL. Estes campos devem ser separados por **","** (vírgula) e obrigatoriamente devem estar salvos na aba **"Detalhes Configuração para Razão Auxiliar ECD"**. Caso não esteja, ao tentar gerar o arquivo do ECD uma mensagem informando sobre tal fato será apresentada.

O espaço **"SQL"** está destinado à construção da query a ser empregada na Geração do Arquivo ECD.

O botão ![Imagem 4: O botão "Validar SQL" irá ratificar se a instrução SQL informada está sendo executada corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/360061935793) **"Validar SQL"** irá ratificar se a instrução SQL informada está sendo executada corretamente.

**Observação:** não se pode informar uma cláusula ORDER BY. Os campos que deverão ser ordenados devem ser informados no campo **"Lista de Campos p/ Ordenação"**; todas essas validações serão feitas na Geração do Arquivo ECD, na parte referente à geração do registro I500 e seus filhos, I510, I550 e I555. O resultado obtido com a query será utilizado para gerar tais registros.

### Aba Detalhes Configuração para Razão Auxiliar ECD

Nesta aba, determinam-se as especificações dos campos que serão utilizados na Lista de Campos p/ Ordenação. Deve-se preencher os seguintes dados:

No campo **"Sequência"** defina qual será a sequência do campo perante os demais.

Informa-se no campo **"Nome do Campo"** a nomenclatura que o campo irá possuir; aqui não se pode ter espaços em branco ou caracteres especiais.

Determina-se no campo **"Descrição do Campo"** qual é a denominação do campo em questão, com base na informação inserida no campo anterior.

No campo **"Tamanho do Campo"** qual o tamanho do campo que está sendo cadastrado.

Define-se também a **"Largura do Campo"** em questão.

No campo **"Tipo do Campo"** determina-se aqui a categoria do campo, ou seja, se será do tipo **"Carácter"** ou **"Numérico"**.

Caso o campo anterior tenha sido definido como Numérico, informa-se no campo **"Qtd. Casas Decimais"** a quantidade de casas decimais que o campo irá aceitar.

Define-se no campo **"Totalização"** se o campo irá atuar como totalizador; têm-se as seguintes alternativas:

- **Totalizar:** pode-se utilizar esta opção apenas se o campo for do tipo Numérico;
- **Zerar na Totalização:** esta opção também poderá ser empregada apenas se o campo for do tipo Numérico;
- **Texto Fixo:** por esta opção define-se que o campo possuirá um texto fixo.

Caso o campo Totalização tenha sido definido como Texto Fixo, este deverá ser informado no campo **"Texto Fixo"**.

Os campos que estiverem com a marcação **"Participa Quebra?"** efetuada serão utilizados na cláusula ORDER BY da instrução SQL cadastrada no respectivo espaço. O sistema irá formular essa cláusula automaticamente para geração do registro I550 do ECD.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607454-Configura%C3%A7%C3%A3o-para-Raz%C3%A3o-Auxiliar-ECD#top)
