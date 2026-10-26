---
id: "34613039791383"
titulo: "Integração de ATS <> Vlow"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com Gestão de Talentos e ATS"
atualizado_em: "2026-09-26T01:41:49Z"
rotulos: ["Configuração", "Integração", "Admissão", "Mindsight", "Integração de ATS <> Vlow", "Contratação de um candidato", "Configuração da vaga", "Endpoints acessados no Vlow", "Vlow", "Pessoas+"]
---

# Integração de ATS <> Vlow

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K4STVR7FGYH4XWP7AAXT8WRH)

1. [Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K4STVR7G7A6BHQA6RH6B0DHG)
2. [Fluxo de integração entre os sistemas](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K4STWGTZ6ESA412EWN756X3K)
3. [Campos integrados com a folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K439TWJEA1G7WDB1J43NG345)
4. [Endpoints acessados no Vlow](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K43A3YR7SAAS71QCPT6GB3Y7)

[Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K455KJMSC6X20TBRNE6MZT7Y)

1. [Data limite para admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K4AAM470BNQP5RSPDAM21477)
2. [Configurações da vaga na Mindsight](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K455KJMSC6X20TBRNE6MZT7Y)
3. [Contratação do candidato](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K45658JM3AKE7YGRAKYHGP3M)
4. [Acompanhamento da integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K459163NXPM8S0BZXQYT4T5V)
5. [Processo admissional no Vlow](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K45AHTX6Z0HXFXMH1ZGREDNJ)

[Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K4SV425G4YVDG5TSRF23PZPV)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K4SV56MHY9370YPVB61XFZ6A)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K4SV5395BQBA5F8KFF2TD47K)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A integração entre **Sankhya Om (Pessoas+)**, **Mindsight (ATS)** e **Vlow (Vixting)** automatiza e agiliza o processo de admissão, conectando recrutamento, admissão e saúde ocupacional em um fluxo digital único:

- o RH abre a requisição de vaga no **Mindsight (ATS)** já cria a vaga sem passar pelo processo de requisição e aprovação;
- quando o candidato é aprovado, seus dados são enviados para a **Vlow (Vixting)**, que gerencia a admissão e os processos de saúde ocupacional;
- por fim, todas as informações são integradas ao **Pessoas+**, garantindo que a gestão de pessoal seja feita com segurança e eficiência.

### 2. Fluxo de integração entre os sistemas

1. **Configuração da vaga:** Vlow → ATS
2. **Contratação de um candidato:** ATS → Vlow

### 3. Campos integrados com a folha

A integração entre o **Vlow** e o **ATS** garante que as informações fluam automaticamente entre os sistemas. Atualmente, os seguintes dados são integrados:

- **empresa;**
- **filiais;**
- **unidades de negócio;**
- **cargos;**
- **departamentos.**

Além disso, no momento em que o candidato é aprovado no **ATS**, outras informações essenciais para a admissão são coletadas e enviadas diretamente para o **Vlow**, como:

- nome;
- e-mail;
- CPF;
- celular;
- regime de trabalho;
- data limite para conclusão da admissão;
- salário do candidato.

### 4. Endpoints acessados no Vlow

A integração faz requisições GET nos seguintes endpoints:

- /company/groups;
- /company/affiliates;
- unit-business;
- /job-role;
- /department.

A integração faz requisições POST no seguinte endpoint:

- /employee.

## Jornada de uso

### 1. Data limite para admissão

A data limite define até quando o candidato pode concluir seu processo no Vlow. Clique na sua foto (canto superior direito da tela) e, em seguida, em Configurações > Integrações > Vixting.

