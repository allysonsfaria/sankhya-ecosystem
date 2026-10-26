---
id: "42427451068695"
titulo: "Importação de clientes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427451068695-Importa%C3%A7%C3%A3o-de-clientes"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T17:58:19Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5780574", "sync_hash_8d2fabc024bb"]
---

# Importação de clientes

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=z0r-e5etCUA)

Antes de descrever cada passo do processo, é importante esclarecer que **Importação de dados** significa, neste contexto, migrar seus clientes para o Ploomes de forma massiva a partir de uma planilha em Excel, sem a necessidade de cadastrar cliente por cliente de forma manual.

A sua planilha deverá conter apenas **uma aba**, não poderá ter **caracteres especiais** e nem **fórmulas**!

## Passo 1: Entre na tela de clientes

![Imagem 1: Passo 1: Entre na tela de clientes](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323856/6900734cb7df321f88010c80/mceclip0.png?expires=1786536000&signature=b585133f6b424b22158a251ab386dc981efe35c8418d382447947337f9c0fbde&req=dyYuFct9lYRZFb4V1XW4gQPzlkytWQDViDVCOzBpL%2BgFY4ybMWaPmXGsyqmI%0Apzh9OpNffFfCgf%2BdlzqeSDv7%2BA%3D%3D%0A)

## Passo 2: Clique em Menu

![Imagem 2: Passo 2: Clique em Menu](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323861/0794f74ef6e446e1383c6e58/mceclip2.png?expires=1786536000&signature=2ec7a04acffbbaf8ef3305f237e655bbb77a4ae2f4cc30bf9387cc65b4451dd7&req=dyYuFct9lYdeFb4V1XW4gbbHrpNoEx148BVLh8uBhhBsZD3q2027o6TfcYSA%0AzuQk%2Bmb9PtrA%2FOEaVCI2zWeLBA%3D%3D%0A)

## Passo 3: Clique em Importar clientes pelo Excel

![Imagem 3: Passo 3: Clique em Importar clientes pelo Excel](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323868/b0d8213110a79eb05b5b72bd/mceclip3.png?expires=1786536000&signature=7baa31728503ea1ef74f3a4a68cfd74582838c21214a3be6020d19637685ec4c&req=dyYuFct9lYdXFb4V1XW4gXgYIX0s8giHd9PeEjOjMFxaXvUYEB43dJe1vdmc%0At26wNqyYpVW7c9vploWeiEqS7A%3D%3D%0A)

## Passo 4: Escolha uma planilha em seu computador.

Evite nomes longos e com caracteres estranhos. Em seguida, clique em avançar.

![Imagem 4: Evite nomes longos e com caracteres estranhos. Em seguida, clique em avançar.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323875/49ad5bc116f715ede8443456/mceclip5.png?expires=1786536000&signature=fcbd685ab7e0d0389456780f46def5fa39a9dc6b30c6410ed0390857feb80598&req=dyYuFct9lYZaFb4V1XW4gZ1Ouoz6Ty%2Flgc4kU5Jr6LCSvlSU9srptvpzovGo%0AT%2FSeDEQaLhL%2BKvJOEK3iLxiXUw%3D%3D%0A)

