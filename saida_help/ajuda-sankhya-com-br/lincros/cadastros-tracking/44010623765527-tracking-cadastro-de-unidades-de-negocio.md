---
id: "44010623765527"
titulo: "[Tracking] - Cadastro de Unidades de Negócio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010623765527--Tracking-Cadastro-de-Unidades-de-Neg%C3%B3cio"
trilha: "Lincros > Tracking > Cadastros - Tracking"
atualizado_em: "2026-10-05T18:42:14Z"
rotulos: ["sync_hc", "lincros", "lincros_13438240", "sync_hash_7d52be659a36"]
---

# [Tracking] - Cadastro de Unidades de Negócio

**Menu**: Configurações > Cadastros > Unidades de Negócio

**Objetivo**: Explicar como cadastrar uma unidade de negócio no Tracking.

**Considerações**:

- Possuir algum usuário administrador;
- Algumas das configurações estão disponíveis apenas a partir da versão 4.28;

Abaixo segue os procedimentos:

1. Acessar o ambiente do Tracking (<https://espaco-cliente-tracking.lincros.com/>);
2. No menu, ir em Cadastros > Unidades de Negócio > Novo:

   ![Imagem 1: No menu, ir em Cadastros > Unidades de Negócio > Novo:](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1964853874/1f9d13d19f0cf733b8b88b908fd3/D7BB90080254901FC9B3A766F3358414?expires=1791331200&signature=1ecb1998248a457c76337596cbeab072f14cefbbd3df5c6d92fdb7d589bb5444&req=dSkhEsF7nolYXfMW3nq%2BgawilMXhN6ZlaEpzR3bl6WSd%2Bmg7IPC3XO1oT%2B5Z%0AqSi9a8Pp0NJ1vgaawPsL0m6xaJw%3D%0A)
3. Na janela que abrirá, deverão ser informados os campos: **Nome**: Informar o nome da unidade de negócio; **CNPJ**: Informar o CNPJ dessa unidade; **Código**: Informar o código desejado — esse código deve ser o mesmo que se utiliza no depósito no Routing, caso haja integração.

   ![Imagem 2: Na janela que abrirá, deverão ser informados os campos: Nome : Informar o nome da unidade de negócio; CNPJ : Informar o…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1964853896/613606b92a545e0d591edbcdf2df/26A23DBB8EBCE598DD25BA2250C53761?expires=1791331200&signature=02dbb07173edf2e6276873af4cffb42b85a134b7dda69ca21f60d8b04682a9fa&req=dSkhEsF7nolWX%2FMW3nq%2BgdkjB%2Bx5uF%2Fj4RHGSSUDNgYL3RKIAl%2BijwWBWHzs%0Aq67I%2F6gFHnGa4HmJ7NzefxHBZwU%3D%0A)
4. Em "**Configurações Gerais**" tem as seguintes opções para configurar:

- **Bloquear alterações após a roteirização**: Impede que uma viagem seja reimportada após ter sido roteirizada;
- **Utilizar Gerenciadora de Risco**: Habilita o funcionamento da integração com a GR Apisul;
- **Habilitar Anomalias de PDV**: Habilita o módulo de Anomalias de PDV;
- **Habilitar integração com Lincros Routing**: Habilita o envio de informações de coordenadas e tempo de atendimento para o Lincros Routing;
- **Permitir reversão da devolução antes do tratamento da Central**: Possibilita que o motorista realize uma reversão de uma devolução lançada antes de a Central de Atendimento tratá-la;
- **Ativar guia 'Recebimento' nos Detalhes da Entrega**: Habilita a exibição da guia 'Recebimento' nos Detalhes da Entrega;
- **URL do Roteirizador**: <https://routing.lincros.com/> (Não obrigatório, caso não utilize o roteirizador)
- **Token do Depósito**: Caso não possua, verificar com o Suporte Lincros;
- **Habilitar cálculo de ETA**: Habilita o processamento do Tempo Estimado de Chegada nas entregas.

5. Em "**Configurações para o Smartphone**" as opções a serem parametrizadas são:

- **Habilitar Controle de Volumes**: Habilitar recurso de Controle de Volumes na confirmação da entrega no Tracking Mobile
- **Nível de tratamento de devolução**: Tem as opções: Total; Documento; Item do documento; Volume;
- **Tratamento de item na devolução**: Habilitado quando o nível de tratamento for marcado em "Item do documento". Opções: Padrão; Por valor; Por quantidade; Por peso;
- **Exibir campo quantidade para o motorista**: Campo adicional solicitando que o motorista informe a quantidade de produtos devolvidos por item da Nota Fiscal;
- **Utilizar GPS para finalizar a viagem**: O motorista somente poderá finalizar a viagem caso esteja dentro do raio da Unidade do Depósito;
- **Exigir quantidade de ativos entregues no registro da Entrega**: Campo para informar quantidade de ativos entregues ao confirmar uma entrega;
- **Exigir nome e assinatura na movimentação de ativos**: Obrigatório coletar nome, documento e assinatura do responsável pela movimentação;
- **Validar motorista no login**: Inclui campo adicional de senha na tela de inicialização da viagem;
- **Utilizar controle de descarga**: Habilita o módulo de controle de descarga;
- **Utilizar QRCode para iniciar a viagem**: Bloqueia o método convencional, permitindo iniciar a viagem apenas por QR Code;
- **Limitar versão mobile**: Utilizado para restringir o acesso dos motoristas a uma determinada versão;
- **Restringir início de viagem já iniciada**: O motorista conseguirá iniciar a viagem uma única vez;
- **Tempo para notificar parada de refeição (em minutos)**: Define o tempo em rota que fará com que o motorista realize a parada para refeição;
- **Validar data e hora automática**: Impede que o motorista inicie a viagem sem configurar a data e hora automática da rede no smartphone;
- **Exige entrega dentro do raio**: Impede que o motorista aponte uma entrega fora do raio do cliente.

6. Para finalizar o cadastro da nova Unidade de Negócio, é preciso informar os usuários que devem ser vinculados à nova unidade, localizando-os no lado esquerdo e movendo-os para o lado direito.

![Imagem 3: 6. Para finalizar o cadastro da nova Unidade de Negócio, é preciso informar os usuários que devem ser vinculados à nova…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1964853910/749837983e0b7037f47f563bcbdf/208F1CF0A85AF8D31887CC9BF721483B?expires=1791331200&signature=7ba6a028934f3a5c2b6980212a53772285df80d9ee98e25504afe29f37951d0f&req=dSkhEsF7noheWfMW3nq%2BgScdJlz9YKh%2FDP3mtns%2BW7ycafwjcYdb2fn2C7ww%0ArstB5Sn6zoHUwSbKGitGn63IPVo%3D%0A)

![Imagem 4: 6. Para finalizar o cadastro da nova Unidade de Negócio, é preciso informar os usuários que devem ser vinculados à nova…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1964853935/ff1b83144483bfb702d8ae781afc/70F288E27D404F384D2CEFD1B7A4BD2B?expires=1791331200&signature=aa6fb4524d5f4cad7dc21c7231229bc5f9307cbfa2a589a9fdd7c15619b008de&req=dSkhEsF7nohcXPMW3nq%2BgeK6xwkKpbkZqGqOMTV31FKkmXV3%2BPL9K8VvXfYK%0AIOG5TOY4KYGt9BgHoSf0iRZ9r%2Bc%3D%0A)

7. Após informar os usuários vinculados, caso as demais configurações estejam preenchidas, pode ser clicado em "Salvar" para finalizar o cadastro.

8. Após criada a Unidade de Negócio, é necessário criar um Depósito para essa Unidade de Negócio. Para mais informações, consulte o artigo [[Tracking] - Cadastro de depósito](https://sankhya.zendesk.com/hc/pt-br/articles/44010623765527).

**Obs**.: Após finalizar a criação da unidade de negócios, é importante realizar logout e logar novamente no ambiente, para que os usuários vinculados tenham visualização da nova unidade. O criador também deve informar seu usuário em "usuários vinculados" para ter visão da unidade criada.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
