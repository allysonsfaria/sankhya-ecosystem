---
id: "42546913948055"
titulo: "Como cadastrar ocorrências com estabilidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055-Como-cadastrar-ocorr%C3%AAncias-com-estabilidade"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Configurações de Tipos de Ocorrências"
atualizado_em: "2026-10-02T15:27:42Z"
rotulos: ["FPCODHISESTABIL", "Indenização de Estabilidade", "Cadastro de Ocorrências com Estabilidade para Folha de Pagamento", "Quantos meses de estabilidade?"]
---

# Como cadastrar ocorrências com estabilidade

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Ocorrências > Cadastro
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O Pessoas+ permite controlar a estabilidade provisória do colaborador por meio das ocorrências cadastradas no sistema.

Esse controle pode ser realizado de duas formas:

- pela própria ocorrência de afastamento;
- por uma ocorrência específica destinada ao controle da estabilidade.

A configuração correta garante que o sistema reconheça automaticamente períodos de estabilidade durante rotinas como aviso-prévio, provisões e cálculo de rescisão.

### 2. Pré-requisitos

- Permissão para cadastrar **Ocorrências** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Configuração do parâmetro **Cód. Hist. Ocorr. para Estabilidade - FPCODHISESTABIL** quando utilizada uma ocorrência específica para estabilidade.

### 3. Jornada de Uso

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha);
2. Informe a **Empresa** e o **Tipo de Filtro** e clique em **Pesquisar**;
3. Localize a **Ocorrência** cadastrada;

   O sistema permite controlar a **estabilidade do colaborador** de duas formas:

   #### 🔹Controle pela Própria Ocorrência de Afastamento

   Quando a estabilidade estiver diretamente relacionada ao afastamento (como em situações previstas pela legislação), basta configurar a própria ocorrência.

   4. marque a propriedade **Indenização de Estabilidade**;
   5. informe a **quantidade de meses de estabilidade**;
   6. salve as alterações.

      ![Imagem 1: salve as alterações.](https://ajuda.sankhya.com.br/hc/article_attachments/42547812882711)

      Após o retorno do colaborador, o sistema reconhecerá automaticamente o período de estabilidade durante os cálculos trabalhistas, além disso:

      - se for lançado um aviso-prévio, o sistema exibe um **alerta**.
      - se a rescisão for calculada, o sistema verifica se aplica **quebra de estabilidade** e faz os cálculos necessários.

      #### 🔹Controle por Ocorrência Específica de Estabilidade

      Também é possível criar uma ocorrência exclusiva para controlar a estabilidade.

      Nesse caso:

      1. cadastre uma nova ocorrência;
      2. marque **Indenização de Estabilidade**;
      3. configure a quantidade de meses de estabilidade;
      4. salve as alterações;

         ![Imagem 2: salve as alterações;](https://ajuda.sankhya.com.br/hc/article_attachments/42547812883991)
      5. acesse a tela **Preferências** (Configurações > Avançado) e informe o código dessa ocorrência no parâmetro **FPCODHISESTABIL**.

         ![Imagem 3: acesse a tela Preferências (Configurações > Avançado) e informe o código dessa ocorrência no parâmetro FPCODHISESTABIL .](https://ajuda.sankhya.com.br/hc/article_attachments/42547818246295)

         Sempre que essa ocorrência for lançada para um colaborador, o sistema aplicará automaticamente as regras de estabilidade correspondentes.

#### Comportamento do sistema

Quando houver estabilidade vigente, o Pessoas+ poderá:

- identificar automaticamente o período protegido;
- emitir alertas durante o aviso-prévio;
- considerar a estabilidade no cálculo da rescisão;
- calcular indenizações, quando aplicável.

### 6. Pontos de Atenção

- A propriedade **Indenização de Estabilidade** deve estar marcada.
- Reserve o uso do parâmetro **FPCODHISESTABIL** para um único tipo "guarda-chuva" de estabilidade manual, evitando cadastrar vários tipos concorrentes para o mesmo controle.
- Configure corretamente a quantidade de meses de estabilidade.
- Alterações nessas configurações podem impactar cálculos futuros.

### 7. Dicas de Usabilidade

- Utilize a própria ocorrência quando a estabilidade decorrer diretamente do afastamento.
- Utilize uma ocorrência específica apenas quando houver necessidade de controle individualizado.
- Valide a configuração antes de realizar cálculos de rescisão.

## Perguntas Frequentes (FAQ)

**1. Preciso criar uma ocorrência específica para controlar estabilidade?**

Não. Quando a estabilidade estiver vinculada ao afastamento, basta configurar a própria ocorrência.

**2. Quando devo utilizar uma ocorrência específica?**

Quando a empresa desejar controlar situações de estabilidade de forma independente do afastamento.

**3. O que acontece se o parâmetro FPCODHISESTABIL não estiver configurado?**

As ocorrências específicas de estabilidade não serão reconhecidas para aplicação automática das regras.

**4. A estabilidade interfere na rescisão?**

Sim. O Pessoas+ considera a estabilidade durante o cálculo da rescisão e aplica as regras correspondentes.

## Artigos Relacionados

- [Cadastro de Ocorrências para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
- [Configurações das Propriedades da Ocorrência para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42544737715479)
- [Lançamento de Ocorrências para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/42603052607255)
- [Quitação de Férias em caso de Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/31144991936151)
