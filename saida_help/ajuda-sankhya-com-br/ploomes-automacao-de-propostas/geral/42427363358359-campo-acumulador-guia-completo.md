---
id: "42427363358359"
titulo: "Campo Acumulador: guia completo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427363358359-Campo-Acumulador-guia-completo"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-11T16:14:59Z"
rotulos: ["sync_hc", "ploomes_14421751", "ploomes", "sync_hash_347b2a689afb"]
---

# Campo Acumulador: guia completo

## 1) Sobre o Campo Acumulador

O Campo Acumulador é um tipo de campo personalizado que calcula e exibe valores agregados de registros relacionados como a soma do faturamento de um cliente, a quantidade de propostas em aberto de um negócio ou o ticket médio por produto.

Com ele, informações que antes exigiam relatórios ou cálculos manuais passam a estar disponíveis diretamente nos formulários, tabelas e abas do Ploomes, consolidadas e atualizadas automaticamente conforme os registros relacionados mudam.

Exemplos de uso:

- **Valor total de vendas** de um cliente nos últimos 12 meses
- **Quantidade de propostas em aberto** vinculadas a um negócio
- **Ticket médio por produto** no trimestre atual
- **Faturamento consolidado de uma empresa matriz**, somando o total de vendas de todas as suas filiais cadastradas
- **Quantidade de clientes ativos vinculados a uma empresa**, contando todas os contatos (filiais, pessoas) relacionadas a uma mesma empresa

---

## 2) Pré-requisitos

**Para criar e configurar o campo:**

- Acesso pela **plataforma web**
- Perfil de administrador

**Para visualizar o campo:**

- Qualquer usuário com a **permissão de visualização do campo** habilitada, definida pelo Administrador nas “c**onfigurações de visualização do campo”**, dentro do editor de campos.

---

## 3) Configurando o Campo Acumulador

Na tela de configuração do campo acumulador, o usuário verá 3 etapas, sendo elas:

## 3.1) Etapa 1: Selecionar entidade e operação (obrigatório)

Selecione a **entidade relacionada** cujos registros serão acumulados. As opções variam conforme o formulário onde o campo foi criado:

| Formulário | Entidades disponíveis |
| --- | --- |
| Empresa | Produto de cliente, Negócio, Proposta, Venda, Documento, Tarefa, Registro de Interação, **Empresa e Pessoa** |
| Pessoa | Produto de cliente, Negócio, Proposta, Venda, Documento, Tarefa e Registro de Interação |
| Produto de cliente | Negócio |
| Produto | Produto da proposta, da venda e do documento |
| Vínculo do produto | Vínculo do produto da proposta, da venda e do documento |
| Usuário | Cliente, Negócio, Proposta, Venda, Documento, Tarefa e Registro de Interação |
| Negócio | Negócio derivado, Proposta, Venda, Documento, Tarefa, Registro de Interação |

Em seguida, selecione a **operação**:

- **Contagem** — conta registros (não exige campo base)
- **Soma / Média / Valor Máximo / Valor Mínimo** — exige a seleção de um campo numérico (Número inteiro, Moeda, Decimal ou Porcentagem)

## 3.2) Etapa 2: Filtrar data (obrigatório)

Selecione o **campo de data** de referência da entidade relacionada e defina o tipo:

- **Data fixa** — data específica no calendário
- **Data relativa** — período dinâmico (Hoje, Semana atual, N meses no passado, Ano atual etc.)

## 3.3) Etapa 3: Usar filtros adicionais (opcional)

Adicione até **4 filtros** para refinar os registros calculados. Regras:

- Apenas o operador **"E"** é suportado
- Campos de data não podem ser usados aqui
- Apenas campos da **entidade relacionada** estão disponíveis

## 3.4) Etapa 4: Testar (opcional)

Antes de salvar, use a **Área de Teste** para validar a configuração: selecione um registro e clique em **"Calcular valor do campo"** para ver o resultado antecipado.

Exemplo de configuração do campo acumulador:

[GIF animado: Imagem 1: Exemplo de configuração do campo acumulador:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2226636938/3dbe76a3562937f52f0a61b0855a/Ploomes-Mdulos_Administraoemais27pginas-TrabalhoMicrosoftEdge2026-03-3015-19-20-ezgif_com-video-to-gif-converter.gif?expires=1786536000&signature=00285d1ad53ace16e1d55bd5cfcea86d9f23f4aa742e257fcd51f2a137cf183a&req=diIlEM99m4hcUfMW3nq%2BgaG2qtTDwAhiKy2DfPFliidcB3P9An31VnBT%2F95R%0AX4qtBDqTi25WY09Ol60yE9mxO6g%3D%0A)

---

## 4) Utilizando o Campo Acumulador

## 4.1) Onde o valor é exibido

Após o primeiro cálculo, o valor estará disponível em:

- **Tabelas dinâmicas** — como filtro, não é possível usá-lo para ordenação
- **Formulários** das entidades configuradas
- Como **variável em campos de fórmula**
- Como **valor padrão** disponível para os campos de “Texto simples” e “Texto multilinha”
- **Nos relatórios** — como filtro para segmentar resultados ou como critério de agrupamento para organizar os dados
- **Automações** — como filtro

