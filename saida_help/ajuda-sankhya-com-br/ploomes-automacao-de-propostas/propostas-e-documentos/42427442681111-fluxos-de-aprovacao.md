---
id: "42427442681111"
titulo: "Fluxos de aprovação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427442681111-Fluxos-de-aprova%C3%A7%C3%A3o"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-10T18:03:10Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452296", "sync_hash_1cdfcfb76d94"]
---

# Fluxos de aprovação

As **regras de negócio** definem como uma empresa funciona e refletem suas políticas internas, processos e diretrizes de operação.

O Ploomes permite internalizar essas regras de negócio, ou seja, incorporá-las diretamente na plataforma. Dessa forma, é possível garantir que os processos de venda sejam executados de acordo com as regras e padrões definidos pela empresa.

## Como fazer?

- Acesse **Administração > Fluxos de aprovação**;
- Selecione a entidade desejada (**Proposta**, **Venda** ou **Documento**);
- Clique em **Novo fluxo de aprovação**.

![Imagem 1: Clique em Novo fluxo de aprovação .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148891851/0a79586201a1cd022f0a59407e17/image.png?expires=1786536000&signature=4488da50eccfa101946d31ab07311ec881674cb3a866e210c32db10b19ab05f8&req=diEjHsF3nIlaWPMW3nq%2BgUwYhkOSzpDbraRPnfWxAogfWI7P3E%2BPoV2rpvY8%0Al%2FUulrK7jBiAddsfNqtmW1odNAE%3D%0A)

Na tela que se abrir, é possível definir o **nome do fluxo**, os **filtros** e o que acontece em cada caso. As opções de Resultado são:

- **Bloqueio** – impede que a proposta seja criada caso a regra seja quebrada;
- **Aprovação** – dispara um fluxo de aprovação para um determinado grupo de pessoas quando a regra for quebrada. Os envolvidos poderão aprovar ou reprovar a proposta, além de adicionar comentários sobre a decisão;
- **Alerta** – o vendedor será alertado de que algo está fora dos padrões, mas a proposta poderá ser gerada normalmente.

## Primeiro exemplo:

Como primeiro exemplo, vamos criar uma regra onde, **quando o produto da proposta for “Cama”, não será permitido conceder descontos maiores que 10%**.

- Selecione a entidade **Proposta** e clique em **Novo fluxo de aprovação**;
- Defina o **título do fluxo de aprovação**;
- Como filtro, adicione:

  - **Produtos da proposta > Produto > Igual a > Cama**;
  - **Produtos da proposta > Desconto > Maior que > 10**;
- Adicione um **aviso**, caso deseje;
- Selecione a opção **Bloqueio**.

[GIF animado: Imagem 2: Selecione a opção Bloqueio .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2149048273/e18cafa8a87c23241eeb8e3bc1c7/fluxo.gif?expires=1786536000&signature=95e630e51e3645f50b673dccc0ce885e5fd0b3cd602962c59a7d030e6217f338&req=diEjH8l6lYNYWvMW3nq%2BgbPEzafVEDNvuyZzAv%2BarEh%2B4URaTzQ2g4ursBNe%0APt5U6Z%2BO6tSOxyAzCvJxB%2Bk%2B1eE%3D%0A)

Quando uma proposta for gerada com essas condições, será exibido um **aviso de bloqueio**, impedindo a criação ou edição da proposta.

![Imagem 3: Quando uma proposta for gerada com essas condições, será exibido um aviso de bloqueio , impedindo a criação ou edição…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2152072824/0b2463629280549a03ab0340fe24/image.png?expires=1786536000&signature=9bcea1671b304cca281aca4e94384e09b86cafac6bbb3e8f155c509459d5d7d3&req=diEiFMl5n4ldXfMW3nq%2BgYeCqZtOfBLPF6HgEt58U7mmSZb5drpOcosxWc0C%0AGsuL%2FpmyNnkqzVXP%2FkJeW4hN8SM%3D%0A)

## Segundo exemplo:

Como segundo exemplo, quando o **desconto da proposta** for **maior que 15%** e o **cliente** for do estado do **Rio de Janeiro**, será disparado um fluxo de aprovação para o usuário **“Suporte Ploomes”**.

- Selecione a entidade **Proposta** e clique em **Novo fluxo de aprovação**;
- Defina o **título do fluxo de aprovação**;
- Como filtro, adicione:

  - **Desconto > Maior que > 15**;
  - **Cliente > Estado > Igual a > Rio de Janeiro**;
- Adicione um **aviso**, caso deseje;
- Busque pelo usuário e clique em **Adicionar.**

[GIF animado: Imagem 4: Busque pelo usuário e clique em Adicionar.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2151830351/be07fe16f0d755ca7516c8fb6980/aprovacao.gif?expires=1786536000&signature=6cc3e6cc13237492886721e554269e54c717062aa489bfa460ed4d30ece1ce99&req=diEiF8F9nYJaWPMW3nq%2BgZzjIUmnlNCRYKsARSCQxIj%2FGw0WbLoddiYi0V0i%0A3wVXk5xEdCwjgGC4kXOykWnqaFI%3D%0A)

Ao tentar criar uma proposta com essas condições, será exibido o seguinte alerta:

![Imagem 5: Ao tentar criar uma proposta com essas condições, será exibido o seguinte alerta:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2151887587/f5f47a22dacc3f8ed2fd9a48a04d/image.png?expires=1786536000&signature=633b856ab151b5f465a179f3dec8b162185fd597449be7bfa0e0a7ed95cdc702&req=diEiF8F2moRXXvMW3nq%2BgX6rh%2FB552s7oKxcQT0ZIRTOBUnJVAtSjM5Xn8%2FF%0AWZkPVcAv7%2BE4U3Olw1zuqdwtbz8%3D%0A)

Quando a proposta for enviada para aprovação, os usuários envolvidos serão notificados. Ao clicar no alerta, o usuário será direcionado para a página da proposta, onde poderá **Aprovar** ou **Recusar** a solicitação, além de adicionar um **comentário** visível para todos os envolvidos no fluxo de aprovação.

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 6: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1385600924/79f6a151ea52d3d30f94fb6e7844/Automa-C3-A7-C3-A3o%2Bde%2BPropostas%2Be%2BDocumentos.png?expires=1786536000&signature=1205a69ca4e23485f5bac2f03c8bcd5886c98cf896d82c8266f003e13531eecb&req=dSMvE89%2BnYhdXfMW3nq%2BgX5I48lkycX2UVnDfpCPp4H4nZQ6leN%2FxYZ%2BD379%0AXwZkaYUQcFRw1QpTZSaSXhwVnEE%3D%0A)](https://universidade.ploomes.com/courses/trilha-adm-passo5-automacao-de-propostas-e-documentos)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
