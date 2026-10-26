---
id: "37670535404567"
titulo: "Como controlar estoque de produtos com grades"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37670535404567-Como-controlar-estoque-de-produtos-com-grades"
trilha: "Universidade Sankhya > Jornada de Estoques"
atualizado_em: "2026-07-22T14:11:07Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Grade de Produtos", "Sankhya"]
---

# Como controlar estoque de produtos com grades

| Categoria |
| --- |
| [Qual é o objetivo do controle de estoque por grade?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670535404567-Como-controlar-estoque-de-produtos-com-grades#h_01KEYKR051KNPF826VTECB7K8F) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670535404567-Como-controlar-estoque-de-produtos-com-grades#h_01KEYKQD3ZXYCZNVB8XZB8HE30) |
| [Quais os riscos de não se fazer o controle de estoques por grade?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670535404567-Como-controlar-estoque-de-produtos-com-grades#h_01KEYKPYEA5YJSKX5E2NN9PPMX) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670535404567-Como-controlar-estoque-de-produtos-com-grades#h_01KFBTGYE8YMJWNN5X3K37F317) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670535404567-Como-controlar-estoque-de-produtos-com-grades#h_01KEYKPJACM3VPD6H62XRZ6HKP) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670535404567-Como-controlar-estoque-de-produtos-com-grades#h_01KEYKP0N3SFWFJK7YFQMXKKM9) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670535404567-Como-controlar-estoque-de-produtos-com-grades#h_01KEYKMVTFYF54WGCVQXQ14PRD) |

## Controle de estoque por grade

#### Qual é o objetivo do controle de estoque por grade?

O controle de estoque por grade visa organizar e gerenciar produtos com variações específicas, como numeração, cor ou tamanho, de forma estruturada e eficiente. Essa prática simplifica a gestão, aumenta a precisão no controle, facilita as reposições, otimiza o atendimento ao cliente e apoia estratégias de vendas para oferecer visibilidade sobre o desempenho de cada categoria. 

#### Quais problemas este recurso resolve?

- **Desorganização no estoque**, dificultando a visualização e separação dos itens corretos.
- **Erros na separação de pedidos**, gerando trocas e insatisfação dos clientes.
- **Planejamento ineficiente de compras e reposições**, por falta de dados detalhados por variação.
- **Dificuldade em acompanhar tendências e preferências de consumo,** limitando a capacidade de resposta ao mercado.
- **Promoções mal direcionadas**, por falta de visibilidade sobre o desempenho de cada grade.

#### Quais os riscos de não se fazer o controle de estoques por grade?

A ausência de controle por grade compromete a eficiência na gestão de produtos com variações específicas, como tamanhos ou cores. Isso dificulta a localização dos itens, aumenta o tempo de separação e os custos operacionais, além de elevar a chance de erros nos pedidos e devoluções. A falta de visibilidade sobre o giro de cada variação pode gerar acúmulo de itens com baixa saída e ruptura nos mais procurados, impactando diretamente a satisfação do cliente. Sem esses dados, o planejamento de compras se torna impreciso, prejudicando ações promocionais, reduzindo a rentabilidade e limitando a capacidade da empresa de responder às mudanças do mercado, o que afeta sua competitividade e eficiência logística.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052353122)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Uma empresa que atua no comércio de produtos com variações específicas de tamanho e cor recebeu uma nova remessa de itens para seu estoque. Cada item possui diferentes tamanhos e cores disponíveis para venda. Para garantir o controle eficiente dessas variações e agilizar o atendimento aos clientes, é necessário cadastrar o novo produto no ERP, utilizando o recurso de controle por grade para organizar as combinações de tamanho e cor.

**Tarefa:** Realize o cadastro de um produto  no ERP Sankhya, garantindo a organização e controle adequado das variações de tamanho e cor.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Modelo de Grade**
   Menu: Comercial » Consulta

- Clique no botão **Cadastrar Configurações Grade de Produtos(+)**
- Informe a descrição da grade
- E defina se será utilizado ou não máscara para o campo controle. Isso dita se o campo controle será apresentado com outra descrição na central de notas.
- Na aba **Dimensões**, inclua os tipos de controles que serão utilizados. Nesse exemplo, tamanho e cor.
- Na aba **Variações**, inclua as variações de cada dimensão configurada. Nesse exemplo, os tamanhos disponíveis para dimensão tamanho e as cores disponíveis para a dimensão cor.

2. Acesse a tela **Produtos**
   Menu: Configurações » Cadastros » Produtos

- Selecione o produto utilizado para esse cenário
- Na aba **Medidas e Estoques**, sub-aba **Controle Adicional**, selecione no campo **Controlar por** a opção **Grade** e indique o modelo de grade criado anteriormente no campo **Modelo de Grade.**
- Salve as configurações.
- Valide no botão **Grade do Produto**, as informações do modelo de grade e defina uma quantidade mínima de compra para cada variação do produto.

3. **Registro da movimentação**

- Acesse a tela **Portal de Compras**
  Menu: Comercial » Consulta
- No campo **Tipo de Movimento**, selecione **Nota de Compra**.
- No botão **Novo (+)**, selecione **TOP - COMPRA - REVENDA**.
- Clique duas vezes para iniciar o lançamento da **Nota de Compra**, redirecionando para a **Central de Compras**.

  **Preencher o Cabeçalho da Nota de compra**

      Na **Central de Compras**, preencha os seguintes campos obrigatórios:

- **Empresa**: Selecione a empresa responsável.
- **Parceiro**: Informe o fornecedor.
- **Tipo de Operação**: Escolha **Nota de Compra**.
- **Tipo de Negociação**: Informe a modalidade de negociação.
- **Natureza**: Preencha, se necessário.
- **Centro de Resultado (CR)**: Informe, se necessário.
- **Série Nota**: Informe **1**.
- **Número Nota**: Informe **10**.
- **Chave NFe**: Insira uma chave fictícia com 44 dígitos.
- Clique em **Salvar**.

  **Preencher o Painel de Itens**

No **painel de itens**, insira as seguintes informações obrigatórias:

- **Produto**: Cabos de rede.
- Clique no botão **Grade** para visualizar os registros cadastrados com suas respectivas quantidades mínimas de compra.
- Clique no botão **Modo Grade** para melhor visualização dos itens que foram incluídos referente a grade.
- **Local**: Informe o local.
- **Quantidade**: A quantidade é carregada automaticamente conforme a quantidade mínima definida na grade, mas pode ser alterada para mais caso necessário.
- **Valor Unitário**: Informe o valor acordado caso não exista custo definido para este produto.
- Clique em **Salvar**.

4. **Validação Final**

- Confira se os itens foram lançados nas quantidades corretas para cada tamanho cor;
- Para confirmar essa nota de compra clique no botão **Confirmar** no topo da tela;

#### Correção e Repetição

- Revise os registros para confirmar se as operações foram concluídas.
- Cadastre novas grades e faça os devidos vínculos.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo, retorne no vídeo demonstrativo novamente caso necessário.
