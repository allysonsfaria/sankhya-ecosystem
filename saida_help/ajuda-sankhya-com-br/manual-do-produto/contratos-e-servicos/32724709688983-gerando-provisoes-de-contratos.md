---
id: "32724709688983"
titulo: "Gerando Provisões de Contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32724709688983-Gerando-Provis%C3%B5es-de-Contratos"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-08-24T18:44:09Z"
rotulos: ["Configuração", "Contrato", "Movimentação Financeira", "Preferências", "Financeiro"]
---

# Gerando Provisões de Contratos

🔸**Nome da Tela:** Contratos

🔸 **Módulo**: Contratos e Serviços

🔸 **Caminho de Acesso**: Sankhya Gestão de Negócios > Documentação de Telas (Manual) > Contratos e Serviços

## 🧩 Descrição

Esta funcionalidade permite registrar e gerenciar receitas ou despesas futuras previstas para contratos no ERP Sankhya. Ela oferece duas modalidades principais:

- **Provisões Dinâmicas**, ideais para contratos com vigência indeterminada, que se atualizam automaticamente a cada faturamento, e
- **Provisões Fixas**, para contratos com vigência pré-determinada, onde as provisões são baixadas progressivamente conforme o faturamento.

O objetivo é proporcionar um controle financeiro mais preciso e preditivo sobre os compromissos contratuais.

## 🛠️ Pré-requisitos

**Permissões necessárias**

- Acesso às telas "Preferências", "Contratos" e "Faturamento de Contratos".
- Permissão para alterar parâmetros do sistema e para criar/manipular movimentações financeiras e provisões.

**Parâmetros essenciais**

- QTDMESPROVFATC - Qtd de meses p/provisionar faturamento do contrato: Define a quantidade de meses para retroalimentar as provisões.
- CONTPROV - Informar Qtd Provisão qdo no último mês?: Controla o comportamento da provisão no último mês.

**Configurações relacionadas**

- Cadastro de contratos no sistema.
- Configurações financeiras básicas (Parceiro, Empresa, Tipo de Título, Natureza, Banco, etc.) para o lançamento manual de provisões fixas.

## 🧱 Estrutura da Tela

A funcionalidade de provisões de contratos não está concentrada em uma única tela, mas se estende por múltiplas telas, sendo as principais:

### 🔸 Campos

| **Nome do Campo** | **Tipo** | **Obrigatório?** | **Descrição** | **Validações** | **Exemplo** |
| --- | --- | --- | --- | --- | --- |
| **QTDMESPROVFATC** (Preferências) | Numérico | Sim | Quantidade de meses para provisionar faturamento do contrato. | Aceita valores numéricos. | 6 |
| **CONTPROV** (Preferências) | Booleano (Ligado/Desligado) | Sim | Informar Qtd Provisão quando no último mês? | Valores: Ligado ou Desligado. | Desligado |
| **Qtd. Provisão** (Contratos - Aba Propriedades) | Numérico | Não (para prov. dinâmicas pode ser deixado em branco; para prov. fixas, se automático, é mandatório) | Quantidade de meses para retroalimentar as provisões a partir do faturamento (para provisões dinâmicas) ou quantidade total de provisões a serem geradas (para provisões fixas automáticas). | Prioriza o valor informado aqui sobre o parâmetro QTDMESPROVFATC. | 6 |
| **Parceiro** (Provisões Financeiras) | Lookup | Sim | Parceiro relacionado à provisão. | Deve ser um parceiro válido e cadastrado. | Cliente A |
| **Empresa** (Provisões Financeiras) | Lookup | Sim | Empresa relacionada à provisão. | Deve ser uma empresa válida e cadastrada. | Empresa X |
| **Dt. Negociação** (Provisões Financeiras) | Data | Sim | Data de negociação da provisão. | Deve ser uma data válida. | 01/01/2025 |
| **Dt. Vencimento** (Provisões Financeiras) | Data | Sim | Data de vencimento da provisão. | Deve ser uma data válida. | 01/02/2025 |
| **Vlr do Desdobramento** (Provisões Financeiras) | Monetário | Sim | Valor total do desdobramento da provisão. | Deve ser um valor monetário positivo. | 1.000,00 |
| **Tipo de Título** (Provisões Financeiras) | Lookup | Sim | Tipo de título financeiro da provisão. | Deve ser um tipo de título financeiro válido e cadastrado. | Receita |
| **Natureza** (Provisões Financeiras) | Lookup | Sim | Natureza financeira da provisão. | Deve ser uma natureza financeira válida e cadastrada. | Aluguel |
| **Banco** (Provisões Financeiras) | Lookup | Sim | Banco associado à provisão. | Deve ser um banco válido e cadastrado. | Banco Y |
| **Número de Parcelas** (Ao parcelar) | Numérico | Sim | Quantidade de parcelas a serem geradas para a provisão. | Valor numérico. | 12 |
| **Frequência** (Ao parcelar) | Seleção | Sim | Frequência de geração das parcelas. | Mensal, Bimestral, etc. | Mensal |
| **Tipo de Parcelamento** (Ao parcelar) | Seleção | Sim | Tipo de parcelamento a ser aplicado. | Deve ser "Duplicação sem juros e multas (fixas)" para provisões fixas. | Duplicação sem juros e multas (fixas) |
| **Data base de Vencimento** (Ao parcelar) | Data | Sim | Data base para cálculo dos vencimentos das parcelas. | Deve ser uma data válida. | 01/02/2025 |

