---
id: "39369036119447"
titulo: "ICMS não destacado no Livro Fiscal para Nota Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39369036119447-ICMS-n%C3%A3o-destacado-no-Livro-Fiscal-para-Nota-Fiscal"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-08-31T18:21:32Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "ICMS", "TOP", "CST", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# ICMS não destacado no Livro Fiscal para Nota Fiscal

**Situação**

Quando os campos **Base de ICMS**, **Alíquota** e **Valor do ICMS** do Cadastro Livro ICMS/IPI são alimentados — e quando o valor é desviado para as colunas Isentas ou Outras, mesmo havendo imposto destacado na nota **(sendo esse destaque, devido ou não)**.

**Causa**

Em todos os casos abaixo, considera-se que a nota **tem base, alíquota e valor de ICMS preenchidos no item** e que a nota entra no livro normalmente. O que muda de um caso para o outro é apenas o destino desse valor.

Duas situações diferentes, que não devem ser confundidas:

- **Campos alimentados** — o valor é escriturado como crédito (entradas) ou débito (saídas) nas colunas de ICMS do livro.
- **Campos não alimentados** — a linha da nota é gerada no livro, mas os campos de ICMS ficam zerados e o valor contábil é levado para a coluna **Isentas** ou **Outras**. Não há erro de geração: é uma decisão de escrituração.

Premissas fixas de todos os cenários:

1. CFOP do item com ICMS p/ o Livro Fiscal = Usar da TOP/Empresa;
2. nota liberada;
3. TOP atualizando o livro fiscal;
4. empresa **não** optante pelo Simples Nacional;
5. nota de venda ou compra;

**Solução**

## REGRAS QUE VALEM PARA TODOS OS CSTS

| **Condição** | **Resultado** |
| --- | --- |
| **TOP com Tipo de ICMS = Sem créd/déb — Isentas** | Todo o valor contábil vai para a coluna Isentas. Os campos de ICMS não são alimentados em nenhum CST — a opção da TOP decide antes de o sistema olhar o CST do item. |
| **TOP com Tipo de ICMS = Sem créd/déb — Outras** | Todo o valor contábil vai para a coluna Outras. Os campos de ICMS não são alimentados em nenhum CST. |
| **CFOP do item com ICMS p/ o Livro Fiscal = Isentas ou Outras** | O CFOP prevalece sobre a TOP. Mesmo com a TOP marcada para creditar ou debitar, o valor vai integralmente para Isentas ou Outras e os campos de ICMS ficam zerados. |
| **Empresa optante pelo Simples Nacional, com “Considerar Tipo de ICMS da TOP p/ entrada em empresa Simp.Nac.?” = Não**  **e**  **“Escriturar valor de ICMS de entrada para Empresa Simples?” = Não** | O Tipo de ICMS da TOP é ignorado: o sistema trata a nota como Outras e não escritura ICMS de nenhum CST. |

##

## O CAMPO DO CADASTRO DE EMPRESAS QUE MUDA O RESULTADO

A partir daqui o comportamento se divide em dois conjuntos de regras, definidos pelo campo **Usar Tratamento de Código Tributação Definido no Cadastro de Empresas?** (aba Geração ICMS/IPI do Cadastro de Preferências da Empresas). Nesta relação ele aparece como “Trat. por CST”.

### Trat. por CST = Sim

Cada CST tem um campo próprio no Cadastro de Empresas dizendo para onde o valor contábil vai (Isentas ou Outras). A maioria dos CSTs deixa de escriturar ICMS nesta configuração.

**Dois campos deixam de ter efeito:** “Tratar Código Tributação Isentas como Isentas?” e “Tratar Diferenciamento Parcial?” não são consultados — valem apenas na outra configuração.

Todos os campos por CST precisam estar preenchidos. Se algum estiver em branco, a geração do livro é interrompida com a mensagem “Tratamento por cód.trib. incompleto, corrija em Preferências/Empresa.” — não há comportamento silencioso.

### Trat. por CST = Não

