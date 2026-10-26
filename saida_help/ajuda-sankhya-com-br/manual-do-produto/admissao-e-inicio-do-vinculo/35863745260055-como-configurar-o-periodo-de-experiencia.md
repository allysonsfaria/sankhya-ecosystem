---
id: "35863745260055"
titulo: "Como configurar o período de experiência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35863745260055-Como-configurar-o-per%C3%ADodo-de-experi%C3%AAncia"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Admissão e Início do Vínculo"
atualizado_em: "2026-10-02T15:03:54Z"
rotulos: ["Configuração", "Funcionários", "Contrato", "Admissão", "eSocial", "Configuração Funcionários", "Período de Experiência", "Pessoal+", "Contrato temporário", "Menor aprendiz", "Dispensado da Experiência"]
---

# Como configurar o período de experiência

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros > Configuração Funcionários > Aba Admissão > Período de Experiência
**ID da Tela:** br.com.sankhya.cadastro.funcionarios

---

## Descrição e Usabilidade

O **Período de Experiência** é utilizado para definir as regras do contrato inicial do colaborador, permitindo estabelecer prazos e condições conforme a legislação trabalhista.

Essa configuração é utilizada para:

- controlar os prazos do contrato de experiência;
- garantir conformidade com o limite legal de até 90 dias;
- definir corretamente as informações enviadas ao eSocial.

A seção será exibida apenas para vínculos que permitem contrato de experiência, como:

- Contrato temporário (50);
- Menor aprendiz (55);
- Prazo determinado – pessoa jurídica ou física, urbano ou rural (60, 65, 70, 75)

Para outros vínculos (como estagiário, servidor público, autônomo, pensionista, diretor sem vínculo empregatício, funcionário avulso, entre outros (02, 10, 15, 20, 25, 30, 31, 35, 40, 80, 90, 99), essa seção não será exibida, pois não se aplica contrato de experiência.

### 1. Descrição da Funcionalidade

O cadastro das informações de contrato de experiência é feito na tela **Configuração Funcionários**, na aba **Admissão** > **Período de Experiência**.

Os campos dessa seção funcionam da seguinte maneira:

- **Dispensado da Experiência**: ao ativá-la, todos os campos de período são desabilitados e será necessário informar apenas a **Data Término do Contrato**.

**Nota:** para os contratos temporários e por prazo determinado, é obrigatório informar a **Data Término do Contrato**. Caso não seja preenchida, o sistema exibirá a seguinte mensagem:

**"A data de término do contrato é obrigatória quando o vínculo for prazo determinado ou contrato temporário."**

Entretanto, se o campo **Objeto determ. contratação por prazo determinado (obra, serv., safra, etc.)** estiver preenchido, a **Data Término do Contrato** não será obrigatória. Nesse caso, o sistema envia automaticamente ao eSocial que o contrato é por prazo determinado vinculado a um fato (como obra, serviço ou safra).

- **Dias do 1º e do 2º período**: define a quantidade de dias de cada período de experiência.

  - O sistema calcula automaticamente as datas de vencimento.
  - O limite total permitido é de **90 dias**, seja em um único período ou na soma dos dois.

  ⚠️ Caso ultrapasse esse limite, o sistema exibirá alerta.
- **Referência para vencimento do 2º período**: define qual data será utilizada como base para cálculo do segundo período:
  - **Data de admissão:** cálculo a partir da admissão.
  - **Data de vencimento do 1º período:** cálculo a partir do fim do primeiro período.

    **Nota:** para novos cadastros, o sistema considera por padrão a data de admissão como referência inicial.

| 🔧 Se o campo **"Referência para vencimento do 2º período"** não aparecer na sua tela:   1. Clique no botão Configuração da Tela. 2. Abra a aba Admissão. 3. Em Campos disponíveis, pesquise por "Referência para vencimento do 2º período". 4. Dê um duplo clique no campo para movê-lo para os Campos exibidos. 5. Clique em Salvar para aplicar as alterações. |
| --- |

- **Possui Cláusula de Suspensão da Experiência por Afastamento**: deve ser marcada se houver afastamento não relacionado ao trabalho (como licença médica comum ou outro motivo pessoal), assim, a data de término do contrato será prorrogada para compensar o período de afastamento.

Acesse também o artigo [Suspensão de Contrato de Experiência por Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/29875364946199) para compreender como o sistema trata essas situações no cálculo e no envio ao eSocial.

### 2. Pré-requisitos

Antes de configurar o período de experiência:

- O colaborador deve estar cadastrado.
- O vínculo deve permitir contrato de experiência.
- A data de admissão deve estar informada.

### 3. Jornada de Uso

1. Na tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Localize o colaborador;
3. Acesse a aba **Admissão > Período de Experiência**;
4. Preencha conforme necessário:
   - informe os dias do 1º e 2º período;
   - defina a referência de cálculo do 2º período;
   - caso aplicável, marque a dispensa da experiência;
   - informe a data de término do contrato (quando necessário).
5. Salve as alterações.

🔹 Exemplo 1 – **Referência pela data de admissão**

Data de admissão: 02/06/2025

Dias para vencimento do 2º período: 45 dias

Dias para vencimento do 2º período: 90 dias

Data de vencimento do 1º período = 16/07/2025

Data de vencimento do 2º período = 02/06/2025 + 90 = 30/08/2025

🔹 Exemplo 2 – **Referência pelo 1º período**

Data de admissão: 02/06/2025

Dias do 1º período: 45 dias → Vencimento em 16/07/2025

Dias do 2º período: 45 dias

Data de vencimento do 2º período = 16/07/2025 + 45 = 30/08/2025

### 4. Pontos de Atenção

- O período total não pode ultrapassar **90 dias**.
- A data de término é obrigatória para contratos por prazo determinado, exceto quando houver objeto da contratação informado.
- A escolha da referência impacta diretamente o cálculo do vencimento.
- A marcação de suspensão altera automaticamente a data final do contrato.

### 5. Dicas de Usabilidade

- Utilize dois períodos (ex: 45 + 45) para melhor controle contratual.
- Revise os cálculos de vencimento antes de salvar.
- Utilize a cláusula de suspensão apenas quando houver previsão contratual.
- Garanta que as informações estejam alinhadas com o contrato formal.

## Perguntas Frequentes (FAQ)

**1. Posso cadastrar mais de dois períodos de experiência?**

Não. O sistema permite apenas dois períodos, respeitando o limite total de 90 dias.

**2. O que acontece se ultrapassar 90 dias?**

O sistema exibirá um alerta e não permitirá o cálculo correto do contrato.

**3. Quando a data de término do contrato não é obrigatória?**

Quando o campo **Objeto da contratação por prazo determinado** estiver preenchido.

**4. O que acontece ao marcar a suspensão por afastamento?**

O sistema prorroga automaticamente a data final do contrato, considerando o período de afastamento.

## Artigos Relacionados

- [Suspensão de Contrato de Experiência por Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/29875364946199)
- [Cadastro do Funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
