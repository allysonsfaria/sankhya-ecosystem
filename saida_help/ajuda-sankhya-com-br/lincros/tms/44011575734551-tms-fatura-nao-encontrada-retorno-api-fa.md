---
id: "44011575734551"
titulo: "[TMS] Fatura não encontrada - retorno API fatura/recuperarDados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011575734551--TMS-Fatura-n%C3%A3o-encontrada-retorno-API-fatura-recuperarDados"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T19:06:37Z"
rotulos: ["sync_hc", "lincros", "sync_hash_05ca59db6678", "lincros_13438113"]
---

# [TMS] Fatura não encontrada - retorno API fatura/recuperarDados

**Menu**: Financeiro > Faturas 
**Objetivo:**Auxiliar no entendimento do retorno "Fatura não encontrada" da API fatura/recuperarDados.

**Considerações**: A fatura deve estar importada dentro do TMS e sem erros de importação e com seus respectivos CT-es.

Após o aceite da fatura a mesma estará disponível para a integração, uma vez informado o OID da mesma e feito a chamada da API fatura/recuperarDados ela retorna a seguinte mensagem de erro:

![Imagem 1: Menu : Financeiro > Faturas Objetivo: Auxiliar no entendimento do retorno "Fatura não encontrada" da API…](https://ajuda.sankhya.com.br/hc/article_attachments/44011575938711)

Identificado o erro, devemos nos atendar a um campo na fatura, sendo o campo Unidade, podemos verificar isso acessando a fatura pelo caminho: Financeiro > Faturas:

![Imagem 2: Identificado o erro, devemos nos atendar a um campo na fatura, sendo o campo Unidade, podemos verificar isso acessando…](https://ajuda.sankhya.com.br/hc/article_attachments/44011569288727)

O CNPJ da unidade precisa estar vinculado ao usuário de perfil WebService que gerou o token da chamada da API, podemos validar isso acessando o caminho Sistema > Acesso > Usuário > Usuários da empresa e pesquisando pelo usuário, ao acessa-lo precisamos vincular a unidade a ele:

![Imagem 3: O CNPJ da unidade precisa estar vinculado ao usuário de perfil WebService que gerou o token da chamada da API, podemos…](https://ajuda.sankhya.com.br/hc/article_attachments/44011576465815)

As Unidades no campo "Disponíveis" não estão vinculadas ao usuário, e as dentro do campo "Selecionadas" estão, após fazer esse procedimento e salvar o usuário geramos um token novo e fazemos a chamada da API fatura/recuperarDados com o mesmo OID da fatura:

![Imagem 4: As Unidades no campo "Disponíveis" não estão vinculadas ao usuário, e as dentro do campo "Selecionadas" estão, após…](https://ajuda.sankhya.com.br/hc/article_attachments/44011558335895)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