Vale a regra interna padrão do sistema. Menos CSTs são bloqueados, e as opções Com créd/déb — Isentas e Com créd/déb — Outras passam a escriturar ICMS em todos os CSTs.

**Aqui sim** os campos “Tratar Código Tributação Isentas como Isentas?” (CST 40) e “Tratar Diferenciamento Parcial?” (CST 51 e 53) decidem o resultado.

## Relação por CST: quando os campos de ICMS do Livro Fiscal são alimentados

Ter valor de ICMS na nota e a TOP marcada para creditar ou debitar **não garante** que os campos **Base de ICMS**, **Alíquota** e **Valor do ICMS** sejam preenchidos na tela "Cadastro Livro ICMS/IPI". O CFOP, o CST do item e os campos por CST do Cadastro de Empresas decidem, nessa ordem, se o valor entra nas colunas de ICMS ou vai para **Isentas** ou **Outras**.

Nos quadros abaixo, considera-se que a nota tem base, alíquota e valor de ICMS preenchidos no item, que a nota está liberada e que a TOP atualiza o livro fiscal. Duas situações diferentes, que não devem ser confundidas:

- **Campos alimentados**: o valor é escriturado como crédito (entradas) ou débito (saídas) nas colunas de ICMS do livro.
- **Campos não alimentados**: a linha da nota é gerada no livro, mas os campos de ICMS ficam zerados e o valor contábil é levado para a coluna Isentas ou Outras. Não é erro de geração: é uma decisão de escrituração.

### Regras que valem para todos os CSTs

- **TOP com Tipo de ICMS = "Sem créd/déb - Isentas"**: todo o valor contábil vai para Isentas e nenhum CST escritura ICMS. A opção da TOP decide antes de o sistema olhar o CST do item.
- **TOP com Tipo de ICMS = "Sem créd/déb - Outras"**: todo o valor contábil vai para Outras e nenhum CST escritura ICMS.
- **CFOP do item com "ICMS p/ o Livro Fiscal" = Isentas ou Outras**: o CFOP prevalece sobre a TOP. Mesmo com a TOP marcada para creditar ou debitar, o valor vai integralmente para Isentas ou Outras.
- **Empresa optante pelo Simples Nacional**, com "Considerar Tipo de ICMS da TOP p/ entrada em empresa Simp.Nac.?" = Não e "Escriturar valor de ICMS de entrada para Empresa Simples?" = Não: o Tipo de ICMS da TOP é ignorado, o sistema trata a nota como Outras e não escritura ICMS de nenhum CST.

### O campo do Cadastro de Empresas que muda o resultado

A partir daqui o comportamento se divide em dois conjuntos de regras, definidos pelo campo **"Usar Tratamento de Código Tributação Definido no Cadastro de Empresas?"**, na aba "Geração ICMS/IPI" do Cadastro de Empresas. Nos quadros ele aparece abreviado como **Trat. por CST**.

- **Trat. por CST = Sim**: cada CST tem um campo próprio no Cadastro de Empresas dizendo para onde o valor contábil vai (Isentas ou Outras). A maioria dos CSTs deixa de escriturar ICMS. Os campos "Tratar Código Tributação Isentas como Isentas?" e "Tratar Diferenciamento Parcial?" **não são consultados** nesta configuração. Todos os campos por CST precisam estar preenchidos: se algum estiver em branco, a geração é interrompida com a mensagem "Tratamento por cód.trib. incompleto, corrija em Preferências/Empresa."
- **Trat. por CST = Não**: vale a regra interna padrão. Menos CSTs são bloqueados, e as opções "Com créd/déb - Isentas" e "Com créd/déb - Outras" passam a escriturar ICMS em todos os CSTs. É aqui que os campos "Tratar Código Tributação Isentas como Isentas?" (CST 40) e "Tratar Diferenciamento Parcial?" (CST 51 e 53) decidem o resultado.

### Quadro resumo: os campos de ICMS são alimentados?

**Saídas**

