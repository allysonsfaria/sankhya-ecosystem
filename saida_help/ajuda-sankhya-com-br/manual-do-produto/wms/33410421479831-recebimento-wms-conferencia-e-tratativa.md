---
id: "33410421479831"
titulo: "Recebimento WMS: Conferência e Tratativa de Divergências no Coletor (WMS, Coletor)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:13:15Z"
rotulos: ["Conferência", "WMS", "Coletor", "Recebimento", "Estoque"]
---

# Recebimento WMS: Conferência e Tratativa de Divergências no Coletor (WMS, Coletor)

**Módulo**: WMS (Total Cross)
**Versão Mínima**: A partir da 4.20.00
**Caminho de Acesso**: Menu Principal > Conferência > Conferência de Entrada

---

## Sumário

- [Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#descri%C3%A7%C3%A3o-e-usabilidade)
  - [Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#descri%C3%A7%C3%A3o-da-funcionalidade)
  - [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#pr%C3%A9-requisitos)
  - [Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#diagrama-de-fluxo)
  - [Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#jornada-de-uso)
  - [Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#pontos-de-aten%C3%A7%C3%A3o)
  - [Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#dicas-de-usabilidade)
  - [Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#casos-de-uso)
- [FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#faq--d%C3%BAvidas-frequentes)
- [Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/33410421479831-Recebimento-WMS-Confer%C3%AAncia-e-Tratativa-de-Diverg%C3%AAncias-no-Coletor-WMS-Coletor#artigos-relacionados)

---

## Descrição e Usabilidade

---

### Descrição da Funcionalidade

Esta funcionalidade centraliza e otimiza o processo de recebimento de mercadorias no coletor WMS (Total Cross). Ela permite que os usuários realizem a conferência de entrada e gerenciem divergências de forma eficiente, seguindo as regras de negócio da empresa.

O sistema foi aprimorado para garantir a continuidade das operações de **armazenagem expressa**, mesmo em casos de **conferência parcial**. O objetivo é garantir a acuracidade do estoque, agilizar o fluxo de recebimento e reduzir erros, proporcionando um controle mais robusto sobre os produtos que entram no armazém, especialmente aqueles que exigem **controle de validade** e **shelf life**.

---

### Pré-requisitos

- **Permissões necessárias**:
- COLETOR\_WMS\_RECEBIMENTO
- COLETOR\_WMS\_CONFERENCIA\_ENTRADA
- **Parâmetros essenciais**:
- LOTEENVIOWMS = S (se houver controle de lote)
- **Configurações relacionadas**:
- Cadastros de produtos com informações de código de barras ou SKU.
- Pedidos de compra devidamente vinculados às notas fiscais de entrada.

---

### Diagrama de fluxo

![Imagem 1: Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/33410405216791)

---

### Jornada de Uso

Para realizar a conferência de entrada no coletor WMS, siga os passos abaixo:

**1. Login do Operador:** Na tela inicial do coletor, insira suas credenciais para autenticação.

**2. Acesso ao Menu principal:** Após o login, você será direcionado ao menu principal do aplicativo Total Cross.

**3. Selecionar Conferência:** Toque na opção "Conferência" (geralmente o primeiro card da primeira linha).

**4. Escolher Tipo de conferência:** Toque na opção "Conferência de Entrada" para prosseguir com o processo.

**5. Acompanhar Estágio do processo:** Um "Stepper" na parte superior da tela indicará visualmente o seu progresso na conferência (Doca, Item, Finalização).

**6. Informar Doca de recebimento:** Na Tela de Doca, informe o código da doca onde os itens estão sendo recebidos. Este campo é obrigatório.

**7. Informar Dados do produto:** Na Tela de Produto, você precisará preencher os seguintes campos para cada item:

- Código do Item: pode ser lido via scanner ou digitado manualmente.
- Quantidade: informe a quantidade recebida do item.
- Lote: se aplicável, digite o número do lote do produto.
- Data de Fabricação e Validade: se aplicável, informe as datas de fabricação e validade do produto. (Essa informação é crucial para a rastreabilidade e para a geração de tarefas de armazenagem, garantindo a continuidade do fluxo logístico mesmo em casos de conferências parciais.)

**8. Próximo Item ou Enviar:**

- Se houver mais itens para conferir, toque em "Próximo item" para registrar o item atual e prosseguir para o próximo.
- Ao finalizar a conferência de todos os itens daquele recebimento, toque em "Enviar".

**9. Feedback do Sistema:** O sistema exibirá "Toasts" ou "Modais" para indicar o status da operação:

- Sucesso: "Envio Confirmado" ou similar.
- Erro: Mensagens indicando erros de preenchimento, divergências ou campos obrigatórios não informados.

---

### Pontos de Atenção

- **Obrigatoriedade de Doca e Quantidade:** A doca de recebimento e a quantidade do item são campos mandatórios para o envio da conferência.
- **Validações específicas:** O sistema realizará validações automáticas, como a conferência do item em relação ao pedido de compra. Divergências serão sinalizadas.
- **Impacto em outras áreas:** Uma conferência incorreta pode gerar inconsistências no estoque, impactando diretamente o inventário e os processos de separação e expedição.
- **Divergências identificadas:** Se houver divergência identificada no processo de recebimento, as tratativas ficarão disponíveis para realização no processo WEB através da tela de Recebimento de Mercadorias.
- **Fluxo contínuo de Armazenagem:** O sistema foi projetado para garantir o fluxo contínuo da armazenagem expressa, mesmo para produtos com controle de validade. As tarefas de armazenagem são geradas corretamente após a conferência, seja ela total ou parcial, assegurando que o processo não seja interrompido por este tipo de produto.

---

### Dicas de Usabilidade

- Utilize o Scanner: Priorize a leitura de códigos de barras via scanner para agilizar o processo e minimizar erros de digitação.
- Verifique o Stepper: Acompanhe o "Stepper" para ter clareza sobre em qual etapa da conferência você está e o que ainda precisa ser feito.
- Pausar Conferência: Em caso de interrupção, utilize o botão "Pausar" para salvar o progresso da conferência e retomá-la posteriormente.
- Atenção aos Feedbacks: Sempre observe as mensagens de "Toast" ou "Modal" para identificar rapidamente se houve algum problema ou se a operação foi bem-sucedida.
- Navegação simplificada: A interface do coletor conta com botões grandes e de fácil visualização, organizados em ordem alfabética para agilizar a navegação entre as funcionalidades.
- Encerramento rápido: Para finalizar sua sessão rapidamente, utilize o botão "Sair', posicionado no cabeçalho da tela.

---

### Casos de Uso

✅ **Exemplo 1:** Um operador recebe uma carga de 50 unidades do "Produto A" e 30 unidades do "Produto B" na Doca 3. Ele informa a doca, lê o código do "Produto A", digita 50, clica em "Próximo item". Em seguida, lê o código do "Produto B", digita 30, e clica em "Enviar", finalizando a conferência.

✅ **Exemplo 2**: Um operador recebe uma carga de 100 unidades do "Produto C" (com controle de validade). Ele confere 50 unidades e informa a data de validade 01/01/2026, pausa a conferência e a retoma no dia seguinte. Ao conferir as 50 unidades restantes, o sistema gera a tarefa de armazenagem expressa sem erros, direcionando o produto ao local correto e mantendo a informação de validade.

❌ **Erro Comum:** O operador tenta enviar a conferência sem ter informado a quantidade de um dos itens, resultando em uma mensagem de erro "Campo 'Quantidade' é obrigatório".

---

## FAQ – Dúvidas Frequentes

**1. O que devo fazer se o coletor não reconhecer o código de barras do produto?**
Você pode digitar o código do item manualmente. Verifique também se o cadastro do produto está atualizado no sistema.

**2. Posso continuar uma conferência que foi pausada?**
Sim, após pausar uma conferência, ela ficará disponível para ser retomada no menu de "Conferências Pendentes" ou similar.

**3. O que acontece se a quantidade conferida for diferente da quantidade do pedido de compra?**
O sistema registrará a divergência. Dependendo da configuração, isso pode gerar um alerta ou exigir uma ação de um supervisor para aprovar a diferença.

**4. O sistema pode apresentar erro na armazenagem de produtos com controle de validade após uma conferência parcial?** O sistema Sankhya WMS foi projetado para suportar a movimentação de produtos com controle de validade e shelf life, mesmo após conferências parciais. A tarefa de armazenagem expressa é gerada corretamente para esses itens, garantindo a continuidade do fluxo sem interrupções.

**5. Como acesso as diferentes opções de conferência?** Todas as opções de conferência estão disponíveis diretamente na tela como botões visuais. Basta tocar no botão desejado para iniciar a atividade.

---

## Artigos Relacionados

- [WMS Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/sections/360007733394-WMS)

---
