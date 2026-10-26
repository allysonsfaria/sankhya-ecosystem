---
id: "44010732289431"
titulo: "[Routing] - Importações de tempo de espera"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010732289431--Routing-Importa%C3%A7%C3%B5es-de-tempo-de-espera"
trilha: "Lincros > Roteirizador > Importações - Roteirizador"
atualizado_em: "2026-10-05T18:44:41Z"
rotulos: ["sync_hc", "lincros", "lincros_13432989", "sync_hash_fe05cdd9d750"]
---

# [Routing] - Importações de tempo de espera

**Menu**: Importações > Tempo de Espera

**Objetivo**: Realizar o cadastro de tempo de espera do atendimento de um cliente no roteirizador.

## Considerações:

- O cadastro de tempo de espera permite que o roteirizador calcule o tempo que o motorista ficará no cliente;
- Auxilia na criação das rotas do cliente de acordo com o horário de jornada do motorista e os tempos de atendimentos em clientes;
- Necessário já ter o layout de importação configurado em: Cadastros > Layout de Importação;
- É necessário ter os campos abaixo já cadastrados no Router:

- [Depósito](https://intercom.help/ajudalincros/pt-BR/articles/14443341-routing-cadastro-de-deposito)

Para o cadastro de importações de tempo de espera é necessário informar os seguintes campos:

1. **Depósito**: Para o cadastro de um produto é necessário vincular ele à um depósito;
2. **Layouts**: Selecionar a opção 'Importação Padrão de Tempo de Espera de Clientes';
3. **Arquivo**: Selecionar o arquivo para iniciar a importação. Lembrando que o tamanho limite do arquivo é 1mb;

## Exemplo da Tela de Importações de Tempo de Espera

![Imagem 1: Exemplo da Tela de Importações de Tempo de Espera](https://ajuda.sankhya.com.br/hc/article_attachments/44010732443415)

**Obs**.: Os campos que aparecem em vermelho são de preenchimento obrigatório.

Abaixo segue um passo a passo de como importar o tempo de espera para o roteirizador:

Cliente 12345678

![Imagem 2: Cliente 12345678](https://ajuda.sankhya.com.br/hc/article_attachments/44010732603799)

1. Digamos que este cliente '12345678' tenha um tempo de espera para ser atendido de 1 hora e 30 minutos.
2. Para facilitar você pode utilizar o conversor de horas para segundos. Na coluna 'A' informar o código do cliente, na coluna 'B' informar a quantidade de horas e na coluna 'E' informar a quantidade de minutos, conforme exemplo abaixo:

   ![Imagem 3: Para facilitar você pode utilizar o conversor de horas para segundos. Na coluna 'A' informar o código do cliente, na…](https://ajuda.sankhya.com.br/hc/article_attachments/44010703699223)
3. Utilizando planilha de conversor, a coluna 'H' será preenchida com a quantidade de segundos que possui 1 hora e 30 minutos.

   ![Imagem 4: Utilizando planilha de conversor, a coluna 'H' será preenchida com a quantidade de segundos que possui 1 hora e 30…](https://ajuda.sankhya.com.br/hc/article_attachments/44010703845399)
4. Para realizar a importação, gerar um arquivo 'TXT' somente com a informação da coluna 'A' e coluna 'J', separados por ponto e vírgula, conforme abaixo:

   ![Imagem 5: Para realizar a importação, gerar um arquivo 'TXT' somente com a informação da coluna 'A' e coluna 'J', separados por…](https://ajuda.sankhya.com.br/hc/article_attachments/44010688405399)
5. Acessar o menu: Importações > Tempo de Espera;
6. Clicar na opção 'Novo';
7. Preencher as informações abaixo e selecionar o arquivo 'TXT' que foi gerado com os clientes e tempo de espera em segundos:

   ![Imagem 6: Preencher as informações abaixo e selecionar o arquivo 'TXT' que foi gerado com os clientes e tempo de espera em…](https://ajuda.sankhya.com.br/hc/article_attachments/44010725217815)
8. Após, clicar em 'Confirmar';
9. Ao término da importação, o sistema irá apresentar se a importação foi realizada com sucesso ou com erros, conforme exemplo abaixo:

   ![Imagem 7: Ao término da importação, o sistema irá apresentar se a importação foi realizada com sucesso ou com erros, conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/44010717239703)
10. Após a importação, verificar no cadastro do cliente que o tempo de espera foi alterado para 1 hora e 30 minutos, conforme abaixo:

    ![Imagem 8: Após a importação, verificar no cadastro do cliente que o tempo de espera foi alterado para 1 hora e 30 minutos,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010704394519)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
