---
id: "37861019296791"
titulo: "Como parametrizar os contratos para cálculo de vencimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento"
trilha: "Universidade Sankhya > Jornada de Serviços"
atualizado_em: "2026-07-22T14:06:52Z"
rotulos: ["Configuração", "Parceiro", "Contrato", "Vencimento", "Financeiro"]
---

# Como parametrizar os contratos para cálculo de vencimento

| Categoria |
| --- |
| [Como funciona o cálculo de vencimento das faturas do contrato?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7QBPX5QXS1FMSYBJ4VQZZ) |
| [Quais problemas esse processo resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7RCZNH9RCKWXPV5Z7FRYW) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7RP0CJF3N4WSKDVNRYEY9) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7RZSHJ4KBM6M1A87D8VAX) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7SCK5T0TF949GXEMRNY82) |
| [Cálculo de vencimento fixo](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7TFM933DQQ7JGJYAQ0F5S) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7SXG6WA5P20TRWRHVHG8V) |
| [Cálculo de vencimento com uma quantidade fixa de dias úteis](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7T9TG3SMRG53M3QDGSVRC) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7X3XNR2NQ79SFRCSA05AN) |
| [Cálculo de vencimento utilizando a configuração do Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7Y8S5K3Y6VMXTBYBQ692A) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37861019296791-Como-parametrizar-os-contratos-para-c%C3%A1lculo-de-vencimento#h_01KFK7YE26AR99HNVJ7H9060EN) |

## Parametrização para cálculo de vencimento da faturas do contrato

#### Como funciona o cálculo de vencimento das faturas do contrato?

Quando um contrato é faturado, o sistema precisa saber qual será a data de vencimento da nota gerada. Essa data pode seguir um padrão fixo ou ser calculada com base em regras específicas, conforme o tipo de negociação definido no contrato.

No Sankhya, existem dois caminhos principais:

**Vencimento fixo** - Aqui, o dia do vencimento é sempre o mesmo, independente da data em que o contrato foi faturado. Ideal para contratos com previsibilidade e clientes que organizam o fluxo de caixa com antecedência.

**Vencimento variável** - Neste modelo, o sistema calcula a data de vencimento conforme regras que você parametriza. Entre as variações possíveis:

- **A partir da data de faturamento utilizando o Tipo de Negociação**: o vencimento é calculado conforme a data do faturamento e o tipo de negociação associado ao contrato.
- **Considerando uma quantidade fixa de dias úteis a partir da data de faturamento**: o sistema adiciona uma quantidade definida de dias úteis à data de faturamento.
- **Prazo fixo (em dias corridos) com base no dia 1º do mês de referência**: soma-se um número fixo de dias corridos, contando a partir do primeiro dia do mês em que o serviço foi prestado.

#### Quais problemas esse processo resolve?

- Permite atender diferentes exigências de clientes: cada um pode ter um modelo de cobrança diferente.
- Facilita o controle do contas a receber, pois os vencimentos seguem um padrão claro.
- Reduz erros e retrabalho, pois evita a necessidade de editar notas manualmente após a emissão.

#### Quais os riscos de não utilizar?

Se o contrato não estiver corretamente parametrizado para o cálculo de vencimento, o financeiro pode perder o controle sobre os prazos e ter dificuldades para prever quando os valores serão recebidos. A nota pode sair com vencimento no mesmo dia do faturamento, quando o combinado com o cliente era um prazo maior, ou ainda vencer antes da data acordada. Esse desalinhamento compromete a relação com o cliente, gera dúvidas no momento da cobrança e exige retrabalho para cancelar ou corrigir as notas emitidas com vencimento incorreto.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1102633108)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto**: Você já cadastrou alguns contratos anteriormente. Agora, é hora de revisar e parametrizar a regra de vencimento das faturas conforme o combinado com cada cliente:

**Contrato – Super Mais:** Esse contrato já tem a regra de vencimento definida: dia 10 de cada mês, independentemente da data de faturamento. 

**Contrato – Bom Preço:** Ficou definido com o cliente que o vencimento será sempre 5 dias úteis a partir da  data do faturamento.

**Contrato – Comercial Viana:** Prefere pagar 20 dias corridos após o 1º dia do mês de referência.

**Tarefas**: 
Acesse o contrato do cliente Super Mais e valide se os campos estão configurados corretamente e o vencimento definido como fixo.

Configure os demais contratos para que o vencimento calculado atenda o que foi definido com os clientes.

#### Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya

##### Cálculo de vencimento fixo:

- Acesse a tela **Contratos**
  Menu: Contratos e Serviços » Arquivos » Contratos
- Na seção de **Filtros rápidos,** preencha o campo **Parceiro** informe, Super Mais.
- Abra o contrato do parceiro e confira os seguintes campos na aba **Propriedades**:

**Dia do pagamento** - Deve estar com o valor 10

**Prazo de vencimento** - Deve ficar vazio

**Dia Fixo para vencimento** - Esse campo deve ficar marcado para que o vencimento aconteça sempre no dia 10 de cada mês

- Salve as informações

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1102633540)

##### Cálculo de vencimento com uma quantidade fixa de dias úteis:

- Acesse a tela **Contratos**
  Menu: Contratos e Serviços » Arquivos » Contratos
- No campo **Parceiro** informe, Rede Bom Preço para localizar o contrato desse cliente.
- Abra o contrato do parceiro e confira os seguintes campos na aba **Propriedades**:

**Dia do pagamento** - Deve estar com o valor 5 pois serão 5 dias úteis a partir da data do faturamento.

**Prazo de vencimento** - Deve ficar vazio

**Dia Fixo para vencimento** - Desmarcado

**Considera dia do pagamento como dia útil -** Marcado

- Salve as informações

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1103861724)

##### Cálculo de vencimento com uma quantidade fixa de dias corridos:

- Acesse a tela **Contratos**
  Menu: Contratos e Serviços » Arquivos » Contratos
- No campo **Parceiro** informe, Comercial Viana para localizar o contrato desse cliente.
- Abra o contrato do parceiro e confira os seguintes campos:

**Dia do pagamento** - Deve estar com o valor 0 pois não utilizaremos esse campo.

**Prazo de vencimento** - 20 pois serão 20 dias.

**Dia Fixo para vencimento** - Desmarcado.

**Considera dia do pagamento como dia útil -** Desmarcado.

- Salve as informações

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1103239726)

##### Cálculo de vencimento utilizando a configuração do Tipo de Negociação:

- Acesse a tela **Contratos**
  Menu: Contratos e Serviços » Arquivos » Contratos
- No campo **Parceiro** informe, **Frigolog Distribuidora** para localizar o contrato desse cliente.
- Abra o contrato do parceiro e confira os seguintes campos:

**Tipo negociação -** A prazo 45 dias

- Salve as informações

#### Correção e Repetição

- Garanta que cada contrato possui suas regras de vencimento devidamente configuradas.
- A validação dos cálculos de vencimento será feita nas próximas atividades então não altere essas informações.
