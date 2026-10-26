---
id: "43539147592471"
titulo: "ICMS TTD de Santa Catarina na importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43539147592471-ICMS-TTD-de-Santa-Catarina-na-importa%C3%A7%C3%A3o"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-10-21T18:34:06Z"
rotulos: ["Nota de Nacionalização", "ICMS TTD", "ICMS TTD de Santa Catarina na importação", "TTD da empresa"]
---

# ICMS TTD de Santa Catarina na importação

**IMPEX · MANUAL DO USUÁRIO**

**ICMS TTD de Santa Catarina na importação**

Como configurar e usar o cálculo automático da antecipação de ICMS dos Tratamentos Tributários Diferenciados 409, 410 e 411 nas importações de empresas catarinenses, do parâmetro ao lançamento financeiro.

| **QUEM USA**  **Fiscal e Comex** | **ONDE**  **ImpEx › Cadastros e Portal de Importação** | **APLICA-SE A**  **Empresas com endereço em SC** |
| --- | --- | --- |

### VISÃO GERAL

#### O que é e como funciona

##### Empresas de Santa Catarina detentoras de TTD recolhem, no desembaraço, uma antecipação de ICMS calculada com alíquota reduzida sobre a base do ICMS da importação. Até agora esse valor era apurado fora do sistema e digitado à mão na nota de nacionalização.

Com esta funcionalidade o ImpEx passa a calcular a antecipação sozinho, a partir de um cadastro por empresa e Incoterm, e a levar o valor para o lugar certo conforme o modo escolhido em cada TTD:

| **MODO DIRETO**  **Soma no Vlr. Destaque da nota**  O valor calculado entra direto no campo **Vlr. Destaque** da nota de nacionalização, junto com os demais valores destacados.   - Não gera título no financeiro. - Configuração: Gera Despesa no Financeiro = Não. | **MODO DESPESA**  **Vira despesa da importação com financeiro**  O valor calculado substitui o valor de uma despesa da importação com a natureza informada no TTD e gera o título a pagar pela ação **Gerar Financeiro dos Impostos**.   - Chega à nota pelo vínculo Incoterm × Natureza. - Configuração: Gera Despesa no Financeiro = Sim + Natureza. |
| --- | --- |

Uma mesma empresa pode ter mais de um TTD ativo para o mesmo Incoterm. O sistema calcula cada um e soma os resultados, respeitando o modo de cada linha.

### PRÉ-REQUISITOS

#### Antes de começar

- **Versão do ImpEx** com o cadastro ICMS TTD disponível no menu ImpEx › Cadastros. Se o item não aparece, a atualização ainda não foi aplicada no ambiente.
- **Endereço da empresa em Santa Catarina.** O sistema lê a UF pela cidade cadastrada na empresa (Configurações › Empresas). Empresa fora de SC nunca terá TTD calculado, mesmo com o cadastro feito.
- **Termo de concessão do TTD em mãos**, com a alíquota de incidência (a alíquota cheia do ICMS usada no cálculo por dentro) e a alíquota de antecipação a recolher no desembaraço.
- **Para o Modo Despesa:** uma natureza financeira reservada para a antecipação do ICMS TTD e o parceiro que receberá o pagamento (em geral a Secretaria da Fazenda de SC).

#### Passo 1. Ativar o parâmetro de cálculo

O cálculo fica desligado por padrão. Enquanto o parâmetro estiver desmarcado, nada muda no comportamento atual do sistema, mesmo que existam TTDs cadastrados.

Caminho: **Configurações  ›  Preferências  ›  Configurações  ›  Diversas**

1. Pesquise pela chave CMX\_CALCTTDSC (descrição Calcular ICMS TTD SC (409/410/411) automaticamente).
2. No campo **Ligado/Desligado**, selecione **Ligado** e salve.
3. O parâmetro é lido a cada cálculo. Não é preciso reiniciar o servidor, basta recarregar o Portal de Importação se ele já estava aberto.

