---
id: "41826803259415"
titulo: "Como cadastrar um estagiário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41826803259415-Como-cadastrar-um-estagi%C3%A1rio"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Vínculos Específicos do Colaborador"
atualizado_em: "2026-10-02T15:05:58Z"
rotulos: ["Configuração", "Funcionários", "ID: br.com.sankhya.cadastro.funcionarios", "eSocial", "Configuração Funcionários", "Central do eSocial", "Cadastro", "Pessoal+", "Termo de Compromisso de Estágio (TCE)", "S-2300 – Trabalhador Sem Vínculo de Emprego/Estatutário", "Cadastro de Estagiário", "Bolsa Estágio"]
---

# Como cadastrar um estagiário

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros > Configuração Funcionários
**ID da Tela:** br.com.sankhya.cadastro.funcionarios

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O cadastro de estagiário permite registrar estudantes contratados por meio de estágio obrigatório ou não obrigatório, conforme as regras previstas na legislação, garantindo que o sistema realize corretamente o tratamento desse tipo de vínculo durante os processos de folha de pagamento e integração com o eSocial.

O estágio **não caracteriza vínculo empregatício**, desde que sejam atendidos todos os requisitos estabelecidos pela **Lei nº 11.788/2008 (Lei do Estágio)**, como a celebração do Termo de Compromisso de Estágio (TCE), a supervisão da instituição de ensino e da concedente, além da compatibilidade entre as atividades desenvolvidas e o curso do estudante.

Por esse motivo, o cadastro do estagiário possui configurações específicas que o diferenciam de uma admissão regida pela Consolidação das Leis do Trabalho (CLT). Entre essas diferenças estão:

- utilização de um padrão de cadastro específico para estagiários;
- informação da **Bolsa Estágio** em substituição ao salário-base;
- parametrizações próprias de contrato e regime trabalhista;
- adequação das informações de lotação e cargo às atividades de estágio.

Embora o processo de cadastro seja semelhante ao de uma admissão convencional, essas configurações são indispensáveis para que o sistema execute corretamente os cálculos da folha, as obrigações legais e a geração dos eventos do eSocial.

### 2. Pré-requisitos

Antes de cadastrar um estagiário, verifique se:

- possui permissão de acesso à tela **Configuração Funcionários** (Pessoal+ > Cadastros).  Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema;
- o estudante possui Termo de Compromisso de Estágio (TCE) formalizado;
- o cargo e a lotação destinados ao estágio já estão cadastrados;
- o [padrão de cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/41316403366551) para estagiários está disponível no sistema.

### 3. Jornada de Uso

#### 3.1 Cadastre o estagiário

1. Acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros);
2. Após selecionar a **Empresa** desejada, clique no botão **Cadastrar Funcionário**;
3. Ao iniciar o cadastro, escolha se deseja fazer o cadastro utilizando um padrão cadastrado previamente ou sem padrão;

   ![Imagem 1: Ao iniciar o cadastro, escolha se deseja fazer o cadastro utilizando um padrão cadastrado previamente ou sem padrão;](https://ajuda.sankhya.com.br/hc/article_attachments/41829233772439)

   | 💡 **Dica**  A seleção do padrão é recomendada, pois ele aplica automaticamente as parametrizações específicas para esse tipo de vínculo, reduzindo configurações manuais e evitando inconsistências na folha de pagamento e no eSocial. |
   | --- |
4. Preencha o **CPF** e o **Nome**do estagiário;

   | ℹ️ **Notas**  - O preenchimento da **Matrícula** depende da configuração do campo **Gera Matrícula do Funcionário automaticamente**, disponível na aba **Informações Gerais** da tela **Empresas** (Pessoal+ > Cadastros). - O campo **Código** pode ser preenchido automaticamente ou manualmente, conforme a configuração definida no botão **Configuração da Tela**, opção **Numeração**.  Ao ativar o parâmetro **Utiliza Sequência do Cód. Funcionário por Empresa? – FPCODFUNCPOREMP**, o sistema gera uma sequência de códigos exclusiva para cada empresa. Caso contrário, será única para todas as empresas.  📚 Para saber mais, acesse [Definição da Numeração dos Cadastros no Pessoal+](https://ajuda.sankhya.com.br/hc/pt-br/articles/41317860396823). |
   | --- |
5. Após preencher os dados cadastrais obrigatórios, acesse a aba **Contrato** e informe o valor da **Bolsa Estágio / Pró-Labore**;

   ![Imagem 2: Após preencher os dados cadastrais obrigatórios, acesse a aba Contrato e informe o valor da Bolsa Estágio / Pró-Labore ;](https://ajuda.sankhya.com.br/hc/article_attachments/41829283438487)

   | **⚠️** **Atenção**  Estagiários não possuem salário-base. O pagamento é realizado por meio da Bolsa Estágio, conforme previsto no Termo de Compromisso de Estágio. |
   | --- |
6. Acesse a aba **Lotação** e selecione o **Cargo** compatível com as atividades desenvolvidas pelo estagiário;

   ![Imagem 3: Acesse a aba Lotação e selecione o Cargo compatível com as atividades desenvolvidas pelo estagiário;](https://ajuda.sankhya.com.br/hc/article_attachments/41829348633111)

   Essas informações devem refletir as atividades previstas no Termo de Compromisso de Estágio.
7. Na aba **Admissão**, informe o regime trabalhista conforme o tipo de vínculo de estágio:

   ![Imagem 4: Na aba Admissão , informe o regime trabalhista conforme o tipo de vínculo de estágio:](https://ajuda.sankhya.com.br/hc/article_attachments/41830266289175)
   - **Código de Categoria para o eSocial**: 901 - Estagiário;
   - **Situação no eSocial**: Oficial (S-2200/S-2300);
   - **Vínculo**: 02 - Estagiário;
   - **Regime Trabalhista**: CLT - Consolidação das Leis de Trabalho;
   - **Regime de Jornada**: Submetidos Horário Trabalho (Cap. II CLT);
   - **Regime Previdenciário**: RGPS - Regime Geral Previdência Social;
   - **Tabela de Categoria [FGTS]**: 00 Estagiários.
8. Na seção **Período de Experiência**, marque **Dispensado da Experiência**, pois não se aplica contrato de experiência para essa contratação;
9. Na aba **Estágio**, preencha os dados do Termo de Compromisso de Estágio (TCE);

   ![Imagem 5: Na aba Estágio , preencha os dados do Termo de Compromisso de Estágio (TCE);](https://ajuda.sankhya.com.br/hc/article_attachments/41829437586711)
10. Após preencher todas as informações obrigatórias:

    - revise os dados informados;
    - clique em **Salvar**.

      O estagiário estará apto para participar dos processos da folha de pagamento de acordo com as regras aplicáveis ao estágio.

#### 3.2 Envio ao eSocial

Após concluir o cadastro do estagiário, acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha) para gerar e enviar o evento **S-2300 – Trabalhador Sem Vínculo de Emprego/Estatutário**, responsável por comunicar ao eSocial o ingresso do estagiário na empresa.

O envio desse evento depende de:

- cadastro do estagiário concluído;
- informações contratuais preenchidas corretamente;
- categoria do trabalhador configurada como **901 – Estagiário**;
- configurações do ambiente do eSocial devidamente parametrizadas.

Após a geração do evento, acompanhe seu processamento pela **Central do eSocial**, verificando se o retorno foi recepcionado com sucesso.

| **⚠️** **Atenção**  O estagiário **não utiliza o evento S-2200**, destinado aos trabalhadores com vínculo empregatício. Como o estágio não gera vínculo de emprego, sua admissão é comunicada exclusivamente por meio do **evento S-2300**, conforme as regras do eSocial. |
| --- |

### 4. Pontos de Atenção

- O estágio não gera vínculo empregatício quando observados os requisitos da Lei nº 11.788/2008.
- O cadastro deve ser realizado utilizando o padrão específico para estagiários.
- Estagiários recebem Bolsa Estágio, e não salário-base.
- O cargo e a lotação devem ser compatíveis com as atividades previstas no estágio.
- O encerramento do estágio não deve ser feito por rescisão trabalhista, e não gera TRCT (Termo de Rescisão do Contrato de Trabalho), esse documento é exclusivo para contratos regidos pela CLT. O encerramento correto é formalizado pelo Termo de Realização/Encerramento de Estágio, assinado pela empresa, pelo estagiário e pela instituição de ensino.
- Informações incorretas podem impactar o processamento da folha e a geração dos eventos do eSocial.

### 5. Dicas de Usabilidade

- Utilize sempre o padrão de cadastro de estagiário.
- Revise o valor da Bolsa Estágio antes de concluir o cadastro.
- Mantenha os dados do Termo de Compromisso de Estágio atualizados.
- Verifique se o cargo está compatível com as atividades exercidas pelo estudante.

## Perguntas Frequentes (FAQ)

**1. O estagiário possui vínculo empregatício?**

Não. O estágio não gera vínculo empregatício quando atende aos requisitos previstos na Lei nº 11.788/2008.

**2. O estagiário possui salário-base?**

Não. O pagamento é realizado por meio da Bolsa Estágio.

**3. Posso utilizar um cadastro padrão de empregado CLT para estagiários?**

Não é recomendado. Utilize sempre o padrão específico para estagiários para que o sistema aplique automaticamente as parametrizações necessárias.

**4. É obrigatório informar a Bolsa Estágio?**

Sim. Esse valor é utilizado pelo sistema durante o processamento da folha.

**5. O cargo influencia o cadastro do estagiário?**

Sim. O cargo deve ser compatível com as atividades previstas no estágio e com o Termo de Compromisso.

**6. O estagiário é enviado ao eSocial?**

Sim. O cadastro deve seguir as regras vigentes do eSocial para essa categoria de trabalhador, conforme o tipo de vínculo informado.

**7. O encerramento do estágio pode ser feito por rescisão, gerando TRCT?**

Não. O TRCT é um documento exclusivo para contratos regidos pela CLT. Como o estágio não gera vínculo empregatício (Lei nº 11.788/2008), seu encerramento correto é feito por meio do Termo de Realização/Encerramento de Estágio, assinado pela empresa, pelo estagiário e pela instituição de ensino. Usar rescisão/TRCT nesse caso configura erro de enquadramento legal e pode gerar inconsistências no cadastro e na folha.

## Artigos Relacionados

- [Cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
- [Requisição de Transferência - Transferência de estagiário](https://ajuda.sankhya.com.br/hc/pt-br/articles/30772702977431)
- [Dúvidas sobre o processamento de pagamentos para estagiários no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/39355063269015)
