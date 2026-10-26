---
id: "38858116404503"
titulo: "Cadastro de Carga Horária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Jornada, Escalas e Calendário"
atualizado_em: "2026-09-30T17:31:43Z"
rotulos: ["Configuração", "Carga Horária", "Jornada de Trabalho", "br.com.sankhya.rh.CargaHoraria", "eSocial", "Folha de Pagamento", "Pessoal+"]
---

# Cadastro de Carga Horária

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros
**ID da Tela:**br.com.sankhya.rh.CargaHoraria

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria#h_01KK22J26Z03N30NW2PHV0VSRA)

1. [Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria#h_01KK22BJSPANCMHZB70MGR9G0Q)
2. [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria#h_01KK22BJSXEK0C13CDPGF8B43V)
3. [Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria#h_01KK22BJT17XKWE63T2T7SFE5C)
4. [Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria#h_01KK22BJVJB6N473Y0HT4W1T5W)
5. [Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria#h_01KK22BJVQDNXPWB9Y6A3GMS0Q)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria#h_01KK22BJVSE3JXW4HZ26AXBE2R)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **Carga Horária** define a jornada de trabalho do colaborador, indicando os dias e horários previstos de **entrada, saída, intervalos e folgas**.

A legislação trabalhista estabelece uma jornada máxima de **44 horas semanais** para trabalhadores sob regime CLT. No sistema, o cadastro da carga horária permite controlar essa jornada e apoiar o cálculo correto de horas extras, atrasos, banco de horas e demais apurações de ponto.

Além disso, essas informações são utilizadas para a geração das informações enviadas ao **eSocial**.

No sistema existem dois conceitos principais:

- **Carga Horária:** utilizada quando o horário é flexível, sendo necessário apenas cumprir a quantidade de horas diárias prevista.
- **Jornada de Trabalho:** utilizada quando os horários de entrada e saída são fixos, permitindo ao sistema validar as batidas de ponto e identificar atrasos ou horas extras.

### 2. Pré-requisitos

**Permissões necessárias**

- Deve **ter acesso liberado para a tela Carga Horária**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

**Configurações relacionadas**

Antes de cadastrar uma carga horária, verifique:

- Se a empresa já possui regras definidas de jornada ou escalas de trabalho.
- Se existem convenções ou acordos coletivos que impactam a jornada.
- Se os horários e intervalos já estão definidos para os funcionários.

### 3. Jornada de Uso

Esta tela define o comportamento de cada carga horária em relação aos direitos trabalhistas, à flexibilidade de horários, integração com eSocial e conformidades com normas.

[GIF animado: Imagem 1: Esta tela define o comportamento de cada carga horária em relação aos direitos trabalhistas, à flexibilidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/38901572237847)

#### 3.1 Cadastrar uma carga horária

1. Acesse a tela **Carga Horária** (Pessoal+ > Cadastros).
2. Clique em **Cadastrar Identificação da Carga Horária**.
3. Preencha os campos principais:

   - **Descrição**: nome que identifique facilmente a jornada.
   - **Cód. Carga Horária**: pode ser gerado automaticamente ou manualmente, conforme a configuração definida por meio do botão ![Imagem 2: Cód. Carga Horária : pode ser gerado automaticamente ou manualmente, conforme a configuração definida por meio do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/38901729792407) **Configuração da Tela**, opção **Numeração**.
   - **Tipo Carga Horária**:

     - Carga Horária (horário flexível)
     - Jornada de Trabalho (horário fixo)
4. Informe o **Tipo de Jornada**, conforme o modelo de trabalho adotado pela empresa, como:

   - Jornada 12x36;
   - Jornada com folga fixa;
   - Jornada com folga variável;
   - Turno ininterrupto de revezamento;
   - Demais tipos de jornada.
5. Marque a opção **Possui Horário Noturno** caso a jornada inclua trabalho no período noturno.
6. Clique em ![Imagem 3: Clique em Salvar (F7) .](https://ajuda.sankhya.com.br/hc/article_attachments/38901729799319) **Salvar [F7]**.
7. Configure as abas abaixo:

(3)**Aba Geral**

Nesta aba são definidas as configurações principais da carga horária.

Principais campos:

- **Ativa:** habilita a carga horária para uso.
- **Permite flexibilidade de horário:** permite variação no horário de entrada ou saída.
- **Considera redução de horas noturnas:** aplica a redução legal da hora noturna.
- **Compõe eSocial:** envia as informações da jornada ao eSocial.

Também é possível configurar **alternância de jornadas**, permitindo que colaboradores alternem entre escalas diferentes.

**(3)Aba Escala de Serviço**

Na aba **Escala de Serviço**, é possível definir escalas de trabalho.

Exemplo:
**Escala 5x2** → trabalha cinco dias e folga dois.

Para configurar:

1. Marque **Escalonar Dias de Trabalho** e informe:

   - o número de **Dias de Trabalho;**
   - o número de **Dias de Folga;**
   - **a Quantidade de Turnos.**

Também é possível configurar regras de feriados e DSR para a apuração do ponto.

- Considera Ocorrências nos Feriados
- Considerar Folga com percentual de DSR/Feriado
- Considera Súmula nº444 TST:
- Considerar feriado VA e VT:

(3)**Aba Intervalo**

Na aba **Intervalo**, configure as regras de descanso.

Defina:

- **Tipo**

  - Fixo
  - Variável
  - Sem intervalo
- **Duração em minutos**
- **Horário de início** e **término**
- **Aplica Tolerância**

A seção **Pausa** é destinada às indicações de pausas durantes os turnos da carga horária, com regras de tolerância, horas extras ou atrasos.

(3)**Aba Horário**

Na aba **Horário**, são definidos os horários de entrada e saída para cada dia ou sequência da escala.

Para cadastrar:

1. Clique em **Cadastrar Configurações de Ponto**.
2. Informe:

   - **Dia da semana ou sequência da escala**
   - **Turno**
   - **Entrada do turno**
   - **Saída do turno**

     Também é possível configurar:

- Validação de **entrada e saída** no ponto;
- **Descanso semanal**;
- **Duração da jornada para o eSocial**.

3. Caso existam pausas durante o turno, utilize a **sub-aba Paradas Programadas** para registrar esses períodos.
4. Para agilizar o cadastro de outros dias ou turnos, utilize o botão **Duplicar**.
5. Após finalizar as configurações, clique em ![Imagem 4: Após finalizar as configurações, clique em Salvar (F7) .](https://ajuda.sankhya.com.br/hc/article_attachments/38901729799319) **Salvar [F7]**.

### 4. Pontos de Atenção

- A carga horária influencia diretamente o **controle de ponto, cálculo de horas extras e banco de horas**.
- Certifique-se de cadastrar corretamente **intervalos e descansos semanais**.
- Para escalas fixas, é necessário cadastrar **todos os dias trabalhados e os dias de folga**.
- Alterações na carga horária podem impactar funcionários que já utilizam essa configuração.
- Quando uma carga horária estiver vinculada a colaboradores, a alteração dos horários seguirá as seguintes regras:

  - **Permite alteração quando:**

    - Não existirem registros de ponto nas tabelas **TFPPONFECHAMENTO** ou **TFPRPO** nos **últimos 2 meses** (contados da data atual).
  - **Não permite alteração quando:**

    - Existirem registros de ponto nesse período.
    - Nesse caso, o sistema apresentará a mensagem:

      **“Não é possível alterar/excluir, pois existe lançamento para esta Carga Horária no módulo de Ponto.”**
  - **Carga horária sem vínculo**

    - Se a carga horária **não estiver vinculada a colaboradores**, todas as alterações de horários podem ser realizadas normalmente.
- Verifique se a opção **Compõe eSocial** está marcada quando a jornada precisa ser enviada ao governo.

### 5. Dicas de Usabilidade

- Utilize descrições claras, como:
  **"Escala 12x36 Noturna"** ou **"Jornada Comercial 44h"**.
- Utilize o botão **Duplicar** para acelerar o cadastro de horários semelhantes.
- Padronize as cargas horárias da empresa para facilitar a manutenção e o controle de ponto.

### Artigos Relacionados

- [Inclusão e Alteração de Carga Horária no Cadastro do Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/38911679393175)
- [Cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599)
