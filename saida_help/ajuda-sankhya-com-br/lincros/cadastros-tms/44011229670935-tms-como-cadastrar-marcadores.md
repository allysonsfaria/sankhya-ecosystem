---
id: "44011229670935"
titulo: "[TMS] - Como cadastrar Marcadores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011229670935--TMS-Como-cadastrar-Marcadores"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:59:03Z"
rotulos: ["sync_hc", "lincros", "lincros_13438934", "sync_hash_f46692217c56"]
---

# [TMS] - Como cadastrar Marcadores

**Menu**: Cadastros gerais  > Configurações da empresa > Marcadores

**Objetivo**: Como realizar o cadastro de marcadores

**Considerações**:

- Possuir permissão de acesso nas configurações da empresa;

**Contexto**:

Marcador é um recurso dentro do TMS que permite a segmentação de determinadas informações dentro do sistema. É possível utilizá-lo para identificar clientes, centros de custo, ressaltar ações a serem tomadas e pode inclusive ser utilizado para trazer tabelas de frete específicas conforme a negociação.

Para exemplificar: O conhecimento possui um marcador XYZ, e existem 3 tabelas de frete da determinada transportadora que atendem aquela rota. Caso alguma das tabelas possua o marcador XYZ, então esta será a tabela buscada para cálculo.

Caso nenhuma das tabelas possua o marcador, a busca trará qualquer uma das tabelas (Exceto se a opção Menor valor estiver marcada no cadastro da Transportadora empresa, então trará a de menor valor).

É importante ressaltar que o marcador serve como um ‘agrupador’ de informações, e não deve ser confundido com as restrições de busca da tabela de frete.

---

## Entenda como criar:

[Como cadastrar um marcador](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011229670935--TMS-Como-cadastrar-Marcadores#cadastrar-marcador)

[Como cadastrar um marcador Anymarket](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011229670935--TMS-Como-cadastrar-Marcadores#marcador-anymarket)

---

## Como cadastrar um marcador

Para cadastrar um marcador, é preciso acessar no TMS o menu Cadastros gerais  > Configurações da empresa > Marcadores e clicar em “Novo”:

![Imagem 1: Para cadastrar um marcador, é preciso acessar no TMS o menu Cadastros gerais > Configurações da empresa > Marcadores e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011229812759)

![Imagem 2: Para cadastrar um marcador, é preciso acessar no TMS o menu Cadastros gerais > Configurações da empresa > Marcadores e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011237357207)

**Código**: É o código que você irá utilizar para identificar aquele marcador, é o que aparecerá visualmente em tela. Exemplo: ECM

**Descrição**: É identificação que será utilizada para ‘chamar’ esse marcador, ou seja, o nome dele. Exemplo: E-commerce.

A **classificação** é uma funcionalidade desenvolvida para alguns determinados clientes que desenvolveram um relatório diferenciado, cujo marcador é trazido em colunas específicas, sendo estas as colunas de classificação do marcador. Portanto, para os demais clientes, essa informação não precisa ser selecionada.

Em seguida, as cores de texto e fundo são referências visuais para o marcador.

Na sessão de restrições, é necessário informar em quais partes da plataforma será possível incluir o marcador. Por exemplo, um marcador que serve para identificar tabela de frete de E-commerce não precisa ser colocado como disponível para “pendências”.

Por fim, as **faixas** servem para identificar se o marcador compreende apenas algum tipo de faixa. Por exemplo:

Marcador E-commerce 1 - De 0kg à 10Kgs.

Marcador E-commerce 2 - De 10,01Kgs à 20Kg, etc.

**Obs.:** Esse campo é apenas informativo, portanto, além de não ser de cadastro obrigatório, ele não atua como restritivo ou executa qualquer função.

![Imagem 3: Obs.: Esse campo é apenas informativo, portanto, além de não ser de cadastro obrigatório, ele não atua como restritivo…](https://ajuda.sankhya.com.br/hc/article_attachments/44011277515671)

---

## Como cadastrar um marcador Anymarket

- O Marcador Anymarket serve para que o Anymarket consiga localizar aquela negociação e apresentá-la dentro da plataforma de e-commerce utilizada pelo cliente Lincros.
- Os preenchimentos obrigatórios para o correto funcionamento do marcador são:

1 - **Descrição:** deve ser obrigatoriamente NORMAL ou EXPRESSA

      - O Anymarket só consegue receber esses 2 valores de marcadores. Em caso de grafia incorreta, as tabelas com esse marcador não serão localizadas e consequentemente exibidas pelo Anymarket.

2 - **Restrição:** Tabela de Frete

![Imagem 4: 2 - Restrição: Tabela de Frete](https://ajuda.sankhya.com.br/hc/article_attachments/44011237746967)

![Imagem 5: 2 - Restrição: Tabela de Frete](https://ajuda.sankhya.com.br/hc/article_attachments/44011277760919)

O restante dos campos podem ficar sem preenchimento. Não esqueça de salvar a criação dos marcadores.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