| CST | Trat. por CST = Sim Com créd/déb do imposto | Trat. por CST = Sim Com créd/déb Isentas ou Outras | Trat. por CST = Não Com créd/déb do imposto | Trat. por CST = Não Com créd/déb Isentas ou Outras |
| --- | --- | --- | --- | --- |
| **00** | **SIM** | **SIM** | **SIM** | **SIM** |
| **02** | **NÃO** | **NÃO** | **NÃO** | **NÃO** |
| **10** | **SIM** | **SIM** | **SIM** | **SIM** |
| **15** | **NÃO** | **NÃO** | **NÃO** | **NÃO** |
| **20** | **SIM** | **SIM** | **SIM** | **SIM** |
| **30** | **NÃO** | **NÃO** | **SIM** | **SIM** |
| **40** | **NÃO** | **NÃO** | **DEPENDE** | **SIM** |
| **41** | **NÃO** | **NÃO** | **NÃO** | **SIM** |
| **50** | **NÃO** | **NÃO** | **NÃO** | **SIM** |
| **51** | **SIM** | **SIM** | **DEPENDE** | **SIM** |
| **53** | **PARCIAL** | **PARCIAL** | **PARCIAL** | **PARCIAL** |
| **60** | **NÃO** | **NÃO** | **NÃO** | **SIM** |
| **61** | **NÃO** | **NÃO** | **NÃO** | **NÃO** |
| **70** | **SIM** | **SIM** | **SIM** | **SIM** |
| **90** | **SIM** | **NÃO** | **SIM** | **SIM** |

**Entradas** (apenas os CSTs em que o resultado muda em relação às saídas)

| CST | Trat. por CST = Sim Com créd/déb do imposto | Trat. por CST = Sim Com créd/déb Isentas ou Outras | Trat. por CST = Não Com créd/déb do imposto | Trat. por CST = Não Com créd/déb Isentas ou Outras |
| --- | --- | --- | --- | --- |
| **10** | **NÃO** | **NÃO** | **NÃO** | **SIM** |
| **15** | **NÃO** | **NÃO** | **NÃO** | **NÃO** |
| **30** | **NÃO** | **NÃO** | **NÃO** | **SIM** |
| **70** | **NÃO** | **NÃO** | **NÃO** | **SIM** |

**SIM** = campos de ICMS escriturados. **NÃO** = valor vai para Isentas ou Outras. **DEPENDE** e **PARCIAL** = ver a linha do CST na relação detalhada. As exceções cadastrais do final do artigo prevalecem sobre este quadro.

### Relação detalhada: CST 00 a 41

