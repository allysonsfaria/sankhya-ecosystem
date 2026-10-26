---
id: "27883754211863"
titulo: "Ações - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27883754211863-A%C3%A7%C3%B5es-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Ações e automações"
atualizado_em: "2026-09-23T17:33:06Z"
rotulos: ["Configuração", "Agendamento", "Analytics Studio", "Automação", "Logs", "Fluxos"]
---

# Ações - Analytics Studio

A ferramenta Ações no [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio) permite automatizar processos e operações dentro da plataforma por meio da criação de fluxos que consistem em uma sequência de passos. Esses passos são executados em ordem, permitindo desde simples manipulações de dados até integrações complexas.

---

### Como Criar uma Ação

Para criar uma ação, acesse a seção de **"Interações"** do componente desejado e adicione uma nova ação de acordo com as necessidades específicas do fluxo. Ao configurar a ação, defina um nome que identifique claramente sua finalidade ou contexto, facilitando a organização e o gerenciamento.

#### Adicionando e Gerenciando Passos

- **Adição de Passos:** a ação pode conter vários passos, que serão executados em sequência.
- **Ordem dos Passos:** a ordem dos passos é essencial, pois determina a sequência de execução. Para reordenar, basta clicar e arrastar o passo para a nova posição.
- **Exclusão de Passos:** para remover um passo, clique com o botão direito sobre ele e selecione **"Remover"**.

#### Agendamento de Ações

As ações podem ser agendadas para execução automática usando um código **"CRON"** (por exemplo, a cada hora, diariamente).

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=gLehj2XvVaI)

#### Log de Execução

O Analytics AI gera logs detalhados que registram a execução de cada ação, incluindo informações sobre o usuário que a iniciou, o horário de execução e o resultado de cada passo (sucesso ou falha).

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=CL8fhMNGr5Y)

---

### Principais Passos de Ação

#### Alterar Relacionamento

Permite modificar o relacionamento entre registros de cadastros. Para configurar, realize os passos abaixo:

1. Selecione o cadastro principal;
2. Escolha o cadastro pai;
3. Defina o conteúdo do relacionamento.

**Exemplo:** para mudar o status de uma tarefa para **"Concluído"**, o cadastro principal seria **"Tarefa"**, o cadastro pai seria **"Status"** e o conteúdo seria **"Concluído"**.

#### Chamar Ação

Possibilita a execução de outra ação previamente configurada, permitindo a reutilização de fluxos comuns entre diferentes ações, otimizando o desenvolvimento e facilitando a manutenção.

#### Ir para a Tela

Redireciona o usuário de uma tela para outra dentro do Analytics AI. Para configurar essa etapa:

1. Escolha a tela de destino
2. Ative a opção **"Trazer Seleção"** para levar os filtros e seleções da tela atual para a nova tela.

#### Recarregar Tela

Essa etapa é essencial para situações em que uma ação altera dados e há a necessidade de que a interface reflita essas mudanças.

#### Filtrar

O passo Filtrar é usado para aplicar filtros em cadastros ou registros antes de executar outras operações.

**Exemplo:** em um cálculo de folha de pagamento, pode-se filtrar a natureza **"Salários"** antes de efetivar o cálculo de salários, depois filtrar a natureza de **"Benefícios"** e efetuar o cálculo.

#### Filtrar com Atributo

Permite aplicar filtros dinamicamente, baseados em variáveis, ao invés de valores fixos.

**Exemplo:** é possível criar um atributo que identifique todos os clientes que realizaram compras nos últimos 12 meses e utilizar esse atributo para filtrar uma ação. Isso não seria viável com o filtro comum, que exigiria a seleção manual de cada cliente.

#### Criar/Alterar Registro

Esse passo permite criar novos registros ou alterar registros existentes em um cadastro.

#### Enviar E-mails

Automatiza o envio de e-mails personalizados utilizando dados dinâmicos. 

#### Limpar Atributo

Permite limpar o valor de um atributo específico em registros selecionados com base no filtro atual da ação.

#### Limpar Cadastro

Remove registros de um cadastro com base no filtro atual da ação.

#### Executar JAR

Possibilita executar um código Java personalizado, expandindo as capacidades da plataforma com lógica customizada.

#### Rodar Conexão

Permite que seja executado conexões previamente configuradas dentro da ação, integrando processos de carregamento de dados em seus fluxos automatizados.

- **Referência:** para aprender a configurar conexões, seja via CSV ou banco de dados, consulte a documentação **"Conexões"**. Essa documentação fornece orientações detalhadas sobre como criar conexões pelo database.
- **Uso do Rodar Conexão:** dentro de uma ação, pode-se vincular e executar conexões que foram configuradas com SQL. Esse passo é especialmente útil para automatizar processos que envolvem a transferência de grandes volumes de dados entre sistemas.

**Exemplo de Aplicação:** processos diários de carregamento de dados:

- Para carregar dados diariamente do ERP para o Analytics AI, é possível configurar uma série de conexões para serem executadas em sequência, garantindo a importação organizada e eficiente de todos os dados necessários.
- Essa ação pode ser agendada com o uso de um código Cron, permitindo a automação completa do processo de carregamento sem necessidade de intervenção manual.

Essa abordagem integra carregamentos de dados complexos diretamente em fluxos automatizados, tornando o processo de integração com fontes externas rápido, eficiente e escalável.

#### Cálculo

É utilizado para realizar cálculos numéricos sobre atributos em cadastros. Para configurar, siga os passos abaixo:

- Selecione o atributo destino.
- Defina a VIEW que fornecerá os dados para o cálculo.
- Aplique a fórmula desejada para calcular e popular o atributo numérico.

**Exemplo:** calcular o valor total de uma proposta baseada na quantidade, valor unitário e percentual de desconto.

---

![Imagem 1: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157353974935) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
