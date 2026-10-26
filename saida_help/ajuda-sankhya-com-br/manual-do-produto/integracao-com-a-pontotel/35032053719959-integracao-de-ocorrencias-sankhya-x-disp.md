---
id: "35032053719959"
titulo: "Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com a Pontotel"
atualizado_em: "2026-09-26T01:41:25Z"
rotulos: ["Configuração", "Ocorrências", "Integração", "LOGTABOPER", "Pontotel", "Integração Sankhya <> Pontotel", "Log de Alterações do Gateway", "ID: br.com.sankhya.rh.LancamentoOcorrencias", "Pessoas+", "Afastamentos", "Dispensas"]
---

# Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel

**Módulo**: Pessoas+ / Integrações
**Caminho de Acesso**: Menu Principal > Integrações > Dispensas e Afastamentos

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#1-descri%C3%A7%C3%A3o-da-funcionalidade)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#2-pr%C3%A9-requisitos)
- [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#3-diagrama-de-fluxo)
- [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#4-jornada-de-uso)
- [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#5-pontos-de-aten%C3%A7%C3%A3o)
- [6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#6-dicas-de-usabilidade)
- [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#faq-%E2%80%93-d%C3%BAvidas-frequentes)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959-Integra%C3%A7%C3%A3o-de-Ocorr%C3%AAncias-Sankhya-x-Dispensas-e-Afastamentos-Pontotel#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **integração entre Sankhya e Pontotel permite que ocorrências lançadas no Sankhya Om sejam automaticamente refletidas na Pontotel como afastamentos ou dispensas**, conforme o tipo e configuração.

Isso elimina lançamentos manuais, agiliza o processo de abono de jornadas e garante consistência entre os sistemas. Além dos tipos que abonam dias inteiros, também são integrados os tipos que abonam parcialmente a jornada, com atualização recorrente e imediata.

### 2. Pré-requisitos

- **Permissões necessárias**
  - Ter contratado e implementado o Pessoal+ e o Sankhya Om.
  - Ter realizado o [setup de integração Sankhya/Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063).
- **Parâmetros essenciais**
  - Habilitação do recurso Log de Alterações do Gateway (parâmetro LOGTABOPER - Ativar armazenamento de log de modificações em tab = ligado na tela Preferências do Sankhya Om).
- **Configurações relacionadas**
  - Base Sankhya online e responsiva durante as consultas.
  - Token válido e URL atualizada no [Gateway](https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway).
  - Data final preenchida nos lançamentos de Ocorrências no Sankhya Om. Afastamentos não precisa ter a data final informada.
  - Folha do colaborador destravada no período em que a dispensa/afastamento será integrado.

### 3. Diagrama de fluxo

![Imagem 1: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/35032053718167)

### 4. Jornada de Uso

#### Cadastro e lançamento da Ocorrência

1. O usuário realiza o cadastro da ocorrência/afastamento na tela **Ocorrências** do Sankhya Om.

   ![Imagem 2: O usuário realiza o cadastro da ocorrência/afastamento na tela Ocorrências do Sankhya Om.](https://ajuda.sankhya.com.br/hc/article_attachments/35034080249367)
2. Faz o lançamento da ocorrência/afastamento para o funcionário.

   ![Imagem 3: Faz o lançamento da ocorrência/afastamento para o funcionário.](https://ajuda.sankhya.com.br/hc/article_attachments/35034095301911)

Os **anexos incluídos no lançamento** (ex: atestado ou outros comprovantes) **não** **serão integrados para o lançamento na Pontotel.** Os mesmos seguirão disponíveis para consultas/conferências no Sankhya Om.

#### Integração do lançamento de Ocorrências

O sistema valida o tipo de ocorrência e pré-requisitos. 

**1. Ocorrências Exclusivas de Afastamento**

Estes eventos são integrados como afastamentos, pois representam ausências prolongadas ou de natureza específica.
A = Acidente de Trabalho
D = Doença
G = Licença Gestante
P = Licença Paternidade
R = Licença Representante Sindical

**2. Ocorrências Exclusivas de Dispensa**

Este evento é integrado como dispensa, geralmente por representar ausências pontuais e justificadas por lei, sem caracterizar um afastamento contínuo.
I = Atestado em Horas

**3. Ocorrências com Classificação Flexível**

Para as ocorrências listadas abaixo, o usuário pode escolher se elas serão integradas como afastamento ou dispensa, dependendo das políticas internas da empresa e da natureza específica do evento.
B = Bonificado
E = Licença Alistamento Eleitoral
J = Licença Comparecimento em Juízo
K = Licença Remunerada
M = Serviço Militar
O = Licença Óbito
S = Sem Remuneração
T = Atestado em Dias

Os seguintes tipos de **ocorrências** **não são integrados**:

C = Compensação em Dias - é tratado no banco de horas na Pontotel
F = Férias - tratada no fluxo de integração de férias
H = Trabalhado - não abona jornada
L = Faltas - é tratada na folha na Pontotel
N = Não é Afastamento - não abona jornada
Q = Compensação em Horas - é tratada no banco de horas na Pontotel
X = Faltas em Horas - é tratada na folha na Pontotel
4 = Reintegração - não abona jornada

A ocorrência é integrada automaticamente à Pontotel como dispensa na folha do funcionário, abonando horas ou dias.

![Imagem 4: A ocorrência é integrada automaticamente à Pontotel como dispensa na folha do funcionário, abonando horas ou dias.](https://ajuda.sankhya.com.br/hc/article_attachments/35034601193495)

Além da configuração para definir os tipos não "fixo" como dispensa ou afastamento, também é possível para as ocorrências de dispensas definir se os lançamentos integrados na folha do colaborador devem:

- descontar DSR (sim ou não);
- considerar a dispensa como horas trabalhadas (sim ou não);
- descontar nas horas da jornada do dia (sim ou não).

Tais configurações serão aplicadas a todos os lançamentos integrados.

#### Integração do lançamento de Afastamentos

As ocorrências caracterizadas como afastamentos refletem na folha, abonando dia(s):

- cadastro;

  ![Imagem 5: cadastro;](https://ajuda.sankhya.com.br/hc/article_attachments/35035253515031)
- folha.

  ![Imagem 6: folha.](https://ajuda.sankhya.com.br/hc/article_attachments/35035268479511)

É possível definir para os afastamentos se os lançamentos integrados no cadastro e folha do colaborador devem removê-lo do REP-P durante o afastamento. Caso seja removido, ele não estará disponível nos coletores para registro de ponto. 

#### Campos integrados

**Ocorrência (Sankhya) → Dispensa (Pontotel)**

| **Campo Sankhya** | **Campo Pontotel** | **Descrição** |
| --- | --- | --- |
| Tabela consultada no Sankhya: TFPOCO e TFPHIS | | |
| CODEMP | Código do funcionário | O código do empregador e código do funcionário são utilizados para identificar na  Pontotel o empregado cujo período deverá ser abonado. O código do cadastro do  empregado na Pontotel deverá ter código igual à concatenação CODEMP+CODFUNC. |
| CODFUNC |
| CODEMP | Código | Código único que identifica o lançamento na Pontotel e permite que o mesmo seja atualizado. |
| CODFUNC |
| NUOCOR |
| DESCRHISTOCOR | Motivo padrão | A descrição da ocorrência no Sankhya Om integra como motivo padrão. |
| DTINICOCOR | Data hora início | Data e horário de início do abono. |
| DTFINALOCOR | Data hora fim | Data e horário do fim do abono. |

**Ocorrência (Sankhya) → Afastamento (Pontotel)**

| **Campo Sankhya** | **Campo Pontotel** | **Descrição** |
| --- | --- | --- |
| Tabela consultada no Sankhya: TFPOCO e TFPHIS | | |
| CODEMP | Código do funcionário | O código do empregador e código do funcionário são utilizados para identificar na Pontotel empregado cujo período deverá ser abonado. O código do cadastro do empregado na Pontotel deverá ter código igual à concatenação CODEMP+CODFUNC. |
| CODFUNC |
| CODEMP | Código | Código único que identifica o lançamento na Pontotel e permite que o mesmo seja atualizado. |
| CODFUNC |
| NUOCOR |
| DESCRHISTOCOR | Nome da Jornada | A descrição da ocorrência no Sankhya Om integra com nome da jornada na Pontotel. |
| DTINICOCOR | Data início | Data início do abono. |
| DTFINALOCOR | Data fim | Data do fim do abono, se não estiver preenchida, é considerado como indeterminado. |

### 5. Pontos de Atenção

- O fluxo contempla a inclusão, atualização e também a exclusão das ocorrências, que devem ser realizadas no Sankhya Om para refletirem na Pontotel (caso contrário, a dispensa será novamente atualizada conforme as informações que constam na Sankhya).
- Ocorrências sem data final ou apenas com data de retorno prevista não integram.
- Afastamentos podem não conter data fim preenchida, abonando por um período indeterminado.
- Folha travada impede integração; destrave antes de lançar ou atualizar.
- Tipos "fixo" têm configuração padrão, mas tipos não "fixo" podem ser ajustados conforme regras do cliente.
- Ocorrências lançadas diretamente na Pontotel não são sincronizadas com o Sankhya Om.
- Na primeira execução, apenas ocorrências dos últimos 30 dias são integradas automaticamente.

### 6. Dicas de Usabilidade

- Antes de lançar ocorrências/afastamentos, verificar se não há lançamentos sobrepostos no período.
- Utilizar filtros de tipo de ocorrência para facilitar a gestão.
- Configurar se deve descontar DSR, considerar como horas trabalhadas ou descontar da jornada.

### 7. Casos de Uso

✅ **Exemplo Real:** 

Lançamento de atestado médico no Sankhya Om, com data final preenchida, integrado automaticamente como dispensa na folha do empregado na Pontotel.

❌ **Erro Comum:** 

Tentar integrar dispensa sem data final ou com folha travada no Sankhya Om, impedindo o abono na Pontotel.

## FAQ – Dúvidas Frequentes

1. **Quais tipos de ocorrência são integrados?**

   Tipos que abonam dias inteiros ou parcialmente, conforme configuração. Tipos “fixo” têm integração padrão; tipos não “fixo” podem ser ajustados.
2. **O que acontece se a folha estiver travada?**

   A integração não ocorre; é necessário destravar a folha para que o lançamento seja refletido.
3. **Posso integrar dispensas sem data final?**

   Não. Dispensas exigem data final preenchida para integração.
4. **Os anexos do Sankhya são integrados à Pontotel?**

   Não. Anexos permanecem disponíveis apenas no Sankhya.
5. **Como excluir ou atualizar lançamentos?**

   Realize a alteração no Sankhya; a Pontotel refletirá automaticamente, desde que a folha esteja destravada.

## Artigos Relacionados

- [Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
- [Setup inicial de integração Sankhya <> Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063)
- [Integração de Empresas Sankhya x Empregadores Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919)
- [Integração de Funcionários Sankhya x Empregados Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031)
- [Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207)
- [Integração de Escalas Pontotel e Carga Horária Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887)
- [Integração de Férias Sankhya x Férias Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023)
- [Integração de Usuários (Sankhya) x Usuários (Pontotel)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951)
- [Integração de Apontamentos e Faltas Pontotel x Verbas e Faltas Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/35056595712279)