| CST | Situação | Resultado | Observação |
| --- | --- | --- | --- |
| **00** | TOP: Com créd/déb do imposto | **ALIMENTA** | Vale nas duas configurações da empresa. |
| **00** | TOP: Com créd/déb - Isentas ou Outras | **ALIMENTA** | A diferença entre o valor contábil e a base vai para Isentas ou Outras. |
| **02** | Qualquer opção da TOP, em venda ou compra | **NÃO ALIMENTA** | Tratamento monofásico: base e valor do ICMS são zerados no fim da geração e o imposto vai para o campo de ICMS Retido. Nenhuma configuração de TOP ou de empresa altera. |
| **10** | Saída, qualquer opção com créd/déb | **ALIMENTA** | Escritura nas duas configurações. |
| **10** | Entrada, Trat. por CST = Sim, qualquer opção com créd/déb | **NÃO ALIMENTA** | Valor vai para Isentas ou Outras conforme "Valor da Substituição Tributária ou Valor Contábil p/ Cód.Trib. 10 e 15 em Entradas". |
| **10** | Entrada, Trat. por CST = Não, Com créd/déb do imposto | **NÃO ALIMENTA** | Valor levado para a coluna Outras. |
| **10** | Entrada, Trat. por CST = Não, Com créd/déb - Isentas ou Outras | **ALIMENTA** | Escritura o ICMS mesmo em entrada com substituição. |
| **10** | Entrada, exceções | **DEPENDE** | CFOP 1410, 1411, 2410, 2411, 1918 ou 2918; ou "Escriturar compras de emissão própria (Tributação 10 e 70)?" = Sim em nota de emissão própria; ou TOP relacionada em "Creditar ICMS e ICMS/ST da NFe Entrada ref. Remessa Garantida (CST 010)" com CFOP 1949 ou 2949. |
| **15** | Qualquer opção da TOP, em venda ou compra | **NÃO ALIMENTA** | Além do bloqueio das entradas com substituição, vale o tratamento monofásico: base e valor zerados no fim da geração, e o ICMS somado ao ST vai para o campo de ICMS Retido. |
| **20** | Qualquer opção com créd/déb | **ALIMENTA** | Escritura nas duas configurações. Com Trat. por CST = Sim, a parcela reduzida da base vai conforme "20 - Com redução de base de cálculo (Redução da base vai p/)". |
| **30** | Trat. por CST = Sim, em entrada ou saída, qualquer opção com créd/déb | **NÃO ALIMENTA** | Todo o valor contábil vai conforme "30 - Isenta e não tribut. e c/cobrança por S.T. (Valor Contábil vai p/)". |
| **30** | Entrada, Trat. por CST = Não, Com créd/déb do imposto | **NÃO ALIMENTA** | Valor levado para a coluna Outras. |
| **30** | Saída, Trat. por CST = Não, Com créd/déb do imposto | **ALIMENTA** | Em saída o CST 30 não é bloqueado nesta configuração. |
| **30** | Trat. por CST = Não, Com créd/déb - Isentas ou Outras | **ALIMENTA** | Escritura em entrada e em saída. |
| **40** | Trat. por CST = Sim, qualquer opção com créd/déb | **NÃO ALIMENTA** | Valor levado conforme "40 - Isentas (Valor Contábil vai p/)". O campo "Tratar Código Tributação Isentas como Isentas?" não é consultado nesta configuração. |
| **40** | Trat. por CST = Não, Com créd/déb do imposto | **DEPENDE** | "Tratar Código Tributação Isentas como Isentas?" = Sim: não alimenta, o valor vai para Isentas. = Não: os campos de ICMS são alimentados. |
| **40** | Trat. por CST = Não, Com créd/déb - Isentas ou Outras | **ALIMENTA** | Escritura independentemente do campo acima. |
| **41** | Trat. por CST = Sim, qualquer opção com créd/déb | **NÃO ALIMENTA** | Valor levado conforme "41 - Não tributadas (Valor Contábil vai p/)". |
| **41** | Trat. por CST = Não, Com créd/déb do imposto | **NÃO ALIMENTA** | Valor levado para a coluna Outras. |
| **41** | Trat. por CST = Não, Com créd/déb - Isentas ou Outras | **ALIMENTA** | Os campos de ICMS passam a ser escriturados mesmo em CST não tributado. |

### Relação detalhada: CST 50 a 90

