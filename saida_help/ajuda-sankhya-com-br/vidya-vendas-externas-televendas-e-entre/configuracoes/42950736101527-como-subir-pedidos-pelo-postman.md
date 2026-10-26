---
id: "42950736101527"
titulo: "Como subir pedidos pelo Postman"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950736101527-Como-subir-pedidos-pelo-Postman"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T17:02:52Z"
rotulos: ["sync_hc", "vidya", "vidya_600089", "sync_hash_f8da0b80c338"]
---

# Como subir pedidos pelo Postman

## Visão geral

Este artigo mostra como enviar (subir) um pedido manualmente utilizando o Postman, através da requisição sendOrderOffline da coleção "BFF Implantação". Esse processo é útil em situações de suporte, testes ou reprocessamento de pedidos que precisam ser cadastrados diretamente na API, sem passar pela tela padrão do sistema.

## Pré-requisitos

- Ter o Postman instalado e acesso à coleção "BFF Implantação".
- Possuir usuário e senha válidos (autenticação Basic Auth) para o ambiente de destino.
- Ter em mãos o corpo (body) JSON do pedido que será enviado, com os dados do parceiro, produtos e demais campos exigidos pela operação.

## Passo a passo

**Passo 1.Abra a requisição sendOrderOffline**

Na coleção "BFF Implantação", localize a pasta com as requisições e selecione (ou duplique) a requisição sendOrderOffline. Se for criar uma nova a partir de uma existente, clique nos três pontinhos (...) ao lado do nome da requisição no menu lateral para editá-la.
![Imagem 1: Na coleção "BFF Implantação", localize a pasta com as requisições e selecione (ou duplique) a requisição…](https://ajuda.sankhya.com.br/hc/article_attachments/42957594525207)

**Passo 2.Preencha a URL da requisição**

No campo de URL, informe o endereço completo do ambiente de destino seguido do caminho do serviço, por exemplo:

http://<endereco-do-ambiente>:1500/ppid/sendOrderOffline/

Você pode digitar a URL manualmente ou selecioná-la a partir do histórico de requisições do Postman, como mostrado abaixo.

![Imagem 2: Você pode digitar a URL manualmente ou selecioná-la a partir do histórico de requisições do Postman, como mostrado…](https://ajuda.sankhya.com.br/hc/article_attachments/42957564673559)

Histórico de URLs sugerido pelo Postman ao clicar no campo de endereço.

![Imagem 3: Histórico de URLs sugerido pelo Postman ao clicar no campo de endereço.](https://ajuda.sankhya.com.br/hc/article_attachments/42957625533975)

URL completa preenchida no campo de endereço.

**Passo 3.Cole o corpo (body) do pedido em formato JSON**

Clique na aba Body, mantenha a opção raw selecionada com o formato JSON e cole o conteúdo do pedido que deseja enviar (dados do parceiro, itens, quantidades, valores, condições de pagamento etc.). Esse conteúdo normalmente é copiado de uma fonte já formatada (planilha, sistema de origem ou histórico da área de transferência).

![Imagem 4: Clique na aba Body, mantenha a opção raw selecionada com o formato JSON e cole o conteúdo do pedido que deseja enviar…](https://ajuda.sankhya.com.br/hc/article_attachments/42957582297879)

Corpo da requisição (JSON) colado na aba Body, com os dados do pedido.

**Passo 4.Configure o método HTTP como POST**

Por padrão, ao duplicar ou reabrir uma requisição, o método pode aparecer como GET. Clique no seletor de método (à esquerda do campo de URL) e selecione POST, já que o envio de um novo pedido exige esse método.

![Imagem 5: Por padrão, ao duplicar ou reabrir uma requisição, o método pode aparecer como GET. Clique no seletor de método (à…](https://ajuda.sankhya.com.br/hc/article_attachments/42957582974103)

Lista de métodos HTTP disponíveis no Postman.

| **Atenção**  Se você clicar em Send com o método ainda em GET, a API retornará o erro 405 - Method Not Allowed, como no exemplo abaixo. Basta alterar o método para POST e enviar novamente. |
| --- |

![Imagem 6: Se você clicar em Send com o método ainda em GET, a API retornará o erro 405 - Method Not Allowed, como no exemplo…](https://ajuda.sankhya.com.br/hc/article_attachments/42957650754199)

Erro 405 (Method Not Allowed) retornado quando a requisição é enviada com o método GET.

![Imagem 7: Erro 405 (Method Not Allowed) retornado quando a requisição é enviada com o método GET.](https://ajuda.sankhya.com.br/hc/article_attachments/42957644911127)

Método corrigido para POST.

**Passo 5.Configure a autenticação (Basic Auth)**

Após corrigir o método, ao reenviar a requisição você poderá receber a mensagem "Usuário/Senha inválido", indicando que a autenticação ainda não foi configurada corretamente para essa requisição.

![Imagem 8: Após corrigir o método, ao reenviar a requisição você poderá receber a mensagem "Usuário/Senha inválido", indicando que…](https://ajuda.sankhya.com.br/hc/article_attachments/42957645379223)

Retorno 200 com erro de autenticação: "Usuário/Senha inválido".

Para resolver, clique na aba Authorization. Em Auth Type, selecione Basic Auth e informe o Username e a Password do usuário autorizado a enviar pedidos nesse ambiente.

![Imagem 9: Para resolver, clique na aba Authorization. Em Auth Type, selecione Basic Auth e informe o Username e a Password do…](https://ajuda.sankhya.com.br/hc/article_attachments/42957645805975)

Aba Authorization com o tipo Basic Auth selecionado.

![Imagem 10: Aba Authorization com o tipo Basic Auth selecionado.](https://ajuda.sankhya.com.br/hc/article_attachments/42957646172311)

Usuário e senha preenchidos para autenticação.

**Passo 6.Envie a requisição**

Com a URL, o método POST, o corpo do pedido e a autenticação configurados, clique em Send. Se tudo estiver correto, a API retornará o status 200 OK com uma mensagem de sucesso, como no exemplo abaixo:

![Imagem 11: Com a URL, o método POST, o corpo do pedido e a autenticação configurados, clique em Send. Se tudo estiver correto, a…](https://ajuda.sankhya.com.br/hc/article_attachments/42957653010071)

Exemplo de resposta de sucesso: "Registro cadastrado com sucesso", com o número do pedido (NUNOTA) gerado.

## Possíveis erros e soluções

| **Erro** | **O que fazer** |
| --- | --- |
| **405 – Method Not Allowed** | O método da requisição está como GET. Altere para POST no seletor ao lado da URL e envie novamente. |
| **"Usuário/Senha inválido"** | As credenciais de autenticação não foram informadas ou estão incorretas. Vá até a aba Authorization, selecione Basic Auth e confira usuário e senha. |
| **Pedido duplicado** | Verifique o campo hasDuplicatedOrder no retorno da API. Se vier true, o pedido provavelmente já foi cadastrado anteriormente — confirme antes de reenviar. |

## Resumo rápido

- Abra a requisição sendOrderOffline no Postman.
- Preencha a URL do ambiente + /ppid/sendOrderOffline/.
- Cole o JSON do pedido na aba Body (raw / JSON).
- Selecione o método POST.
- Configure a Basic Auth com usuário e senha válidos na aba Authorization.
- Clique em Send e confira a mensagem "Registro cadastrado com sucesso".
