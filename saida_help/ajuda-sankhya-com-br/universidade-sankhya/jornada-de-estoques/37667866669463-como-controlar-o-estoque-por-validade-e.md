---
id: "37667866669463"
titulo: "Como controlar o estoque por validade e saída prioritária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37667866669463-Como-controlar-o-estoque-por-validade-e-sa%C3%ADda-priorit%C3%A1ria"
trilha: "Universidade Sankhya > Jornada de Estoques"
atualizado_em: "2026-07-22T14:11:13Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "Portal de Vendas", "Estoque", "FEFO"]
---

# Como controlar o estoque por validade e saída prioritária

| Categoria |
| --- |
| [Qual é o objetivo da priorização da saída de produtos pelo critério FEFO e qual sua importância?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37667866669463-Como-controlar-o-estoque-por-validade-e-sa%C3%ADda-priorit%C3%A1ria#h_01KEYEFQJA54VJRGR83GCPT692) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37667866669463-Como-controlar-o-estoque-por-validade-e-sa%C3%ADda-priorit%C3%A1ria#h_01KEYEFA2T8XDPK8JWHAF81N2D) |
| [Quais os riscos de não utilizar a priorização da saída de produtos pelo critério?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37667866669463-Como-controlar-o-estoque-por-validade-e-sa%C3%ADda-priorit%C3%A1ria#h_01KEYEEV8QRKWMERWQ5NZYHV6R) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37667866669463-Como-controlar-o-estoque-por-validade-e-sa%C3%ADda-priorit%C3%A1ria#h_01KFBT1WQNHZ0M4PNWM01KQNWZ) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37667866669463-Como-controlar-o-estoque-por-validade-e-sa%C3%ADda-priorit%C3%A1ria#h_01KEYEEF1KGSH39PN200DG4PSZ) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37667866669463-Como-controlar-o-estoque-por-validade-e-sa%C3%ADda-priorit%C3%A1ria#h_01KEYEDMNTZBNDC0H351AWBT02) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37667866669463-Como-controlar-o-estoque-por-validade-e-sa%C3%ADda-priorit%C3%A1ria#h_01KEYEACG2B0RPAK73V1RZCS1A) |

## Priorização da saída de produtos pelo critério FEFO

#### Qual é o objetivo da priorização da saída de produtos pelo critério FEFO e qual sua importância?

O objetivo da priorização da saída de produtos pelo critério FEFO (First Expired, First Out) é garantir que os itens com a data de validade mais próxima sejam consumidos ou vendidos primeiro, reduzindo perdas e evitando desperdícios. Sua importância está na otimização da gestão de estoque, garantindo conformidade com normas sanitárias, preservação da qualidade dos produtos, redução de prejuízos financeiros e maior eficiência operacional na logística de armazenagem e distribuição.

#### Quais problemas este recurso resolve?

- **Redução de perdas por vencimento**: Prioriza a saída de produtos com validade mais próxima, evitando desperdício.
- **Preservação da qualidade**: Garante que os clientes recebam itens dentro do prazo e em boas condições.
- **Otimização da gestão de estoque**: Facilita o controle de lotes e evita acúmulo de produtos prestes a vencer.
- **Conformidade com normas regulatórias**: Assegura o cumprimento de exigências sanitárias e evita penalidades.
- **Fortalecimento da confiança do consumidor**: Melhora a reputação da empresa e impulsiona a fidelização.

#### Quais os riscos de não utilizar a priorização da saída de produtos pelo critério?

A ausência do controle de estoque por data de validade pode resultar em perdas financeiras devido ao vencimento de produtos, aumento do desperdício e impactos na rentabilidade. Além disso, a comercialização de itens vencidos pode comprometer a segurança do consumidor, gerar penalidades por descumprimento de normas regulatórias e prejudicar a reputação da empresa. A falta desse controle também dificulta a gestão eficiente do estoque, aumentando o risco de acúmulo de mercadorias inutilizáveis e reduzindo a confiabilidade nas operações de armazenamento e distribuição.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052257513)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Na **Axis** alguns produtos do portfólio são controlados por validade, a equipe de vendas tem o desafio de garantir que os itens com a data de validade mais próxima sejam vendidos primeiro, evitando desperdício e garantindo a conformidade com as normas regulatórias.

**Tarefa:**

- Habilite o rastreamento de lotes e datas de validade no cadastro de um produto, que tenha na sua base de dados.
- Ajuste as regras de movimentação de estoque, garantindo que a saída dos produtos ocorra sempre priorizando aqueles com a validade mais próxima.
- Realize uma simulação de movimentação interna para verificar se o sistema está direcionando corretamente os produtos conforme o critério FEFO.
- Gere um relatório de vencimentos no ERP Sankhya para validar a correta priorização dos produtos na saída.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Acesse a tela Produtos**
   Menu: Configurações » Cadastros » Produtos

- Selecione o produto do exemplo
- Na aba **Medidas e Estoques**, sub-aba **Controle Adicional**, selecione no campo **Controlar por** a opção **Data de validade.**
- Na aba **Geral**, habilite a opção **Utiliza data de Validade.**

2. **Registro da movimentação de entrada**

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
- **Número Nota**: Informe **100**.
- **Chave NFe**: Insira uma chave fictícia com 44 dígitos.
- Clique em **Salvar**.

  **Preencher o Painel de Itens**
- No painel de itens, insira as seguintes informações obrigatórias:

- **Produto**: PRODUTO X
- Ao selecionar este produto, o campo **Data de Validade** será habilitado para que você informe a data de vencimento do item.
- **Local**: Informe o local.
- **Quantidade**: Registre a quantidade negociada.
- **Valor Unitário**: Informe o valor acordado.
- Clique em **Salvar**.

3. **Validação Final**

- Para confirmar essa nota de compra clique no botão **Confirmar** no topo da tela.
- Após a confirmação da nota, acesse o cadastro do produto e vá até a aba **Estoque**. Uma nova linha será adicionada, registrando o controle por data de validade com a data informada e a quantidade adquirida deste item.

4. **Registro da movimentação de Saída**

- Acesse a tela **Portal de Vendas**
  Menu: Comercial » Consulta
- No campo **Tipo de Movimento**, selecione **Nota de Venda**.
- No botão **Novo (+)**, selecione **TOP - Venda NF-E**.
- Clique duas vezes para iniciar o lançamento da **Nota de Venda**, redirecionando para a **Central de Vendas**.

**Preencher o Cabeçalho da Nota de venda**

Na **Central de Vendas**, preencha os seguintes campos obrigatórios:

- **Empresa**: Selecionar a empresa responsável pela operação.
- **Parceiro**: Informar o cliente ou parceiro de negócio.
- **Tipo de Operação**: Escolher “**Venda NF-E”**.
- **Tipo de Negociação**: Informar a modalidade de negociação acordada.
- **Vendedor**: Selecionar o vendedor responsável pela negociação.
- **Série Nota**: Informe **1**.
- **Natureza**: Preencher este campo caso a preferência **EXIGNATCFR** (Exigir natureza na central/financeiro/rateio) esteja ativada.
- **Centro de Resultado (CR)**: Informar o centro de resultado, caso a preferência **EXIGCRCFR** esteja ativada.

- Após preencher todos os campos, clique em **"Salvar"** para registrar as informações. 

  **Preencher o Painel de Itens**

- No painel de itens, insira as seguintes informações obrigatórias:

- **Produto**: PRODUTO X (utilizar o mesmo que informou na entrada).
- Ao selecionar este produto, na aba controle, consegue visualizar a data de controle desse produto.
- **Local**: Informe o local.
- **Quantidade**: Registre a quantidade negociada.
- **Valor Unitário**: Informe o valor acordado.
- Clique em **Salvar**.

5. **Validação Final**

- Para confirmar essa nota de compra clique no botão **Confirmar** no topo da tela.
- Com esse registro no sistema, sempre que houver saída do item na **Central de Vendas**, você poderá visualizar, na seção **Detalhes de Estoque**, as quantidades disponíveis e suas respectivas datas de validade. Isso garante que a saída seja realizada priorizando os itens com a data de validade mais próxima.

#### Correção e Repetição

- Revise os registros para confirmar se as operações foram concluídas.
- Cadastre novas informações de data de validade.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo, retorne no vídeo demonstrativo novamente caso necessário.