| CST | Situação | Resultado | Observação |
| --- | --- | --- | --- |
| **50** | Trat. por CST = Sim, qualquer opção com créd/déb | **NÃO ALIMENTA** | Valor levado conforme "50 - Suspensão (Valor Contábil vai p/)". |
| **50** | Trat. por CST = Não, Com créd/déb do imposto | **NÃO ALIMENTA** | Valor levado para a coluna Isentas. |
| **50** | Trat. por CST = Não, Com créd/déb - Isentas ou Outras | **ALIMENTA** | Os campos de ICMS passam a ser escriturados. |
| **51** | Trat. por CST = Sim, com base de ICMS preenchida no item | **ALIMENTA** | Escritura base, alíquota e valor; a parcela diferida vai conforme "51 - Diferimento (Valor Contábil vai p/)". O campo "Tratar Diferenciamento Parcial?" NÃO é consultado nesta configuração: havendo base no item, escritura mesmo com ele desmarcado. |
| **51** | Trat. por CST = Sim, com base de ICMS zerada | **NÃO ALIMENTA** | Sem base no item, todo o valor contábil vai para Isentas ou Outras. |
| **51** | Trat. por CST = Não, Com créd/déb do imposto | **DEPENDE** | "Tratar Diferenciamento Parcial?" = Não: não alimenta, o valor vai para Isentas. = Sim: os campos são alimentados. |
| **51** | Trat. por CST = Não, Com créd/déb - Isentas ou Outras | **ALIMENTA** | Escritura independentemente do campo acima. |
| **53** | Mesmas regras do CST 51, com uma sobreposição, em venda ou compra | **PARCIAL** | O tratamento monofásico zera a base de ICMS no fim da geração e zera os campos de ST retido; o valor do ICMS permanece. O livro fica com valor de imposto sem base correspondente. |
| **60** | Trat. por CST = Sim, qualquer opção com créd/déb | **NÃO ALIMENTA** | Valor levado conforme "60 - ICMS cobrado anteriormente por S.T. (Valor Contábil vai p/)". O imposto já foi recolhido na etapa anterior. |
| **60** | Trat. por CST = Não, Com créd/déb do imposto | **NÃO ALIMENTA** | Valor levado para a coluna Outras. |
| **60** | Trat. por CST = Não, Com créd/déb - Isentas ou Outras | **ALIMENTA** | Os campos de ICMS passam a ser escriturados. |
| **60** | Exceções | **DEPENDE** | TOP relacionada em "Creditar ICMS e ICMS/ST de NFe Compra Combustível (CST 060, 061)"; ou "Creditar ICMS e ICMS ST de CT-e com CST 060 - Dec. 19671/99 AM" = Sim com a empresa localizada no Amazonas; ou cálculo de ST pelo regime especial do Decreto 38.296/PE. |
| **61** | Qualquer opção da TOP, em venda ou compra | **NÃO ALIMENTA** | Tratamento monofásico: base, alíquota e valor do ICMS são zerados, junto com os campos de ST retido. |
| **61** | Única exceção | **DEPENDE** | TOP relacionada em "Creditar ICMS e ICMS/ST de NFe Compra Combustível (CST 060, 061)". Esse cadastro é aplicado por último e devolve base, alíquota e valor. |
| **70** | Saída, qualquer opção com créd/déb | **ALIMENTA** | Escritura nas duas configurações. Com Trat. por CST = Sim, a redução vai conforme "70 - C/ redução de base de cálculo e cobrança do ICMS por S.T. (Redução vai p/)". |
| **70** | Entrada, Trat. por CST = Sim, qualquer opção com créd/déb | **NÃO ALIMENTA** | Valor levado conforme "Valor da Substituição Tributária ou Valor Contábil p/ Cód.Trib. 70 em Entradas". |
| **70** | Entrada, Trat. por CST = Não, Com créd/déb do imposto | **NÃO ALIMENTA** | Valor levado para a coluna Outras. |
| **70** | Entrada, Trat. por CST = Não, Com créd/déb - Isentas ou Outras | **ALIMENTA** | Escritura o ICMS mesmo em entrada com substituição. |
| **70** | Entrada, exceção | **DEPENDE** | "Escriturar compras de emissão própria (Tributação 10 e 70)?" = Sim em nota de emissão própria. |
| **90** | Trat. por CST = Sim, Com créd/déb do imposto | **ALIMENTA** | Base, alíquota e valor escriturados. Em entrada, a diferença de base é destinada conforme "90 - Outras Com Crédito/Débito (Valor Contábil vai p/)". |
| **90** | Trat. por CST = Sim, Com créd/déb - Isentas ou Com créd/déb - Outras | **NÃO ALIMENTA** | Todo o valor contábil vai para a coluna Outras, conforme "90 - Outras (Valor Contábil vai p/)". O CST 90 é o único que exige a opção "Com créd/déb do imposto" para escriturar. |
| **90** | Trat. por CST = Não, qualquer opção com créd/déb | **ALIMENTA** | Nesta configuração o CST 90 escritura nas três opções. |

### Exceções cadastrais que forçam a escrituração

