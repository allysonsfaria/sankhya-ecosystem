---
id: "40475279854999"
titulo: "Como integrar a GRRF ao financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40475279854999-Como-integrar-a-GRRF-ao-financeiro"
trilha: "Manual do Produto > Pessoas+ > Rescisão > Documentos e Guias da Rescisão"
atualizado_em: "2026-10-02T15:45:47Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "Geração de Guias", "GRRF", "FGTS", "Pessoal+", "ID: br.com.sankhya.rh.GeracaoGuias", "Integração Financeira da Guia de Recolhimento Rescisório do FGTS - GRRF", "Valor p/JAM"]
---

# Como integrar a GRRF ao financeiro

**Módulo:** Pessoal+
**Caminho de Acesso:**Pessoal+ > Rotinas Folha > Geração de Guias
**ID da Tela:** br.com.sankhya.rh.GeracaoGuias

---

## Descrição e Usabilidade

Após a geração da GRRF, o sistema permite realizar a integração financeira dos valores relacionados ao recolhimento rescisório do FGTS.

Essa funcionalidade possibilita:

- gerar demonstrativos para conferência;
- integrar títulos financeiros;
- controlar vencimentos;
- registrar encargos e juros;
- centralizar o controle financeiro da GRRF.

A integração é utilizada principalmente para automatizar os lançamentos financeiros relacionados às guias rescisórias.

### Pré-requisitos

Antes da integração financeira, é necessário:

- [GRRF previamente gerada](https://ajuda.sankhya.com.br/hc/pt-br/articles/40469921798935);
- folha rescisória calculada;
- configuração financeira cadastrada;
- usuário com acesso à rotina financeira da GRRF.

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/40476542714775)

1. Acesse a tela**Geração de Guias**(Pessoal+ > Rotinas Folha);
2. Clique no card **GRRF**;
3. Selecione a ação **Financeiro**;
4. Utilize a aba **Geral** para configuração das informações da guia:

   - **Informações Gerais**

     Configure os campos:

     - **Saldo FGTS**;
     - **Aviso Prévio**;
     - **Dissídio**: utilize essa marcação quando houver:

       - diferenças salariais;
       - folha complementar;
       - verbas indenizatórias retroativas.
     - **Imprimir Mês Anterior**: essa marcação só tem efeito se, no cálculo da rescisão, a opção **Calcula Mês Anterior** também tiver sido marcada.

       Com as duas opções marcadas, você pode escolher se o campo **25 - Mês Anterior a Rescisão** será impresso na guia.
   - **Dados da Folha**

     Configure:

     - **Tipo de Folha**;
     - **Referência**;
     - **Vencimento**;
     - **Empresa**;
     - **Período de demissão**;
     - **Seleção de funcionários**.

       **⚠️ S**elecione corretamente os trabalhadores que devem compor a integração financeira e confirme.
   - **Encargos e JAM**

     As seções abaixo são utilizadas para cálculos relacionados a pagamentos fora do prazo.

     - **Valores**;
     - **Valor p/JAM**;
     - **Encargos**.
5. Após preencher as informações, clique em **Gerar Demonstrativo**.

   O sistema exibirá os valores calculados para conferência antes da integração financeira.

   Nessa etapa é possível:

- validar valores;
- conferir encargos;
- imprimir o demonstrativo;
- revisar inconsistências.

6. Após conferir os dados, acesse a aba **Integração Financeira**;

   Configure:

- data de negociação;
- data de vencimento;
- data de entrada e saída;
- natureza;
- histórico.

7. Após preencher as informações financeiras, clique em **Integrar Financeiro.**

   O sistema realizará a geração dos títulos financeiros vinculados à GRRF.

### Pontos de Atenção

- **Conferência antes da integração**

  Sempre valide o demonstrativo antes de integrar os títulos financeiros.
- **Encargos por atraso**

  Pagamentos realizados fora do prazo podem gerar:

  - juros;
  - encargos;
  - JAM.
- **Dissídio e verbas complementares**

  Folhas complementares podem alterar os valores da integração financeira.
- **Configuração financeira**

  A integração depende de uma configuração financeira válida no sistema.

### Dicas de Usabilidade

- Gere o demonstrativo antes da integração;
- Valide encargos e juros em pagamentos atrasados;
- Confira vencimentos antes da geração dos títulos;
- Utilize históricos padronizados para facilitar auditorias;
- Revise os funcionários selecionados antes da integração.

## Artigos Relacionados

- [Geração da Guia de Recolhimento Rescisório do FGTS - GRRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/40469921798935)
- [Cálculos de Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
- [Geração do arquivo do Seguro-Desemprego](https://ajuda.sankhya.com.br/hc/pt-br/articles/7080813239831)
