---
id: "44010711897751"
titulo: "[Routing] - Importação de clientes no roteirizador via arquivos - Layout Delimitado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010711897751--Routing-Importa%C3%A7%C3%A3o-de-clientes-no-roteirizador-via-arquivos-Layout-Delimitado"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T18:44:07Z"
rotulos: ["sync_hc", "lincros", "sync_hash_bececd437442", "lincros_13432334"]
---

# [Routing] - Importação de clientes no roteirizador via arquivos - Layout Delimitado

## Este artigo não está visível para os clientes

**Menu:** Cadastros > Layout de Importação

**Objetivo**: Como realizar a importação de clientes para o roteirizador via arquivos

## Considerações:

- É necessário ter os campos abaixo já cadastrados no Router para iniciar a importação de clientes para o roteirizador via arquivos:

- [Depósito](https://intercom.help/ajudalincros/pt-BR/articles/14443341-routing-cadastro-de-deposito)

Segue abaixo os procedimentos para realizar a importação de clientes no roteirizador via arquivos:

1. Primeiramente deve-se verificar o layout de importação padrão que foi configurado para o depósito do cliente;
2. Configurar de acordo com as necessidades do cliente na implantação do mesmo;

## Tipo de Layouts

- **Tipo de layout fixo:** Informe de que caráter até que carácter corresponde o cadastro. Exemplo: Cliente dígito 0 até dígito 6 corresponde ao código do cliente;
- **Tipo de layout delimitado**: Nesta opção, você pode escolher um separador para as informações enviadas no arquivo;
- **Banco de dados**: É configurado o acesso ao banco de dados do cliente e criado um script de select e response para envio e retorno de informações de clientes com o ERP do cliente;

No exemplo abaixo, temos o depósito da Teste Suporte, aqui utilizamos o tipo 'Delimitado'. Então, as informações do arquivo devem vir separadas por ponto e vírgula ';'

![Imagem 1: No exemplo abaixo, temos o depósito da Teste Suporte, aqui utilizamos o tipo 'Delimitado'. Então, as informações do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010692674839)

Abaixo os campos que foram determinados para este exemplo:

![Imagem 2: Abaixo os campos que foram determinados para este exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/44010712236055)

Seguinte a ordem: Posição '0' Código do Cliente - Posição '1' Nome do Cliente - Posição '2' Endereço - Posição '3' Bairro - Posição '4' Cidade - Posição '5' Estado.

Neste caso, o arquivo 'TXT' deveria vir no modelo: Código do Cliente;Nome do Cliente;Endereço do Cliente;Cidade;Estado; Ou quando informado o Bairro: Código do Cliente;Nome do Cliente;Endereço do Cliente;Bairro;Cidade;Estado;

## Como fazer a importação do arquivo

1. Acessar o menu: Importações > Cliente;
2. Clicar no botão 'Novo';
3. Selecione o depósito em questão;
4. No campo 'Layout' o próprio sistema irá preencher;
5. Selecione o arquivo em questão a ser importado;
6. Clique em 'Confirmar';

![Imagem 3: Clique em 'Confirmar';](https://ajuda.sankhya.com.br/hc/article_attachments/44010692926487)

Para conferir se o arquivo foi importado corretamente, clicar em 'Filtrar' e filtrar pelo depósito em questão;

## Status de Sucesso

![Imagem 4: Status de Sucesso](https://ajuda.sankhya.com.br/hc/article_attachments/44010670995223)

## Importado Parcialmente

![Imagem 5: Importado Parcialmente](https://ajuda.sankhya.com.br/hc/article_attachments/44010700478743)

## Não importado

![Imagem 6: Não importado](https://ajuda.sankhya.com.br/hc/article_attachments/44010680692759)

Ao clicar no ícone vermelho

![Imagem 7: Ao clicar no ícone vermelho](https://ajuda.sankhya.com.br/hc/article_attachments/44010700730263)

conseguimos verificar o que não foi importado e o respectivo motivo, conforme o exemplo abaixo:

![Imagem 8: conseguimos verificar o que não foi importado e o respectivo motivo, conforme o exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44010693413143)

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