Cadastros específicos do Cadastro de Empresas devolvem o crédito ou débito de ICMS mesmo nos CSTs bloqueados. São aplicados depois de toda a regra por CST e prevalecem sobre ela.

| Cadastro (Cadastro de Empresas) | CST afetado | Efeito |
| --- | --- | --- |
| Creditar ICMS e ICMS/ST de NFe Compra Combustível (CST 060, 061) | **60 e 61** | Recebe a relação de TOPs. Para as notas dessas TOPs, base, alíquota e valor do ICMS são gravados. É o único caminho que devolve os valores do CST 61. |
| Creditar ICMS e ICMS/ST da NFe Entrada ref. Remessa Garantida (CST 010) | **10** | Recebe a relação de TOPs. Vale para entradas com CFOP 1949 ou 2949. |
| Escriturar compras de emissão própria (Tributação 10 e 70)? | **10 e 70** | Igual a Sim, faz as entradas de emissão própria voltarem a escriturar ICMS. |
| Creditar ICMS e ICMS ST de CT-e com CST 060 - Dec. 19671/99 AM | **60** | Igual a Sim, com a empresa localizada no Amazonas. |
| Regime especial de ST do Decreto 38.296/PE | **60 e 61** | Itens com cálculo de ST por esse regime escrituram o ICMS. |

### Pontos de atenção

1. **O CST 90 é o único que exige a opção "Com créd/déb do imposto".** Com Trat. por CST = Sim, o CST 90 deixa de escriturar ICMS nas opções "Com créd/déb - Isentas" e "Com créd/déb - Outras". Nenhum outro CST tem essa exigência: o 00, o 20 e o 70 de saída escrituram nas três opções. Quem precisa do CST 90 escriturado deve usar a TOP com "Com créd/déb do imposto"; a destinação de Isentas e Outras continua sendo feita pelos campos por CST do Cadastro de Empresas.
2. **As duas configurações levam a resultados opostos.** Com Trat. por CST = Não, as opções "Com créd/déb - Isentas" e "Com créd/déb - Outras" escrituram ICMS em todos os CSTs, inclusive 40, 41, 50, 60 e nas entradas com substituição. Com Sim, essas mesmas opções bloqueiam o CST 90. Ao mudar esse campo, toda a escrituração de ICMS muda de comportamento.
3. **Dois campos da empresa só têm efeito em uma das configurações.** "Tratar Código Tributação Isentas como Isentas?" e "Tratar Diferenciamento Parcial?" são lidos apenas quando "Usar Tratamento de Código Tributação Definido no Cadastro de Empresas?" está desmarcado. Com ele marcado, o CST 51 escritura sempre que houver base de ICMS no item, ainda que "Tratar Diferenciamento Parcial?" esteja como Não; e o CST 40 nunca escritura, ainda que "Tratar Código Tributação Isentas como Isentas?" esteja como Não. É a causa mais comum de diagnóstico errado nesses dois CSTs.
4. **CSTs de combustível têm prioridade sobre qualquer configuração.** Nos CSTs 02, 15, 53 e 61 o tratamento monofásico é aplicado no fim da geração, em notas de venda e compra, e zera os campos de ICMS independentemente da TOP, do CFOP e do Cadastro de Empresas. No CST 53 o efeito é parcial: a base é zerada e o valor do imposto permanece.
5. **Entradas com substituição não creditam por padrão.** Nos CSTs 10, 15, 30 e 70 o bloqueio nas entradas existe porque o imposto foi retido na etapa anterior. Os campos "Valor da Substituição Tributária ou Valor Contábil..." apenas escolhem a coluna de destino; não devolvem o crédito. Para isso existem as exceções cadastrais acima.
6. **Antes de abrir chamado, confirmar três cadastros**, na ordem em que o sistema decide: 1) CFOP do item, cujo campo "ICMS p/ o Livro Fiscal" precisa estar em "Usar da TOP/Empresa"; 2) "Tipo de ICMS" da TOP; 3) o campo por CST no Cadastro de Empresas. Se os três estiverem coerentes com esta relação e o resultado divergir, então há o que investigar.
