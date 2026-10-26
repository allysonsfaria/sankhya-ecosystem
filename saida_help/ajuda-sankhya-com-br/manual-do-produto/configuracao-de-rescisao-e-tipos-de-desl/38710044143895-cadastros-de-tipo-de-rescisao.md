---
id: "38710044143895"
titulo: "Cadastros de Tipo de Rescisão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38710044143895-Cadastros-de-Tipo-de-Rescis%C3%A3o"
trilha: "Manual do Produto > Pessoas+ > Rescisão > Configuração de Rescisão e Tipos de Desligamento"
atualizado_em: "2026-09-27T18:15:54Z"
rotulos: ["Configuração", "RAIS", "eSocial", "ID: br.com.sankhya.rh.TipoRescisao", "Configuração Funcionários", "Tipo de Rescisão", "Cadastro", "Cadastro de códigos de afastamento", "Conformidade com Tabela 19 do eSocial", "FGTS", "Pessoal+"]
---

# Cadastros de Tipo de Rescisão

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.TipoRescisao

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A tela **Tipo de Rescisão** é utilizada para cadastrar e configurar os diferentes motivos de desligamento utilizados no sistema.

Para cada tipo de rescisão, devem ser informados os códigos exigidos pelos órgãos governamentais, garantindo que:

- O cálculo da rescisão seja adequado às indenizações e direitos do trabalhador;
- As guias de FGTS sejam geradas de forma adequada;
- As informações enviadas ao eSocial estejam consistentes;
- As obrigações como RAIS e GFIP sejam atendidas corretamente.

### 2. Pré-requisitos

**Permissões necessárias**

- Deve ter permissão para **consultar dados dos funcionários.**
- Deve **ter acesso liberado para a tela Tipo de Rescisão**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

**Configurações relacionadas**

Antes de cadastrar um **Tipo de Rescisão**, verifique:

- Conhecimento do motivo legal do desligamento;
- Consulta à [Tabela 19 – Motivos de Desligamento do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/leiautes-esocial-v-1-1-beta/tabelas.html#19);
- [Cadastro de Código de Afastamento para Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/13729923854487) realizado.

### 3. Jornada de Uso

![Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/38710122660375)

1. Acesse a tela **Tipo de Rescisão** (Pessoal+ > Cadastros).
2. Clique em **Cadastrar Tipo de Rescisão**.
3. Preencha:

| **Campos** | **Funcionalidade** | **Observações** |
| --- | --- | --- |
| **Cód.Tipo Rescisão** | Identificador único do tipo de rescisão. | Pode ser preenchido automaticamente ou manualmente, conforme a configuração do botão ![Imagem 2: Pode ser preenchido automaticamente ou manualmente, conforme a configuração do botão Configuração da Tela > Numeração .](https://ajuda.sankhya.com.br/hc/article_attachments/42315327970711) **Configuração da Tela > Numeração**. |
| **Descrição** | Descrição detalhada do tipo de rescisão. |  |
| **Aba Geral** | | |
| **Cód. Afastamento da RAIS** | Código de afastamento conforme tabela oficial do eSocial/RAIS. | É importante mencionar que para cada Tipo de Rescisão, há um [Código de Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/13729923854487) específico para Causa, FGTS e RAIS que devem ser devidamente informados, do contrário, o processo não será realizado corretamente. |
| **Cód. Afastamento FGTS** | Código de afastamento conforme tabela oficial do FGTS/Caixa. |
| **Cód. Causa do Afastamento** | Código de causa do afastamento conforme eSocial. |
| **Cód. Saque (FGTS)** | Código de tipo de saque de FGTS permitido conforme a rescisão.   - Valores aceitos:   - `S` ou `1` = Saque liberado imediatamente   - `N` ou `0` = Saque não permitido / Bloqueado   - `C` = Saque parcial permitido (contribuições)   - `T` = Saque total permitido (após período de carência)   - `A` = Saque autorizado após liberação   - `M` = Saque multa (40% de multa) - Determina se e quando o funcionário pode sacar:   - Sem justa causa: Saque total + 40% de multa   - Com justa causa: Sem saque (bloqueado)   - Acordo: Saque total, sem multa   - Morte: Saque total pelos beneficiários |  |
| **Permite gerar previsão** | Indica se este tipo de rescisão permite gerar previsões de rescisão. |  |
| **Motivo desligamento eSocial** | Motivo técnico do desligamento conforme definições da tabela 19 do eSocial. |  |

4. Clique em ![Imagem 3: Clique em Salvar (F7) .](https://ajuda.sankhya.com.br/hc/article_attachments/38710502496151) **Salvar (F7)**.

### 4. Pontos de Atenção

- Os códigos de RAIS, FGTS e Causa devem estar alinhados ao motivo real da rescisão. Configuração incorreta pode gerar:

  - Recolhimento indevido de FGTS;
  - Geração apenas de GFIP sem GRRF;
  - Inconsistências no eSocial.

    **Exemplo:** se uma Dispensa sem Justa Causa estiver configurada com código de FGTS de Pedido de Demissão, o recolhimento poderá ocorrer apenas via GFIP, sem geração de GRRF.
- Sempre valide o **Motivo de desligamento eSocial** antes de utilizar o tipo no cálculo.
- O cadastro do Tipo de Rescisão apenas configura os códigos no sistema. O envio ao eSocial acontece na **Central do eSocial**, após salvar e calcular a rescisão do funcionário.

### 5. Dicas de Usabilidade

- Utilize descrições padronizadas para facilitar a identificação pelos usuários.
- Revise os códigos sempre que houver atualização na legislação.
- Teste a previsão antes de aplicar o tipo de rescisão em produção.

### Artigos Relacionados

- [Aviso Prévio](https://ajuda.sankhya.com.br/hc/pt-br/articles/38693057310487)
- [Cálculo de Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847)
