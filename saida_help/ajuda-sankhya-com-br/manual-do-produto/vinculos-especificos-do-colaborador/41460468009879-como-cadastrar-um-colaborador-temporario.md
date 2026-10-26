---
id: "41460468009879"
titulo: "Como cadastrar um colaborador temporário (vínculo 65)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41460468009879-Como-cadastrar-um-colaborador-tempor%C3%A1rio-v%C3%ADnculo-65"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Vínculos Específicos do Colaborador"
atualizado_em: "2026-10-02T15:06:39Z"
rotulos: ["Contrato", "ID: br.com.sankhya.cadastro.funcionarios", "eSocial", "Configuração Funcionários", "Cadastro", "Pessoal+", "Regime Trabalhista", "Data Término do Contrato", "Cadastro de Colaborador Temporário - Vínculo 65", "65 - Prazo Determinado Urbano (Pessoa Física)"]
---

# Como cadastrar um colaborador temporário (vínculo 65)

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros > Configuração Funcionários
**ID da Tela:** br.com.sankhya.cadastro.funcionarios

---

## Descrição e Usabilidade

O vínculo **65 - Prazo Determinado Urbano (Pessoa Física)** é utilizado para contratação de trabalhadores urbanos por prazo determinado quando o empregador é uma pessoa física (CPF).

Esse vínculo atende situações em que o contratante não é uma empresa, mas necessita contratar um trabalhador por período previamente definido para execução de atividades temporárias, projetos específicos ou serviços transitórios.

| **⚠️** **Atenção**  O vínculo 65 deve ser utilizado exclusivamente para empregados urbanos contratados por pessoa física (CPF) com prazo determinado. A data de término do contrato é obrigatória e será considerada tanto nos processos internos da folha quanto nos envios ao eSocial. |
| --- |

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/41463202197911)

1. Para realizar a admissão do colaborador temporário, acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Informe a **Empresa** e clique em **Aplicar**;
3. Clique em **Cadastrar Funcionário**;
4. Defina se utilizará um **Padrão do Novo Cadastro** para preenchimento das principais informações de contrato ou se seguirá **Sem Padrão**;
5. Preencha **Nome** e **CPF** do colaborador;
6. Preencha as informações das abas da tela conforme as regras e necessidade da sua empresa;
7. Na aba **Admissão**, atente-se para o preenchimento dos seguintes campos:
   - **Data de Admissão**: informe a data de início;
   - **Código de Categoria para o eSocial**: geralmente 101 (Empregado - Geral);
   - **Vínculo**: selecione 65 - Prazo determinado urbano (física);
   - **Regime Trabalhista**: CLT - Consolidação das Leis de Trabalho;
   - **Regime Previdenciário**: RGPS - Regime Geral de Previdência Social;
   - **Data Término do Contrato**: informe a data prevista para encerramento do contrato. Esse campo é obrigatório para vínculos por prazo determinado e será utilizado pelo eSocial para caracterização da modalidade contratual.
8. Caso a contratação seja realizada como contrato de experiência, configure o **Período de Experiência** observando:
   - limite máximo de 90 dias;
   - divisão em até dois períodos.
9. Salve o cadastro.

   | **⚠️** **Atenção**  Após concluir a admissão, envie o evento **S-2200** ao eSocial. |
   | --- |

**Exemplo Prático**

Um arquiteto autônomo necessita contratar um assistente por quatro meses para auxiliar em um projeto específico.

Configuração:

- Vínculo: 65
- Data de Admissão: 01/07/2025
- Data de Término: 31/10/2025
- Empregador: João da Silva (CPF)
- Local de Trabalho: escritório urbano

### Pontos de Atenção

- Esse vínculo deve ser utilizado somente quando o empregador for pessoa física.
- A Data Término do Contrato deve ser informada no momento da admissão.
- O trabalhador contratado pelo vínculo 65 possui os mesmos direitos básicos garantidos aos demais empregados regidos pela CLT:
  - FGTS;
  - 13º salário proporcional;
  - Férias proporcionais acrescidas de 1/3;
  - INSS;
  - Aviso prévio, quando aplicável.
- O contrato pode ser prorrogado apenas uma vez.
- O prazo total não pode ultrapassar dois anos. Contratos que ultrapassarem esse prazo poderão ser caracterizados como contratos por prazo indeterminado.
- Em caso de encerramento antecipado sem justa causa, poderão existir reflexos rescisórios previstos em lei.
- O vínculo 65 - Prazo Determinado Urbano (Pessoa Física) não se aplica a trabalhos rurais.

## Perguntas Frequentes (FAQ)

**1. Posso utilizar esse vínculo para empresas?**

Não. O vínculo 65 é exclusivo para empregadores pessoa física.

**2. O contrato pode durar mais de dois anos?**

Não. O prazo máximo legal é de dois anos.

**3. O vínculo 65 permite período de experiência?**

Sim. Até 90 dias.

**4. Qual a diferença para o vínculo 60?**

A diferença está apenas no tipo de empregador:

- 60 = Pessoa Jurídica (CNPJ)
- 65 = Pessoa Física (CPF)

**5. O trabalhador possui FGTS?**

Sim. O recolhimento ocorre normalmente conforme a legislação.

**6. Posso deixar a data de término em branco?**

Não. Para contratos por prazo determinado a data de término é obrigatória e deve ser informada no momento da admissão.

**7. Posso prorrogar um contrato com vínculo 65?**

Sim. O contrato pode ser prorrogado uma única vez, desde que o prazo total da contratação não ultrapasse dois anos.

**8. O que acontece se o contrato ultrapassar dois anos?**

Caso o contrato permaneça ativo além do limite legal, ele poderá ser caracterizado como contrato por prazo indeterminado, conforme a legislação trabalhista.

**9. Posso utilizar esse vínculo para atividades rurais?**

Não. O vínculo 65 é destinado exclusivamente a atividades urbanas. Para atividades rurais devem ser utilizados os vínculos específicos previstos para esse tipo de contratação.

**10. Qual evento deve ser enviado ao eSocial após a admissão?**

Após concluir o cadastro do colaborador, deve ser enviado o evento **S-2200 – Cadastramento Inicial do Vínculo e Admissão do Trabalhador**, observando os prazos legais do eSocial.

**11. Posso transformar o contrato em prazo indeterminado?**

Sim. Nesse caso, a empresa deverá realizar os procedimentos contratuais e legais aplicáveis para alteração da modalidade de contratação.
