---
id: "10086051863063"
titulo: "Como cadastrar as fórmulas contábeis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10086051863063-Como-cadastrar-as-f%C3%B3rmulas-cont%C3%A1beis"
trilha: "Manual do Produto > Pessoas+ > Integração Contábil e Financeira > Estrutura Contábil e Plano de Contas"
atualizado_em: "2026-10-02T17:49:08Z"
rotulos: ["Configuração", "Fórmulas", "Impostos", "Contabilização", "Fórmula", "br.com.sankhya.rh.FormulaContabil", "Fórmula Contábil", "Configurar base e percentuais (FGTS INSS etc.)", "Adicionar fórmulas para eventos e impostos", "Descrição condições e fórmulas secundárias", "Pessoal+"]
---

# Como cadastrar as fórmulas contábeis

```
 Módulo: Pessoal+ > Cadastros
```

O cadastro das fórmulas que serão utilizadas para a contabilização de eventos ou para a base dos impostos é feito na tela Fórmulas Contábeis (Pessoal+ > Cadastros). Sendo que, devem ser associadas às [configurações de integração contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/10137196517783) para os eventos provisionados e aqueles de base de encargos.

![Imagem 1: O cadastro das fórmulas que serão utilizadas para a contabilização de eventos ou para a base dos impostos é feito na…](https://ajuda.sankhya.com.br/hc/article_attachments/29807195372695)

Para a criação de fórmulas, clique no botão ![Imagem 2: Para a criação de fórmulas, clique no botão "Adicionar Fórmula" e depois, na seção " Informações Gerais" , preencha a…](https://ajuda.sankhya.com.br/hc/article_attachments/18700212253847) **"Adicionar Fórmula"** e depois, na seção **"Informações Gerais"**, preencha a **"Descrição"**. 

Caso esta fórmula utilize condições, ative a marcação **"Utiliza condição"**, assim será exibida a marcação **"Edita segunda fórmula"** que irá atrelar a segunda fórmula à primeira fórmula.

[GIF animado: Imagem 3: Caso esta fórmula utilize condições, ative a marcação "Utiliza condição" , assim será exibida a marcação "Edita segunda…](https://ajuda.sankhya.com.br/hc/article_attachments/29807456838167)

Na seção **"Valor Base"**, marque as opções que serão incorporadas ao cálculo. São elas:

|  | **Descrição** | **Funcionalidade** | **Aplicação** |
| --- | --- | --- | --- |
| **Utiliza valores de incorporação? (V\_Incorpora)** | Indica se o evento deve **incorporar valores automáticos** ao cálculo. | - Quando marcada, o sistema incorpora automaticamente valores configurados no evento ao cálculo da folha de pagamento. - Quando desmarcada, o valor não é incorporado e pode ser tratado como adicional ou extra. | Eventos que possuem incorporação automática (como auxílio-doença incorporado, abono incorporado). |
| **Considera 1/3 de férias?** | Indicador para inclusão do **1/3 adicional de férias.** | - Quando ativada, o sistema calcula e **adiciona automaticamente 1/3 (um terço) do valor das férias** ao pagamento de férias, conforme legislação trabalhista brasileira. - Quando desativada, calcula apenas o valor base das férias sem o terço adicional. | Eventos de férias que devem receber o acréscimo de 1/3 sobre o valor das férias. |
| **Desconsidera valor de licença gestante? (V\_licgest)** | Indicador para **exclusão do valor de licença maternidade** dos cálculos. | - Quando marcada, o sistema **não inclui o período de licença maternidade** no cálculo deste evento específico. - Quando desmarcada, inclui normalmente.   Útil para eventos que não devem considerar o período de ausência da gestante. | Eventos que possuem regras específicas que excluem períodos de licença maternidade (como comissões, bônus por assiduidade). |
| **Desconsidera valor de licença gestante 13º salário? (V\_licgest13)** | Indicador para **exclusão específica do valor de licença maternidade no cálculo do 13º salário.** | - Quando marcada, o sistema **exclui períodos de licença maternidade** do cálculo do 13º salário deste evento. - Quando desmarcada, inclui normalmente. Diferencia-se do campo anterior por ser específico apenas para 13º. | Eventos que têm tratamento diferenciado para licença maternidade no cálculo do 13º (ex: adicional noturno, periculosidade que não se estendem à licença maternidade no 13º). |
| **Desconsidera valor de afastamentos parte empresa? (V\_afastpartemp)** | Indicador para **exclusão de valores de afastamentos de responsabilidade da empresa.** | - Quando marcada, o sistema **exclui do cálculo deste evento todos os períodos onde houve afastamento remunerado pela empresa** (licença, suspensão temporária). - Quando desmarcada, inclui normalmente.  **Exemplo:** se a empresa tem um benefício que só se aplica quando o funcionário está trabalhando (não pago em afastamento). | Eventos que possuem regras de não-incidência em períodos de afastamento remunerado pela empresa (como auxílio-presença, bônus de assiduidade). |

Informe um **"Multiplicador"** se a fórmula utilizar um multiplicador fixo.

Já na seção **"Percentuais"**, realize as marcações que correspondem aos percentuais referentes ao FGTS, INSS, RAT, FAP, entre outros:

|  | **Descrição** | **Funcionalidade** | **Aplicação** |
| --- | --- | --- | --- |
| **Utiliza Percentual de FGTS? (V\_perfgts)** | Indica se o evento utiliza percentual de **Fundo de Garantia do Tempo de Serviço**. | - Quando marcada, o sistema calcula e aplica o percentual de FGTS (normalmente 8%) sobre o valor da rubrica. - Quando desmarcada, o FGTS não é calculado sobre esse evento.  Afeta depósitos da empresa na conta vinculada do FGTS do funcionário. | Eventos que integram a base de cálculo do FGTS (salário, adicionais, 13º, férias).  **Exemplo**: Salário base (utiliza FGTS), Bônus (pode não utilizar FGTS) |
| **Utiliza Percentual Empresa de INSS? (V\_perinss)** | Indica se o evento gera **contribuição patronal ao INSS** (desconto pela empresa)**.** | - Quando marcada, o sistema calcula o percentual de INSS a cargo da empresa (normalmente entre 8% a 28% conforme atividade) sobre o valor do evento. - Quando desmarcada, nenhuma contribuição de INSS empresa é calculada. É um custo para a empresa, não desconto do funcionário. | Eventos que formam a base de contribuição patronal ao INSS.  **Exemplo**: Salário base (utiliza INSS empresa), Plano de saúde (pode não utilizar INSS empresa) |
| **Utiliza Percentual Empresa de INSS 13º salário? (V\_perinss13)** | Indicador específico para **contribuição patronal ao INSS incidente sobre o 13º salário**. | - Quando marcada, o sistema calcula o percentual de INSS a cargo da empresa especificamente no mês do 13º salário (normalmente dezembro). - Quando desmarcada, não há cálculo de INSS empresa para esse evento em folhas de 13º. Permite diferenciação entre cálculos do INSS normal vs 13º. | Eventos que têm tratamento especial para o 13º (adicionais, comissões que só incidem no mês de 13º).  **Exemplo**: Adição integral (INSS empresa no 13º), Auxílio cesta básica (sem INSS empresa no 13º) |
| **Utiliza Percentual Terceiros de INSS? (V\_pergrps)** | Indica se o evento gera **contribuição ao INSS de terceiros** (contribuição sindical, contribuição confederativa)**.** | - Quando marcada, o sistema calcula contribuições adicionais de INSS não-patronal (como Grupo de Sincato/Contribuição Sindical - GRPS) sobre o valor do evento. - Quando desmarcada, nenhuma contribuição de terceiros é calculada. Diferentes regras de descontos podem se aplicar. | Eventos que geram contribuições sindicais ou de terceiros.  **Exemplo**: Salário base (utiliza GRPS), Auxílio complementar (pode não utilizar GRPS) |
| **Utiliza Percentual Seguro de INSS (V\_persegu)** | Indica se o evento forma a **base para cálculo de seguros de INSS** (Seguro de Acidente do Trabalho - SAT)**.** | - Quando marcada, o sistema inclui o valor do evento na base de cálculo do Seguro de Acidentes do Trabalho (SAT), que é contribuição patronal obrigatória. - Quando desmarcada, o evento não compõe a base SAT.  O SAT é uma alíquota adicional que varia de 0,5% a 3% conforme o risco da atividade. | Eventos que integram a base de cálculo do SAT.  **Exemplo**: Salário (utiliza SAT), Diárias (pode não utilizar SAT) |
| **Utiliza Percentual Seguro de INSS (V\_FAP)** | Indica se o evento forma a **base para cálculo do FAP (Fator Acidentário de Prevenção).** | - Quando marcada, o sistema inclui o valor do evento na base de cálculo do FAP, que é um modificador aplicado ao SAT (Seguro de Acidente do Trabalho).  O FAP varia de 0,5 a 2,0 conforme o histórico de acidentes da empresa. - Quando desmarcada, o evento não participa do cálculo do FAP. É um ajuste ao SAT baseado em desempenho. | Eventos que devem considerar o FAP corporativo.  **Exemplo**: Salário (utiliza FAP), Reembolsos (normalmente não utilizam FAP) |
| **Utiliza percentual pis s/folha (V\_perPIS)** | Indica se o evento incide na **base de cálculo do PIS (Programa de Integração Social) - desconto do funcionário.** | - Quando marcada, o sistema calcula o PIS sobre o valor do evento (alíquota de 1% a 2,65% conforme a categoria). - Quando desmarcada, nenhum PIS é calculado. É uma contribuição social descontada do funcionário ou paga pela empresa conforme regime. | Eventos que formam a base de cálculo do PIS.  **Exemplo**: Salário (utiliza PIS), Auxílio-educação (pode não utilizar PIS) |
| **Utiliza Percentual RAT? (V\_perRAT)** | Indica se o evento forma a **base para cálculo do RAT (Risco Ambiental do Trabalho - adicional sobre SAT).** | - Quando marcada, o sistema inclui o valor do evento na base de cálculo do RAT, que é uma alíquota adicional ao SAT aplicada para empresas com riscos ambientais específicos (0,5% a 5% conforme o agente nocivo). - Quando desmarcada, o evento não participa do RAT. É um adicional ao SAT para proteção em ambientes insalubres. | Eventos que devem considerar o adicional de risco ambiental.  **Exemplo**: Salário base (utiliza RAT), Adicional de insalubridade (pode não utilizar RAT, pois já é compensação) |

Ao finalizar as configurações, clique em **"Finalizar Edição"** no canto superior direito da tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10086051863063-Como-cadastrar-as-f%C3%B3rmulas-cont%C3%A1beis#top)