[GIF animado: Imagem 1: A data limite define até quando o candidato pode concluir seu processo no Vlow. Clique na sua foto (canto superior…](https://ajuda.sankhya.com.br/hc/article_attachments/34627497964055)

Ela pode ser configurada de duas formas no ATS:

- **Referência pela data atual**: soma a data de hoje + número de dias configurados.

  **Exemplo:** considerando que o número de dias configurado foi 3 e o recrutador está movendo um candidato para a etapa de contratados no dia 07/02/2025, então a data limite será 10/02/2025 (três dias após a data atual).
- **Referência pela data de admissão**: data da admissão – número de dias configurados.

  **Exemplo:** considerando que o número de dias configurado foi 3 e o recrutador marcou o dia 07/02/2025 como a admissão desse candidato, então a data limite será 04/02/2025 (três dias antes da data de admissão).

Essa data também pode ser editada manualmente no momento da contratação. 

### 2. Configuração da vaga na Mindsight

Na criação ou edição da vaga, selecione:

- empresa;
- filial;
- cargo;
- departamento.

Esses dados definem onde o colaborador será alocado. Se a vaga não tiver todos os campos preenchidos, não será possível enviá-la para o Vlow na contratação.

[GIF animado: Imagem 2: Esses dados definem onde o colaborador será alocado. Se a vaga não tiver todos os campos preenchidos, não será possível…](https://ajuda.sankhya.com.br/hc/article_attachments/34627829185431)

### 3. Contratação do candidato

Ao mover o candidato para etapa de **Contratado(a)**, deve-se ativar a opção **"Enviar para o processo de admissão da Vixting"**, assim, o modal se expandirá com os dados necessários para a integração.

Caso a vaga não tenha todos os campos de integração preenchidos, não será possível enviar o candidato para a Vixting no momento em que o recrutador for realizar a etapa de contratação. Um aviso será exibido, solicitando que a vaga seja editada com todos os dados requeridos pela integração.

Faça o cadastro e envio do formulário de admissão, preenchendo:

- empresa, filial, cargo e departamento;
- CPF, e-mail, celular;
- regime de trabalho e data limite para admissão.

![Imagem 3: regime de trabalho e data limite para admissão.](https://ajuda.sankhya.com.br/hc/article_attachments/34627964194711)

Depois da confirmação, os dados são enviados ao Vlow. O candidato recebe automaticamente o formulário por e-mail ou WhatsApp, e os próximos passos ficam com o Departamento Pessoal no Vlow.

💡 Importante salientar que mesmo após o envio, o DP pode corrigir ou atualizar os dados no Vlow.

Observe abaixo, todo o processo da contratação.

[GIF animado: Imagem 4: Observe abaixo, todo o processo da contratação.](https://ajuda.sankhya.com.br/hc/article_attachments/34629448376727)

### 4. Acompanhamento da integração

Ao enviar um candidato para o Vlow, o ATS mostra o status do envio na aba **Contratados:**

- [Na Fila](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K5Y63RVYYAWP6HEV81FYEC8A)
- [Enviado](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K5Y64B6S4FRK6BKY5Q0V3A5C)
- [Erro](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383-Integra%C3%A7%C3%A3o-de-ATS-Vlow#h_01K5Y64EDX826JE5KAF2Q6JX78)

Esse status é representado por um ícone colorido que está ao lado do nome de cada candidato. Ao clicar sobre o ícone de status, será exibida a tela com os logs detalhados das integrações.

Nessa tela, o recrutador pode acompanhar todas as tentativas de envio de um candidato do ATS para o Vlow, incluindo:

- timeline com diferenciação por cores segundo o status da tentativa;
- status HTTP retornado (`201`, `400`, `408`, `409`, etc.);
- mensagem explicativa do sistema;
- data e hora de cada tentativa.

Com isso, o próprio usuário consegue entender por que um envio funcionou ou falhou, sem depender do suporte.

Exemplo:

![Imagem 5: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/35168217336727)

![Imagem 6: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/35168211753239)

![Imagem 7: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/35168217339671)

#### Na fila

Indica que os dados estão em processamento. 

O sistema faz até 5 tentativas automáticas de envio. A primeira ocorre no momento em que o recrutador move o candidato para essa etapa, e as demais são feitas com um intervalo de 1 hora entre elas. 

![Imagem 8: O sistema faz até 5 tentativas automáticas de envio. A primeira ocorre no momento em que o recrutador move o candidato…](https://ajuda.sankhya.com.br/hc/article_attachments/34629568107159)

#### Enviado

Os dados dessa admissão foram enviados com sucesso e o candidato já está no Vlow.

![Imagem 9: Os dados dessa admissão foram enviados com sucesso e o candidato já está no Vlow.](https://ajuda.sankhya.com.br/hc/article_attachments/34629706049687)

#### Erro

Indica que os dados não foram enviados para o Vlow após as 5 tentativas.

![Imagem 10: Indica que os dados não foram enviados para o Vlow após as 5 tentativas.](https://ajuda.sankhya.com.br/hc/article_attachments/34629770447895)

Se ocorrer erro, você pode clicar em **Enviar admissão** para reenviar. O candidato voltará ao status de "na fila" enquanto o sistema tenta reenviar seus dados.

[GIF animado: Imagem 11: Se ocorrer erro, você pode clicar em Enviar admissão para reenviar. O candidato voltará ao status de "na fila" enquanto…](https://ajuda.sankhya.com.br/hc/article_attachments/34630171136407)

Caso o problema persista, entre em contato com o CS responsável para uma investigação mais minuciosa.

### 5. Processo admissional no Vlow

Depois que os dados chegam ao Vlow:

1. O candidato recebe por e-mail um formulário para preencher.

   ![Imagem 12: O candidato recebe por e-mail um formulário para preencher.](https://ajuda.sankhya.com.br/hc/article_attachments/34630193610263)
2. Acessa o Vlow por meio do link enviado no e-mail e faz o cadastro de seus dados pessoais.

   ![Imagem 13: Acessa o Vlow por meio do link enviado no e-mail e faz o cadastro de seus dados pessoais.](https://ajuda.sankhya.com.br/hc/article_attachments/34630290074775)
3. O Departamento Pessoal acompanha e valida o processo direto no Vlow.

   ![Imagem 14: O Departamento Pessoal acompanha e valida o processo direto no Vlow.](https://ajuda.sankhya.com.br/hc/article_attachments/34630261248919)

## Pontos de atenção

- Todos os campos obrigatórios (empresa, filial, cargo, departamento) devem estar preenchidos na vaga para envio ao Vlow.
- Caso falte algum campo, o sistema impede o envio e solicita edição da vaga.
- O sistema realiza até 5 tentativas automáticas de envio dos dados ao Vlow, com intervalos de 1 hora.
- Em caso de erro, é possível reenviar manualmente; persistindo o problema, contate o suporte.

## FAQ – Dúvidas Frequentes

1. **Quais dados são integrados entre ATS e Vlow?**

   Empresa, filiais, unidades de negócio, cargos, departamentos, nome, e-mail, CPF, celular, regime de trabalho, data limite para admissão e salário.
2. **O que acontece se a vaga não tiver todos os campos preenchidos?**

   O sistema impede o envio do candidato ao Vlow e solicita edição da vaga.
3. **Como funciona a data limite para admissão?**

   Pode ser configurada por referência à data atual ou à data de admissão, e ajustada manualmente.
4. **Como acompanhar o status da integração?**

   Na aba "Contratados" do ATS, é possível visualizar se o envio está "na fila", "enviado" ou "erro".
5. **O que fazer em caso de erro no envio ao Vlow?**

   Reenvie manualmente pelo ATS; se persistir, contate o suporte.

## Artigos Relacionados

- [Requisição de Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#admissao)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Integração de Folha <> Gestão de Talentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/34631564024599)
- [Integração de ATS <> Admissão Digital Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567)
