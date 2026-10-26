---
id: "37670367016599"
titulo: "Como controlar produtos por local"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37670367016599-Como-controlar-produtos-por-local"
trilha: "Universidade Sankhya > Jornada de Estoques"
atualizado_em: "2026-07-22T14:11:08Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Logística"]
---

# Como controlar produtos por local

| Categoria |
| --- |
| [Qual é o objetivo do controle de estoque por local?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670367016599-Como-controlar-produtos-por-local#h_01KEYKF74XADNZJM1003PN06JZ) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670367016599-Como-controlar-produtos-por-local#h_01KEYKESRNNP3PZNMDSW7XE62W) |
| [Quais os riscos de não se fazer o controle de estoques por local?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670367016599-Como-controlar-produtos-por-local#h_01KEYKEB24SYYJ1T2G702NXVR4) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670367016599-Como-controlar-produtos-por-local#h_01KFBTEJ5555G1MMEF937JVXZ2) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670367016599-Como-controlar-produtos-por-local#h_01KEYKDWVBC9TNH1484EFA1XQ9) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670367016599-Como-controlar-produtos-por-local#h_01KEYKDDDHBCC19HDPX1G6NP0J) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37670367016599-Como-controlar-produtos-por-local#h_01KEYKBTH3GZAQJCRVWJG4E2P5) |

## Controle de estoque por local

#### Qual é o objetivo do controle de estoque por local?

O controle de estoque por local visa otimizar a organização, localização e entrega de itens armazenados, proporcionando mais eficiência operacional e rastreamento em tempo real. Facilita a identificação rápida de produtos, reduz erros operacionais, melhora a precisão nas retiradas e armazenamento, e apoia o planejamento estratégico de reabastecimento. Promove mais produtividade ao automatizar e agilizar processos, garantindo um estoque mais organizado, rastreável e alinhado às demandas da empresa.

#### Quais problemas este recurso resolve?

- **Dificuldade na localização de produtos**: Reduz o tempo de busca, otimizando a operação.
- **Erros em separação e expedição**: Garante maior precisão na entrega.
- **Desorganização no armazenamento**:  Estrutura e padroniza a disposição dos itens.
- **Perdas e extravios de mercadorias**: Rastrear movimentações, evitando perdas.
- **Falta de controle sobre movimentações**: Registra entradas, saídas e transferências.
- **Retrabalho e desperdício de tempo**:  Automatiza processos e reduz esforços manuais.
- **Dificuldade no reabastecimento**: Permite reposição eficiente e evita rupturas de estoque.
- **Erros na contagem e inventário**: Facilita a conferência e melhora a acuracidade dos saldos.
- **Baixa eficiência operacional**:  Agiliza processos e melhora o desempenho logístico.

#### Quais os riscos de não se fazer o controle de estoques por local?

A ausência desse controle compromete diretamente a eficiência logística da empresa. Dificulta a localização de itens, gera desorganização no armazenamento e aumenta o risco de perdas, extravios e erros na separação de pedidos. Sem um mapeamento claro dos locais de estoque, o rastreamento das movimentações se torna falho, afetando o planejamento de reposições, a utilização do espaço e a execução de auditorias. Como consequência, a empresa enfrenta rupturas, aumento de custos operacionais, insatisfação de clientes e prejuízos financeiros, enfraquecendo sua competitividade e comprometendo a sustentabilidade do negócio.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052006662)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa **Axis** enfrenta dificuldades na localização e movimentação de produtos, resultando em atrasos nas expedições, perdas de mercadorias e retrabalho na separação de pedidos. Para otimizar esse processo, foi implementado o controle de estoque por local, permitindo rastrear a posição exata de cada item e automatizar movimentações de entrada e saída.

**Tarefa:** Você recebeu a tarefa de configurar o sistema para controlar o estoque por local, assegurando a correta armazenagem e movimentação dos produtos.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Registro de Locais**

- Acesse a tela **Locais**
  Menu: Comercial » Arquivo » Cadastros
- Clique em **Mostrar hierarquia** para visualizar os registros;
- Caso já exista o cadastro, apenas anote o nome do local que será utilizado nos próximos passos, se não existir, faça o registro.

Clique no botão **(+)** para incluir um novo registro sintético:

- **Cód local:** Informe 0100.
- **Descrição:** Armazém.
- Marque o campo **Ativo** e salve o registro.

Clique no botão **(+)** para incluir um novo registro, desta vez, analítico:

- **Cód local:** Informe 0101.
- **Descrição:** Almoxarifado.
- Marque o campo **Ativo.**
- Marque o campo **Analítico** e salve o registro.

2. **Cadastro de Produtos**

- Acesse a tela **Produtos**
  Menu: Configurações » Cadastros » Produtos

- Na aba **Geral,** no campo **Local padrão:** Indique o local padrão para ser direto o produto no momento da chegada da mercadoria na empresa;
- Na aba **Medidas e estoque,** na sub-aba **“Estoque”** marque o campo **Usa local** para indicar que este produto terá controle por local;

3. **Validação Final**

- Acesse a tela **Consulta de produtos.**
  Menu: Comercial » Consulta
- Clique na lupa para carregar todos os produtos;
- No painel denominado **Detalhes de estoque**, é possível identificar os locais onde existem estoque de cada um dos produtos conforme as entradas/compras que foram realizadas indicando estes locais;
- Essa informação também pode ser consultada diretamente no cadastro do produto, na aba **“Estoque”**.

#### Correção e Repetição

- Revise os registros para confirmar se as operações foram concluídas.
- Cadastre novos locais e faça os devidos vínculos.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo, retorne no vídeo demonstrativo novamente caso necessário.
