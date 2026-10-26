---
id: "34153647667351"
titulo: "Como controlar as férias em dobro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro"
trilha: "Manual do Produto > Pessoas+ > Férias > Programação e Controle de Férias"
atualizado_em: "2026-10-02T15:41:33Z"
rotulos: ["Configuração", "Férias", "Pessoal+", "ID: br.com.sankhya.mgepes.rh.DashControleFeriasDobro", "Controle de Férias Dobro", "Legislação Trabalhista", "RH"]
---

# Como controlar as férias em dobro

**Módulo:** Pessoal+
**Versão Mínima:** 5.48.0 
**Caminho de Acesso:** Pessoal+ > Consultas
**ID da Tela:** br.com.sankhya.mgepes.rh.DashControleFeriasDobro

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#descri%C3%A7%C3%A3o-e-usabilidade)

[1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#1-descri%C3%A7%C3%A3o-da-funcionalidade)

[2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#4-jornada-de-uso)

[3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#4-jornada-de-uso)

[4. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#5-pontos-de-aten%C3%A7%C3%A3o)

[5. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#6-dicas-de-usabilidade)

[6. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#h_01K2J7T0K47D9B9PK1RCXEFXMW)

[Perguntas frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#h_01JXZD26WS16MD2RV6DQZ3KG9X)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/34153647667351-Como-controlar-as-f%C3%A9rias-em-dobro#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O dashboard de **Controle de Férias Dobro** é uma tela que ajuda a controlar férias que estão perto do prazo limite de vencimento e podem gerar pagamento em dobro, conforme a lei trabalhista. 

[GIF animado: Imagem 1: O dashboard de Controle de Férias Dobro é uma tela que ajuda a controlar férias que estão perto do prazo limite de…](https://ajuda.sankhya.com.br/hc/article_attachments/34154640416407)

### 2. Pré-requisitos

**Permissões necessárias**

- Deve ter permissão para **consultar dados dos funcionários.**
- Deve **ter acesso liberado para a tela do dashboard**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

**Parâmetros essenciais**

- O sistema deve estar com os **períodos aquisitivos configurados corretamente**.

**Configurações relacionadas**

- Verifique se as **empresas e departamentos** estão cadastrados corretamente.

### 3. Jornada de Uso

1. Acesse a tela **Controle de Férias** (Pessoal+ > Consultas) no sistema.
2. **Use os filtros** para localizar as informações e clique em **"Atualizar"**:

   - **Empresa;**
   - **Vínculo;**
   - **Departamento;**
   - **Período do Limite de Gozo** (escolha a data);
   - **Apenas com limite em 90 dias** (marque se quiser ver só as férias mais urgentes).
3. **Observe a lista de funcionários** com férias próximas do prazo.

   O dashboard apresenta as informações essenciais para o controle das férias.

   - **Empresa**, **Departamento**, **Código** e **Nome do Funcionário**: informações de identificação da empresa e do colaborador;
   - **Data de Início e Final do Período Aquisitivo**: indica o período em que o funcionário adquiriu o direito às férias;
   - **Quantidade de Dias de Férias Disponíveis**: mostra o saldo de dias de férias que o funcionário ainda tem para gozar;
   - **Prazo Limite para Gozo das Férias**: esta é a data crucial! É o último dia em que as férias podem ser gozadas para evitar o pagamento em dobro;
   - **Quantidade de Dias (entre a data atual e a data limite)**: apresenta quantos dias faltam da data de hoje até o Prazo Limite, permitindo uma rápida visualização da urgência.
4. **Analise os prazos** e tome as ações necessárias para evitar pagamento em dobro.

#### Entendendo o cálculo do Prazo Limite

O cálculo da data limite para gozo das férias é feito automaticamente pelo sistema.

A lógica é simples:

Data Limite = Último dia do próximo Período Aquisitivo (PA) - Quantidade de dias de férias disponíveis

**Exemplo 1:**

- Período Aquisitivo (PA) Atual: 02/01/2023 - 01/01/2024
- Dias de Férias Disponíveis: 30 dias
- Próximo PA: 02/01/2024 - 01/01/2025

  Neste caso, o último dia do próximo PA é 01/01/2025. Subtraindo os 30 dias de férias disponíveis, chegamos à seguinte Data Limite:

- Data Limite: 01/01/2025 - 30 dias = 03/12/2024

  Ou seja, o funcionário precisa gozar suas férias até 03/12/2024 para que a empresa não precise pagar em dobro.

**Exemplo 2:**

- Período Aquisitivo (PA) Atual: 28/12/2022 - 27/12/2023
- Dias de Férias Disponíveis: 10 dias
- Próximo PA: 28/12/2023 - 27/12/2024

  Seguindo a mesma lógica, o último dia do próximo PA é 27/12/2024. Subtraindo os 10 dias de férias disponíveis, a Data Limite será:

- Data Limite: 27/12/2024 - 10 dias = 18/12/2024

  Assim, as férias devem ser gozadas até 18/12/2024 para evitar o pagamento em dobro.

### 4. Pontos de Atenção

- O dashboard **mostra apenas funcionários com saldo de férias disponível** (ou seja, sem data de saída registrada).
- Não aparecem funcionários que já têm **data prevista para tirar férias**.
- Se marcar a opção **"Apenas com limite em 90 dias"**, serão exibidas só as férias com prazo menor ou igual a 90 dias a partir da data atual.

### 5. Dicas de Usabilidade

- Use o filtro de **90 dias** para priorizar casos mais urgentes.
- Consulte o dashboard com frequência, assim você evita multas e pagamentos em dobro.
- Aproveite os filtros por **departamento** para organizar melhor as liberações de férias.

### 6. Casos de Uso

- RH precisa planejar férias para não pagar em dobro.
- Gestores querem saber quais funcionários devem sair de férias primeiro.
- Auditorias internas precisam garantir que a empresa está cumprindo a lei.

## Perguntas frequentes (FAQ)

**1. O que é "férias com risco de pagamento em dobro"?**

É quando o funcionário não tira as férias no prazo certo. Pela lei, a empresa deve pagar o valor em dobro.

**2. O dashboard mostra todas as férias da empresa?**

Não. Ele mostra apenas as férias com saldo disponível e que ainda não têm data prevista para início.

**3. Como saber quais casos são mais urgentes?**

Marque o filtro **"Apenas com limite em 90 dias"**. Assim, você vê só os prazos que vencem logo.

**4. Preciso calcular a data limite manualmente?**

Não! O sistema calcula automaticamente para você.

## Artigos Relacionados

[Férias](https://ajuda.sankhya.com.br/hc/pt-br/articles/7091805775255)
