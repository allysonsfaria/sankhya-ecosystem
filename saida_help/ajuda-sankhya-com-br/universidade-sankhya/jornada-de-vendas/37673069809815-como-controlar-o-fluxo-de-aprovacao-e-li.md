---
id: "37673069809815"
titulo: "Como controlar o fluxo de aprovação e liberar desconto por item da nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37673069809815-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-desconto-por-item-da-nota"
trilha: "Universidade Sankhya > Jornada de Vendas"
atualizado_em: "2026-07-22T14:10:54Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Liberação de Limites", "Desconto", "Financeiro"]
---

# Como controlar o fluxo de aprovação e liberar desconto por item da nota

| Categoria |
| --- |
| [O que é o evento 25 (Desconto por item da nota) e por que ele é importante?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673069809815-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-desconto-por-item-da-nota#h_01KEYQXJ6Y6ENMNCPQYB4FSJ5N) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673069809815-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-desconto-por-item-da-nota#h_01KEYQX0YKWCZFTSMY7A7BRJXG) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673069809815-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-desconto-por-item-da-nota#h_01KFBVHPS2AJJD3H8G4299ERSR) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673069809815-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-desconto-por-item-da-nota#h_01KEYQWJCT9F0FQZPZEN6HV8EP) |
| [Pronto para o próximo nível? Siga o passo a passo e conquiste seus objetivos com o ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673069809815-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-desconto-por-item-da-nota#h_01KEYQN4Q9ZNTV2Q4WDKFMTDQT) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673069809815-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-desconto-por-item-da-nota#h_01KEYQK5YSZSW59GWVHTQCTXSG) |

## Liberação do Evento 25 (Desconto por item da nota)

#### O que é o evento 25 (Desconto por item da nota) e por que ele é importante?

Quando o desconto aplicado a um item excede o limite permitido no cadastro do produto, é necessária a aprovação de um usuário autorizado. Esse processo é fundamental para garantir controle financeiro, conformidade com as políticas comerciais, rastreabilidade das aprovações e evitar prejuízos ou erros nas vendas.

![Imagem 1: Quando o desconto aplicado a um item excede o limite permitido no cadastro do produto, é necessária a aprovação de um…](https://ajuda.sankhya.com.br/hc/article_attachments/37673069804439)

O Evento 25 é acionado quando o preço unitário do item fica abaixo do mínimo permitido, calculado a partir da porcentagem de desconto máximo aplicada sobre o preço de tabela no cadastro do produto. Ou seja, sempre que o preço for inferior, o evento será acionado.

**Exemplo:** Se o preço de tabela é R$ 10,00 com 10% de desconto máximo, o preço mínimo permitido é R$ 9,00; assim, o Evento 25 será disparado sempre que o valor unitário final for inferior a esse limite. Isso se aplica inclusive a alterações manuais na Central de Vendas, onde o evento será acionado caso o preço resultante fique abaixo de R$ 9,00, independentemente de como o desconto foi inserido.

#### Quais problemas este recurso resolve?

- **Descontos concedidos acima do permitido:** comprometem a margem de lucro e geram perdas financeiras.
- **Descumprimento das políticas comerciais:** causa desvios nas condições de venda estabelecidas pela empresa.
- **Falta de rastreabilidade das aprovações:** dificulta a auditoria e o controle interno.
- **Aplicação indevida de descontos:** gera vendas fora dos limites definidos sem aprovação adequada.
- **Ausência de controle de autorizações:** permite exceções sem a devida responsabilidade definida.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1055293731)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis** possui uma política rigorosa de controle de descontos para proteger suas margens de lucro e garantir alinhamento com as estratégias comerciais. No cadastro dos produtos, o percentual de **% Desconto Máximo permitido é de 5%**. Durante uma negociação, o vendedor aplica um desconto de **12%**, excedendo o limite configurado.

**Tarefa:** Registre o pedido de venda e inclua o percentual de 12% no produto. Em seguida, efetue o procedimento de liberação exigido para que o pedido possa ser devidamente confirmado.

#### Pronto para o próximo nível? Siga o passo a passo e conquiste seus objetivos com o ERP Sankhya

1. Acesse a tela **“Produtos”**

Menu: Configurações » Cadastros » Produtos

- Selecione o produto desejado e execute um duplo clique sobre a opção correspondente.
- Na aba **“Venda”,** no campo: **“% Desconto Máximo”** (é definido o percentual máximo de desconto permitido para o produto no momento da venda).
- Clique no botão Salvar [**F7]** para registrar as informações.

2. Registre o pedido de venda assegurando a precisão das informações nos campos principais, com destaque para o percentual de desconto por item, que deve ser corretamente preenchido no campo “**% Desconto**".

- Certifique-se de se o **% Desconto Máximo** esteja configurado para o produto.

3. **Geração do evento 25**

- Ao tentar confirmar o pedido, o sistema detecta que o percentual de desconto no pedido foi excedido e gera o Evento 25 **(Desconto por item da nota).**

4. **Vincular o liberador**

- Um pop-up denominado **Liberações Solicitadas** será exibido.
- Informe o **usuário liberador** no campo designado.
- Marque a opção **Notificação** para informar o liberador sobre a necessidade de aprovação.
- Clicar no botão **Definir liberador**.
- A coluna **Nome (Liberador)** será automaticamente atualizada.
- Clique no botão “**Salvar** **Liberações”** para registrar a solicitação.

5. **Realizar a liberação**
   **A liberação pode ser feita de duas formas:**

- **Na Central de Vendas:** Clique no botão **"Liberações”.**
- **Na Tela Liberação de Limites:** Acesse diretamente esta tela, que possui o mesmo layout da Central de Vendas.
- Insira o **usuário e a senha** do liberador autorizado.
- No painel lateral, localize o pedido que apresenta o **Nro Único** e selecione-o.
- Clique em **Liberar**.
- Caso necessário, adicione uma observação justificando a liberação.

6. **Caso o usuário liberador esteja logado**

- Se o liberador já estiver logado no sistema, marque a opção **Sou Liberador** para agilizar o processo.

7. **Confirmar o pedido**

- Retorne à **Central de Vendas** e clique novamente em **Confirmar** para concluir o pedido.
- No **Portal de Vendas**, habilite o filtro **Liberação - Pendentes** para verificar que o pedido liberado já não aparece mais na lista.
- Limpe o filtro e realize uma nova busca pelo número do pedido para confirmar que ele foi processado corretamente.

#### Correção e Repetição

- **Verifique os dados:** Confirmar a configuração do campo “**% Desconto Máximo”** no cadastro do produto.
- **Valide o bloqueio:** Certifique-se de que o **%** percentual de desconto do produto excede o limite informado pelo vendedor.
- **Correção de  falhas:** Ajuste erros, como liberador incorreto, dados incompletos ou aplicação inadequada de limites.
- **Confirme a operação:** Verificar e corrigir as falhas, retorne na central de vendas e confirme a operação para que o pop-up **"Liberações Solicitadas"** apresente na tela, realize novamente a definição do liberador, garantindo que os campos estejam corretamente preenchidos e as permissões sejam respeitadas.
- **Pratique:** Simule outros cenários para reforçar o aprendizado da equipe.
