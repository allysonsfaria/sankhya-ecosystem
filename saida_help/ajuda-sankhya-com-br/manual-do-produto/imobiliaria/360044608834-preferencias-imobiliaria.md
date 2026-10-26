---
id: "360044608834"
titulo: "Preferências Imobiliária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria"
trilha: "Manual do Produto > Imobiliária > Imobiliária"
atualizado_em: "2026-07-29T14:07:03Z"
rotulos: ["Configuração", "Contrato", "br.com.sankhya.tim.cad.timparametrosh5", "Parâmetros", "Financeiro", "Correção da poupança e geração de parcelas", "Tipos de detalhamento de parcelas e taxas", "Tipo percentual e base de cálculo de juros", "TIMGERALBLQ", "Aluguel", "Imobiliária"]
---

# Preferências Imobiliária

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311309056535) Módulo: Imobiliária > Configuraçoes
![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311309059991) Versão disponível: a partir da 3.32
```

---

Através desta tela, você pode consultar todos os parâmetros que atuam no [Módulo Imobiliária](https://ajuda.sankhya.com.br/hc/pt-br/sections/360007732594-Imobili%C3%A1ria).

![Imagem 3: Através desta tela, você pode consultar todos os parâmetros que atuam no Módulo Imobiliária .](https://ajuda.sankhya.com.br/hc/article_attachments/360061015734)

Abaixo, temos alguns parâmetros principais e imprescindíveis para o correto funcionamento do Módulo:

#### Aluguéis

- **Parâmetro para correção do valor do depósito da poupança:**

| **TIMCODMOEPOUPA** | Este parâmetro é utilizado para indicar o índice da correção do valor do depósito quando o tipo de garantia do [Contrato de Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213) for **"Poupança"**. |
| --- | --- |

- **Parâmetros para geração do financeiro de aluguel:**

| **TIMTOPGERALUG** | Todas as parcelas de aluguel, avulsas e fechamento serão geradas com o número da TOP informada neste parâmetro. |
| --- | --- |
| **TIMNATGERALUG** | A natureza informada neste parâmetro será utilizada para a geração das parcelas de aluguel, avulsas e fechamento. |
| **TIMNATGERALUGAR** | Neste parâmetro você deverá informar a natureza para a geração de aluguéis garantidos. |
| **TIMTOPMFD** | Neste parâmetro deve-se inserir a TOP a ser utilizada para a geração de parcelas avulsas de taxas. |
| **TIMPROJGERALUG** | O Projeto informado neste parâmetro será utilizado para a geração das parcelas do tipo aluguel, avulsa, fechamento, MFD e das notas fiscais. |
| **TIMTITGERALUG** | O Tipo de Título inserido na configuração deste parâmetro será utilizado para geração das parcelas de aluguel, avulsa e fechamento. |
| **TIMALUGATEVENC** | Se este parâmetro estiver ligado, o término do período do aluguel será a própria data de vencimento e, caso esteja desligado, o vencimento será um dia após o final do período. |
| **TIMMINDIASALU** | Neste parâmetro você deverá inserir a quantidade mínima de dias para gerar o aluguel avulso. Caso a diferença de dias entre o dia do vencimento do primeiro aluguel e a data de início do contrato for maior ou igual ao informado neste parâmetro, será gerado um aluguel proporcional a estes dias; se for menor, os dias serão adicionados ao período seguinte. |
| **TIMCODLAYOUTTXT** | Informa-se neste parâmetro o Código do EDI que será utilizado para a geração do arquivo para o bureau de impressão de boletos. |
| **TIMVALDESCPARC** | Quando este parâmetro estiver ligado, não será permitido que os descontas lançados na parcela gerem um valor à receber menor do que a taxa de administração. |

| **TIMIPMESLS** | O valor informado neste parâmetro definirá se o cálculo releva a quantidade de meses em atraso. |
| --- | --- |
| **TIMAPLDEFLA** | O valor que você inserir neste, definirá se será aplicada ou não a correção com base nos índices para uma parcela não vencida. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)

#### Detalhamentos

- **Parâmetros para geração dos detalhamentos do financeiro de aluguel:**

| **TIMHISTDETLALUG** | Informa-se neste parâmetro o código do Tipo de Detalhamento que será utilizado no detalhamento da parcela do aluguel e do repasse. |
| --- | --- |
| **TIMHISTDETLTXAD** | Neste parâmetro informa-se o código do Tipo de Detalhamento que será utilizado no detalhamento da taxa de administração na parcela do aluguel e do repasse. |
| **TIMHISTDETLTXINT** | Neste, insere-se o código do Tipo de Detalhamento a ser utilizado no detalhamento da taxa de intermediação na parcela do aluguel e do repasse. |

- **Parâmetros para cálculo de juros:**

| **IMHISTJUROSLOC** | Neste parâmetro deve-se inserir o Tipo de Detalhamento de juros por atraso de pagamento nos Contratos de Locação. |
| --- | --- |
| **TIMTIPJUROSLOC** | Caso esteja informado **"C"** neste parâmetro, indica-se que o tipo de juros calculado será o juros composto (incidirá juros sobre juros); se não, será realizado o cálculo do juros simples. |
| **TIMPERCJUROSLOC** | Define-se neste parâmetro o percentual mensal de juros a ser aplicado na Atualização do Aluguel. Este percentual será dividido por 30 e multiplicado pelo número de dias em atraso, conforme o que for definido no parâmetro TIMTIPJUROSLOC. |
| **TIMJURINCMUL** | Se este parâmetro estiver ligado, o valor base para o cálculo do juros será o de **"Aluguel + Multa"**; caso esteja desligado, o valor base será apenas o valor do aluguel. |

- **Parâmetros para cálculo de multa:**

| **TIMHISTMULTALOC** | Informa-se neste parâmetro o código do Tipo de Detalhamento de multa por atraso de pagamento em Contratos de Locação. |
| --- | --- |
| **TIMMULTADIALOC** | Neste, insere-se o percentual acumulativo e o diário de multa, tendo como limite de acumulação o que for definido no parâmetro TIMMULTANDIAS. |
| **TIMMULTANDIAS** | Informa-se neste o número máximo de dias que uma multa será acumulada. |

- **Parâmetros para cálculo da correção monetária:**

| **TIMINDPROP** | Caso o mês do vencimento não possua índice cadastrado, se este parâmetro estiver ligado, pegará o primeiro índice anterior ao vencimento; caso esteja desligado, o índice será zerado. |
| --- | --- |
| **TIMHISTCORMOLOC** | Insere-se neste parâmetro o código do Tipo de Detalhamento de correção monetária por atraso de pagamento em Contratos de Locação. |

| **TIMDESLCORM** | Este parâmetro irá calcular a correção monetária em atraso, portanto o valor informado definirá se irá ter correção monetária das parcelas atrasadas. |
| --- | --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)

#### Jurídico

- **Parâmetros do envio ao DEJUR:**

| **TIMAGEFINDEJUR** | Este parâmetro define com qual periodicidade será executada a rotina de envio de títulos para o jurídico. |
| --- | --- |
| **TIMQTDDIASDEJUR** | Define-se neste parâmetro a quantidade de dias de atraso para enviar os aluguéis para o jurídico. Assim, após o título estar vencido a mais dias do que o valor do parâmetro, este será enviado ao jurídico, o boleto do contrato será bloqueado e o estágio do contrato alterado para **"Jurídico"**. |
| **TIMNOMEADVOG** | Deve-se inserir neste parâmetro o nome do advogado que será definido como advogado responsável pela cobrança do título. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)

#### Repasses

- **Parâmetro para geração automática de repasse:**

| **TIMAGEGERREP** | Este parâmetro definirá com qual periodicidade será executada a rotina de geração de repasses. O padrão cron é originário do UNIX e possui 5 possibilidades: **"Min Hor Dia Mês Sem"**, que são: Min – Minuto da execução (De 0 a 59); Hor – Hora da Execução (De 0 a 23); Dia – Dia da execução (De 0 a 31); Mês – Mês da execução (1 a 12); Sem – Dia da semana da execução (De 0 a 6, 0 é domingo).  **Nota:** Em todas estas opções, você poderá utilizar o **"\*"**, que indica todos os valores possíveis. |
| --- | --- |

- **Parâmetros da parcela de repasse:**

| **TIMTOPREP** | Insira neste parâmetro a TOP que será utilizada para gerar o financeiro das parcelas de repasse. |
| --- | --- |
| **TIMTOPREPRECCOM** | A TOP que será utilizada para gerar o financeiro das parcelas de repasse quando o mesmo for negativo e gerar uma receita à compensar, deverá ser inserida neste parâmetro. |
| **TIMNATREP** | A natureza a ser utilizada para gerar o financeiro das parcelas de repasse deverá ser inserida neste parâmetro. |
| **TIMPROJREP** | Neste parâmetro, deve-se inserir o código do projeto que será usado para gerar o financeiro das parcelas de repasse. |
| **TIMCTAREP** | Insira a Conta Bancária que será utilizada para gerar o financeiro das parcelas de repasse na configuração deste parâmetro. |
| **TIMHISDTLREPPRO** | O código do Tipo de Detalhamento a ser utilizado para gerar um detalhamento na parcela de aluguel, indicando o repasse para o proprietário deverá ser informado neste parâmetro. |
| **TIMHISDTLREPBEN** | Insira neste, o código do Tipo de Detalhamento que será usado para gerar um detalhamento na parcela de aluguel, indicando o repasse à um beneficiário. |

- **Parâmetros da compensação de títulos:**

| **TIMDIASCOMPREP** | Neste parâmetro, você deverá informar a quantidade de dias entre a data do repasse e a data de vencimento do título serão considerados para fazer a compensação no repasse. **Observação:** Caso o valor seja igual a 0, todos os títulos compensáveis em aberto e com vencimento igual ou menor à data do repasse, serão compensados; se você informar o valor 2, serão compensados com vencimento até 2 dias após a data do repasse. |
| --- | --- |
| **TIMTOPBAIDESCOM** | Informe neste parâmetro a TOP que será utilizada no momento do repasse, na baixa do título de despesa gerado para compensar a receita da imobiliária contra o Parceiro do repasse. |
| **TIMTOPBAIRECCOM** | No momento do repasse, a baixa do título de receita contra o Parceiro a ser compensada no repasse será feita com a TOP que você informar neste parâmetro. |
| **TIMHISDTLCOMREP** | Informe neste parâmetro o código de Tipo de Detalhamento que será utilizado para gerar um detalhamento na parcela de aluguel e do repasse, indicando a compensação do título. |

- **Parâmetros da geração dos detalhamentos do IRRF:**

| **TIMHISTDETLIRRF** | Insira neste parâmetro qual o Tipo de Detalhamento que será utilizado no detalhamento gerado no IRRF da parcela do aluguel e do repasse. |
| --- | --- |
| **TIMCODTABIRRF** | O código da tabela que será utilizada para o cálculo da retenção do IRRF das parcelas de aluguel deverá ser inserido neste parâmetro. |
| **TIMTIPOTABIRRF** | Neste parâmetro, informe o Tipo de Tabela que será utilizada no cálculo de IRRF. |
| **VLRCALIRRF** | Este parâmetro limitará a geração do IRRF para títulos financeiros. Desta forma, caso seja informado o valor 10 neste parâmetro, nosso sistema não permitirá que seja gerado o IRRF menor do que R$10,00. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)

#### Notas Fiscais

- **Parâmetros da nota de serviço de repasse:**

| **TIMTOPNFLOC** | Neste parâmetro você informará o Tipo de Operação para a geração da nota de taxa de administração ou intermediação, no momento da geração do repasse. A TOP não poderá gerar financeiro. |
| --- | --- |
| **TIMTIPNEGNFLOC** | Informe na configuração deste parâmetro, o código do Tipo de Negociação que será vinculada à nota de taxa de administração ou intermediação no momento da geração do repasse. |
| **TIMNATTXADMNF** | Neste, você deverá informar a natureza que será vinculada à nota, quando a mesma for uma nota de taxa de administração. |
| **TIMNATTXINTNF** | Informa-se neste parâmetro a natureza que será vinculada à nota, quando tratar-se de uma nota de taxa de administração. |

- **Parâmetros do item da nota de serviço de repasse:**

| **TIMCODCFOPNFLOC** | Informe neste parâmetro, a CFOP que será vinculada ao item das notas de taxas de administração ou intermediação. |
| --- | --- |
| **TIMSERVTXADM** | Aqui deverá ser informado o serviço que será vinculado ao item quando tratar-se de uma nota da taxa de administração. |
| **TIMSERVTXINT** | Aqui, você informará o serviço que será vinculado ao item quando tratar-se de uma nota de taxa de intermediação. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)

#### Divulgação

- **Parâmetros para configuração da divulgação de imóveis:**

| **TIMFUNDESCRANUN** | Neste, você deverá inserir a função desenvolvida no banco de dados, que retorna o texto do anúncio conforme o padrão determinado pela empresa. |
| --- | --- |
| **TIMFUNVLRANUN** | Insira neste parâmetro a função desenvolvida no banco de dados para calcular o valor do anúncio, conforme regras e valores definidos pela empresa. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)

#### FAC

- **Parâmetro para configuração da FAC:**

| **TIMCORFACRAP** | Neste parâmetro, você deverá informar o código do [Corretor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116973) que será utilizado para o lançamento de FAC rápida. |
| --- | --- |

####

- **Parâmetro para configuração da entrega de chaves:**

| **TIMNURFETERMO** | Informa-se neste parâmetro, o código do relatório formatado que será impresso como termo de saída de chaves. |
| --- | --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)

#### Fotos

- **Parâmetros para configuração da vinculação de fotos:**

| **TIMFTPFOTIMOV** | Neste parâmetro você deverá inserir o caminho para as fotos dos Imóveis após conectar ao servidor de FTP. |
| --- | --- |
| **TIMPATHREPIMOV** | Informe na configuração deste parâmetro, a pasta criada com o número do Imóvel, onde estão gravadas as fotos. |
| **TIMFTPFOTNOTA** | Você informará neste parâmetro uma nota para que a pasta das fotos seja criada, após a pasta com o número de uma nota fiscal. Esta nota deverá existir na tabela TGFCAB. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)

#### Loteamentos

| **TIMBLOCPARC** | Quando você habilitar este parâmetro, impedirá que os títulos financeiros sejam bloqueados em todo o módulo de Loteamento. |
| --- | --- |
| **TIMGERALBLQ** | Quando este parâmetro estiver ligado, as parcelas de aluguel geradas no sistema ficarão bloqueadas automaticamente. Isso significa que, na aba **"Gestão Imobiliária"** da tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), o campo **"Bloqueada"** será marcado. **Importante:** O **desbloqueio das parcelas** de aluguel pode ser realizado para as parcelas elegíveis ao desbloqueio, conforme as seguintes regras: - Parcela de receita, originada de aluguel; - Em aberto (ainda não baixada); - Vinculada ao contrato de locação e à negociação informada; - Com "Data de Vencimento Inicial" anterior à "Data do Próximo Reajuste"; - Gerada como bloqueada inicial (conforme a marcação do parâmetro "TIMGERALBLQ"); - Não renegociada. Pode-se **desbloquear** as parcelas de aluguel seguindo uma das opções abaixo: - Na tela de [Atualização de Aluguéis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045929273-Atualiza%C3%A7%C3%A3o-de-Alugu%C3%A9is), acesse o botão **"Efetivar Reajuste"** para realizar o desbloqueio. - Na rotina de [Renovação de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055876113-Renova%C3%A7%C3%A3o-de-Contratos), clique no botão "**Efetivar"** para desbloquear as parcelas. - Na aba [Negociações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abanegocia%C3%A7%C3%B5es) do [Contrato de Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o), escolha no botão **"Aluguéis"** a opção **"Gerar Aluguéis"** para desbloquear automaticamente as parcelas associadas. - Na aba [Negociações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abanegocia%C3%A7%C3%B5es) do [Contrato de Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o), botão "**Aluguéis"**, utilize a opção **"Prorrogar Negociação"**. Todas as parcelas dessa negociação serão desbloqueadas, desde que a **"Data de Vencimento Inicial"** da parcela seja menor do que a **"Data do Próximo Reajuste"** do contrato. |
| **TIMRENSEMPARC** | Quando você ligar este parâmetro, as parcelas de uma renegociação de um contrato serão zeradas. |
| **TIMNVALENTRE** | Se você habilitar este parâmetro, será possível criar parcelas de entradas e de fechamento branco com datas de vencimentos diferentes, ao efetivar uma renegociação de saldos; caso esteja desligado (padrão), este processo não poderá ser feito, fazendo com que seja emitida a seguinte mensagem:  **"Data de vencimento da primeira parcela de entrada/sinal não é igual a data especificada na renegociação."** |
| **TIMNAOVALVLRFIN** | Para rodar os contratos sem a validação de parcelas zeradas e com as intermediárias/balões acima do valor a financiar, é necessário que você habilite este parâmetro |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608834-Prefer%C3%AAncias-Imobili%C3%A1ria#top)
