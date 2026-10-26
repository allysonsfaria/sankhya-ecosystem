---
id: "13729923854487"
titulo: "Cadastro de Códigos de Afastamento para Rescisão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13729923854487-Cadastro-de-C%C3%B3digos-de-Afastamento-para-Rescis%C3%A3o"
trilha: "Manual do Produto > Pessoas+ > Rescisão > Configuração de Rescisão e Tipos de Desligamento"
atualizado_em: "2026-09-27T18:16:25Z"
rotulos: ["Configuração", "eSocial", "Folha de Pagamento", "ID: br.com.sankhya.rh.CodigoAfastamento", "Motivo de Desligamento eSocial", "Tipo de Rescisão", "Cadastro de afastamentos", "Configuração de direitos trabalhistas", "Informações para rescisão", "Cadastro de códigos de afastamento", "Configuração de direitos e tabelas", "Definição de motivos de rescisão", "FGTS", "Pessoal+", "TRCT"]
---

# Cadastro de Códigos de Afastamento para Rescisão

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros 
**ID da Tela:** br.com.sankhya.rh.CodigoAfastamento

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O **Código de Afastamento** é utilizado para identificar os diferentes tipos de desligamento ou afastamento do funcionário, como licenças, transferências, afastamentos legais, entre outros.

Ele é fundamental para garantir que as informações enviadas aos órgãos oficiais estejam corretas, especialmente em relação a:

- eSocial (eventos de desligamento);
- FGTS;
- RAIS;
- TRCT – Termo de Rescisão de Contrato de Trabalho.

#### Base legal

A correta classificação do afastamento está relacionada às seguintes normas:

- Consolidação das Leis do Trabalho (CLT);
- Manual de Orientação do eSocial (evento S-2299 – Desligamento);
- Manual da RAIS;
- Manual da GRRF/FGTS;
- Layout oficial do TRCT.

Cada tipo de desligamento possui regras específicas quanto a direitos trabalhistas (aviso prévio, 13º salário, férias, multa do FGTS, entre outros).

Essa tela é utilizada para cadastrar e parametrizar esses códigos conforme as regras da empresa.

![Imagem 1: Essa tela é utilizada para cadastrar e parametrizar esses códigos conforme as regras da empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/17849034004247)

### 2. Pré-requisitos

**Permissões necessárias**

- Deve **ter acesso liberado para a tela Código de Afastamento**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

### 3. Jornada de Uso

1. Acesse a tela **Código de Afastamento** (Pessoal+ > Cadastros).
2. Clique em **Cadastrar Códigos de Afastamento**.
3. Preencha os campos:

   - **Cód. Afastamento**: informe um código numérico interno para identificação no sistema.
   - **Descrição**: preencha um nome claro que identifique o motivo do afastamento.
   - **Código Governamental**: informe o código oficial correspondente ao motivo do afastamento.
4. Na aba **Geral**, configure os direitos aplicáveis ao afastamento:

   | **Campo** | **Funcionalidade** | **Observação** |
   | --- | --- | --- |
   | **Direito a férias com menos de um ano** | Indica se o afastamento gera direito a férias proporcionais em caso de saída antes de um ano.  - Marcado: funcionário tem direito a férias proporcionais mesmo não completando um ano. - Desmarcado: sem direito a férias proporcionais antes de um ano completo. | - Afeta cálculo de verbas rescisórias para afastamentos curtos. - Importante para validação de legislação trabalhista (CLT Art. 146-148).  Exemplo: marcar para licenças remuneradas; desmarcar para afastamentos não remunerados. |
   | **Direito ao aviso prévio** | Define se o colaborador tem direito a aviso prévio durante este afastamento.  - Marcado: o sistema obrigará o cumprimento de aviso prévio; - Desmarcado: não há obrigatoriedade de aviso prévio. | - Afeta o cálculo de dias de aviso prévio indenizado (se rescindir durante afastamento). - Integrado com cálculo de indenizações trabalhistas.  Exemplo: marcar para demissões; desmarcar para afastamentos que não geram rescisão. |
   | **Abate nos meses das médias** | Define se o período de afastamento deve ser excluído do cálculo de médias salariais.  - Marcado: o mês/período é desconsiderado para cálculos de médias. - Desmarcado: o período é incluído normalmente nas médias. | - Afeta cálculos de:    - gratificações semestrais ou anuais;   - bônus baseados em média;   - médias para contribuições previdenciárias. Exemplo: marcar para afastamentos não remunerados ou sem atividade; desmarcar para períodos normais. - Importante para garantir justiça em benefícios baseados em médias. |
   | **Direito ao décimo terceiro** | Indica se o afastamento gera direito ao pagamento de décimo terceiro salário.  - Marcado: o período de afastamento é contabilizado para cálculo de 13º; - Desmarcado: o período não conta para o 13º. | - Afeta o cálculo do décimo terceiro proporcional.  Exemplo: marcar para férias e licenças remuneradas; desmarcar para faltas injustificadas. |
   | **Direito à multa do FGTS** | Indica se o funcionário tem direito à multa de 40% sobre o saldo do FGTS durante este afastamento | - Afeta cálculos automaticamente no processamento de folha. - Importante para afastamentos que resultam em rescisão.  Exemplo: marcar para demissões sem justa causa; desmarcar para afastamentos temporários. |
