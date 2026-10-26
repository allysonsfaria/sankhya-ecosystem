---
id: "40468352285591"
titulo: "Cálculo do Frete Mínimo ANTT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40468352285591-C%C3%A1lculo-do-Frete-M%C3%ADnimo-ANTT"
trilha: "Sankhya Official Pack - SOP > TMS"
atualizado_em: "2026-08-27T12:17:27Z"
rotulos: ["MDF-e", "Configuração", "Frete", "Transporte", "Configurações TMS", "Frete Mínimo ANTT (Read-Only)", "Memória de Cálculo (Read-Only)", "Cálculo do Frete Mínimo", "Tabela de Frete ANTT", "Valida Frete Mínimo ANTT", "frete mínimo ANTT", "ANTT"]
---

# Cálculo do Frete Mínimo ANTT

A validação do Frete Mínimo ANTT garante que o valor pago ao motorista pelo afretamento não fique abaixo do piso mínimo definido pela tabela ANTT (Resoluções 5.867/2020, 5.965/2022 e atualizações). É aplicada no momento de confirmar um afretamento e impede a confirmação caso o valor acertado esteja abaixo do mínimo legal.

A regra incide sobre todos os afretamentos quando o parâmetro está habilitado, incluindo afretamentos com
veículo próprio da empresa.

