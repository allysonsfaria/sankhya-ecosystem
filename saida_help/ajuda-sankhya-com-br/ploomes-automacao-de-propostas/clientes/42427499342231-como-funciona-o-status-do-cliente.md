---
id: "42427499342231"
titulo: "Como funciona o Status do cliente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427499342231-Como-funciona-o-Status-do-cliente"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T18:04:40Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7939134", "sync_hash_88347f69db4b"]
---

# Como funciona o Status do cliente?

O relacionamento com seus clientes, na maioria das vezes, é de longo prazo. Ao longo desse período, cada cliente passa por diferentes fases e apresenta comportamentos distintos.

Para organizar melhor a sua base de clientes, é recomendável classificá-los por **Status**. Dessa forma, você terá uma visão clara da situação atual de cada cliente.

## Como alterar?

Para adicionar ou alterar um status, o campo **Status** deve estar incluído no formulário. Assim, ao criar ou editar um cliente, você visualizará o campo e poderá preenchê-lo.

Caso o campo não esteja no formulário, acesse **Administração > Campos e formulários > Cliente > Adicionar campo**.

⚠️ Somente usuários com o perfil "Administrador" têm acesso a essa tela e configuração.

![criação de cliente](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048285516/4983ff659f3024d22dd33d16f003/image.png?expires=1786536000&signature=7ca28ae59cf2ab2259b09e40522415837c3279b8591c2c9a0f501cc45ae5ac30&req=diAjHst2mIReX%2FMW3nq%2BgbmQyb92iygvT%2Bgkj7UlSMiVZhK9ICu1wwAZIALW%0AgbCT0g745BDquBYxjR7CUOy9eb0%3D%0A)

Também é possível alterar o **Status** dos clientes de forma rápida diretamente pela tela principal de **Clientes**.

![Tela do cliente](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048421991/7bf20e5dd660c91436d8a9e8dcd6/image.png?expires=1786536000&signature=b24e3aac18adc215ccc206de656784cc08d465af1a24be633ba678e71d88a90e&req=diAjHs18nIhWWPMW3nq%2BgVlBIfNu0Ok6ygD35mPq3mH3HHB5PeLqNd97gV0Z%0AMFd8s6%2Fnfp0YDNY1m5rh6O7kc%2BE%3D%0A)

## O que é cada status?

**Ativo:** cliente que já comprou de você e segue demonstrando interesse, mantendo o consumo dos seus produtos ou serviços.

**Descartado:** cliente que, por algum motivo, está impossibilitado de negociar, como em casos de falência da empresa, mudança de ramo de atividade, entre outros.

**Inativo:** cliente que já comprou anteriormente, porém deixou de negociar, podendo ser uma situação momentânea ou permanente.

**Prospecção:** um cliente em prospecção é aquele que você está iniciando um relacionamento ou oportunidade de venda, ou seja, está em processo de convencimento do seu produto ou serviço.

## Como utilizar?

Sempre que um cliente é criado, seu status é definido automaticamente como **Prospecção**. Ao realizar uma venda para esse cliente, o status é alterado automaticamente para **Ativo**.

Para inativar um cliente, é possível configurar uma automação para facilitar o processo.

Por exemplo: se um cliente estiver vinculado a um negócio que foi marcado como **Perdido**, você pode definir uma automação para que o status desse cliente seja alterado automaticamente para **Inativo**.

## Como configurar?

- Acesse **Administração** > **Automações;**
- Selecione a entidade **Negócio** (também pode estar escrito como: **Card**, **Pipe**, **Workflow**);
- Clique em **Nova automação**;
- Adicione como **Gatilho** a opção **Quando o negócio for perdido**;
- Configure a automação para editar o campo **Status** do cliente, definindo-o como **Inativo**.

  [GIF animado: configuração da automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048492695/42ed889bad878855b17301bf5dd5/artigo5.gif?expires=1786536000&signature=1a7ffbb17945116621c686e89ff74cc74f666a81a2bf9987745f3abdf3757a95&req=diAjHs13n4dWXPMW3nq%2BgY%2BUh6brnYVUNIB%2BQxD%2BbGWU8%2FbFfVkhAhKCGt2J%0AgDPKtRysOY5k0Hhc3QCePlQnb1Q%3D%0A)

## Campo status

No campo **Status** nativo do Ploomes, não é possível adicionar novas opções. No entanto, é possível criar um novo campo do tipo **Opções pré-cadastradas** para substituí-lo e cadastrar as opções desejadas.

## Como criar o campo?

- Acesse **Administração > Campos e formulários > Cliente;**
- Selecione o formulário desejado (**Empresas** ou **Pessoas**);
- Clique em **Adicionar** **campo** > **Criar campo**;
- Escolha o tipo **Opções pré-cadastradas**;
- Defina o **Título** do campo e cadastre as opções desejadas.

  [GIF animado: como criar o campo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048519935/5b9855d7f9cabac4b606e2da8ff2/artigo6.gif?expires=1786536000&signature=7a71e47c654f49867eaf417c346cf747c131e7a540d7d4feb30e7df864e06e78&req=diAjHsx%2FlIhcXPMW3nq%2BgSflaPI9tCWGlpKECDrjkeHUGHYpbjYTxlJREdbT%0AivNQ50VN6FQJkcahB6ZBOaEcWzU%3D%0A)

Após cadastrar todas as opções desejadas, salve o campo e, em seguida, salve o formulário para aplicar a atualização.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
