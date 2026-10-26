---
id: "41456466315927"
titulo: "Como cadastrar um colaborador temporário (vínculo 60)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41456466315927-Como-cadastrar-um-colaborador-tempor%C3%A1rio-v%C3%ADnculo-60"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Vínculos Específicos do Colaborador"
atualizado_em: "2026-10-02T15:05:40Z"
rotulos: ["Contrato", "ID: br.com.sankhya.cadastro.funcionarios", "CLT", "eSocial", "Configuração Funcionários", "FGTS", "Pessoal+", "Contrato de Trabalho Temporário - Vínculo 60", "60 - Prazo Determinado Urbano (Pessoa Jurídica)"]
---

# Como cadastrar um colaborador temporário (vínculo 60)

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros > Configuração Funcionários
**ID da Tela:** br.com.sankhya.cadastro.funcionarios

---

## Descrição e Usabilidade

O vínculo **60 - Prazo Determinado Urbano (Pessoa Jurídica)** é utilizado para contratação de trabalhadores urbanos por prazo determinado quando o empregador é uma empresa (CNPJ).

Esse tipo de contratação é utilizado quando a empresa necessita contratar colaboradores por período previamente definido, em situações como aumento temporário da demanda, execução de projetos específicos, atividades transitórias ou contrato de experiência.

O contrato possui data de início e término previamente definidas e segue as regras da Consolidação das Leis do Trabalho (CLT).

Exemplos:

- contratação para eventos temporários;
- reforço operacional em períodos sazonais;
- projetos com duração definida;
- contrato de experiência.

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/41458087531927)

1. Para realizar a admissão do colaborador temporário, acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Informe a **Empresa** e clique em **Aplicar**;
3. Clique em **Cadastrar Funcionário**;
4. Defina se utilizará um **Padrão do Novo Cadastro** para preenchimento das principais informações de contrato ou se seguirá **Sem Padrão**;
5. Preencha **Nome** e **CPF** do colaborador;
6. Preencha as informações das abas da tela conforme as regras e necessidade da sua empresa;
7. Na aba **Admissão**, atente-se para o preenchimento dos seguintes campos:
   - **Data de Admissão**: informe a data de início;
   - **Código de Categoria para o eSocial**: geralmente 101 (Empregado - Geral);
   - **Vínculo**: selecione 60 - Prazo Determinado Urbano (PJ);
   - **Regime Trabalhista**: CLT - Consolidação das Leis de Trabalho;
   - **Regime Previdenciário**: RGPS - Regime Geral de Previdência Social;
   - **Data Término do Contrato**: informe a data prevista para encerramento do contrato. Esse campo é obrigatório para vínculos por prazo determinado e será utilizado pelo eSocial para caracterização do tipo de contratação.
8. Caso a contratação seja realizada como contrato de experiência, preencha as informações do **Período de Experiência**.

   O prazo pode ser de até 90 dias, podendo ser dividido em dois períodos sucessivos, conforme previsto na legislação trabalhista.
9. Salve o cadastro.

   | **⚠️** **Atenção**  Após o cadastro, envie o evento **S-2200** ao eSocial. |
   | --- |

**Exemplo Prático**

Uma empresa de eventos precisa contratar profissionais para atuar em uma feira durante seis meses.

Configuração:

- Vínculo: 60
- Data de Admissão: 01/06/2025
- Data de Término: 30/11/2025
- Empregador: Empresa de Eventos Ltda (CNPJ)
- Local de Trabalho: área urbana

### Pontos de Atenção

- A contratação deve atender aos requisitos legais aplicáveis aos contratos por prazo determinado previstos na CLT.
- Esse vínculo deve ser utilizado exclusivamente quando o empregador for pessoa jurídica.
- O trabalhador contratado pelo vínculo 60 possui os mesmos direitos básicos garantidos aos demais empregados regidos pela CLT:
  - FGTS;
  - 13º salário proporcional;
  - Férias proporcionais acrescidas de 1/3;
  - INSS;
  - Aviso prévio, quando aplicável.
- A Data de Término do Contrato é obrigatória.
- O contrato não pode ser prorrogado mais de uma vez.
- Caso ocorra prorrogação do contrato, o prazo total, incluindo o período originalmente contratado, não poderá ultrapassar dois anos.
- O prazo total do contrato não pode ultrapassar dois anos. Caso o contrato ultrapasse esse limite legal, ele passa a ser considerado contrato por prazo indeterminado.
- Em caso de rescisão antecipada sem justa causa pelo empregador, poderá haver incidência da multa rescisória sobre o FGTS conforme a legislação vigente.
- O vínculo 60 - Prazo Determinado Urbano (Pessoa Jurídica) não se aplica a atividades rurais.

## Perguntas Frequentes (FAQ)

**1. Posso deixar a data de término em branco?**

Não. Para contratos por prazo determinado a data de término é obrigatória.

**2. Posso transformar o contrato em prazo indeterminado?**

Sim. Porém deverá ser realizada a alteração contratual conforme a legislação e procedimentos da empresa.

**3. O vínculo 60 permite contrato de experiência?**

Sim. O período de experiência pode ser configurado por até 90 dias.

**4. Qual a diferença entre os vínculos 60 e 65?**

O vínculo 60 é utilizado quando o empregador possui CNPJ (Pessoa Jurídica). O vínculo 65 é utilizado quando o empregador é Pessoa Física (CPF).

**5. Esse vínculo gera FGTS?**

Sim. O empregado possui direito ao recolhimento de FGTS normalmente.

**6. Posso prorrogar um contrato com vínculo 60?**

Sim. O contrato por prazo determinado pode ser prorrogado uma única vez, desde que a duração total do vínculo não ultrapasse dois anos.

**7. O que acontece se o contrato ultrapassar dois anos?**

Caso o contrato permaneça ativo além do limite legal, ele poderá ser caracterizado como contrato por prazo indeterminado, conforme a legislação trabalhista.

**8. Posso utilizar esse vínculo para atividades rurais?**

Não. O vínculo 60 é destinado exclusivamente a atividades urbanas. Para atividades rurais devem ser utilizados os vínculos específicos previstos para esse tipo de contratação.

**9. Qual evento deve ser enviado ao eSocial após a admissão?**

Após concluir o cadastro do colaborador, deve ser enviado o evento **S-2200 – Cadastramento Inicial do Vínculo e Admissão do Trabalhador**, observando os prazos legais do eSocial.

**10. Posso utilizar o vínculo 60 para contratação efetiva?**

Não. O vínculo 60 é destinado a contratos com prazo determinado. Para contratações sem data prevista de término, deve ser utilizado o vínculo correspondente ao contrato por prazo indeterminado.