![Imagem 1: A regra incide sobre todos os afretamentos quando o parâmetro está habilitado, incluindo afretamentos com veículo…](https://ajuda.sankhya.com.br/hc/article_attachments/40474194475671)

#### Variáveis Obrigatórias para o Cálculo

O cálculo do frete mínimo ANTT depende do preenchimento correto de variáveis obrigatórias para que a validação seja realizada com sucesso. As seguintes informações são necessárias:

| Variável | Descrição | Onde preencher | Formato/Validação |
| --- | --- | --- | --- |
| Distância (km) | Distância em quilômetros da rota da viagem | Ordem de Carga (Viagem) | Número > 0 |
| Tipo de Carga | Classificação da carga conforme MDF-e: Granel Sólido, Granel Líquido, Frigorificada, Conteinerizada, Carga Geral, Neogranel, Perigosa, etc. | Produto Principal (campo TPCARGAMDFE) | Seleção obrigatória (01-12) |
| Quantidade de Eixos | Soma total de eixos da composição: cavalo + carreta 1 + carreta 2 + carreta 3 | Cadastro de Veículos (campo NUMEIXOS) | Número > 0 |
| Coeficiente CC | Custo de Carga e Descarga (valor fixo em R$) conforme tabela ANTT vigente | Tabela ANTT Frete Mínimo | Valor decimal (R$) |
| Coeficiente CCD | Custo Direto de Deslocamento (valor em R$ por km) conforme tabela ANTT vigente | Tabela ANTT Frete Mínimo | Valor decimal (R$/km) |
| Tipo de Tabela (TIPTAB) | Tipo de operação: A, B, C ou D conforme composição e tipo de frota | Tabela ANTT Frete Mínimo | A | B | C | D |
| Tabela ANTT Ativa | Tabela vigente conforme Diário Oficial marcada como Ativa | Tabela de Frete ANTT | Status = Ativa (S) |
| Valor Frete Acertado | Valor em R$ acordado entre transportador e embarcador | Afretamento (Viagem) | Valor decimal (R$) ≥ Frete Mínimo |
| Composição de Veículos | Cavalo mecânico + até 3 implementos (carretas/reboques) com eixos definidos | Cadastro de Veículos e Composição | Mínimo 1 veículo com eixos > 0 |

| **Validação Crítica:**Caso alguma variável obrigatória não esteja preenchida ou possua valor zero/nulo, a rotina exibirá uma mensagem de erro e impedirá a confirmação do afretamento. Antes de confirmar, verifique se todas as informações obrigatórias foram preenchidas corretamente. |
| --- |

#### O que esta rotina valida e garante

- **Bloqueio na confirmação** quando o valor de frete acertado for menor que o frete mínimo ANTT calculado para a composição/rota.
- **Rastreabilidade** do valor calculado e da memória de cálculo em campos dedicados, permitindo que QA, operador e motorista acompanhem a validação.
- **Cálculo prévio** disparado pelo botão Calcular Valores, sem bloqueio — o operador visualiza o valor mínimo antes de tentar a confirmação.

#### Jornada do Usuário

**Fluxo padrão**

**(1)** Crie a Viagem (Ordem de Carga) e adicione um Afretamento para iniciar o processo.

**(2)** Edite o afretamento informando os dados necessários, como motorista, veículo, valor do frete acertado e adiantamento.

**(3)** Clique em **Calcular Valores** para visualizar o valor do frete mínimo ANTT calculado conforme a rota e a composição dos veículos.

> Esta ação é apenas informativa e não bloqueia a operação.

**Resultado desta etapa:** O campo de frete mínimo ANTT será preenchido com o valor calculado, e a memória de cálculo ficará disponível para consulta e rastreabilidade do cálculo realizado.

**(4)** Analise os valores apresentados e, caso necessário, ajuste o valor do frete acertado para que fique igual ou superior ao frete mínimo calculado.

**(5)** Após a conferência das informações, clique em **Confirmar Afretamento**.

**Validação realizada na confirmação:**
O sistema valida automaticamente se o valor do frete acertado é maior ou igual ao frete mínimo ANTT. Caso o valor esteja abaixo do mínimo, a confirmação será bloqueada e uma mensagem de validação será exibida.

**(6)** Se todas as validações forem atendidas, o afretamento será confirmado e passará para o status **"CONFIRMADO"**, concluindo a operação.

#### Mensagens de validação que podem ser exibidas ao operador

O sistema exibe mensagens de validação para orientar o operador durante o processo. Abaixo estão as possíveis situações e o significado de cada uma:

| Situação | Mensagem | Como resolver |
| --- | --- | --- |
| Valor de frete menor que o mínimo | "O valor do frete motorista (X) deve ser igual ou maior que o valor do frete mínimo (Y). Verifique." | Aumentar o valor do frete acertado para ser igual ou superior ao valor mínimo informado. |
| Distância da viagem zerada ou nula | "O campo Distância da viagem deve ser maior do que zero para validar o frete mínimo." | Informar a distância em km na Ordem de Carga. |
| Produto principal não informado | "Não foi encontrado o Produto Principal informado na viagem." | Garantir que um produto foi selecionado como produto principal da viagem. |
| Produto sem classificação de carga | "Não foi configurado o campo 'Tipo de Carga MDF-e' para o produto principal da viagem, não será possível validar o frete mínimo." | Contactar o departamento de cadastro para preencher o campo 'Tipo de Carga MDF-e' no produto. |
| Composição sem eixos | "Informar a quantidade de eixos da composição de veículos para validar o frete mínimo." | Garantir que os veículos (cavalo e carretas) têm a quantidade de eixos preenchida. |
| Nenhuma Tabela ANTT ativa | "Para validar o frete mínimo ANTT é obrigatório haver pelo menos uma Tabela de Frete ANTT ativa. Cadastre em: ... ou desative o parâmetro 'Valida Frete Mínimo ANTT' nas Configurações TMS." | Contactar o gestor TMS para cadastrar uma Tabela de Frete ANTT vigente nas Configurações TMS. |
| Tarifa não localizada para a combinação | "Não foi localizada tarifa mínima ANTT para X eixo(s), tipo de carga 'Y' e tipo de tabela 'Z'. Cadastre em: Tarifa Mínima ANTT." | Contactar o gestor TMS para cadastrar a tarifa para essa combinação de tipo de carga, quantidade de eixos e tipo de operação. |

#### Campos exibidos ao operador

Exibe o detalhamento do cálculo realizado para obtenção do valor do frete mínimo, no seguinte formato:

**Frete Mínimo ANTT (Read-Only)**

Exibe o valor do frete mínimo ANTT calculado pela rotina, considerando informações como distância, tipo de carga, quantidade de eixos e tipo de operação. O campo é preenchido automaticamente ao clicar em **Calcular Valores** ou ao **Confirmar**.

**Memória de Cálculo (Read-Only)**

Exibe o detalhamento do cálculo realizado para obtenção do valor do frete mínimo, no seguinte formato:

```
Tipo de Carga: [DESCRIÇÃO] | Qtd. Eixos: [NÚMERO] | Tipo de Cálculo: [TIPO] | ((KM=[DISTÂNCIA] x
CCD=[VALOR/KM]) + CC=[VALOR FIXO]) = [RESULTADO
```

Exemplo: Tipo de Carga: Carga Geral | Qtd. Eixos: 3 | Tipo de Cálculo: A | ((KM=1200 x CCD=4.50) + CC=500.00) = 5.900,00

#### Pré-requisitos para utilização da rotina

- **Validação habilitada nas Configurações TMS**

O parâmetro **"Valida Frete Mínimo ANTT"** deve estar configurado como **"S (Sim)"**. Caso esteja desativado, a validação não será executada.

- **Tabela ANTT cadastrada**

Deve existir uma tabela de frete ANTT cadastrada com os coeficientes **CC** (custo fixo) e **CCD** (custo por km) para cada combinação de tipo de carga e quantidade de eixos.

- **Produto com tipo de carga**

O produto principal da viagem deve possuir o campo **"Tipo de Carga MDF-e"** preenchido.

- **Distância informada**

A Ordem de Carga deve possuir a distância da viagem preenchida com valor maior que zero.

- **Composição com eixos**

Os veículos utilizados na viagem (cavalo e carretas) devem possuir a quantidade de eixos devidamente informada.

#### Dicas de usabilidade

- **Use Calcular Valores antes de Confirmar**

Ao clicar em **''Calcular Valores''**, é possível visualizar o frete mínimo ANTT e a memória de cálculo antes da confirmação. Caso o valor esteja abaixo do mínimo, o ajuste pode ser realizado antes da validação.

- **Consulte a memória de cálculo**

Se o valor do frete mínimo parecer divergente, verifique o campo **"Memória de Cálculo"** para entender como o cálculo foi realizado. Informações como distância ou tipo de carga incorretos podem impactar diretamente o resultado.

- **Valide os pré-requisitos antes da operação**

Ao receber mensagens de erro, verifique se todas as configurações e informações obrigatórias foram preenchidas corretamente antes de tentar novamente.

- **A validação também se aplica a veículos próprios**

A regra de frete mínimo ANTT é aplicada a todos os afretamentos, inclusive aqueles realizados com veículos próprios da empresa.

- **O valor do frete pode ser ajustado após o cálculo**

Após calcular o frete mínimo, ainda é possível editar o valor do frete acertado. Se o valor informado atender ao mínimo exigido, a confirmação será realizada normalmente.

#### Fluxo visual simplificado

| Crie a Viagem → Adicione o Afretamento → Preencha os dados do Afretamento → Clique em Calcular Valores (visualizar frete mínimo) → Ajuste o valor, se necessário → Confirme o Afretamento (validação automática) → ✓ Afretamento Confirmado |
| --- |

#### Telas utilizadas no processo de validação do frete mínimo ANTT

As telas a seguir são utilizadas na configuração e validação do cálculo do frete mínimo ANTT. É importante que os gestores TMS conheçam essas configurações para garantir o correto funcionamento da rotina.

**1. Configuração TMS**

A tela **"Configuração TMS"** (Logística » TMS » Configurações TMS) é responsável pelas configurações gerais do módulo TMS e pelo controle da validação do frete mínimo ANTT.

Para que a rotina funcione corretamente, o parâetro "Valida Frete Mínimo ANTT" deve estar habilitado (**"S" - Sim**). Quando ativado, o sistema passa a realizar a validação automática do frete mínimo durante as operações de afretamento.

Caso esse parâetro esteja desabilitado, nenhuma validação será executada e os afretamentos poderão ser confirmados sem a verificação do valor mínimo ANTT.

**O que configurar nesta tela:**

- Marque o parâmetro **"Valida Frete Mínimo ANTT"** como **"S (Sim)"** para ativar a validação.
- Verifique se há outras configurações TMS relacionadas ao frete mínimo.
- Salve as configurações após qualquer alteração realizada.

| **Pré-requisito crítico**: Esta configuração deve estar habilitada antes do cadastro das tabelas ANTT e tarifas mínimas. Sem ela ativa, as demais configurações relacionadas ao frete mínimo ANTT não serão utilizadas pela rotina de validação. |
| --- |

![Imagem 2: Pré-requisito crítico : Esta configuração deve estar habilitada antes do cadastro das tabelas ANTT e tarifas mínimas.…](https://ajuda.sankhya.com.br/hc/article_attachments/40474194476567)

**2. Tabela de Frete ANTT**

**Dependência:** Configure previamente o parâetro **"Valida Frete Mínimo ANTT"** nas **Configurações TMS** antes de realizar os cadastros desta tela.

A tela **"Tabela de Frete ANTT"** (Logística » TMS » Cadastros » Tabela de Frete ANTT) é utilizada para cadastrar as tabelas vigentes de frete mínimo publicadas pela ANTT conforme regulamentação do Diário Oficial.

Como essas tabelas podem ser atualizadas periodicamente pelo órgão regulador, é importante mantê-las sempre atualizadas no sistema.

Cadastre as faixas de tabela conforme os tipos de operação **A, B, C e D**, considerando os critérios de distância e taxas definidos pela normativa vigente. As tabelas em vigor devem estar marcadas como ativas, enquanto tabelas expiradas devem ser desativadas.

**O que configurar nesta tela:**

- **Coeficiente CC** — Custo de Carga e Descarga (valor fixo em R$);
- **Coeficiente CCD** — Custo Direto Deslocamento (valor variável em R$ por km);
- Tipo de Carga (Granel Sólido, Granel Líquido, Frigorificada, Conteinerizada, Carga Geral, Neogranel, Perigosa, etc);
- Quantidade de Eixos da composição (ex: 2 eixos, 3 eixos, 5 eixos, etc);
- Tipo de Tabela (A, B, C ou D) conforme a operação;
- Todos os campos obrigatórios para o registro completo da tarifa.

**IMPORTANTE**: Esta tela depende do cadastro prévio da **Tabela de Frete ANTT**. Primeiro, cadastre a tabela vigente e, em seguida, realize o cadastro das tarifas mínimas nesta tela. Sem as tarifas devidamente cadastradas, o sistema exibirá mensagem de erro ao tentar confirmar um afretamento.

![Imagem 3: IMPORTANTE : Esta tela depende do cadastro prévio da Tabela de Frete ANTT . Primeiro, cadastre a tabela vigente e, em…](https://ajuda.sankhya.com.br/hc/article_attachments/40474194478743)