5. Selecione o **Tipo de Tabela** conforme a finalidade do código:
   - RAIS;
   - Causa do afastamento;
   - FGTS.
6. O **Código HomologNet** corresponde ao campo **"22 – Causa do Afastamento"** do arquivo TRCT.

   ⚠️ É obrigatório quando o **Tipo de Tabela** for **Causa do afastamento**.

   A lista já está fixa no sistema, sendo necessário apenas selecionar a opção correspondente.

   Essa configuração é feita uma única vez e será utilizada sempre que o código for aplicado.
7. Finalizado o cadastro, clique em ![Imagem 2: Finalizado o cadastro, clique em Salvar (F7) .](https://ajuda.sankhya.com.br/hc/article_attachments/23967315950999) **Salvar [F7]**.

**Exemplo:** Demissão Sem Justa Causa

**Código:** 60

**Descrição:** Demissão sem justa causa

**Código Governamental**: 31

**Tipo de Tabela**: Causa do Afastamento

**Direitos**:

✓ **Multa FGTS** (Sim - 40%)

✓ **Décimo Terceiro** (Sim)

✓ **Aviso Prévio** (Sim ou indenizado)

✓ **Férias < 1 ano** (Sim)

☐ **Abate em Médias** (Não)

| Onde esse cadastro é utilizado no sistema:  1️⃣ **Tela Cálculos de Rescisão**  Ao realizar uma rescisão na rotina de cálculo, o sistema utilizará o  Código de Afastamento para:   - Determinar os direitos do funcionário; - Aplicar regras de cálculo (aviso, médias, 13º, multa FGTS); - Definir o motivo enviado ao eSocial; - Preencher informações no TRCT.   2️⃣ **Aba Afastamento da tela Configuração Funcionários**  No cadastro do funcionário, o Código de Afastamento selecionado será vinculado ao histórico do funcionário, registrando oficialmente o motivo do desligamento.  Essa informação passa a compor o histórico funcional e será utilizada em obrigações legais. |
| --- |

### 4. Pontos de Atenção

- O Código Governamental deve estar alinhado com a legislação vigente.
- Alterações em códigos já utilizados podem impactar históricos e obrigações transmitidas.
- Sempre valide a parametrização antes de fechar a folha.
- O **Tipo de Tabela** **Causa do afastamento** exige preenchimento do **Código HomologNet**.
- Inconsistências podem gerar:

  - rejeição no evento S-2299 do eSocial;
  - divergências na GRRF;
  - problemas no TRCT.
- O cadastro dos Códigos de Rescisão apenas configura os códigos no sistema. O envio ao eSocial acontece na **Central do eSocial**, após salvar e calcular a rescisão do funcionário.

### 5. Dicas de Usabilidade

- Utilize descrições padronizadas.
- Evite duplicidade de códigos para o mesmo motivo.
- Revise a parametrização junto ao contador antes de criar novos códigos.
- Realize testes em ambiente de homologação quando houver mudanças.

### Artigos Relacionados

- [Como realizar uma rescisão no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13729923854487-Cadastro-de-C%C3%B3digos-de-Afastamento-para-Rescis%C3%A3o#top)
