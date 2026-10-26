---
id: "360045114513"
titulo: "Domínio - Endereço da loja"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114513-Dom%C3%ADnio-Endere%C3%A7o-da-loja"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > E-commerce"
atualizado_em: "2026-07-29T14:37:15Z"
rotulos: ["#Ecommerce", "Configuração", "Web", "Portal de Vendas", "Procedimento: Acessar painel editar DNS", "Domínio: Registro.br configurar IP salvar", "Configuração DNS: Entrada \"A\" para servidor", "DNS", "Domínio"]
---

# Domínio - Endereço da loja

O domínio, ou endereço virtual da loja, deve ser configurado nas opções de DNS do domínio, apontando a entrada **"A"** do endereço para o servidor onde a loja estará hospedada.

#### Mas o que é DNS?

O Sistema de Nomes de Domínio, mais conhecido pela nomenclatura em inglês Domain Name System (DNS), é um sistema hierárquico e distribuído de gerenciamento de nomes para computadores, serviços ou qualquer máquina conectada à internet ou à uma rede privada. Para mais informações sobre este tema, [clique aqui.](https://pt.wikipedia.org/wiki/Sistema_de_Nomes_de_Dom%C3%ADnio)

#### Como configurar o domínio de minha loja?

É muito simples realizar esta configuração! Será utilizado como exemplo, a configuração de um domínio utilizando o [registros.br](https://registro.br/) mas, genericamente, o procedimento é similar para demais mecanismos de gerenciamento de DNS.

O primeiro passo, é acessar o painel administrativo no registro.br, utilizando a conta que permite gerenciar o domínio. Após o login, será exibido a lista de domínios que sua conta está gerenciando. A imagem a seguir, exibe a tela com o domínio já selecionado.

![Imagem 1: O primeiro passo, é acessar o painel administrativo no registro.br , utilizando a conta que permite gerenciar o…](https://ajuda.sankhya.com.br/hc/article_attachments/360061011934)

Em seguida, clique no domínio que deseja realizar a configuração. Ao clicar no domínio, o sistema exibe detalhes sobre o mesmo (Titular, Contatos, DNS e Provedor de Serviços). Na seção DNS, clique no link **"EDITAR ZONA"**, conforme ilustra a imagem a seguir:

![Imagem 2: Em seguida, clique no domínio que deseja realizar a configuração. Ao clicar no domínio, o sistema exibe detalhes sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/360061011954)

Agora o sistema exibe uma área para editar/incluir as configurações do domínio. É importante deixar as configurações do DNS no modo avançado (por padrão o domínio inicia no modo básico).

Com a edição de DNS no modo avançado, clique no botão **"NOVA ENTRADA"** e insira uma entrada do tipo **"A"**, apontando para o IP 104.198.79.205. A imagem a seguir, exibe o domínio com a entrada do tipo A configurado devidamente.

![Imagem 3: Com a edição de DNS no modo avançado, clique no botão "NOVA ENTRADA" e insira uma entrada do tipo "A" , apontando para…](https://ajuda.sankhya.com.br/hc/article_attachments/360061011974)

Caso sua loja responda também ao endereço começando com www, basta criar uma nova entrada do tipo CNAME apontando para o endereço principal de seu domínio. A imagem acima ilustra esta configuração.

**Importante:** Não deixe de clicar em **"SALVAR"** para que as configurações realizadas sejam salvas. Vale ressaltar, que esta configuração pode levar até 48 horas para serem propagadas, ou seja, para que ao acessar o endereço de sua loja, ela seja exibida em seu navegador.

No exemplo utilizado acima, a loja é exibida acessando com o endereço principal (ex.: minhaloja.com.br) e também com o endereço começando com www (ex.: [www.minhaloja.com.br)](http://www.minhaloja.com.br)).

#### Não tenho um domínio, e agora?

Caso não tenha ainda um domínio para sua loja, não se preocupe. No próprio registro.br, é possível realizar o registro de um domínio nacional (.com.br). Basta localizar um domínio disponível e avançar com a aquisição.

Para mais detalhes de como adquirir um domínio, [clique aqui](https://registro.br/ajuda/registro-de-novos-dominios/).
