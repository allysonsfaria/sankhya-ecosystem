---
id: "42427429767063"
titulo: "Integração com FoccoERP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:43Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5680977", "sync_hash_ac22302aee4e"]
---

# Integração com FoccoERP

**Observação: Para que seja possível utilizar a integração, é necessário ter o o módulo de "e-commerce" contratado na plataforma de FoccoERP.** Caso não tenha este módulo contratado, entre em contato com seu executivo de relacionamento da Focco.

## Sumário

**[Mapa geral da integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_1f0fb6ccc8)**

**[Instruções da ativação da integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_93069ac210)**

1. [Habilitação da integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_87396b9d23)
2. [Autorização da integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_664820dfe3)
3. [URL da API e FoccoERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_e7ff1255e4)
4. [URLs de importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_8ad7892819)
5. [Importação de pedidos dos últimos dois anos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_89f0019fca)
6. [Importação de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_b8087b3da5)
7. [Mapeamento de campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_641b1f1711)
8. [Ativação da integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_fae497022b)
9. [Consulta a estoque, em tempo real, por campo de fórmulas externas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427429767063-Integra%C3%A7%C3%A3o-com-FoccoERP#h_8608b82788)

## Mapa geral da integração

## Clientes (Empresas e Pessoas):

- **Ploomes > Focco:**

  - Criação: não disponível
  - Alteração: não disponível;
  - Exclusão: não disponível.

- **Focco > Ploomes**

  - Criação: disponível para clientes com a propriedade "e-commerce" ativa. Clientes criados no Focco são trazidos ao Ploomes nos seguintes momentos:

    - Ao ativar a integração;
    - Ao clicar em “Atualizar” na seção "Atualize sua base de clientes", dentro da tela de configurações da integração;
    - A cada 24 horas;
    - Quando um pedido chega do Focco ao Ploomes (seja um pedido novo ou um pedido alterado) e o cliente não existe no Ploomes.
  - Alteração: disponível para clientes com a propriedade "e-commerce" ativa. Clientes alterados no Focco são alterados no Ploomes nos seguintes momentos:

    - Ao ativar a integração;
    - Ao clicar em “Atualizar” na seção "Atualize sua base de clientes", dentro da tela de configurações da integração;
    - A cada 24 horas;
    - Quando um pedido chega do Focco ao Ploomes (seja um pedido novo ou um pedido alterado).
  - Exclusão: não disponível.

## Produtos:

- **Ploomes > Focco:**

  - Criação: não disponível;
  - Alteração: não disponível;
  - Exclusão: não disponível.
- **Focco > Ploomes:**

  - Criação: disponível para produtos com a propriedade "e-commerce" ativa e que possuam uma "Classificação". Produtos criados no Focco são trazidos ao Ploomes nos seguintes momentos:

    - Ao ativar a integração;
    - Ao clicar em “Atualizar” na seção "Atualize sua base de produtos", dentro da tela de configurações da integração;
    - A cada 24 horas;
    - Quando um pedido chega do Focco ao Ploomes (seja um pedido novo ou um pedido alterado) e o produto não existe no Ploomes.
  - Alteração: disponível para produtos com a propriedade "e-commerce" ativa e que possuam uma "Classificação". Produtos alterados no Focco são trazidos ao Ploomes nos seguintes momentos:

    - Ao ativar a integração;
    - Ao clicar em “Atualizar” na seção "Atualize sua base de produtos", dentro da tela de configurações da integração;
    - A cada 24 horas;
    - Quando um pedido chega do Focco ao Ploomes (seja um pedido novo ou um pedido alterado).
  - Exclusão: não disponível.

## Vendas / Pedidos:

- **Ploomes > Focco:**

  - Criação: disponível para vendas que tenham o campo Tipo de Pagamento preenchido e cujo cliente possua uma transportadora definida no seu cadastro no Focco. Vendas criadas no Ploomes são levadas ao Focco nos seguintes momentos:

    - Ao criar uma venda no Ploomes;
    - Obs.: o Focco pode ter regras específicas de bloqueio de pedido configuradas. Nestes casos, o pedido não será enviado, e o usuário que criou o pedido receberá uma notificação e um registro de interação explicando o erro retornado pelo Focco. O usuário deverá, então, ajustar o problema, excluir uma venda e gerar uma nova.
  - Alteração: não disponível;
  - Exclusão: não disponível.
- **Focco > Ploomes:**

  - Criação: disponível. Pedidos de venda criados no Focco são trazidos ao Ploomes como vendas nos seguintes momentos:

    - Ao ativar a integração, caso eu ative a opção "Deseja importar todos os pedidos de venda dos ultimos dois anos?";
    - A cada 1 hora;
    - Ao clicar em “Atualizar integração” na extremidade inferior da tela de configurações da integração;
    - Obs.: pedidos de clientes sem a propriedade "e-commerce" ativada serão trazidos ao Ploomes. Isso significa que estes serão cadastrados no Ploomes mesmo sem a propriedade em questão.
  - Alteração: disponível. Pedidos de venda alterados no Focco são alterados no Ploomes nos seguintes momentos:

    - Ao ativar a integração, caso o Ploomes já possua vendas com ID Focco, elas serão atualizadas (caso sejam dos últimos 2 anos). Este mecanismo blinda o Ploomes de duplicidade de dados caso a integração seja ativada, inativada e reativada;
    - A cada 1 hora;
    - Ao clicar em “Atualizar integração” na extremidade inferior da tela de configurações da integração.
  - Exclusão: não disponível.

## Formas de Pagamento:

- **Ploomes > Focco:**

  - Criação: não disponível;
  - Alteração: não disponível;
  - Exclusão: não disponível.
- **Focco > Ploomes:**

  - Criação: disponível. Formas de pagamento criadas no Focco são criadas no Ploomes nos seguintes momentos:

    - Ao ativar a integração;
    - A cada 1 minuto.
  - Alteração: disponível. Formas de pagamento alteradas no Focco são alteradas no Ploomes nos seguintes momentos:

    - Ao ativar a integração, caso o Ploomes já possua formas de pagamento com ID Focco, elas serão atualizadas. Este mecanismo blinda o Ploomes de duplicidade de dados caso a integração seja ativada, inativada e reativada;
    - A cada 1 minuto.
  - Exclusão: não disponível.

## Integração com Clientes (Empresas e Pessoas):

- Chave para vínculo entre um cliente cadastrado no Ploomes e um cliente cadastrado no Focco:

  - Chave principal: **ID Cliente Focco**;
  - Chave secundária: **CNPJ/CPF**.
- O mapeamento de campos possui opções fixas e limitadas entre os sistemas. Alguns campos padrões já existentes nos dois sistemas são mapeados de forma automática e não podem ser alterados (\*). E outros campos possuem a possibilidade de vincular um campo do FoccoERP a outro campo compatível do Ploomes.

  - Os campos mapeáveis para os cadastros de Clientes do Focco que são importados como Empresa no Ploomes:

    - Nome Fantasia\*
    - Razão Social\*
    - E-mail\*
    - Número Telefone\*
    - CNPJ\*
    - CEP\*
    - Endereço\*
    - Bairro\*
    - Número Endereço\*
    - Complemento\*
    - Cidade\*
    - UF\*
    - País\*
    - Data Nascimento\*
    - Inscrição Estadual
    - Contato
  - Os campos mapeáveis para os cadastros de Clientes do Focco que são importados como Pessoa no Ploomes:

    - Contato\*
    - Email\*
    - Número Telefone\*
    - CPF\*
    - CEP\*
    - Endereço\*
    - Bairro\*
    - Número Endereço\*
    - Complemento\*
    - Cidade\*
    - UF\*
    - País\*
    - Data Nascimento\*
    - Inscrição Estadual
    - Contato
- Ao ativar a integração, dois campos dinâmicos de cliente são criados no Ploomes:

  - ID Cliente Focco;
  - Código Cliente Focco.
- Os dois campos acima são utilizados para vincular um cliente do Ploomes a um cliente do Focco. Caso estes campos estejam vazios no Ploomes, a integração tentará vincular os clientes a partir do CNPJ/CPF. Caso ocorra um "match", o cliente do Ploomes será atualizado com o ID Cliente Focco e o Código Cliente Focco. Exemplo:

  - Cadastrei um cliente no Ploomes;
  - Em seguida, cadastrei o mesmo cliente no Focco;
  - Gerei uma venda no Ploomes;
  - Quando a venda chegar ao Focco, o cliente Ploomes não terá um ID Cliente Focco, nem um Código Cliente Focco. Neste momento, a integração buscará o cliente no Focco pelo CNPJ/CPF. Ao encontrá-lo, o cliente Ploomes receberá o ID Cliente Focco e o Código Cliente Focco, e o pedido será salvo no Focco.
- Obs.: o Focco permite cadastro de dois clientes com o mesmo CNPJ/CPF. Nestes casos, quando a integração tentar realizar o vínculo por estes parâmetros e encontrar dois clientes, um deles será selecionado aleatoriamente.

## Integração com Produtos

- Chave para vínculo entre um produto cadastrado no Ploomes e um produto cadastrado no Focco:

  - Chave para trazer um produto do Focco ao Ploomes: **Código**;
  - Chave para enviar um produto dentro de um pedido do Ploomes ao Focco: **Id Produto Focco**;
- O mapeamento de campos possui opções fixas e limitadas entre os sistemas. Alguns campos padrões já existentes nos dois sistemas são mapeados de forma automática e não podem ser alterados (\*). E outros campos possuem a possibilidade de vincular um campo do FoccoERP a outro campo compatível do Ploomes.

  - Os campos mapeáveis para os cadastros de Produto do Focco que são importados como Produto no Ploomes:

    - Descrição\*
    - Código\*
    - Unidade de Medida\*
    - Classificação\*
    - Configurado
    - Descrição Complementar
    - Descrição Técnica
    - Observação
- Ao ativar a integração, dois campos dinâmicos de produto são criados no Ploomes:

  - ID Produto Focco;
  - Código Empresa Produto Focco.
- O Código Empresa Produto Focco é apenas para referência, já que o Focco é multi empresas. O ID Produto Focco é utilizado como chave de integração, como explicado acima.
- O campo de "Marcadores" do Ploomes será preenchido com o status do produto no Focco ("DISPONÍVEL FOCCO" e "INDISPONÍVEL FOCCO"). Isso permitirá criar filtros nos modelos de proposta, vendas e documentos no Ploomes que limite a listagem de produtos apenas para os disponíveis;
- Obs.: produtos sem o parâmetro e-commerce ativado que chegarem ao Ploomes por pedidos gerados no Focco não terão nenhum marcador atrelado.

## Integração com Pedidos de Vendas e Produtos da Venda

- Chave para vínculo entre uma venda cadastrada no Ploomes e um pedido cadastrado no Focco: **ID Pedido de Venda Focco**;
- O mapeamento de campos possui opções fixas e limitadas entre os sistemas. Alguns campos padrões já existentes nos dois sistemas são mapeados de forma automática e não podem ser alterados (\*). E outros campos possuem a possibilidade de vincular um campo do FoccoERP a outro campo compatível do Ploomes.

  - Os campos mapeáveis para os cadastros de Vendas do Focco que são importados como Vendas no Ploomes:

    - Data Emissão\*
    - Item\*
    - Cliente\*
    - Valor Líquido\*
    - Tipo Frete
    - Valor Frete
    - UF
    - Valor IPI
    - Valor Sub ICMS
  - Os campos mapeáveis para os cadastros de Produtos da Venda do Focco que são importados como Produtos da Venda no Ploomes:

    - Valor Total\*
    - Valor Unitário\*
    - Quantidade\*
    - Valor IPI
    - Valor Sub ICMS
- Ao ativar a integração, alguns campos dinâmicos de venda e produtos da venda são criados no Ploomes:

  - Venda:

    - ID Pedido de Venda Focco: utilizado como chave de integração, como explicado acima;
    - Status Pedido de Venda Focco: informação sobre o status do pedido ao usuário;
    - Tipo de Pagamento Focco: campo de preenchimento obrigatório durante a criação da venda no Ploomes para envio ao Focco.
  - Produto da venda:

    - Valor ICMS Sub Prod. Venda: ICMS calculado pelo Focco e devolvido ao Ploomes. Apenas informação ao usuário;
    - Valor IPI Sub Prod. Venda: IPI calculado pelo Focco e devolvido ao Ploomes. Apenas informação ao usuário

## Instruções de ativação da integração

## 1) Habilitação da Integração

Entre em Administração e, em Integrações Plug and Play, procure pelo ícone do Focco. Em seguida, clique em “Habilitar Integração”.0

![Imagem 1: Entre em Administração e, em Integrações Plug and Play, procure pelo ícone do Focco. Em seguida, clique em “Habilitar…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488268/9c3cff6cfd5f32cc2f0bb824/k-ivkfT0EFknKhnVb8Eb4SlDMQ5w6ZMbMVE35C2KzyOb8klfxs7LafsCimaM2ofHRG2wrzf8035SAW3JZHr6IDu4BdUCXOXeC-1hCj6E7B1is_egdJIAUKT9J1_udgSiE3E3aL-b?expires=1786536000&signature=2ea0980e3905ac3a9333fd96498089e3eae9c9dffe65a10396a15d5839dea4c9&req=cCAuEsF2n4dXFb4V1XW4gZjJ9IPm0pD7C6t4%2BW2TFm5zMlMRoicMCpSc2ElG%0AutPP1w53I%2Fq8LcPBjKrVFbdqbQ%3D%3D%0A)

## 2) Autorização da Integração

Em seguida, clique em Autorizar a Integração, como mostra a imagem abaixo:

![Imagem 2: Em seguida, clique em Autorizar a Integração, como mostra a imagem abaixo:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488271/c3e0cfa485f014d2e4d8c612/53IgPaqt5RuTJS9PE7QDUD29AW2QcFZMSaYd7B7goyQa4Cmr7UxdTqMJvfRnylS7D5XlLIv4OIM9XM-E7CDCQXl3f6ymrqpSHsXZQ3CR2E7kZTH0HjxnTg-GVKP4rJVGsqSCr7_O?expires=1786536000&signature=83d93bde4f466d70c7744f6a32bcd0db43f9c108da0bc6052dd607619590372a&req=cCAuEsF2n4ZeFb4V1XW4gfsp%2BvsGMzUrR2hMjBp%2FE72bWCrUH5I7I0S80kHJ%0AkkNNSwqDqXimdSHYUodKsxJMww%3D%3D%0A)

Feito isso, você chegará à tela abaixo, onde deverá preencher a URL da sua API Focco ERP (explicado no item a seguir), bem como suas credenciais de acesso ao ERP e o Token para autorização nos endpoint’s dinâmicos do integrador.

![Imagem 3: Feito isso, você chegará à tela abaixo, onde deverá preencher a URL da sua API Focco ERP (explicado no item a seguir),…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1463451324/af8e343a2eab08c90b22664224ef/autorizacao-integracao-focco-ploomes.png?expires=1786536000&signature=c952073d48aacc0fe01c321a2919027fcf116558b72bcac09599fd537d1dee96&req=dSQhFc17nIJdXfMW3nq%2BgUzAMbgAhJDSvbKsAeNHvgoySDgcHGMcvjsGo3%2F5%0AHtEnyVwxCNe6slJS6uhmRmBpW%2F0%3D%0A)

## 3) URL da API Focco ERP

Para conseguir a URL da API Focco ERP, você precisa solicitar à equipe da Focco ou copiar a URL que você já utiliza para acessar o Focco ERP, como mostra a imagem abaixo (é preciso manter a barra (“/”) após o ".br"):

![Imagem 4: Para conseguir a URL da API Focco ERP, você precisa solicitar à equipe da Focco ou copiar a URL que você já utiliza…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488277/0bdef97f39b400ff7125506d/X0U0x1vid3du5hGz7W3eh36ni0qpsw2jMeMTJOgxa4mbpIgmr4EwifElV-TpkvAEpkp5T8ec-Cl7RVLHV4oi6slbqVBb5_9iKb2MA_hKdG3EJSvhSGZlfsoRoeY_aRePhVOc3J25?expires=1786536000&signature=85462fe5a60165c6939a261e822bb62f44dea88e23482c495132674cf28cfc6f&req=cCAuEsF2n4ZYFb4V1XW4gYpK9ykBHQEK4tMNQavU4CzJ5l0kBNq4PLqGt9EM%0A6exTUkuLA%2F0a75KBQ13szb7aAw%3D%3D%0A)

## 4) URLs de importação

Para criar as URLs de importação, é necessário seguir os passos abaixo:

1. Acesse sua conta Focco;
2. No Menu de Programas, pesquise por “FINT0200”;
3. Clique em “Cadastro de Programas do Integrador”:

   ![Imagem 5: Clique em “Cadastro de Programas do Integrador”:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/423476418/c875ce73ca40ee6e112bb972/w-5K-PyB77EBAYER93zK82WtLY3Zry9G9kU2vIRRor6zWYJjfHqo9D60Jhng8P5sQh9B5FxYsd3r1_Ya27UYAhSieZoMHAfam2U9YoHm_Odnm_5Nqcb-WCx76RW9juv6JlAQu2lH?expires=1786536000&signature=c2da1c972ac8808ac181cfbf98df2cb159229b6f99df9d1162e0d841ec9580c2&req=cCIkEs54mYBXFb4V1XW4gY%2Fbm%2FVHR3C4Vm4kfc61Zh57pGrLSCE%2BKhADnjI4%0ApKnIR1%2BeVYlVAclRfjmvohaMOw%3D%3D%0A)
4. Dentro da janela que se abrir (exemplificada abaixo), copie qualquer uma das opções da coluna “chave” que está destacada em vermelho. Guarde essa informação em um bloco de notas da seguinte maneira: ?chave=CHAVE\_COPIADA

   ![Imagem 6: Dentro da janela que se abrir (exemplificada abaixo), copie qualquer uma das opções da coluna “chave” que está…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/423476422/190407b0a3446d0bc52073bd/WP8I_kf7jYOeSi7t1hkRepb00Sp4ECCozVd2jft6Y7g0NhspHw0nuAUIvpgo0mhjmERckA-d55fqVk9z-qkEWswQWwHsiib47T59u1iqj6ZFACcy8kZQ9SzX7ZMi6MJW9mCT-fub?expires=1786536000&signature=21c0bcd5994a7ef3f6957572e971361ad63159e9706cf47e10334b7726879359&req=cCIkEs54mYNdFb4V1XW4gY6jwiVvfkS51YvvOxSvbm4AO23fXA%2BjV%2Fn2P7pw%0A0srgvSS80PgkAng8xvaeTJbZvg%3D%3D%0A)
5. Volte ao Focco e pesquise no Menu de Programa por “FINT0202”. Em seguida, clique em “Cadastro de Processo de Exportação”:

   ![Imagem 7: Volte ao Focco e pesquise no Menu de Programa por “FINT0202”. Em seguida, clique em “Cadastro de Processo de…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/423476425/9ae58b3d79bba3eacc70890a/mED15MJQ7_YG-TQd-C2NHkDAJHkUoAjZjws6a2rQUJoOQrrbsDqsNgLjMpOZYkqBoNQia0o3O1PPnXFTaUCTj66mQrV0fLSDVFSt5z7GhBCM2M96SF_sSf65b4_lVAX3g2UdCDwE?expires=1786536000&signature=6f127543c75b5b3b0cad91ce0f0fa14a4a64dd88def4a22183b7f2996fb8ae90&req=cCIkEs54mYNaFb4V1XW4geIeOq83jx6SBE3XUDqFXNYH1XuPk8Qf2Q20ks6Q%0AEuueL8983kzqN0R3Z48UyTCJmA%3D%3D%0A)
6. Aqui, vamos criar os processos de exportações: (I) exportador dos pedidos criados até dois anos atrás, (II) exportador dos pedidos criados ou atualizados no dia corrente, (III) exportador de clientes e (IV) exportador de produtos:

   1. Exportador (I):

      1. No campo **Mnemônico**, insira o nome **VENDA**;
      2. No campo **Método**, escolha a opção API;
      3. No campo **Descrição**, você pode escrever o que preferir;
      4. No campo **Select**, insira o seguinte script:

```
select

ped.id

, ped.num_pedido

, est.cli_id

, cli.cod_cli

, est.CNPJ

, est.cpf

, est.descricao

, to_char(ped.dt_emis,'dd/mm/rrrr') dt_emis

     , to_char(ped.modified_on,'dd/mm/rrrr') dt_mod

from tpedidos_venda ped

inner join testabelecimentos est on (ped.est_id_fat = est.id)

left join tclientes cli on (est.cli_id = cli.ID)

where ped.dt_emis >= TRUNC(SYSDATE)-730
```

v. Clique em **Salvar**;

vi. Clique em **Validar SQL**;

vii. Com tudo certo, clique em **Ativo**;

viii. Clique em **Salvar**.

![Imagem 8: viii. Clique em Salvar .](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/423476427/a892e97d628b369967bc033e/mED15MJQ7_YG-TQd-C2NHkDAJHkUoAjZjws6a2rQUJoOQrrbsDqsNgLjMpOZYkqBoNQia0o3O1PPnXFTaUCTj66mQrV0fLSDVFSt5z7GhBCM2M96SF_sSf65b4_lVAX3g2UdCDwE?expires=1786536000&signature=083cef3ac3733d36258d87fdd13ee37d183045d141ae88627011172588078e12&req=cCIkEs54mYNYFb4V1XW4gQnSSjEsy1vs8F4txfWfVkQ7%2F7zUqLzpoC62LraY%0A87DUi61dqohuLdgMluAZ7SEDRQ%3D%3D%0A)

ix. Agora, copie o texto contido no campo GET, junte com o que foi gerado no **item 4** (?chave=CHAVE\_COPIADA)**,** removendo a primeira barra (“/”) e salve em um bloco de notas. Esta será sua **URL de Importação do Ploomes de pedidos de vendas**. O resultado final será algo assim: /FoccoIntegrador/api/v1/Exportacao/venda?chave=CHAVE\_COPIADA

x. Após concluídas as etapas acima, clique em **Cancelar**;

b. Exportador (II):

i. No campo **Mnemônico,** insira o nome **VENDA\_DIARIA**;

ii. No campo **Select**, insira o seguinte script:

```
select
	ped.id
	, ped.num_pedido
	, est.cli_id
	, cli.cod_cli
	, est.CNPJ
	, est.cpf
	, est.descricao
	, to_char(ped.dt_emis,'dd/mm/rrrr') dt_emis
    	, to_char(ped.modified_on,'dd/mm/rrrr') dt_mod
from tpedidos_venda ped
inner join testabelecimentos est on (ped.est_id_fat = est.id)
left join tclientes cli on (est.cli_id = cli.ID)
where ped.dt_emis >= TRUNC(SYSDATE)-730
```

c. Repita os passos "v" a "ix" do Exportador (I). Esta será sua **URL de Importação do Ploomes de pedidos de vendas do dia**. O resultado final será algo assim: /FoccoIntegrador/api/v1/Exportacao/venda\_diaria?chave=CHAVE\_COPIADA

![Imagem 9: c. Repita os passos "v" a "ix" do Exportador (I). Esta será sua URL de Importação do Ploomes de pedidos de vendas do…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/423487963/687221b51f5a95ec4e24dfb8/08yZQT0Yd_eCsGKCxytBjAdyuIGsmE02vxpNogUVNBKY0A8zBkMSMQKshDJ8thKNu63rEB_InIX14uK_j7U5TTT66yeXzUEy25Ta_OUyvpph7FfUpjHgQ_QLYk33J_QFn0xP6I57?expires=1786536000&signature=4fda0e73093b8c9674045e516838f630cbbae937a424e7b025316418e8d95e50&req=cCIkEsF5lIdcFb4V1XW4gUDsJ%2BsHLFLziG%2BNkTTHfX1ULtLSbJOAK%2BnzodQn%0ArGqSA4upkxycMdNQm3G3D92%2BfQ%3D%3D%0A)

d. Após concluídas as etapas acima, clique em **Cancelar;**

7. Exportador (III):

a. No campo **Mnemônico**, insira o nome **CLIENTE**;

b. No campo **Select**, insira o seguinte script:

```
select

est.cli_id

, cli.cod_cli

, est.CNPJ

, est.cpf

, est.descricao

     , to_char(est.dt_cad,'dd/mm/rrrr') dt_cad

from testabelecimentos est

inner join tclientes cli on (est.cli_id = cli.ID)
```

c. Repita os passos "v" a "ix" do Exportador (I). Esta será sua **URL de Importação do Ploomes de clientes**. O resultado final será algo assim: /FoccoIntegrador/api/v1/Exportacao/cliente?chave=CHAVE\_COPIADA

![Imagem 10: c. Repita os passos "v" a "ix" do Exportador (I). Esta será sua URL de Importação do Ploomes de clientes . O resultado…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/423476433/6547631e4530d6e7222bd95b/g38w9OwUDu8uDktiZwU1F8gRB4MkVk13XvVcln-xCTPD0QA00QA-xp7f4y1o8xCeHvebTKuxiJ8iWBySoUjhnCrR-F_6Dp7bcqayA4OjuAUTAHkWORFykMpyJrIlJW2AjzQuaDF3?expires=1786536000&signature=3527837470a9b0a853982bbf6af9c02d33621cd4d77cb0f7c2f2d99bde98e792&req=cCIkEs54mYJcFb4V1XW4gQLAOGHYydvWLnhi1miGdNtbyta7g90i1tN%2Fe1Qb%0Az37lIbjYriU2pfrfWryiCIC17g%3D%3D%0A)

d. Após concluídas as etapas acima, clique em **Cancelar;**

8. Exportador (IV):

a. No campo **Mnemônico**, insira o nome **PRODUTO**;

b. No campo **Select**, use o seguinte script:

```
select

it.id,

    it.cod_item,

     it.desc_tecnica,

ctb_clas.descricao

from titens it

inner join  titens_empr itempr on (it.id = itempr.item_id)

inner join titens_contabil ctb on (itempr.id = ctb.itempr_id)

inner join tgrp_clas_ite ctb_clas  on (ctb.grp_clas_id = ctb_clas.id)
```

c. Repita os passos "v" a "ix" do Exportador (I). Esta será sua **URL de Importação do Ploomes de produtos**. O resultado final será algo assim: /FoccoIntegrador/api/v1/Exportacao/produto?chave=CHAVE\_COPIADA

![Imagem 11: c. Repita os passos "v" a "ix" do Exportador (I). Esta será sua URL de Importação do Ploomes de produtos . O resultado…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/423476437/5974781b9441a9a8b779c4ef/KYqWJdMhj25J6HKNPc0nTLLDgfVydbjCx6MmcvP4kJp6ILigJBxX33UG76u9anwePoU-s6xksTzWc76uthgWh4E_UzqGWw8Viy-BHU_yEZfmkSz1KhXsMLwrJ5ll3jqlfMcN4X8U?expires=1786536000&signature=5855ea93bc7a02fee92e3f97f6873a61a793122aa575545b35499a75a1d5d03e&req=cCIkEs54mYJYFb4V1XW4gZNQULhXILgOmqD5GJ1DaHHP1XZQVILfY2ljrYkU%0AL7ulZS0k34mtB4X5BIZMl%2FrUhA%3D%3D%0A)

9. Agora, copie e cole as URLs de Importação do Ploomes para seus respectivos campos na configuração da integração dentro da interface do Ploomes. O Exportador (II), relacionado aos pedidos de venda do dia, não precisará ser copiado no Ploomes, já que nossa integração o utilizará de outra forma. A imagem abaixo mostra um exemplo de como as informações devem aparecer no Ploomes:

![Imagem 12: 9. Agora, copie e cole as URLs de Importação do Ploomes para seus respectivos campos na configuração da integração…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/423487968/ac39241d3841128cff6bece9/_Sp1pVwnoc5DMm9yuNEe1z4oOzm8C8Tqyk8lKAJhm6zZt72LD2Pl3PlBQSPGDc5K2eHIBZtkm1vH8IdFD2geq-6X0waXn2VCywQzRZUhPYrMxYfUPR9m7TtOLpX2zNeZycgm0Ycu?expires=1786536000&signature=b7d613368c614644e4d840b9f0c3573e5ee2424416e38162b21832e4582876c6&req=cCIkEsF5lIdXFb4V1XW4gavnfz8rHK%2FKzpBqXpUNeMj5I2caZDSVHZqe66uC%0Ath1dcw1l9MP%2Fwm6tJf2H%2BEe%2B9A%3D%3D%0A)

## 5) Importação de pedidos dos últimos dois anos

Caso deseje trazer ao Ploomes o histórico de pedidos do Focco dos últimos dois anos, você deve marcar o campo abaixo como na imagem:

![Imagem 13: Caso deseje trazer ao Ploomes o histórico de pedidos do Focco dos últimos dois anos, você deve marcar o campo abaixo…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488280/e28a8bf589249f6debfbcece/CRJFUn3C_GrL6nff2TTQsi12ra7nqwBOhPnoW_Luvo1vxVyexgObu3ILjdIyn7TuPa9aJ2ToK_n10v4enjRvVLiRNrQr9la1ANGpr73ECxZMeMxVoEFtd4DV3TC59n-6bUHNP3Zg?expires=1786536000&signature=7dc44bd71ce07a111b773458d572304d847a455c934f29cd74dcb7cc2ad3ec74&req=cCAuEsF2n4lfFb4V1XW4gY4ZTeukv55iwjHwTUmoC7wps%2BKfkxaQAQQr4Otj%0AETdVeyj1VsPuyiFl%2B0Y4ZN8%2FOg%3D%3D%0A)

## 6) Importação de produtos

Como produtos podem existir em grande volume, você deverá puxar produtos e suas atualizações do Focco ao Ploomes sob demanda. Para isso, será necessário clicar no botão da imagem abaixo, localizado dentro da tela de Configurações da Integração.

![Imagem 14: Como produtos podem existir em grande volume, você deverá puxar produtos e suas atualizações do Focco ao Ploomes sob…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488290/4a7716adcecd9b0df5e54a78/yhwvggUIlO9mlQN-8wIoYIPFzHJvsw9ulKVyGRKzLwt9XHRfhe0X7-kHQKIVY5uok9ScbodhjlBHsdqll3h6zku-TMGNX5QXJalL5X6t1R0Jd4bGyMqCEpFcGGA2abULHUR7z8I-?expires=1786536000&signature=737006b66c676d3e48bf4142679ded59ad84c0fbdeeb8624c2317ac5bf57924c&req=cCAuEsF2n4hfFb4V1XW4gfySy6koUqbgClrqgJ6gVkC2G6lGPRXo1iAJm4wm%0ACCd%2B6zwPgGphtcuNH6BwaCdGJg%3D%3D%0A)

## 7) Mapeamento de campos

Para definir quais informações são trafegadas de um sistema ao outro (de acordo com o Mapa Geral da Integração) e em qual campo elas são armazenadas, basta escolher um campo na coluna Focco e o seu correspondente na coluna Ploomes.

![Imagem 15: Para definir quais informações são trafegadas de um sistema ao outro (de acordo com o Mapa Geral da Integração) e em…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488295/f595ddbb2ce8fe9e709fa8a6/d1nwrF66PCbVzKAbz9Frb4NUsUPKTOFseEuJ2kZzzNi-dFzyGdj9rW3aeeSHumr_F7oL5Em2LkAC9F8G16kECsQCZHMioB1GHdjGxJXKBV_udXRzdL9ehRfIfxeAyZdUsMwg5bC7?expires=1786536000&signature=77213612a72454328566fba3e40528555ddacd2a4502d8173cf3c1be2a0e98a7&req=cCAuEsF2n4haFb4V1XW4gSRiHr5wvKNY55L5bY5DnrNtlGrPmViqnUmxIPcs%0ALW9CfErWzaq7%2BPHOVYkznfLVNQ%3D%3D%0A)

## 8) Ativação da integração

Com todas as configurações acima finalizadas, basta clicar em **Ativar Integração**.

![Imagem 16: Com todas as configurações acima finalizadas, basta clicar em Ativar Integração .](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488298/e9bffabb49277ad2edbea45b/CKFrVEnPAd1aarVYc87qPGfK0O16PPR9Nf_HHnvw_qht3TXgN6hZk0oFLegn1MIBS7LU8NYEThCd38siP0E8yqliQkIjeyvPBshvKq8x5EnlNkcOc6AfyeYFOtWqkCyxPHh0mkI6?expires=1786536000&signature=d849c0fc086519f221eb12d8a3daf4e0bf235003bf917415928c990d0b2df08d&req=cCAuEsF2n4hXFb4V1XW4geST%2BhFpa9VhBzRIOSt0FE6Dia0lVxHH39pjN81%2F%0AhiCykMwFwrxlPlPMSwge2Z70%2Bw%3D%3D%0A)

Obs: Neste momento, todos os clientes, pedidos de venda (se a opção for ativada), tipos de pagamento e status de pedido serão replicados do Focco ERP para o Ploomes.

## 9) Consulta a estoque, em tempo real, por campo de fórmulas externas

Quando você ativa a integração, uma URL é gerada automaticamente na parte inferior da tela de configurações da integração do Ploomes, como mostra a imagem abaixo:

![Imagem 17: Quando você ativa a integração, uma URL é gerada automaticamente na parte inferior da tela de configurações da…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488303/144774015ed1884e6d281e32/Puot_dk05ePV7iG9lU7q6pP1k4-S4nNS0AESvhx1qMdFjAFM_3QzcJTBMwm5VhC-Ba4jqCBCmdSjp7RGsjqulDEO0tFECD6skkbLzk_rlXme3Lut-6KjAqkS7TzezEfXQs7undxZ?expires=1786536000&signature=0599576f50a69f641912e49eb6a8587a83767a2beeaa6d7adc0067f06d806f04&req=cCAuEsF2noFcFb4V1XW4gXvpUU%2FSzG6JNdAGecfVurnhrnS3NNQnwbCOXsIL%0Ajg9s5aDeWoDb6pAGsCQd5oys2g%3D%3D%0A)

Com esta URL, você pode criar um novo campo de produto de proposta, produto de venda ou produto de documento, e seguir os passos abaixo para configurá-lo para puxar, em tempo real, a disponibilidade em estoque de um determinado produto no Focco ERP:

![Imagem 18: Com esta URL, você pode criar um novo campo de produto de proposta, produto de venda ou produto de documento, e seguir…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/409488307/d23831f2a7fe1afe6d06753c/78WP852XgqYM7gPIVStp02JfSMrTyf1MqWaX039FrLIeGt5TS4fzTxdZxidlE7wQnlMVCot8P1L-e0FGQMycHqLpEvdP61VXRV7dKrkkMx1jKhqhCxLqVnW8foyf3yaPUG_6X0hB?expires=1786536000&signature=ab9dc370dfbf9602d930526b01fb45a434ab7048b50d3c10479c625a45c80622&req=cCAuEsF2noFYFb4V1XW4geqct7E4MeZVX2ZFPCbKtZ%2B%2Bcq1WZdztmk%2BKx7EH%0AY2b%2FpR1WL3Dhi7JRViVYCHeqNg%3D%3D%0A)
