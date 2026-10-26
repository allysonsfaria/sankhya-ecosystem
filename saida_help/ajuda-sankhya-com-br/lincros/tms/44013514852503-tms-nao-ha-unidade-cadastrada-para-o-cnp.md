---
id: "44013514852503"
titulo: "[TMS] Não há unidade cadastrada para o CNPJ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013514852503--TMS-N%C3%A3o-h%C3%A1-unidade-cadastrada-para-o-CNPJ"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T20:00:01Z"
rotulos: ["sync_hc", "lincros", "lincros_13432081", "sync_hash_23b4ca0a60b3"]
---

# [TMS] Não há unidade cadastrada para o CNPJ

**Menu**: Expedição > Coletas > Ordem de coleta

**Objetivo:** Ajudar a identificar o erro 'Não há unidade cadastrada para o CNPJ.' ao criar uma ordem de coleta pela API ordemcoleta/gravarColeta
— Toda vez que uma ordem de coleta for criado utilizando a API e caso no corpo do JSON o CNPJ no campo cnpjUnidade estiver com um CNPJ cujo cadastro ainda não foi realizado a API irá retornar o erro abaixo:

![Imagem 1: Menu : Expedição > Coletas > Ordem de coleta Objetivo: Ajudar a identificar o erro 'Não há unidade cadastrada para o…](https://ajuda.sankhya.com.br/hc/article_attachments/44013528228631)

— Mesmo que o CNPJ da unidade esteja cadastrado e o erro na API continuar, é necessário validar o CNPJ informado no campo cnpjUnidade, uma vez que, neste campo é esperado um CNPJ com 14 dígitos. Caso essa unidade for criada utilizando a API /criarUnidade é preciso se atentar se não foi utilizado um CNPJ com mais de 14 dígitos.

Exemplo de chamada da API onde existe um CNPJ com 15 dígitos e API mesmo assim retornou sucesso: 

![Imagem 2: — Mesmo que o CNPJ da unidade esteja cadastrado e o erro na API continuar, é necessário validar o CNPJ informado no…](https://ajuda.sankhya.com.br/hc/article_attachments/44013490794263)

Com isso, é necessário validar se o mesmo CNPJ utilizado na API /criarUnidade não é o mesmo utilizado na API ordemcoleta/gravarColeta, caso for, basta retirar o dígito errado e chamar a API novamente.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