### 🔸 Botões / Ações

| **Botão** | **Ação** | **Comportamento Esperado** | **Observações** |
| --- | --- | --- | --- |
| **Faturar** (Faturamento de Contratos) | Inicia o processo de faturamento do contrato. | Gera o financeiro real e, para provisões dinâmicas, recria as futuras provisões. Para provisões fixas, baixa a provisão da referência faturada. | Possui uma seta com opções adicionais para provisões. |
| **Setinha no botão Faturar** (Faturamento de Contratos) | Exibe opções para geração de provisões sem faturar. | Abre um menu com "Refazer futuras provisões sem faturar" e "Refazer futuras provisões sem faturar (Considerando mês de referência)". | Permite gerar provisões sem um faturamento real associado, útil para lançamentos iniciais. |
| **Inserir registro** (Contratos - Aba Provisões Financeiras) | Adiciona uma nova linha para o lançamento manual de provisão. | Abre campos para preenchimento dos detalhes da provisão. | Usado para provisões fixas manuais. |
| **Salvar** (Contratos - Aba Provisões Financeiras) | Salva o registro de provisão manual. | Registra a provisão inicial antes de parcelar. | Necessário antes de clicar em "Parcelar". |
| **Parcelar** (Contratos - Aba Provisões Financeiras) | Gera as parcelas da provisão manual. | Abre uma janela para configurar o parcelamento (Número de Parcelas, Frequência, Tipo de Parcelamento, Data base de Vencimento, Data de Negociação). | Essencial para provisões fixas manuais. |
| **Confirmar** (Ao Parcelar) | Confirma a geração das parcelas da provisão manual. | Lança as provisões parceladas no sistema. | Finaliza o processo de lançamento manual de provisões fixas. |

## 👣 Jornada Passo a Passo

### 1. Provisões Dinâmicas (para contratos contínuos)

**1.1. Configuração dos Parâmetros Globais:**

1. Acesse Configurações » Avançado » Preferências.
2. No parâmetro QTDMESPROVFATC, informe a quantidade de meses para retroalimentar as provisões a partir de cada faturamento das referências (Ex: 6).
3. No parâmetro CONTPROV, configure-o como **Desligado**.

