---
id: "42427454423831"
titulo: "Integração com Exact Spotter"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427454423831-Integra%C3%A7%C3%A3o-com-Exact-Spotter"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:02:41Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452429", "sync_hash_4b3d1a0d72a4"]
---

# Integração com Exact Spotter

Esta integração permite o envio em tempo real de leads do Exact Spotter para o Ploomes, a partir de algum evento escolhido pelo usuário Ploomes, permitindo a criação de clientes e negócios de forma customizável.

O Exact Spotter é uma ferramenta de LRM (Lead Relationship Management) brasileira focada em B2B. Eles são especializados em tratar, na jornada do cliente, a fase da prospecção. Essa etapa se encontra indistintamente entre a captação do lead via anúncios (marketing inbound ou outbound) e a avaliação técnica e fit do contato/cliente para o produto. Deste ponto de vista, a atuação desta ferramenta na jornada do cliente vem um passo antes do Ploomes, que é uma ferramenta de CRM (Customer Relationship Management).

O Ploomes recebe em tempo real as informações do **lead** e dos **contatos do lead**, bem como a **atividade** e a **avaliação** de uma interação do lead. Dado a liberdade da integração, o usuário no Ploomes pode escolher quais eventos do Spotter disparam o envio de dados do lead para o Ploomes. A integração também permite mapear campos não tratados por padrão na integração, incluindo os campos dinâmicos do lead no Exact Spotter.

## Como ativar a integração

Caso integre pela **versão antiga** do Spotter, logue pelo link: <http://www.exactsales.com.br>

Caso integre pela **versão nova** do Spotter, logue pelo link: <https://app.exactspotter.com/Account/Login>

Se for cabível a escolha, recomendamos que use a versão nova.

Para ativar a integração, primeiramente é preciso buscar o token de API do Exact Spotter.

Para fazer isso, siga os passos:

1. Acesse sua conta do Exact Spotter;
2. Navegue pelas seguintes páginas: Configurações > Integrações > Token Exact API.

![Imagem 1: Navegue pelas seguintes páginas: Configurações > Integrações > Token Exact API.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330010/086a660d517bb6e5032e625e/mceclip0.png?expires=1786536000&signature=3f37e75285f3c30bdb05ae8bc9e1bf2f5b838f7020f4531b76d55cd16e5de203&req=dyYuFcp%2BnYBfFb4V1XW4gWVRshcQrYIZzck%2F2BE%2BkldoxUDjDkZM%2FYPwbTSE%0AQVMVCd6iarMjXwFfHQwPDEptxg%3D%3D%0A)

![Imagem 2: Navegue pelas seguintes páginas: Configurações > Integrações > Token Exact API.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330018/756da573056d64593eb4060a/mceclip1.png?expires=1786536000&signature=529ce35aa2def84b994f7519c86eae47287b14d6fba4b368fc22b7a90780809e&req=dyYuFcp%2BnYBXFb4V1XW4gcFJ6BknJvMqc%2BVgRwiXDMt0HxJ97rBjwphuNPMU%0ABKgMUph4vkQzqO4GaaaZ981%2FaQ%3D%3D%0A)

![Imagem 3: Navegue pelas seguintes páginas: Configurações > Integrações > Token Exact API.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330032/04ef1d9ca3ab27bf1f61e8e4/mceclip2.png?expires=1786536000&signature=cbba0bbb3cdb5a44bf5eef24184d89215e1505765eadf345a0c111fd10716036&req=dyYuFcp%2BnYJdFb4V1XW4gd8Z1y9707JvcXDbL3TfRRXbqhJsU8JsO6rbyh0r%0ALnLoyq3Duipd8rVV8Ayh%2FQUZ6Q%3D%3D%0A)

Copie o Token Exact fornecido pela plataforma.

