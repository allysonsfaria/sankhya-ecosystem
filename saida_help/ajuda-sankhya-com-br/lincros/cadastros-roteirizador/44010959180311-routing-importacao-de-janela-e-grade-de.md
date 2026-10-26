---
id: "44010959180311"
titulo: "[Routing] - Importação de janela e grade de atendimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010959180311--Routing-Importa%C3%A7%C3%A3o-de-janela-e-grade-de-atendimento"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T18:50:53Z"
rotulos: ["sync_hc", "lincros", "lincros_13432320", "sync_hash_05452317b851"]
---

# [Routing] - Importação de janela e grade de atendimento

**Menu:** Cadastros > Janela de Atendimento e Grade de atendimento

**Objetivo**: Como realizar o cadastro da janela e grade de atendimento de um cliente no roteirizador;

## Considerações:

- O cadastro de janela de atendimento e grade de atendimento permite o roteirizador de estabelecer critérios para roteirizar um cliente automaticamente;
- Sequenciando sua entrega de acordo com a janela de atendimento cadastrada e roteirizando-o ou não de acordo com a sua grade de atendimento;
- É necessário ter os campos abaixo já cadastrados no Router para iniciar o cadastramento:

- [Depósito](https://intercom.help/ajudalincros/pt-BR/articles/14443341-routing-cadastro-de-deposito)

Abaixo segue um exemplo de como importar a janela de atendimento:

1. Acessar o menu: Cadastros > Clientes;
2. Localizar o cliente em questão;

![Imagem 1: Localizar o cliente em questão;](https://ajuda.sankhya.com.br/hc/article_attachments/44010931488663)

3. Clicar no ícone da 'Horário de Atendimento'

![Imagem 2: 3. Clicar no ícone da 'Horário de Atendimento'](https://ajuda.sankhya.com.br/hc/article_attachments/44010931639959)

;

4. Veja que este cliente não possui um horário de atendimento;

![Imagem 3: 4. Veja que este cliente não possui um horário de atendimento;](https://ajuda.sankhya.com.br/hc/article_attachments/44010931785751)

5. Para importar criar um arquivo '.txt' da seguinte forma:

![Imagem 4: 5. Para importar criar um arquivo '.txt' da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/44010935207447)

**Obs**.: Mais abaixo explicamos como realizar o preenchimento deste arquivo.

6. Acessar o menu: Importações > Janela de Atendimento;

7. Clicar na opção 'Novo';

8. Selecionar o depósito em questão e escolher o arquivo '.txt' criado no item '5';

![Imagem 5: 8. Selecionar o depósito em questão e escolher o arquivo '.txt' criado no item '5';](https://ajuda.sankhya.com.br/hc/article_attachments/44010935314839)

9. Clicar em 'Confirmar';

10. Após, verificar se realmente o arquivo foi importado com sucesso, conforme exemplo abaixo:

![Imagem 6: 10. Após, verificar se realmente o arquivo foi importado com sucesso, conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44010932232343)

11. Para confirmar se realmente o arquivo foi importado, o sistema vai apresentar 'Sucesso' e o ícone azul

![Imagem 7: 11. Para confirmar se realmente o arquivo foi importado, o sistema vai apresentar 'Sucesso' e o ícone azul](https://ajuda.sankhya.com.br/hc/article_attachments/44010944791319)

. Caso houver alguma divergência (arquivo não importado) no arquivo ele irá apresentar um ícone vermelho

![Imagem 8: . Caso houver alguma divergência (arquivo não importado) no arquivo ele irá apresentar um ícone vermelho](https://ajuda.sankhya.com.br/hc/article_attachments/44010960357399)

;

![Imagem 9: ;](https://ajuda.sankhya.com.br/hc/article_attachments/44010960456855)

12. Para verificar qual foi o motivo de não ter importado, basta clicar sob o ícone em vermelho, onde o sistema irá abrir uma nova janela apresentando o que de fato ocorreu, conforme exemplo abaixo:

![Imagem 10: 12. Para verificar qual foi o motivo de não ter importado, basta clicar sob o ícone em vermelho, onde o sistema irá…](https://ajuda.sankhya.com.br/hc/article_attachments/44010923621911)

13. Com o arquivo importado com sucesso, verificar no cadastro do cliente em menu: Cadastros > Clientes se a janela de atendimento foi realmente preenchida de acordo com o '.txt' importado;

![Imagem 11: 13. Com o arquivo importado com sucesso, verificar no cadastro do cliente em menu: Cadastros > Clientes se a janela de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010915042839)

## Como montar o arquivo '.txt':

1. Preencher o código do cliente, neste exemplo '321321456';
2. Informar o horário de inicio '08:00';
3. Informar o horário final '18:00';
4. Seguido por um 'X' nos dias da semana que terá atendimento para este cliente. Iniciando na Segunda-Feira. Nesse exemplo, marcamos apenas a segunda-feira e a quinta-feira;
5. Mas digamos que este cliente não atende no intervalo do almoço e que atenda nos sábados também. O arquivo deverá ser importado conforme o exemplo abaixo:

![Imagem 12: Mas digamos que este cliente não atende no intervalo do almoço e que atenda nos sábados também. O arquivo deverá ser…](https://ajuda.sankhya.com.br/hc/article_attachments/44010960832151)

6. Lembrando que o separador sempre vai ser o ponto e virgula ';'

7. Após é necessário importar esta 'Grade de Atendimento' em menu: Importações > Grade de Atendimento;

8. Clicar na opção 'Novo';

9. Selecionar o depósito em questão e escolher o arquivo '.txt' criado acima;

![Imagem 13: 9. Selecionar o depósito em questão e escolher o arquivo '.txt' criado acima;](https://ajuda.sankhya.com.br/hc/article_attachments/44010936173079)

10. Clicar em 'Confirmar';

11. Verificar se realmente foi importado com sucesso, conforme exemplo abaixo:

![Imagem 14: 11. Verificar se realmente foi importado com sucesso, conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44010915295383)

12. Para confirmar se realmente o arquivo foi importado, o sistema vai apresentar 'Sucesso' e o ícone azul

![Imagem 15: 12. Para confirmar se realmente o arquivo foi importado, o sistema vai apresentar 'Sucesso' e o ícone azul](https://ajuda.sankhya.com.br/hc/article_attachments/44010974525847)

. Caso houver alguma divergência (arquivo não importado) no arquivo ele irá apresentar um ícone vermelho

![Imagem 16: . Caso houver alguma divergência (arquivo não importado) no arquivo ele irá apresentar um ícone vermelho](https://ajuda.sankhya.com.br/hc/article_attachments/44010936529815)

;

13. Com o arquivo importado com sucesso, verificar no cadastro do cliente em menu: Cadastros > Clientes se a grade de atendimento foi realmente preenchida de acordo com o '.txt' importado;

![Imagem 17: 13. Com o arquivo importado com sucesso, verificar no cadastro do cliente em menu: Cadastros > Clientes se a grade de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010915625495)

14. Caso tenha mais de um cliente, colocar nas linhas uma abaixo da outra no arquivo '.txt';

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