## 4.2) Como a atualização funciona

O valor do Campo Acumulador é atualizado automaticamente pelo sistema. Entenda quando cada atualização acontece:

- **Ao criar ou editar o campo, ou ao clicar em "Forçar atualização":** o sistema recalcula o valor para todos os registros da entidade.

  - Use a opção "Forçar atualização" quando identificar cadastros com valores incorretos ou desatualizados. Por ser uma operação de alto volume, ela pode levar alguns minutos para ser concluída.
- **Quando um registro relacionado é alterado:** se alguém cria, edita ou exclui um registro que impacta o campo (ex: uma nova venda associada a um cliente), o sistema refaz o calculo contando o que foi alterado, em tempo real.
- **Todo dia, de madrugada:** campos que utilizam **data relativa** (como "mês atual" ou "últimos 3 meses") são recalculados automaticamente pelo sistema. Isso garante que os valores se mantenham corretos conforme o tempo passa, sem nenhuma ação manual necessária.

## 4.3) Importante sobre permissões individuais dos usuários

⚠️ O cálculo do campo acumulador **não respeita as permissões de visualização individuais dos usuários**. O valor exibido é baseado em todos os registros que atendem aos filtros que foram adicionados na configuração do campo. Um usuário pode ver no acumulador um valor que inclui registros aos quais ele não teria acesso direto.

---

## 5) Limitações do Campo Acumulador

- Limite de **40 campos acumuladores por conta**
- Não está disponível no aplicativo mobile a criação e edição
- Não está disponível em **formulários externos**
- Não está mapeado em **integrações externas** (API ou conectores nativos)
- **Não é possível usar o campo para ordenar** tabelas dinâmicas
- **Cards arquivados** são ignorados no cálculo quando a entidade acumulada é Negócio
- **Não é possível criar referências cíclicas** entre campos acumuladores (ex: Campo A acumulando Campo B que acumula Campo A)

---

## 6) F.A.Q.

**6.1) Posso criar um Campo Acumulador pelo celular?**

Não. A criação é exclusiva da versão web. No mobile, os campos criados são exibidos normalmente, mas não é possível criá-los ou editá-los.

**6.2) O campo acumulador respeita as permissões de visualização dos usuários?**

Não. O valor exibido inclui todos os registros que atendem aos filtros configurados, independentemente das permissões individuais de quem visualiza o campo.

**6.3) Posso ordenar uma tabela dinâmica pelo campo acumulador?**

Não. Por ser um valor sempre dinâmico, a ordenação por esse tipo de campo é bloqueada em tabelas dinâmicas.

**6.4) Qual é o limite de Campos Acumuladores?**

40 por conta. Para criar um novo, será necessário excluir um campo existente.

**6.5) Posso usar o Campo Acumulador nos meus relatórios?** Sim. O Campo Acumulador pode ser utilizado nos relatórios do Ploomes de duas formas:

- **Como filtro:** você pode filtrar o relatório com base no valor do campo acumulador. Por exemplo, exibir apenas clientes cujo total de vendas seja maior que R$ 50.000.
- **Como agrupador:** você pode agrupar os dados do relatório pelo campo acumulador, organizando os resultados por faixas de valor acumulado.

**6.6) Os valores do Campo Acumulador estão incorretos ou desatualizados. O que eu faço?**

Acesse a edição do campo, clique em "Forçar atualização" e aguarde o recálculo ser concluído. Essa ação recalcula o valor para todos os registros da entidade de uma vez e pode levar alguns minutos, dependendo do volume de dados.

---

## 7) Glossário

- **Campo acumulador:** Campo personalizado que realiza operações de agregação (soma, contagem, média, máximo ou mínimo) com base em registros de uma entidade relacionada.
- **Entidade:** objeto do Ploomes que representa um tipo de registro (Empresa, Negócio, Proposta etc.).
- **Operação de agregação:** Cálculo aplicado sobre um conjunto de registros: Contagem, Soma, Média, Valor Máximo ou Valor Mínimo.
- **Data relativa:** Período dinâmico e automático (ex: "Mês atual", "N meses no passado").
- **Data fixa:** Data específica e estática selecionada no calendário.
- **Gatilho:** Evento que dispara o recálculo automático do campo (criação, edição ou exclusão de registro relacionado).
- **Card:** Registro de Negócio no Ploomes.
- **Área de teste:** Ferramenta dentro do configurador do campo que permite simular o resultado do cálculo com registros reais antes de salvar.

---

## 8) Artigos relacionados

- [Onde encontro a opção para criar um novo campo no Ploomes? | Central de conhecimento | Ploomes](https://sankhya.zendesk.com/hc/pt-br/articles/42427509973399)
- [Permissões de Perfil de usuário | Central de conhecimento | Ploomes](https://sankhya.zendesk.com/hc/pt-br/articles/42427651167383)
- [Como configurar o funil | Central de conhecimento | Ploomes](https://sankhya.zendesk.com/hc/pt-br/articles/42427673058583)
