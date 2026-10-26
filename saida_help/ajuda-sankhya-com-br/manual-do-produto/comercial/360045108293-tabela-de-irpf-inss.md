---
id: "360045108293"
titulo: "Tabela de IRPF/INSS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:28:17Z"
rotulos: ["AJUDA DO SKW", "manual", "Tabelas", "Configuração", "Tabela de IRPF/INSS", "br.com.sankhya.com.cad.tabeladeirpfinss", "Tabela de IRPF/INSS manual", "Impostos", "Financeiro", "INSS", "IRPF", "Despesas Financeiras", "Retenção de INSS", "Retenção de IRPF"]
---

# Tabela de IRPF/INSS

```
 Módulo: Comercial > Arquivo > Cadastros > Alíquotas
```

---

Através desta tela realiza-se o lançamento de títulos de despesas financeiras correspondentes aos recibos de pagamento referentes ao autônomo. Estes títulos possuem retenção de INSS e IRPF com base na tabela progressiva para que as operações estejam em conformidade fiscal.

Esta tela traz às regras de cálculo do imposto IRPF, às regras de cálculo do imposto INSS e com às regras de qual(is) [Parceiro(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) e [Serviço(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553) se enquadram naquele cálculo.

Para saber mais sobre as funcionalidades desta tela, acesse os links abaixo:

| Funcionalidades da tela | |
| --- | --- |
| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#PainelPrincipal) | [Aba Parceiros sujeitos a tabela progressiva](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#abaparceirossujeitosatabelaprogressiva) |
| [Aba Tabela INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#abatabelainss) | [Aba Tabela IRPF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#abatabelairpf) |
| [Cálculo do Imposto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#comportamentodarotinadeclculodoimposto) | [Cálculo de INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#comportamentoparaoclculodeinss) |
| [Cálculo do INSS para o título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#comportamentodosistemaapsefetuaroclculodoinssparaottulo) | [Cálculo de IRPF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#processodoclculodeirpf) |

---

### Painel Principal

![Imagem 1: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/25478125663511)

O campo **"Competência"** deve ser preenchido coma a data no formato MM/AAAA que corresponde ao inicio da vigência dos valores cadastrados para as alíquotas INSS/IRPF.

Informe no campo **"Regime de apuração"** se a apuração dos títulos será pela data de baixa ou pela data de movimentação, conforme os tipos de regime de apuração:

- **Caixa:** os impostos serão calculados no momento da baixa de títulos. O processo de baixa pode ser efetuado na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos) ou na tela [Baixa Automática](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115773-Baixa-Autom%C3%A1tica);
- **Competência:** os impostos serão calculados com base na data de movimentação do título. Este processo é realizado para todos os títulos da tela Movimentação Financeira.

No campo **"Valor dependente (IRPF)"** informe o valor que será descontado por dependente no cálculo da base do IRPF.

Preencha no campo **"Valor mínimo IRPF"** um valor mínimo de retenção do imposto.

Indique no campo **"Valor mínimo INSS"** o menor valor que pode ser cobrado para o INSS. Abaixo deste valor não é tributado o INSS no título.

O campo **"Valor máximo INSS"** deve ser preenchido com o maior valor de INSS que pode ser cobrado, tudo que exceder este valor não será cobrado. 

A marcação **"Utilizar cálculo INSS cumulativo?"** será utilizada no cálculo do INSS, e deverá ser selecionada em cada Competência inserida para a realização dos cálculos. 

Por meio da marcação **"Considerar FUNRURAL/INSS Parceiro?"** o sistema irá considerar os parceiros vinculados com a marcação **"Calcula FUNRURAL/INSS"** localizada no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal) selecionada para o cálculo, se esta for desativada somente aqueles que forem inseridos na aba Parceiros sujeitos a tabela progressiva serão utilizados no cálculo do INSS.

Com a marcação **"Considerar desconto simplificado para cálculo do IRPF?"** habilitada e o campo **"Método de Cálculo IRRF"** incluído na grade financeiro na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota), ao lançar uma nota fiscal de compra e serviço, o sistema aplicará os métodos para cálculo do IRPF simultaneamente, por deduções legais e por desconto simplificado, destacando nos campos das abas [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abafinanceiro) na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) e [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos#impostos) na Movimentação Financeira, o menor valor calculado entre os dois, indicando a retenção do imposto destacado, bem como o método utilizado para a retenção no campo Método de Cálculo IRPF. 

Na ótica do [EFD-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553-EFD-Reinf), ao incluir a referência da nota lançada nos moldes acima e gerar o arquivo, o documento deverá ser gerado no evento [R-4010](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553-EFD-Reinf#abar1040) considerando o valor do imposto de renda retido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#top)

### Aba Parceiros sujeitos a tabela progressiva

Configure nesta aba os Parceiros para os quais o sistema deve calcular o INSS/IRPF.

![Imagem 2: Configure nesta aba os Parceiros para os quais o sistema deve calcular o INSS/IRPF.](https://ajuda.sankhya.com.br/hc/article_attachments/25481704543127)

O campo **"Parceiro"** permite associar um Parceiro que seja pessoa física e que esteja ativo.

Por meio do campo **"Serviço"** relacione um Parceiro a um Serviço ativo previamente cadastrado no sistema.

Informe no campo **"Número de Dependentes"** o total de dependentes do parceiro, este campo será utilizado para o cálculo da base do IRPF. O valor default do campo é zero.

Com a marcação **"Retém INSS em documentos de origem financeira?"** habilitada, ao lançar um Financeiro que seja de origem no financeiro e atenda as configurações desta rotina, o campo **"Funrural Retido:/INSS Retido"** da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), aba [Outras Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abageral) estará marcado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#top)

### Aba Tabela INSS

Nesta aba tem-se as faixas de alíquotas utilizadas para o cálculo do INSS no período de competência.

![Imagem 3: Nesta aba tem-se as faixas de alíquotas utilizadas para o cálculo do INSS no período de competência.](https://ajuda.sankhya.com.br/hc/article_attachments/25481572211863)

Informe no campo **"Limite"** o maior valor para o qual a alíquota será aplicada, considerando o limite anterior. Caso não exista limite anterior, o valor deverá ser 0,00, por exemplo:

| - Limite: 1.240,70 - Alíquota: 8% | - Limite: 2.079,50 - Alíquota: 9% |
| --- | --- |

**(1)** Neste caso de 0,00 a 1.240,70 a alíquota a ser aplicada será 8%, caso o valor do desdobramento seja entre 1.240,71 a 2.079,50 a alíquota deverá ser 9%.

No campo **"Alíquota"** informe o percentual que será utilizado para o cálculo do imposto.

**Observação:** nessa aba será possível cadastrar a tabela que será utilizada para o cálculo do INSS em que o limite de retenção do INSS para cada parceiro na competência será definido no campo Valor máximo INSS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#top)

### Aba Tabela IRPF

Nesta aba são configuradas as faixas de alíquotas praticadas no período de competência.

![Imagem 4: Nesta aba são configuradas as faixas de alíquotas praticadas no período de competência.](https://ajuda.sankhya.com.br/hc/article_attachments/38426962236951)

Ela é divida em duas sub-abas, sendo que:

#### Sub aba Tabela IRPF

Contém as faixas de alíquotas e limites tradicionais.

No campo **"Limite"** indique o maior valor para o qual a alíquota será aplicada, considerando o limite anterior. Caso não exista limite anterior, o valor deverá ser 0,00, por exemplo:

| - Limite: 2.428,80 - Alíquota: 0% - Valor da dedução: 0,00 | - Limite: 2.826,65 Alíquota: 7,5% Valor da dedução: 182,16 |
| --- | --- |

**(1)** Neste caso de 0,00 a 2.428,80 a alíquota a ser aplicada será 0% (com dedução de 0,00), caso a base de IRPF seja entre 2.428,81 a 2.826,65 a alíquota deverá ser 7,5% (com dedução de 182,16).

Por meio do campo **"Alíquota"** informe o percentual que será utilizado para o cálculo do imposto.

O campo **"Valor da dedução"** pode ser preenchido com o valor que será descontado para calcular o valor do IRPF durante o cálculo.

Ao lançar notas fiscais retroativas (ou seja, referentes a meses anteriores ao da criação da nota), é importante saber que o valor do IR (Imposto de Renda) não será calculado automaticamente com base no mês de competência da nota.

Nesses casos, o valor do imposto deve ser preenchido manualmente pelo usuário, utilizando os dados corretos da tabela de IR correspondente ao mês desejado. Assim, é possível garantir que o cálculo esteja conforme as regras aplicáveis ao período da nota.

**Importante:** verifique a tabela de IR no sistema (Comercial > Arquivo > Cadastros > Alíquotas > Tabela de IRPF/INSS) referente ao mês correto e insira os valores no campo Vlr IRF, localizado na aba Financeiro da nota.

#### Sub aba Redutor Adicional

Ela é utilizada para configuração do benefício da Lei nº 15.270/2025. Deve-se preencher as colunas **Limite**, **Dedução** e **Coeficiente** conforme o padrão para 2026:

- Limite 5000,00 | Dedução 312,89 | Coeficiente 0.
- Limite 7350,00 | Dedução 978,62 | Coeficiente 0,133145.

O processo de cálculo do IRPF para competências a partir de 01/01/2026 segue uma nova etapa após a aplicação da regra tradicional:

##### Aplicação do Redutor Adicional (Lei nº 15.270/2025)

Após encontrar o valor do imposto pela regra tradicional, o sistema identifica se o **Rendimento Tributável** se enquadra nas novas faixas de redução:

1. **Rendimentos até R$ 5.000,00:** o sistema aplica um redutor integral para garantir a **isenção total**. O valor do redutor é limitado ao valor do IR calculado, resultando em um IRRF final de **R$ 0,00**.
2. **Rendimentos entre R$ 5.000,01 e R$ 7.350,00:** o sistema aplica um desconto progressivo calculado pela fórmula:
   - **Fórmula:** Dedução - (Coeficiente \* Valor do Rendimento).
   - **Exemplo de cálculo:** 978,62 – (0,133145 × Rendimento Tributável).
   - O valor apurado nesta fórmula é subtraído do IRRF tradicional para gerar o valor final a ser retido.
3. **Rendimentos acima de R$ 7.350,00:** não se aplica o redutor adicional. O cálculo permanece exclusivamente o tradicional conforme a tabela progressiva vigente.

**Observação Importante:** o valor do redutor adicional nunca poderá ser superior ao valor do IRRF apurado pelo cálculo tradicional, evitando que o imposto retido seja negativo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#top)

#### Cálculo do Imposto

O sistema realizará o cálculo dos impostos de IRF e INSS no financeiro de acordo com as alíquotas e limites definidos na tabela progressiva sempre que for lançado um título de despesa na tela Movimentação Financeira com o parceiro que estiver na tabela progressiva de IRPF e INSS e a data da movimentação corresponder ao mês igual ao da competência da tabela progressiva (para caso de regime de competência), ou se a data de baixa estiver no mês igual ao da competência da tabela (para caso de regime de caixa).

Caso as regras acima sejam atendidas, o sistema verificará o valor do desdobramento com os valores limites de cada imposto e verificará em qual deles ele se encaixa.

**Importante:** o parâmetro **"Desconsiderar Fin. não aplica Tab. Prog. IRPF/INSS - DESFINTABIRINSS"** influenciará na rotina de cálculo do imposto. Desta forma, quando o mesmo encontrar-se desligado, tem-se o seguinte comportamento:

- Se a TOP estiver configurada para calcular conforme a tabela de IRPF/INSS, o valor do desdobramento do financeiro será utilizado para o cálculo conforme a tabela considerando outros financeiros (mesmo que estes não encontrem-se configurados para esta TOP) dentro da mesma competência para compor a base de cálculo.

Quando o parâmetro estiver habilitado, tem-se o comportamento a seguir:

- Se a TOP estiver configurada para calcular conforme a tabela de IRPF/INSS, o valor do desdobramento do financeiro será utilizado para o cálculo conforme a tabela considerando outros financeiros (que estejam configurados para esta mesma TOP) dentro da mesma competência para compor a base de cálculo.

**Observação:** caso o parâmetro seja utilizado no modo habilitado, deve-se atentar se encontra-se no início da competência pois, caso aconteça de ligar ou desligar o mesmo no meio de uma competência, um erro no cálculo será ocasionado devido à uma parte já ter sido calculada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#top)

#### Comportamento para o Cálculo de INSS

Após o sistema verificar o valor do desdobramento e analisar em qual linha dos limites se encaixa, aplicará a alíquota ao valor do desdobramento a partir da fórmula abaixo para o cálculo do imposto:

```
 Valor INSS = Valor do desdobramento * (Alíquota 100)
```

Se o regime for caixa o processo será feito após a baixa. Se o regime for competência o processo será efetuado após lançamento do titulo na tela Movimentação financeira, levando em consideração a data de movimentação do título.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#top)

#### Cálculo do INSS para o Título

Para o cálculo do valor do INSS, o sistema verificará as seguintes condições:

- Quando o valor do INSS não atinge o valor informado no valor mínimo: o valor do INSS é zero na tela Movimentação Financeira, porque não será cobrado imposto.
- Quando o valor do INSS estiver dentro dos limites (é igual ou maior que o mínimo ou é menor ou igual ao máximo): é feito uma verificação em ordem decrescente pela data do título nos títulos do período de competência daquele parceiro (o campo serviço não é utilizado) verificando se existem títulos que não atingiram o valor mínimo. O Valor do INSS é acumulado e adicionado no valor do INSS.
- Quando o valor do INSS ultrapassar o valor informado no campo valor máximo: se a soma do valor do imposto na competência em questão (considerando o título que está sendo lançado no momento) for maior que o valor máximo do imposto definido na tabela progressiva, será calculado somente o valor que falta para atingir o máximo, por exemplo:

Valor máximo: 457,00

Valor calculado na competência: 275,00

Valor calculado para o título atual: 275,00

Total: 550,00 é maior que o máximo, então a conta deverá ser:

Valor máximo – Valor calculado na competência=

457,00-275,00=182,00

Então, o valor do imposto neste caso seria 182,00 em vez de 275,00.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#top)

#### Cálculo de IRPF

O processo será realizado sempre que for lançado um título de despesa na tela Movimentação Financeira. Se o regime for caixa o processo será feito após a baixa. Se o regime for competência o processo será efetuado após lançamento do titulo na Movimentação Financeira levando em conta a data da movimentação do título.  

Para o cálculo da base de IRPF o sistema irá subtrair o valor do INSS e o valor do dependente considerando o número de dependentes que o parceiro possui, conforme a seguinte fórmula:

```
 BASE DO IRPF = Valor do desdobramento - Valor do INSS - (dependentes * valor dependente)
```

**Nota:** o valor dos dependentes pode ser subtraído do valor do desdobramento do título somente se for o primeiro título a calcular o IRPF utilizando a tabela progressiva para aquele parceiro em questão dentro da competência, ou seja, o valor dos dependentes pode ser subtraído somente uma vez na competência.

Após a base ser encontrada, o sistema aplicará a alíquota do imposto para encontrar o valor, de acordo com a seguinte fórmula:

```
 Valor IRPF = ((BASE DO IRPF * (Alíquota/100)) – Valor dedução) – Valor já retido
anteriormente na competência (se houver)
```

Nos próximos títulos, o sistema calculará o IRPF considerando os títulos que calcularam o imposto para o parceiro em questão na mesma competência.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108293-Tabela-de-IRPF-INSS#top)
