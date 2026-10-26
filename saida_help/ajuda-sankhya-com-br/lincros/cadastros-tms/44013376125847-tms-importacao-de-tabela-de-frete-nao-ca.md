---
id: "44013376125847"
titulo: "[TMS] - Importação de tabela de frete não carregando o upload"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013376125847--TMS-Importa%C3%A7%C3%A3o-de-tabela-de-frete-n%C3%A3o-carregando-o-upload"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:55:49Z"
rotulos: ["sync_hc", "lincros", "lincros_13432623", "sync_hash_fe30088f0d52"]
---

# [TMS] - Importação de tabela de frete não carregando o upload

**Menu:** Cadastros gerais > Transportadoras > Negociações > Tabelas de frete

**Objetivo:** Entender o que precisa ser feito para que o sistema importe corretamente a planilha em Excel.

**Considerações:**

- Possuir uma tabela de frete para ser importada no sistema;

Abaixo segue os procedimentos:

Caso ao importar uma planilha em Excel para atualização e/ou criação de uma tabela de frete, é possível que o sistema comporte-se conforme imagem abaixo, no caso, não apresentando a mensagem informando que o "processo de importação iniciado com sucesso, por favor aguarde. Quando finalizado será enviado um e-mail com o resultado da importação".

A imagem abaixo ilustra o retorno incorreto durante a importação de uma tabela de frete. Veja que não há nenhuma mensagem de orientação para o usuário.

![Imagem 1: A imagem abaixo ilustra o retorno incorreto durante a importação de uma tabela de frete. Veja que não há nenhuma…](https://ajuda.sankhya.com.br/hc/article_attachments/44013371634967)

Quando a importação ocorrer com sucesso irá ser apresentado a seguinte mensagem: 'Processo de importação iniciado com sucesso, por favor aguarde. Quando finalizado será enviado um e-mail com o resultado da importação', conforme exemplo abaixo:

![Imagem 2: Quando a importação ocorrer com sucesso irá ser apresentado a seguinte mensagem: 'Processo de importação iniciado com…](https://ajuda.sankhya.com.br/hc/article_attachments/44013371749143)

Na primeira imagem acima, percebe-se que ao importar a planilha, o sistema não apresentou nenhuma mensagem para o usuário, mas há uma explicação: **o nome do arquivo sendo importado não pode conter o caractere especial "Porcentagem" (%)**. Caso tenha este caractere no nome do arquivo a ser importado, então o sistema não conseguirá realizar a importação. Na imagem abaixo, exemplo de um arquivo com nomenclatura incorreta:

![Imagem 3: Na primeira imagem acima, percebe-se que ao importar a planilha, o sistema não apresentou nenhuma mensagem para o…](https://ajuda.sankhya.com.br/hc/article_attachments/44013371874455)

Portanto, deve-se remover o caractere especial do nome do arquivo, e aí sim realizar a importação no sistema novamente.

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
