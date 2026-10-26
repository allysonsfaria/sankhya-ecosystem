---
id: "38157621895191"
titulo: "Como configurar moléstia grave para isenção do IRRF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38157621895191-Como-configurar-mol%C3%A9stia-grave-para-isen%C3%A7%C3%A3o-do-IRRF"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Configurações de Tipos de Ocorrências"
atualizado_em: "2026-10-02T15:27:42Z"
rotulos: ["Configuração", "Impostos", "ID: br.com.sankhya.cadastro.funcionarios", "eSocial", "S-2230", "Central do eSocial", "Evento S-1210", "Pessoal+", "IRRF", "Afastamento previdenciário", "Moléstia Grave", "Lei Federal n.º 7.713/1988 - Artigo 6º inciso XIV."]
---

# Como configurar moléstia grave para isenção do IRRF

A **moléstia grave** é uma condição de saúde prevista em lei que garante **isenção de Imposto de Renda (IRRF)** sobre determinados rendimentos, como aposentadoria, pensão ou reforma.

No Pessoal+, essa configuração é importante para que o **IRRF não seja calculado indevidamente** na folha de pagamento do colaborador.

A isenção de IRRF para portadores de moléstia grave é garantida pela legislação brasileira conforme a [Lei Federal n.º 7.713/1988 - Artigo 6º, inciso XIV](https://www.planalto.gov.br/ccivil_03/leis/l7713.htm).

São doenças definidas pela legislação do Imposto de Renda, como, por exemplo:

- Neoplasia maligna (câncer);
- Cardiopatia grave;
- Doença de Parkinson;
- Esclerose múltipla;
- AIDS;
- Alienação mental;
- Outras previstas em lei.

### Pré-requisitos

Antes de realizar a configuração, é necessário:

- Cadastro do colaborador já criado no sistema;
- Laudo médico oficial que comprove a moléstia grave;
- Data de início da condição informada no laudo;

⚠️ A isenção só é válida quando existe laudo médico conforme exigido pela legislação.

### Jornada de Uso

(1)** Cadastro do colaborador**

1. Acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Localize e abra o cadastro do colaborador.
3. Vá até a aba **Contrato** e preencha o campo **Data do Laudo de Moléstia Grave** conforme o laudo médico.

![Imagem 1: Vá até a aba Contrato e preencha o campo Data do Laudo de Moléstia Grave conforme o laudo médico.](https://ajuda.sankhya.com.br/hc/article_attachments/38159033056791)

💡 A data é essencial para que o sistema aplique a isenção do imposto de renda a partir do período correto.

**(2)** **Lançamento do laudo**

Em caso de afastamento, acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha) e faça o lançamento do laudo comprovante da moléstia grave para o colaborador.

[GIF animado: Imagem 2: Em caso de afastamento, acesse a tela Ocorrências (Pessoal+ > Rotinas Folha) e faça o lançamento do laudo comprovante…](https://ajuda.sankhya.com.br/hc/article_attachments/38169393085335)

📌 Lembre-se também de **gerar e enviar o evento S-2230** (Afastamento temporário) na **Central do eSocial** (Pessoal+ > Rotinas Folha).

(3)** Processo Trabalhista**

Na tela **Processo Trabalhista** (Pessoal+ > Rotinas Folha) existe o campo **Data da moléstia grave atribuída pelo laudo**, utilizado para registrar essa condição quando houver pagamento de valores decorrentes de decisão judicial.

Essa informação permite identificar situações em que **rendimentos pagos em processo trabalhista podem ter tratamento diferenciado na apuração do IRRF**, conforme a legislação vigente.

O comportamento do campo depende do vínculo do trabalhador com o declarante:

- **Funcionário contratado pelo declarante:** o campo será **preenchido automaticamente** com a mesma data informada no campo **Data do Laudo de Moléstia Grave**, localizado na aba **Contrato** da tela **Configuração Funcionários**.
- **Funcionário não contratado pelo declarante:** a **Data da Moléstia Grave deve ser informada manualmente**, conforme o laudo médico apresentado.

![Imagem 3: Funcionário não contratado pelo declarante: a Data da Moléstia Grave deve ser informada manualmente , conforme o laudo…](https://ajuda.sankhya.com.br/hc/article_attachments/38932001551255)

(4)** Cálculo da folha de pagamento**

- Realize o cálculo da folha normalmente;

  O sistema aplica a fórmula de isenção automaticamente para os cadastros que estiverem com o campo **Data do Laudo de Moléstia Grave** preenchido.
- Confira se os valores estão corretos, sem desconto de IRRF.

  - A isenção aplica-se a:

    - IRRF Mensal
    - IRRF de Férias
    - IRRF de 13º salário
- Feche a folha e libere-a ao eSocial.
- Os valores continuam a aparecer no holerite, mas sem desconto de imposto.

**Exemplos:**

**Cenário 1:** Funcionário com Moléstia Grave comprovada

Neste cenário, o colaborador possui **laudo médico válido**, com data informada no cadastro. Por isso, o sistema **não calcula o IRRF** na folha de pagamento.

Funcionário: João da Silva
Empresa: 1
Código do Funcionário: 1
Data do Laudo: 15/03/2025

**Folha de Pagamento – Janeiro/2026**

├─ Salário Base: R$ 5.000,00
├─ IRRF (9040): R$ 0,00  ✅ Isento por moléstia grave
├─ INSS: R$ 501,50     
└─ Líquido: R$ 4.498,50

📌 **Resultado:** mesmo com rendimentos tributáveis, o IRRF não é descontado, pois o colaborador possui moléstia grave registrada no sistema.

---

**Cenário 2:** Funcionário sem Moléstia Grave

Neste cenário, o colaborador **não possui laudo informado** no cadastro. Assim, o sistema realiza o **cálculo normal do IRRF**, conforme a tabela vigente.

Funcionário: Maria Santos
Empresa: 1
Código do Funcionário: 2
Data do Laudo: não informada

**Folha de Pagamento – Janeiro/2026**

├─ Salário Base: R$ 5.000,00
├─ IRRF (9040): R$ 327,50  (conforme tabela de IRRF)
├─ INSS: R$ 501,50
└─ Líquido: R$ 4.171,00

📌 **Resultado:** como não há moléstia grave cadastrada, o IRRF é calculado e descontado normalmente.

**(5)**  **Envio do evento ao eSocial**

Acesse a **Central do eSocial** (Pessoal+ > Rotinas folha) para [gerar e enviar o evento S-1210](https://ajuda.sankhya.com.br/hc/pt-br/articles/37960826085271).

### Pontos de Atenção

- A **data de início da moléstia** é essencial para aplicação correta da isenção.
- A isenção se aplica **somente ao IRRF**, não afetando INSS ou outros descontos.
- A aplicação da isenção deve seguir rigorosamente a legislação vigente.
- As informações relacionadas à **moléstia grave** e à **retenção de IRRF** também impactam a forma como os valores são demonstrados no **Informe de Rendimentos**. A apresentação pode variar conforme exista ou não **processo trabalhista** vinculado ao colaborador.

  - Funcionário com Moléstia Grave **sem processo trabalhista**

    O sistema considera a **isenção de IRRF** nos rendimentos que se enquadram na legislação. No **Informe de Rendimentos**, os valores são apresentados da seguinte forma:

    - Os **rendimentos pagos** aparecem normalmente na seção de rendimentos.
    - O **IRRF** não é demonstrado como valor retido.
    - Os valores podem ser apresentados na parte de **rendimentos isentos**, quando aplicável.
  - Funcionário com Moléstia Grave **com processo trabalhista**

    Quando existe **processo trabalhista**, os valores pagos por decisão judicial ou acordo podem ser apresentados **separadamente** no Informe de Rendimentos.

    Nesse caso, o sistema considera:

    - Dados do **processo trabalhista cadastrado**
    - Natureza dos valores pagos
    - Incidência ou não de **IRRF sobre rendimentos recebidos acumuladamente (RRA)**

    No **Informe de Rendimentos**, os dados podem aparecer em seções específicas, como:

    - **Rendimentos Recebidos Acumuladamente (RRA)**
    - **Valores decorrentes de processo judicial**

### Dicas de Usabilidade

- Sempre valide a configuração conferindo o holerite após o cálculo da folha.
- Mantenha a documentação médica arquivada para eventuais auditorias.
- Caso a moléstia tenha início retroativo, revise as folhas já calculadas, se necessário.

## Artigos Relacionados

- [Cadastro do Funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)

  [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/38157621895191-Como-configurar-mol%C3%A9stia-grave-para-isen%C3%A7%C3%A3o-do-IRRF#top)
