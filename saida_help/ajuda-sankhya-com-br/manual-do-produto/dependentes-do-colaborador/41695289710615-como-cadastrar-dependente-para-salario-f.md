---
id: "41695289710615"
titulo: "Como cadastrar dependente para salário-família"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Dependentes do Colaborador"
atualizado_em: "2026-10-02T15:18:13Z"
rotulos: ["Dependentes", "eSocial", "Folha de Pagamento", "Configuração Funcionários", "Pessoal+", "Cadastro de Dependentes", "Salário-família", "Cadastro de Dependente de Salário-Família", "Lei nº 8.213/1991", "Decreto nº 3.048/1999", "Filho(a)/Enteado(a) Incapaz", "Tabela de Faixas de Salário-Família"]
---

# Como cadastrar dependente para salário-família

**Módulo:** Pessoal+
**Caminho de Acesso:**Pessoal+ > Cadastros > Configuração Funcionários > Aba Dependentes
**ID da Tela:** br.com.sankhya.cadastro.funcionarios

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia#h_01KWMJ292NQDR21YD1KXNEMWCH)

[1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia#h_01KWMJ292QHKM84HWRQS7D0FW3)
[2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia#h_01KWMJ292YG1R87BZ6X7QKY1GD)
[3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia#h_01KWMJ2934SDP97FE5DFWPG83Q)
[4. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia#h_01KWMJ293VDTGGCNVHS68Q93PK)
[5. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia#h_01KWMJ293ZG72Y1YJ4FT3KM27X)

[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia#h_01KWMJ2941VDH281R8GV9HGBF1)
[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/41695289710615-Como-cadastrar-dependente-para-sal%C3%A1rio-fam%C3%ADlia#h_01KWMJ294EV5CDCTEZR68Q8R6X)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O cadastro do **Dependente de Salário-Família** permite identificar quais dependentes devem ser considerados no cálculo automático do benefício previdenciário durante o processamento da folha de pagamento.

Quando corretamente configurado, o sistema verifica automaticamente os critérios previstos na legislação, como o limite de remuneração do trabalhador, a elegibilidade do dependente, a quantidade de dias trabalhados e os valores vigentes da Tabela de Faixas, reduzindo a necessidade de cálculos manuais e evitando pagamentos indevidos ou a ausência do benefício.

O salário-família é um benefício previdenciário destinado aos empregados, empregados domésticos e trabalhadores avulsos que possuam filhos ou equiparados e atendam aos requisitos legais.

O benefício é regulamentado pelas seguintes normas:

- Lei nº 8.213/1991, arts. 65 a 70;
- Decreto nº 3.048/1999 (Regulamento da Previdência Social).

### 2. Pré-requisitos

Antes de realizar o cadastro, verifique se:

- tem acesso ao módulo de Folha de Pagamento e telas relacionadas por meio da rotina de **Acessos** (Configurações > Controle de Acessos);
- tem permissão para editar cadastros de colaboradores, eventos, fórmulas e tabela de faixas;
- o colaborador possui vínculo que permite o recebimento do salário-família;
- os dados cadastrais do dependente (CPF, data de nascimento e parentesco) estão corretos;

  | **⚠️** **Atenção**  O **Grau de parentesco** **Filho(a)/Enteado(a) Incapaz** não concede direito ao salário-família. Essa classificação é tratada pelo sistema como enteado e, por si só, não habilita o benefício. |
  | --- |
- a **Tabela de Faixas - Salário Família** está atualizada conforme a legislação vigente;
- o evento de Salário-Família está ativo e configurado corretamente;
- a competência da folha está aberta para processamento.

### 3. Jornada de Uso

#### 3.1. Evento de Salário-Família

[GIF animado: Imagem 1: 3.1. Evento de Salário-Família](https://ajuda.sankhya.com.br/hc/article_attachments/41768118546071)

O cálculo do salário-família utiliza um evento de folha específico responsável por lançar automaticamente o valor do benefício durante o processamento da folha. Antes de cadastrar os dependentes, confirme se esse evento está corretamente configurado.

1. Acesse a tela **Eventos** (Pessoal+ > Cadastros) e crie ou verifique o**evento de provento** para **salário-família**;
2. Na aba **Básico**:
   - preencha o campo **Identificação do evento** com o código relacionado a **salário-família**;
   - configure a **Unidade** como **Dias**;
   - selecione no campo **Evento como regra em cálculo de** as folhas **Normal** e **Rescisão**;
   - **Selecione a fórmula** correspondente.
3. Na aba **Avançado**:
   - defina **Base DIRF** como **salário-família**;
   - não há incidência para **INSS** e **IRRF**.
4. Na aba **eSocial**:
   - selecione a opção **1409 - Salário-família** no campo **Natureza da Rubrica**;
   - em **Incidência p/ Previdência**, indique a opção **51 - Salário-família**.

#### 3.2. Fórmula

O evento de salário-família deve possuir uma fórmula responsável por validar automaticamente:

- o direito ao benefício;
- a remuneração do trabalhador;
- a quantidade de dependentes elegíveis;
- a tabela de faixas vigente;
- os dias trabalhados na competência.

A fórmula utilizada poderá variar conforme a parametrização da empresa. Caso utilize a fórmula padrão disponibilizada pelo sistema, mantenha-a sem alterações.

1. Acesse a tela **Fórmulas** (Pessoal+ > Cadastros) e crie ou verifique a fórmula para **salário-família**.

   [GIF animado: Imagem 2: Acesse a tela Fórmulas (Pessoal+ > Cadastros) e crie ou verifique a fórmula para salário-família .](https://ajuda.sankhya.com.br/hc/article_attachments/41768239528471)

   **Exemplo da fórmula padrão:**

   IF((QueFuncionario.VINCULO <> 90), IF((&Folqui <> 1), IF(((QueFuncionario.SITUACAO = 1) AND (CTOI(PDESPARAM('COUNT(1)', 'TFPOCO O, TFPHIS H', 'O.CODHISTOCOR = H.CODHISTOCOR AND O.CODEMP = :INT\_CODEMP AND O.CODFUNC = :INT\_CODFUNC AND O.DTFINALOCOR >= :DAT\_DTINI AND O.DTFINALOCOR <= :DAT\_DTFIM AND H.AFASTAMENTO IN ('A', 'D') AND O.DTFINALOCOR IS NOT NULL', STR(QueFuncionario.CODEMP), STR(QueFuncionario.CODFUNC), DTOC(&Refere \* 1.0), DTOC((FSOMAMES(&Refere, 1) -1) \* 1.0))) <> 1)) OR ((((QueFuncionario.SITUACAO = 3) OR (QueFuncionario.SITUACAO = 6)) AND (&DIASTRA > 0)) OR (QueFuncionario.SITUACAO = 5)), FQD(queFuncionario.CODEMP, queFuncionario.CODFUNC, 'S', &Refere) \* FTF(3, 1, @F\_COMPOSICAOSALARIOFOLHA + &VLRINCORPORA + &VlrIncideMedias +@E\_MEDIAFERIASNACOMPETENCIA, &Refere, queFuncionario.TIPTAB), 0) / IF(((&TIPFOL = 'N') AND (MES(queFuncionario.DTADM) = &MESATU) AND (ANO(queFuncionario.DTADM) = &ANOATU)) OR (&TIPFOL = 'R'), IF(QueFuncionario.TIPSAL = '5', QueFuncionario.HORASSEM \* 5, &DiaDivSalBase), 1) \* IF(((&TIPFOL = 'N') AND (MES(queFuncionario.DTADM) = &MESATU) AND (ANO(queFuncionario.DTADM) = &ANOATU)) OR (&TIPFOL = 'R'), IF(&DIASTRA > 0, (&DIASTRA + @F\_DIASDEFERIASNAREFERENCIA + FDiasAfaMotivo(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'T', &TIPFOL)), &DiaDivSalBase), 1), 0), 0)

#### 3.3. Tabela de Faixa para Salário-família

1. Acesse a tela **Tabela de Faixas** (Pessoal+ > Cadastros) **Salário-família** e cadastre ou verifique se os limites de renda e valores do benefício estão atualizados conforme a tabela oficial do governo.

   ![Imagem 3: Acesse a tela Tabela de Faixas (Pessoal+ > Cadastros) Salário-família e cadastre ou verifique se os limites de renda e…](https://ajuda.sankhya.com.br/hc/article_attachments/41768355068183)

#### 3.4. Cadastro de Dependente com Salário-família

[GIF animado: Imagem 4: 3.4. Cadastro de Dependente com Salário-família](https://ajuda.sankhya.com.br/hc/article_attachments/41768376803991)

1. Acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Localize o colaborador e vá até a aba **Dependentes;**
3. Caso o dependente ainda não exista, clique em **+ Cadastrar Dependentes** para cadastrá-lo e preencha os dados obrigatórios.
4. Na subaba **Geral**, marque a opção **Dependente de Salário-Família**. Essa opção informa ao sistema que o dependente poderá participar do cálculo do benefício, desde que os demais requisitos legais também sejam atendidos.

   | **⚠️** **Atenção**  Apenas marcar essa opção não garante o pagamento do benefício. O cálculo também depende das regras legais e das configurações da folha. |
   | --- |
5. Após preencher as informações, clique em **Salvar**.

   O dependente ficará disponível para ser considerado no cálculo das próximas folhas de pagamento.
6. Acesse a tela **Central do eSocial** (Pessoal+ > Rotinas Folha) para gerar e enviar o evento ao eSocial.
   - **S-2200**: utilize quando o dependente for incluído junto com a admissão do colaborador;
   - **S-2205**: use quando o dependente for incluído após a admissão.

     | **⚠️** **Atenção**  O envio do evento ao eSocial mantém o cadastro do trabalhador atualizado perante o governo, porém **não é o envio do evento que determina o cálculo do salário-família**. O benefício é calculado com base nas configurações do cadastro, da folha e nas regras legais vigentes. |
     | --- |

#### 3.5. Cálculo da Folha

1. Execute o cálculo da folha em que o desconto deve ser aplicado, acessando a tela **Cálculos** (Pessoal+ > Rotinas Folha), como, por exemplo, a folha mensal.

   ![Imagem 5: Execute o cálculo da folha em que o desconto deve ser aplicado, acessando a tela Cálculos (Pessoal+ > Rotinas Folha),…](https://ajuda.sankhya.com.br/hc/article_attachments/41769886598423)

   Durante o cálculo da folha, o sistema executa automaticamente a seguinte sequência:

   - identifica os dependentes marcados como **Dependente de Salário-Família**;
   - verifica se o trabalhador possui direito ao benefício;
   - consulta a remuneração da competência;
   - localiza a faixa correspondente na **Tabela de Faixas de Salário-Família**;
   - calcula o valor integral ou proporcional;
   - gera o evento de salário-família na folha.

   Somente quando todas essas condições forem atendidas o benefício será calculado.

### 4. Pontos de Atenção

- O benefício somente é calculado quando o trabalhador atende aos critérios previstos na legislação.
- O sistema utiliza os valores cadastrados na **Tabela de Faixas** para cada competência.
- Alterações realizadas após o cálculo da folha exigem novo processamento.
- A remuneração do trabalhador é considerada para verificar o direito ao benefício.
- O valor poderá ser proporcional aos dias trabalhados no período.
- Dependentes não marcados como **Dependente de Salário-Família** não participam do cálculo.
- A alteração da opção **Dependente de Salário-Família** somente produzirá efeito após novo cálculo da folha.
- Alterações na Tabela de Faixas não recalculam automaticamente folhas já processadas.

### 5. Dicas de Usabilidade

- Mantenha sempre atualizada a **Tabela de Faixas** conforme publicação oficial do INSS.
- Cadastre os dependentes antes do fechamento da folha.
- Sempre confira se o dependente continua atendendo aos critérios legais após completar 14 anos.
- Após qualquer alteração em dependentes ou configurações, recalcule a folha.
- Revise periodicamente os dependentes para identificar filhos que ultrapassaram o limite de idade previsto na legislação.

## Perguntas Frequentes (FAQ)

**1. Quem tem direito ao Salário-Família?**

Empregados, empregados domésticos e trabalhadores avulsos cuja remuneração esteja dentro do limite legal e que possuam filhos ou equiparados que atendam aos requisitos da legislação.

**2. Basta cadastrar o dependente para receber o benefício?**

Não.

Além do cadastro, é necessário marcar a opção **Dependente de Salário-Família**, atender aos critérios legais e possuir remuneração dentro do limite vigente.

**3. Posso cadastrar mais de um dependente para salário-família?**

Sim.

Todos os dependentes elegíveis e marcados como **Dependente de Salário-Família** serão considerados durante o cálculo, desde que atendam aos requisitos previstos na legislação.

**4. O dependente inválido sempre gera Salário-Família?**

Não necessariamente.

O cálculo depende do enquadramento legal e das configurações do cadastro. Além disso, a opção **Filho(a)/Enteado(a) Incapaz**, isoladamente, não concede o benefício.

**5. O que acontece se eu marcar o dependente depois que a folha já foi calculada?**

Será necessário refazer o cálculo da folha para que o benefício seja considerado.

**6. O salário-família depende da remuneração do colaborador?**

Sim.

O sistema compara a remuneração mensal do trabalhador com o limite definido na Tabela de Faixas vigente.

**7. O valor pode ser proporcional?**

Sim.

Quando aplicável, o sistema calcula o benefício proporcionalmente aos dias trabalhados no período.

**8. Alterar a Tabela de Faixas atualiza folhas já calculadas?**

Não.

Após atualizar a tabela, é necessário recalcular a folha para que os novos valores sejam considerados.

**9. Posso alterar a opção Dependente de Salário-Família depois da admissão?**

Sim.

Após salvar a alteração, basta recalcular a folha para que o sistema considere a nova configuração nas competências seguintes.

**10. Posso desmarcar a opção Dependente de Salário-Família?**

Sim.

A partir da alteração, o dependente deixa de ser considerado nos próximos cálculos da folha.

**11. O que acontece se eu alterar a remuneração do colaborador?**

Após recalcular a folha, o sistema reavalia automaticamente o direito ao benefício considerando a nova remuneração.

**12.  O benefício é calculado automaticamente?**

Sim.

Durante o cálculo da folha o sistema verifica automaticamente todas as regras legais e configurações do sistema.

**13. O sistema deixa de calcular automaticamente quando o dependente completa a idade limite?**

Sim.

Ao deixar de atender aos critérios legais, o dependente deixa de ser considerado no cálculo do benefício.

**14. O salário-família é calculado em férias?**

Depende da configuração da folha e das regras legais aplicáveis à competência. O sistema considera as parametrizações existentes no cálculo.

**15. Como identificar por que o benefício não foi calculado ou foi calculado com valor incorreto?**

Verifique, nesta ordem:

1. se o dependente está marcado como **Dependente de Salário-Família**;
2. se a remuneração do colaborador está dentro do limite legal;
3. se a Tabela de Faixas está atualizada com o limite de remuneração e o valor da cota vigente para a competência da folha;
4. se o evento de Salário-Família está ativo, possui as incidências corretas e não teve suas fórmulas de cálculo alteradas manualmente.

   Após corrigir qualquer uma dessas informações, recalcule a folha de pagamento do colaborador para que o benefício seja recalculado.

**16. O envio do S-2205 é obrigatório para calcular o salário-família?**

Não.

O cálculo depende das configurações do cadastro do dependente e das regras da folha. Entretanto, quando o dependente possuir informações que exigem comunicação ao eSocial, o envio do evento S-2205 é obrigatório para manter as informações consistentes perante o governo.

## Artigos Relacionados

- [Cadastro de Dependentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686771632791)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios#AbaDependentes)
- [Tabela de Faixas](https://ajuda.sankhya.com.br/hc/pt-br/articles/36716586861335)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Cálculo da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