![Imagem 1: O parâmetro é lido a cada cálculo. Não é preciso reiniciar o servidor, basta recarregar o Portal de Importação se ele…](https://ajuda.sankhya.com.br/hc/article_attachments/43539147557399)

**Imagem 01.** Preferências do sistema: chave CMX\_CALCTTDSC localizada pela busca e o campo Ligado/Desligado marcado como **Ligado**.

#### Passo 2. Vincular a natureza ao Incoterm

**Somente para o Modo Despesa.** Se todos os seus TTDs forem Modo Direto, pule para o passo 3.

A natureza escolhida para o TTD precisa estar ligada ao Incoterm da importação. É nesse vínculo que você decide se a antecipação vai ou não para a nota de nacionalização, e em qual campo.

Caminho: **ImpEx  ›  Cadastros  ›  Incoterms  ›  aba Naturezas**

4. Abra o Incoterm usado nas importações que terão TTD (por exemplo FOB ou CIF).
5. Na aba **Naturezas**, inclua uma linha com a natureza reservada à antecipação do ICMS TTD. Preencha Sinal = Soma, Receita/Despesa = Despesa, o tipo de operação, o tipo de título, o parceiro e a conta bancária, como nas demais naturezas do Incoterm.
6. No campo **Liga com a Nota de Nacionalização**, escolha o destino do valor:

- **Vlr. Destaque**: a antecipação entra na nota junto dos demais valores destacados (recomendado).
- **Vlr. Outros**: a antecipação entra na nota no campo de outras despesas.
- **Sem ligação**: a antecipação gera a despesa e o título no financeiro, mas **não vai para a nota**. Use quando o recolhimento deve ficar só no financeiro.

7. Repita para cada Incoterm que terá TTD cadastrado.

![Imagem 2: Repita para cada Incoterm que terá TTD cadastrado.](https://ajuda.sankhya.com.br/hc/article_attachments/43539132027927)

**Imagem 02.** Incoterms › aba Naturezas: a natureza **ICMS TTD** incluída no Incoterm EXW, com Liga com a Nota de Nacionalização em **Sem ligação**.

#### Passo 3. Cadastrar o TTD da empresa

Uma linha por combinação de **Empresa + Tipo de TTD + Incoterm**. É aqui que ficam as alíquotas e o modo de lançamento.

Caminho: **ImpEx  ›  Cadastros  ›  ICMS TTD**

![Imagem 3: Caminho: ImpEx › Cadastros › ICMS TTD](https://ajuda.sankhya.com.br/hc/article_attachments/43539147563799)

**Imagem 03.** Tela **ICMS TTD** em ImpEx › Cadastros, com um registro já cadastrado para a empresa.

#### Campos da tela

| **Campo** | **O que informar** |
| --- | --- |
| Empresa**\*** | Empresa catarinense detentora do TTD. |
| Tipo de TTD**\*** | **409** Antecipação na Importação · **410** Crédito Presumido na Saída · **411** Crédito Presumido Ampliado. Use o código do termo de concessão. |
| Incoterms**\*** | Incoterm das importações em que o TTD se aplica. Só importações com este Incoterm recebem o cálculo. |
| Ativo | Vem como **Sim**. Marque **Não** para suspender o cálculo sem apagar a linha (útil quando o TTD vence ou é revogado). |
| % Alíq. Incidência | Alíquota cheia do ICMS usada para calcular a base por dentro (em SC, normalmente **17**). Aceita 4 casas decimais. |
| % Alíq. Antecipação | Alíquota efetiva que o TTD manda antecipar no desembaraço (por exemplo **4**, **2,6** ou **1,4**). Aceita 4 casas decimais. Com zero, nada é calculado. |
| Gera Despesa no Financeiro | **Não** = Modo Direto (soma no Vlr. Destaque). **Sim** = Modo Despesa (gera despesa e título). |
| Natureza da Despesa | Obrigatória quando Gera Despesa = Sim. Precisa ser a mesma natureza vinculada ao Incoterm no passo 2. |
| Parceiro da Despesa | Parceiro de referência para o lançamento da antecipação (em geral a Secretaria da Fazenda de SC). |

**\*** campos obrigatórios e chave do cadastro

![Imagem 4: * campos obrigatórios e chave do cadastro](https://ajuda.sankhya.com.br/hc/article_attachments/43539147568791)

**Imagem 04.** TTD em **Modo Direto**: tipo 409, Incoterm EXW, incidência 17%, antecipação 4% e Gera Despesa no Financeiro desligado.

![Imagem 5: Imagem 04. TTD em Modo Direto : tipo 409, Incoterm EXW, incidência 17%, antecipação 4% e Gera Despesa no Financeiro…](https://ajuda.sankhya.com.br/hc/article_attachments/43539132034199)

**Imagem 05.** TTD em **Modo Despesa**: tipo 411, Gera Despesa no Financeiro ligado, Natureza **ICMS TTD** e Parceiro da Despesa informados no grupo Lançamento.

#### Validações ao salvar

Quando Gera Despesa no Financeiro = Sim, o sistema bloqueia o registro nestas situações:

| **BLOQUEIO** **Natureza não informada.** Mensagem: "Informe a Natureza da Despesa para o TTD configurado com 'Gera Despesa no Financeiro' = Sim." |
| --- |

| **BLOQUEIO** **Natureza sem vínculo com o Incoterm.** Mensagem: "A natureza N não está configurada como 'Vlr. Destaque' ou 'Vlr. Outros' no incoterm X em Incoterms/Natureza..." Volte ao passo 2 e crie o vínculo, ou troque para Modo Direto. |
| --- |

![Imagem 6: BLOQUEIO Natureza sem vínculo com o Incoterm. Mensagem: "A natureza N não está configurada como 'Vlr. Destaque' ou…](https://ajuda.sankhya.com.br/hc/article_attachments/43539147571095)

**Imagem 06.** Bloqueio ao salvar um TTD com Gera Despesa ligado e sem natureza: "Informe a Natureza da Despesa para o TTD configurado com 'Gera Despesa no Financeiro' = Sim."

#### Passo 4. Gerar a nota de nacionalização

A partir daqui não há nada novo a preencher. O cálculo acontece sozinho na geração da nota, para toda importação da empresa cujo Incoterm tenha TTD ativo.

Caminho: **ImpEx  ›  Rotinas  ›  Portal de Importação  ›  Ações  ›  Gerar Nota de Nacionalização**

8. Selecione o processo de importação já desembaraçado e com as despesas lançadas.
9. Acione **Gerar Nota de Nacionalização**, como de costume.
10. Abra a nota gerada. Em **Vlr. Destaque** está o valor habitual acrescido da antecipação dos TTDs em **Modo Direto**.

![Imagem 7: Abra a nota gerada. Em Vlr. Destaque está o valor habitual acrescido da antecipação dos TTDs em Modo Direto .](https://ajuda.sankhya.com.br/hc/article_attachments/43539132040727)

**Imagem 07.** Portal de Importação: menu de ações do processo com **Gerar Nota de Nacionalização** em destaque.

![Imagem 8: Imagem 07. Portal de Importação: menu de ações do processo com Gerar Nota de Nacionalização em destaque.](https://ajuda.sankhya.com.br/hc/article_attachments/43539132043287)

**Imagem 08.** Nota de nacionalização aberta na Central de Compras: em Totais, o campo **Vlr. Destaque** já inclui a antecipação calculada.

| **CONFERÊNCIA** Para validar o valor, use a fórmula da seção Como o valor é calculado sobre os totais da aba de itens do processo. A base do TTD é a mesma base do ICMS antes do cálculo por dentro. |
| --- |

#### Passo 5. Gerar a despesa e o financeiro (Modo Despesa)

**Somente para TTDs com Gera Despesa = Sim.** Aqui o sistema recalcula a despesa da importação e cria o título a pagar.

Caminho: **ImpEx  ›  Rotinas  ›  Portal de Importação  ›  aba Despesas**

11. No processo de importação, abra a aba **Despesas** e inclua uma despesa com a **Natureza da Despesa** informada no TTD. O valor digitado é apenas provisório: será substituído pelo valor calculado.
12. Informe o parceiro favorecido e a data prevista de pagamento, como em qualquer despesa da importação.
13. Salve o processo.

![Imagem 9: Salve o processo.](https://ajuda.sankhya.com.br/hc/article_attachments/43539132045591)

**Imagem 09.** Aba **Despesas** do processo com a linha da natureza **ICMS TTD** incluída. O valor em moeda fica zerado até a geração do financeiro.

Caminho: **Portal de Importação  ›  Ações  ›  Gerar Financeiro dos Impostos**

14. Selecione o processo e acione **Gerar Financeiro dos Impostos**.
15. O sistema recalcula a despesa da natureza do TTD com a antecipação apurada, em moeda nacional, e gera o título a pagar. Ao final aparece a mensagem "Lançamento Realizado."
16. Volte à aba **Despesas**: o valor da linha foi atualizado. Na aba **Demonstração Financeira** do processo aparece o título gerado, com o número único do financeiro e esse mesmo valor.

![Imagem 10: Volte à aba Despesas : o valor da linha foi atualizado. Na aba Demonstração Financeira do processo aparece o título…](https://ajuda.sankhya.com.br/hc/article_attachments/43539132048279)

**Imagem 10.** Menu de ações do Portal de Importação com **Gerar Financeiro dos Impostos** em destaque.

![Imagem 11: Imagem 10. Menu de ações do Portal de Importação com Gerar Financeiro dos Impostos em destaque.](https://ajuda.sankhya.com.br/hc/article_attachments/43539147582615)

**Imagem 11.** Aba **Demonstração Financeira** do processo: título gerado para a natureza ICMS TTD com o valor da antecipação calculada.

| **NOTA** Na nota de nacionalização, o valor dessa despesa segue o que foi definido em Liga com a Nota de Nacionalização no passo 2: entra em Vlr. Destaque ou Vlr. Outros, ou fica só no financeiro se a opção for Sem ligação. |
| --- |

#### Passo 6. Nacionalização a partir de DI/DUIMP XML

Quem nacionaliza pelo **Portal de Importação DUIMP/DI XML** também recebe o cálculo, sem configuração adicional.

Caminho: **ImpEx  ›  Rotinas  ›  Portal de Importação DUIMP/DI XML  ›  Gerar Nacionalização**

Nesse fluxo a nota é montada a partir das mercadorias da declaração, e não das despesas do processo. Por isso o **Vlr. Destaque** da nota recebe a antecipação de **todos** os TTDs ativos do Incoterm, tanto Modo Direto quanto Modo Despesa. A base é a soma, por mercadoria, de: base do II, capatazia, II, IPI, PIS, COFINS, Siscomex, AFRMM e outras despesas.

**REFERÊNCIA**

### Como o valor é calculado

O cálculo é feito sobre o total da importação (soma dos itens), com a mesma base usada para o ICMS antes de incluir o próprio ICMS por dentro:

Base TTD = Vlr. Aduaneiro + II + IPI + PIS + COFINS + Siscomex + AFRMM

 + Outras despesas + ICMS-ST

Base ICMS = Base TTD ÷ (1 − Alíq. Incidência ÷ 100) cálculo por dentro

Valor TTD = Base ICMS × Alíq. Antecipação ÷ 100 arredondado em 2 casas

### Exemplo

Importação com base de R$ 100.000,00, TTD 409 com incidência de 17% e antecipação de 4%:

| **Etapa** | **Valor** |
| --- | --- |
| Base TTD (soma dos itens) | R$ 100.000,00 |
| Fator por dentro: 1 − 17 ÷ 100 | 0,83 |
| Base ICMS: 100.000,00 ÷ 0,83 | R$ 120.481,93 |
| **Antecipação TTD: 120.481,93 × 4%** | **R$ 4.819,28** |

Se a empresa tiver dois TTDs ativos para o mesmo Incoterm, cada um é calculado com suas próprias alíquotas e os resultados são somados, cada um indo para o destino do seu modo.

**SOLUÇÃO DE PROBLEMAS**

### Quando o valor não aparece

O cálculo devolve zero, silenciosamente, sempre que uma destas condições não é atendida. Confira na ordem:

- **Parâmetro CMX\_CALCTTDSC marcado como Ligado** (passo 1).
- **Cidade da empresa pertence a Santa Catarina** no cadastro de Empresas.
- **Existe TTD com Ativo = Sim** para a empresa e para o **mesmo Incoterm** do processo de importação.
- **% Alíq. Antecipação maior que zero** e **% Alíq. Incidência menor que 100**.
- **Os itens do processo têm valores** (aduaneiro, tributos). Base zero não gera antecipação.
- **Modo Despesa:** existe uma despesa no processo com a **mesma natureza** do TTD antes de acionar Gerar Financeiro dos Impostos.
- **Modo Despesa:** a natureza está vinculada ao Incoterm apontando para Vlr. Destaque ou Vlr. Outros (passo 2).

| **DICA:** Para suspender o cálculo em uma única empresa sem mexer no parâmetro geral, marque Ativo = Não nas linhas dela no cadastro ICMS TTD. |
| --- |

**ANEXOS**

### Índice de imagens

Lista das capturas de tela deste manual, na ordem em que aparecem.

| **IMAGEM 01** | Parâmetros do sistema, chave CMX\_CALCTTDSC marcada como Sim. |
| --- | --- |
| **IMAGEM 02** | Incoterms › aba Natureza, natureza do TTD apontando para Vlr. Destaque. |
| **IMAGEM 03** | Menu ImpEx › Cadastros › ICMS TTD e a grade do cadastro. |
| **IMAGEM 04** | Formulário do TTD preenchido em Modo Direto. |
| **IMAGEM 05** | Formulário do TTD preenchido em Modo Despesa (grupo Lançamento). |
| **IMAGEM 06** | Mensagem de bloqueio por natureza sem vínculo com o Incoterm. |
| **IMAGEM 07** | Portal de Importação, ação Gerar Nota de Nacionalização. |
| **IMAGEM 08** | Nota de nacionalização com Vlr. Destaque incluindo a antecipação. |
| **IMAGEM 09** | Aba Despesas do processo com a despesa da natureza do TTD. |
| **IMAGEM 10** | Ação Gerar Financeiro dos Impostos e mensagem Lançamento Realizado. |
| **IMAGEM 11** | Título a pagar gerado no Financeiro com o valor calculado. |

ImpEx · Comércio Exterior · Sankhya Om. Documento de apoio ao card IMPEX-759. Setembro de 2026.