Você pode exportar uma aba de clientes para Excel já com as colunas desejadas. Se precisar de uma planilha modelo base, você pode utilizar esta: [clique aqui](https://docs.google.com/spreadsheets/d/1ko6I_4S3Es98IMPQVWFYmihM-9q8LEXXKr5M8wtI6DU/edit?usp=sharing).

## Passo 5: Realize o mapeamento de campos

Mapear campos significa que você precisa dizer ao Ploomes que os dados de uma coluna específica da seu planilha deverão ser guardadas em um dado campo do Ploomes. Vamos imaginar que sua planilha siga a seguinte estrutura:

![Imagem 5: Mapear campos significa que você precisa dizer ao Ploomes que os dados de uma coluna específica da seu planilha deverão…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323882/f4aa137a3292aac3d9875f98/mceclip9.png?expires=1786536000&signature=1ba9d226a8dc2ad8bda2bcb04a622006ed85edfbc490ba5946df356d36e44c40&req=dyYuFct9lYldFb4V1XW4gdHBCSovtwgMLlyZIcOZT1iq4ZkT0jqCnI3HR452%0A6qXaDGWd1oFE9hmeP5%2BtW%2Bt4xA%3D%3D%0A)

No Ploomes, não chamamos de **Ramo de Atuação**, mas sim de **Segmento**. Então, você deve informar ao sistema que a segunda coluna se refere ao campo de **Segmento**.

Antes disso, entretanto, você precisa definir se aquele campo é um campo de **Empresa ou Pessoa**. Repare na imagem acima: as duas primeiras colunas são **dados da Empresa**. As duas colunas finais são **informações sobre a pessoa** daquela empresa com quem você lida. Por isso, a maneira correta de mapear os campos acima é visto na imagem abaixo:

![Imagem 6: Antes disso, entretanto, você precisa definir se aquele campo é um campo de Empresa ou Pessoa . Repare na imagem acima:…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323885/2361f20902e2a6fc8b6e7f8a/mceclip0.png?expires=1786536000&signature=b04634770f34a66f5179cd253cd85be23851150e84b6b17fea8d81c812c8992e&req=dyYuFct9lYlaFb4V1XW4gZRAUuknLCsmKudtyBg%2FX8tj0otvd9hGmttg1Mjp%0AbWL6yOr9zvHC1C3lXjfPCTKPVQ%3D%3D%0A)

Ao fazer isso, o Ploomes criará uma empresa de nome **Ploomes** com o Segmento **Software**, e adicionará dentro dela uma pessoa de nome **Matheus** e telefone **(11) 3230 - 3035**.

**Fique atento:** se sua planilha tiver muitas colunas, uma barra horizontal será criada para que você consiga rolar a lista para o lado.

A opção "detectar por duplicado por este campo" Impede que sejam importadas duas linhas iguais baseadas em um campo. Normalmente usa-se nome da empresa ou CNPJ.
Mesmo que você mapeie todos os campos obrigatórios, se um cliente estiver com a célula vazia, ele não será importado.

## Passo 6: Avance para a detecção de erros

Nesta etapa, clientes com dados inválidos ou com campos obrigatórios não preenchidos serão destacados para que você esteja ciente do que não será importado. Avance para importar os demais.

## Passo 7: Importação em andamento

É possível que sua barrinha demore a iniciar. Isso acontece em momentos de pico, já que nossa ferramenta de importação tem um limite de importações que podem ocorrer de forma paralela. Você não precisa esperar o processo terminar. Continue usando o sistema normalmente e, quando quiser verificar o status da importação, basta seguir os passos iniciais deste tutorial.

![Imagem 7: É possível que sua barrinha demore a iniciar. Isso acontece em momentos de pico, já que nossa ferramenta de importação…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323891/afc9198885e5d80f889ee9ba/mceclip11.png?expires=1786536000&signature=bd935fafe8f01767f13440e46dc992491935a28973224f3e73f46c9c18818361&req=dyYuFct9lYheFb4V1XW4gRnn1anVIJ6KWiepJSrOpG%2BJMD3S0cQuh7a8ga36%0A%2FUaRKfrjl2T%2FQfya4F37yvT61Q%3D%3D%0A)

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 8: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1385559103/4bc6e261707d93b9acad33676aeb/CRM.png?expires=1786536000&signature=5b96939b9ad0450ecc314bfc6039fcfca69e86da5ae9da4469fe7ab4f1f6fce5&req=dSMvE8x7lIBfWvMW3nq%2Bgb2unEUZ9bfhNhCS%2B2QVq%2Foe3TC%2BmWj%2BoQ3V4GAb%0AksBpirMDNVpLxzlRg3UlOV4VEi0%3D%0A)](https://universidade.ploomes.com/courses/trilha-adm-passo3-crm)

[![Imagem 9: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048764023/73125292d41b6a458093fc895e31/Teste+01.png?expires=1786536000&signature=c1a33aa7c5cd596a03f32c62456659397a6e22a19390f58c5b2e6418b34ffa3d&req=diAjHs54mYFdWvMW3nq%2BgRl1rhtngoE0n5AeZaq1UXCYhydcBIWgPQRxYKRi%0ABCGrFCnVUZwMqZpZOWL5fIcglI0%3D%0A)](https://universidade.ploomes.com/courses/boas-praticas-para-a-importacao-de-dados)