![Imagem 1: No parâmetro CONTPROV , configure-o como Desligado .](https://ajuda.sankhya.com.br/hc/article_attachments/32725125912983)

**1.2. Configuração por Contrato (opcional, mas mandatório se preenchido):**

1. Acesse Contratos e Serviços » Arquivos » Contratos.
2. Localize o contrato desejado.
3. Na aba Propriedades, no campo Qtd. Provisão, você pode informar uma quantidade específica de meses. Este valor sobrepõe o parâmetro QTDMESPROVFATC.

![Imagem 2: Na aba Propriedades , no campo Qtd. Provisão , você pode informar uma quantidade específica de meses. Este valor…](https://ajuda.sankhya.com.br/hc/article_attachments/32725125915159)

**1.3. Lançamento Inicial das Provisões (antes do faturamento):**

1. Acesse Contratos e Serviços » Rotinas » Faturamento de Contratos.
2. Localize o contrato.
3. Clique na **setinha** ao lado do botão Faturar.
4. Escolha uma das opções:
   - Refazer futuras provisões sem faturar
   - Refazer futuras provisões sem faturar (Considerando mês de referência)
5. As provisões serão geradas automaticamente na Movimentação Financeira.

![Imagem 3: As provisões serão geradas automaticamente na Movimentação Financeira .](https://ajuda.sankhya.com.br/hc/article_attachments/32725088762647)

![Imagem 4: As provisões serão geradas automaticamente na Movimentação Financeira .](https://ajuda.sankhya.com.br/hc/article_attachments/32725088769175)

**1.4. Comportamento ao Faturar o Contrato:**

1. Acesse Contratos e Serviços » Rotinas » Faturamento de Contratos.
2. Fature o contrato.
3. As provisões anteriores serão apagadas, e novas provisões serão criadas na mesma quantidade, continuando a retroalimentar enquanto o contrato estiver Ativo.

![Imagem 5: As provisões anteriores serão apagadas, e novas provisões serão criadas na mesma quantidade, continuando a…](https://ajuda.sankhya.com.br/hc/article_attachments/32725088769943)

### 2. Provisões Fixas (para contratos com vigência pré-determinada)

**2.1. Configuração dos Parâmetros Globais:**

1. Acesse Configurações » Avançado » Preferências.
2. No parâmetro QTDMESPROVFATC, informe o valor **0 (zero)**.
3. No parâmetro CONTPROV, configure-o como **Ligado**.

![Imagem 6: No parâmetro CONTPROV , configure-o como Ligado .](https://ajuda.sankhya.com.br/hc/article_attachments/32725088772119)

**2.2. Lançamento Manual das Provisões:**

1. Acesse Contratos e Serviços » Arquivos » Contratos.
2. Localize o contrato.
3. Na aba Propriedades, certifique-se de que o campo Qtd. Provisão esteja vazio.

![Imagem 7: Na aba Propriedades , certifique-se de que o campo Qtd. Provisão esteja vazio.](https://ajuda.sankhya.com.br/hc/article_attachments/32725088774167)

4. Acesse a aba Provisões Financeiras.
5. Clique para **inserir um novo registro**.
6. Preencha os campos obrigatórios: Parceiro, Empresa, Dt. Negociação, Dt. Vencimento, Vlr do Desdobramento, Tipo de Título, Natureza e Banco.
7. Clique em **Salvar**.
8. Clique no botão **Parcelar**.
9. Defina o Número de Parcelas, a Frequência (conforme o contrato), o Tipo de Parcelamento como **Duplicação sem juros e multas (fixas)**, a Data base de Vencimento e a Data de Negociação.
10. Clique em **Confirmar** para lançar as provisões.

![Imagem 8: Clique em Confirmar para lançar as provisões.](https://ajuda.sankhya.com.br/hc/article_attachments/32725125930135)

**2.3. Lançamento Automático das Provisões:**

1. Acesse Contratos e Serviços » Arquivos » Contratos.
2. Localize o contrato.
3. Na aba Propriedades, preencha o campo Qtd. Provisão com a quantidade de provisões a serem geradas, coerente com a vigência do contrato.

![Imagem 9: Na aba Propriedades , preencha o campo Qtd. Provisão com a quantidade de provisões a serem geradas, coerente com a…](https://ajuda.sankhya.com.br/hc/article_attachments/32725088777367)

4. Acesse Contratos e Serviços » Rotinas » Faturamento de Contratos.
5. Localize o contrato.
6. Clique na **setinha** ao lado do botão Faturar.
7. Escolha uma das opções:
   - Refazer futuras provisões sem faturar
   - Refazer futuras provisões sem faturar (Considerando mês de referência)
8. As provisões serão geradas automaticamente na Movimentação Financeira e também exibidas na aba Provisões Financeiras do cadastro do contrato.

![Imagem 10: As provisões serão geradas automaticamente na Movimentação Financeira e também exibidas na aba Provisões Financeiras do…](https://ajuda.sankhya.com.br/hc/article_attachments/32725125934231)

**2.4. Comportamento ao Faturar o Contrato:**

1. Acesse Contratos e Serviços » Rotinas » Faturamento de Contratos.
2. Fature o contrato.
3. A provisão pertinente à referência faturada será baixada, e a quantidade original de provisões geradas anteriormente se manterá.
4. As provisões baixadas podem ser visualizadas na tela Movimentação Financeira ou na aba Provisões Financeiras da tela Contratos.

![Imagem 11: As provisões baixadas podem ser visualizadas na tela Movimentação Financeira ou na aba Provisões Financeiras da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/32725088779927)

Caso um faturamento seja **cancelado** ou **excluído**, o sistema não dá rollback automaticamente nas provisões:

- Nas **provisões fixas**, é necessário realizar o **estorno manual** à provisão baixada na aba Provisões Financeiros do contrato.
- Nas **provisões dinâmicas**, é necessário refazer as provisões na tela de **Faturamento de Contratos**.

## ⚠️ Pontos de Atenção

- **Prioridade da Qtd. Provisão no Contrato (Dinâmicas):** O valor informado no campo Qtd. Provisão na tela de Contratos sempre sobrepõe o parâmetro global QTDMESPROVFATC para provisões dinâmicas.
- **Visibilidade das Provisões Dinâmicas:** Provisões dinâmicas geradas não são exibidas na aba "Provisões financeiras" da tela Contratos; elas constam apenas na Movimentação Financeira como provisão.
- **Comportamento de Recriação (Dinâmicas):** Ao faturar um contrato com provisões dinâmicas, as provisões anteriores são apagadas e novas são criadas na mesma quantidade, retroalimentando o contrato enquanto estiver ativo.
- **Tipo de Parcelamento (Fixas Manuais):** Para provisões fixas lançadas manualmente, é mandatório que o "Tipo de Parcelamento" seja "Duplicação sem juros e multas (fixas)".
- **Coerência da Qtd. Provisão (Fixas Automáticas):** Ao preencher o campo Qtd. Provisão para provisões fixas automáticas, o valor deve ser coerente com a vigência do contrato.
- **Visibilidade das Provisões Fixas:** Provisões fixas são exibidas tanto na Movimentação Financeira quanto na aba "Provisões financeiras" da tela de Contratos.

## 💡 Dicas de Usabilidade

- **Planejamento:** Defina claramente se o contrato exige provisões dinâmicas (para contratos contínuos ou de longo prazo) ou fixas (para contratos com vigência definida) antes de configurar o sistema.
- **Consistência dos Parâmetros:** Mantenha a consistência entre os parâmetros globais (QTDMESPROVFATC e CONTPROV) e a configuração individual por contrato (Qtd. Provisão) para evitar comportamentos inesperados.
- **Visualização:** Para provisões dinâmicas, foque na Movimentação Financeira para acompanhar os lançamentos. Para provisões fixas, utilize tanto a Movimentação Financeira quanto a aba Provisões Financeiras na tela de Contratos.
- **Teste em Ambiente de Homologação:** Antes de aplicar em produção, sempre teste as configurações e o comportamento das provisões em um ambiente de homologação.

## 📘 Casos de Uso

✔ **Contrato de Assinatura de Software (Provisão Dinâmica):** Um contrato de assinatura de software com vigência indeterminada é configurado com QTDMESPROVFATC = 12 meses e CONTPROV = Desligado. O campo Qtd. Provisão no contrato é deixado em branco. A cada faturamento mensal, o sistema automaticamente apaga a provisão anterior e gera 12 novas provisões futuras, garantindo uma projeção contínua da receita.

✔ **Contrato de Aluguel de Imóvel (Provisão Fixa - Lançamento Automático):** Um contrato de aluguel de imóvel com vigência de 24 meses é configurado com QTDMESPROVFATC = 0 e CONTPROV = Ligado. No campo Qtd. Provisão do contrato, é informado 24. Ao usar a opção "Refazer futuras provisões sem faturar" na tela de Faturamento de Contratos, 24 provisões são geradas na Movimentação Financeira e na aba Provisões Financeiras do contrato. A cada faturamento mensal, a provisão correspondente é baixada, mantendo o controle das provisões restantes.

❌ **Erro Comum: Provisões Dinâmicas não Aparecendo na Aba "Provisões Financeiras":** O usuário configura um contrato para provisões dinâmicas e espera ver os lançamentos na aba "Provisões Financeiras" da tela de Contratos. No entanto, as provisões dinâmicas, por padrão, são geradas apenas na Movimentação Financeira. Para visualizar, o usuário deve consultar a tela de Movimentação Financeira.

## ❓ Perguntas Frequentes (FAQ)

1. **As provisões dinâmicas aparecem na aba "Provisões Financeiras" da tela de Contratos?** Não, as provisões dinâmicas são geradas diretamente na Movimentação Financeira como provisão e não são exibidas na aba "Provisões Financeiras" da tela de Contratos.
2. **Qual a diferença entre a "Qtd. Provisão" no contrato e o parâmetro "QTDMESPROVFATC"?** O parâmetro QTDMESPROVFATC é uma configuração global. O campo "Qtd. Provisão" no contrato é específico para cada contrato e, se preenchido, tem precedência sobre o parâmetro global para provisões dinâmicas. Para provisões fixas automáticas, o campo "Qtd. Provisão" é mandatório.
3. **É possível gerar provisões sem faturar o contrato?** Sim, tanto para provisões dinâmicas quanto fixas, você pode usar as opções "Refazer futuras provisões sem faturar" ou "Refazer futuras provisões sem faturar (Considerando mês de referência)" na setinha do botão Faturar na tela Faturamento de Contratos.
4. **O que acontece com as provisões dinâmicas quando o contrato é faturado?** As provisões anteriores são apagadas e novas provisões são criadas na mesma quantidade definida, continuando a retroalimentar o contrato enquanto ele estiver ativo.
5. **Posso misturar provisões dinâmicas e fixas no mesmo contrato?** O sistema não é projetado para misturar os dois tipos de controle de provisão para o mesmo contrato. A escolha deve ser feita com base na natureza da vigência do contrato (determinada ou indeterminada) e a parametrização deve ser consistente para um dos tipos.

## 🔎 Artigos Relacionados

- [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaprovisesfinanceiras)
- [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos)

## 🧠 Palavras-chave

Provisão, Contratos, Sankhya, ERP, Faturamento, Receita, Despesa, Provisão Dinâmica, Provisão Fixa, Movimentação Financeira, Parâmetros, QTDMESPROVFATC, CONTPROV, Qtd. Provisão.