![Imagem 4: Copie o Token Exact fornecido pela plataforma.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330040/fc907d26c895ef5288e0830b/mceclip3.png?expires=1786536000&signature=552cd748860034fa95e9fa6e6ddf5a1eede0bd0ababbb7472d318edc71478671&req=dyYuFcp%2BnYVfFb4V1XW4gWO7H%2BdSXTxUQnP7cQd5aR5H77PuMLR8UTVBJikC%0AHVcoz%2BpkBYDQ7vDB0%2Fd78xCTPQ%3D%3D%0A)

Depois de obter seu Token Exact, autorize a integração no Ploomes fornecendo o token copiado.

![Imagem 5: Depois de obter seu Token Exact, autorize a integração no Ploomes fornecendo o token copiado.](https://downloads.intercomcdn.com/i/o/872294358/35f38ace838be3fd9be26573/image.png?expires=1786536000&signature=019788c1f5d324c3fe45b2f247fa501a9ae791286bf18ab33aa5f9fa634ddcbf&req=fCclFMB6noRXFb4V1XW4gdnSFx1VKb01yhDV376Bgasm7IZeQlNEkYpU5gzU%0AiHe2PM0vEK8QcpJt59eocUKHOw%3D%3D%0A)

Depois da autenticação, escolha o comportamento desejado do Ploomes para esta integração.

![Imagem 6: Depois da autenticação, escolha o comportamento desejado do Ploomes para esta integração.](https://downloads.intercomcdn.com/i/o/872298399/2fd3d38bd8ea973e23a05c32/image.png?expires=1786536000&signature=b5bf2a6a1bb2b47f96f69e0bb6c6392809de11b3bd3d1ab87b7f8466fcaf9a08&req=fCclFMB2nohWFb4V1XW4gWYGVTUwpYq%2BOt8kKP%2FUE9CC3DX7a2z8sv8HbptI%0AWg1xGdqLUPeLWbTsFq3OTX5aJw%3D%3D%0A)

Escolha quais gatilhos enviarão o lead do Spotter para o Ploomes.

![Imagem 7: Escolha quais gatilhos enviarão o lead do Spotter para o Ploomes.](https://downloads.intercomcdn.com/i/o/872298804/2079a597d5e3c2b7ec9b4fcd/image.png?expires=1786536000&signature=8f2071e22c5cb92e781e96277104975dd7653d98051755fb9aca691b51d86bc8&req=fCclFMB2lYFbFb4V1XW4geeDXkER%2BAJr9MfbMkaIJNficEejtTMljduVmJ%2B7%0AMZjFHEq4y29vNT90oeyPUwJL5Q%3D%3D%0A)

Por fim, faça o mapeamento dos campos conforme for necessário. Muitos dos campos padrão já estão mapeados, mas fornecemos suporte aos campos customizados do Spotter.

![Imagem 8: Por fim, faça o mapeamento dos campos conforme for necessário. Muitos dos campos padrão já estão mapeados, mas…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330074/29d3195cc7ec5e7a37155060/mceclip7.png?expires=1786536000&signature=5a5d0c89ca84bdf4e0c0acc24db936912116b2372e52ebb318d40e33b52e7cfb&req=dyYuFcp%2BnYZbFb4V1XW4gQKdj0WuZgpR7hAzUmqTg4f6vkvXCh5VHc1kDDT8%0AMzVXyy8E07gZYaq8wGdojFBBbw%3D%3D%0A)

**Observações:**

- Campos mapeados para cliente no Ploomes são sempre considerados para o lead do Spotter. O tipo de cliente é a empresa (e não os contatos).
- O campo Etapas, Perguntas e Respostas é codificado em um texto multilinha como um relatório, e se espera um campo tipo texto multilinha no Ploomes para recebê-lo.
- O campo Dores, se for desejado usar seu valor, deve ser mapeado para um campo no Ploomes de tipo Opções pré-cadastradas e também múltiplo.
- A detecção de duplicados é realizada pelos campo de **CNPJ** e **Telefone.** Para detectar por CNPJ é preciso mapeá-lo com um campo do Exact Spotter, caso contrário os duplicados serão detectados por padrão pelo Telefone.
