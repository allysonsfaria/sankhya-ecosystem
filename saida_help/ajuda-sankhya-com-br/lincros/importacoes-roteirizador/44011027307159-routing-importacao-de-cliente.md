---
id: "44011027307159"
titulo: "[Routing] - Importação de Cliente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011027307159--Routing-Importa%C3%A7%C3%A3o-de-Cliente"
trilha: "Lincros > Roteirizador > Importações - Roteirizador"
atualizado_em: "2026-10-05T18:53:03Z"
rotulos: ["sync_hc", "lincros", "lincros_13439860", "sync_hash_16153850a6aa"]
---

# [Routing] - Importação de Cliente

**Menu:** Importações > Cliente

**Objetivo**: Criar arquivo \*.TXT com as informações dos clientes para importação.

## Considerações:

- É necessário ter o layout de importação de clientes do tipo 'Delimitado' configurado no sistema;

## Exemplo de Layout do tipo delimitado

Na imagem abaixo, foi configurado o layout de importação de clientes do tipo 'Delimitado', ou seja, é necessário separar as informações através do ponto e vírgulas ';', conforme definido o valor no campo 'Separador';

![Imagem 1: Na imagem abaixo, foi configurado o layout de importação de clientes do tipo 'Delimitado', ou seja, é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/44011022122775)

Abaixo segue um exemplo em relação ao preenchimento dos campos:

![Imagem 2: Abaixo segue um exemplo em relação ao preenchimento dos campos:](https://ajuda.sankhya.com.br/hc/article_attachments/44011042808087)

Na imagem acima, vimos que foram atribuidos os valores: Código\_cliente;Nome;Endereço;;;Bairro;Cidade;Estado;

Exemplificando melhor, ficaria assim:

Posição 0 = Código Cliente

Posição 1 = Nome

Posição 2 = Endereço

Posição 3 = Bairro

Posição 4 = Cidade

Posição 5 = Estado

**Obs.:** A primeira posição sempre irá começar com '0';

## Inserindo as informações do cliente no arquivo '.txt'

Segue abaixo dois exemplos (2 clientes para importar), de como inserir as informações no arquivo .TXT de acordo com os parâmetros do layout em referência:

111;Lincros;Av. Martin Luther, 399; ; ;Victor Konder;Blumenau;SC;

112;Cliente\_2;Endereço\_2; ; ;Bairro\_2;Cidade\_2;UF;

**Obs**.: Como a posição 3 e 4 não foram definidas no layout (são valores nulos), basta deixar em branco essas posições entre ; (ponto e vírgula);

Com as informações dos clientes salvas no arquivo .TXT, basta importar no sistema, pelo menu: Importações > Cliente,  selecionar o Layout de Importação de Clientes (na qual foi configurado a importação via arquivo .TXT), escolher o arquivo TXT salvo no computador  e 'Confirmar'.

Vale lembrar que, somente as posições 0 (Código Cliente) e 1 (Nome) são obrigatórias, conforme o exemplo de layout de importação de clientes apresentados, porém, é necessário informar os separadores com ; para as demais posições que não serão preenchidas.

**Exemplo**: 2;Cliente\_2;Endereço\_2; ; ;Bairro\_2; ; ;

No exemplo acima, não foi informado as posições da Cidade, UF e CEP.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
