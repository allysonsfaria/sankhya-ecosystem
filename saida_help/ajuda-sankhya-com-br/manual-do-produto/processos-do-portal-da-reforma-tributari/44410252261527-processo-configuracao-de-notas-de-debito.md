---
id: "44410252261527"
titulo: "Processo Configuração de Notas de Débito IBS/CBS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Comece por aqui > Processos do Portal da Reforma Tributária"
atualizado_em: "2026-10-21T12:58:13Z"
---

# Processo Configuração de Notas de Débito IBS/CBS

**Módulo:** Livros Fiscais › Cadastros › Portal da Reforma Tributária
**Caminho de acesso:** Menu Principal › Livros Fiscais › Cadastros › Portal da Reforma Tributária › Configurações › Assistentes › NFe débito - IBS/CBS
**Versão mínima Livros:** 5.50.0

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#oque) [Painel de subtipos](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#painel) [Etapa 1: Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#etapa1) [Etapa 2: Empresas e séries](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#etapa2) | [Etapa 3: Exceção de alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#etapa3) [Etapa 4: Resumo e conclusão](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#etapa4) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#pontos) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#faq) |
| --- | --- |

## O que é e para que serve

O módulo **NFe débito - IBS/CBS**, disponível na [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria), guia você na configuração dos Tipos de Operação (TOPs) e das alíquotas usados para emitir Notas de Débito do IBS (Imposto sobre Bens e Serviços) e da CBS (Contribuição sobre Bens e Serviços) no Sankhya Om. A configuração acontece em quatro etapas (Tipo de Operação, Empresas e séries, Exceção de alíquota e Resumo), e o assistente valida o que você informa antes de avançar. Hoje o módulo cobre os subtipos 04 (Multa e juros) e 06 (Pagamento antecipado); os demais aparecem no painel com a marca **Em breve**. Esta configuração é habilitadora: ela prepara o Portal para gerar as notas, mas não emite nem monitora nenhuma delas.

![Imagem 1: O módulo NFe débito - IBS/CBS , disponível na Tela Portal da Reforma Tributária , guia você na configuração dos Tipos…](https://ajuda.sankhya.com.br/hc/article_attachments/44410252254615)

---

## Painel de subtipos

Ao abrir o módulo, você vê o painel **Nota de Débito IBS/CBS**, com dois indicadores no topo e a lista dos subtipos de nota. O indicador **Subtipos configurados** mostra o andamento, por exemplo "1 de 2 subtipos suportados", e o indicador **TOPs cadastradas** mostra as configurações ativas e inativas. Ao encerrar a configuração de um subtipo, ela deixa de ser contada nesse indicador. O filtro **Status** permite listar os subtipos pelo status escolhido.

### Colunas do painel

A lista traz uma linha para cada subtipo, de 01 a 08. Só o 04 e o 06 estão disponíveis: nos demais, o status é **Em breve** e a linha não tem ação. A caixa à esquerda de cada linha apenas indica a linha selecionada e não executa nenhuma ação. O subtipo 06 (Pagamento antecipado) aparece como **Configurado** depois da configuração, mas ainda não oferece suporte à emissão das notas.

| Coluna | O que mostra |
| --- | --- |
| Subtipo | Código e descrição do subtipo. |
| Status | **Configurado**, **Pendente** ou **Em breve**. |
| Cód. TOP | Código da TOP configurada para o subtipo. |
| Nome da TOP | Nome da TOP configurada. Em subtipo sem configuração, aparece "Não configurado". |
| IBS% | Alíquota de IBS configurada para o subtipo. |
| CBS% | Alíquota de CBS configurada para o subtipo. |
| Vigência | Data de início da vigência da exceção de alíquota. |
| Empresas | Quantidade de empresas configuradas para o subtipo. |
| Ações | Botões para iniciar, editar ou encerrar a configuração. |

### Ações do painel

Os botões da linha mudam conforme o status do subtipo.

- **Iniciar configuração** — abre o assistente em branco para um subtipo **Pendente**.
- **Editar** — abre o assistente com a configuração atual já preenchida, para um subtipo **Configurado**.
- **Encerrar** — encerra a configuração de um subtipo **Configurado**. O assistente abre o pop-up **Encerrar configuração**, e você confirma em **Sim** ou cancela em **Não**.

![Imagem 2: Encerrar — encerra a configuração de um subtipo Configurado . O assistente abre o pop-up Encerrar configuração , e você…](https://ajuda.sankhya.com.br/hc/article_attachments/44410252255255)

**⚠️ Atenção**

Ao confirmar, o assistente encerra por vigência a alíquota de IBS/CBS ativa do subtipo e o devolve ao início da configuração, com o status **Pendente**. O Tipo de Operação não é apagado e poderá ser vinculado novamente. O assistente não altera o cadastro das empresas. Para voltar a usar o subtipo, clique em **Iniciar configuração**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#sumario)

---

## Etapa 1: Tipo de Operação (TOP)

Nesta etapa você define a TOP usada para gerar as Notas de Débito do subtipo. O cabeçalho mostra o subtipo em configuração, por exemplo "Subtipo 06 — Pagamento antecipado · finNFe = 6", e a barra de etapas mostra onde você está: Tipo de Operação, Empresas e séries, Exceção de alíquota e Resumo. Em todas as etapas, **Cancelar** volta ao painel, **Voltar** retorna à etapa anterior e **Próximo** avança. Na Etapa 1, o botão **Voltar** também volta ao painel. O botão **Próximo** só é habilitado quando a etapa está válida.

A tela pergunta "Você já possui um Tipo de Operação cadastrado para esta Nota de Débito?" e oferece duas respostas: **Sim, vincular um existente** e **Não, criar um novo**. Ao iniciar uma configuração, você pode criar uma nova TOP, caso ela não exista, ou indicar uma existente. Ao editar, a etapa já abre em **Vinculando TOP existente**, com a TOP da configuração selecionada. As demais etapas são as mesmas nos dois casos.

![Imagem 3: A tela pergunta "Você já possui um Tipo de Operação cadastrado para esta Nota de Débito?" e oferece duas respostas:…](https://ajuda.sankhya.com.br/hc/article_attachments/44410275615639)

### Sim, vincular um existente

Use esta opção quando a TOP já existe no Sankhya Om. Você seleciona a TOP para associá-la à geração automática das Notas de Débito IBS/CBS.

- **Finalidade da Operação** — opcional. As opções da lista dependem das finalidades que você tem cadastradas no Sankhya Om, e a escolha aparece no resumo da Etapa 4 como **Finalidade op.**.

#### Tipo de Operação existente

**O que faz**
Seleciona a TOP já cadastrada que será usada nas Notas de Débito do subtipo.

**Quando usar**
Use quando a sua empresa já tem uma TOP para a nota de débito e você prefere aproveitá-la.

**Como funciona**
Selecione a TOP na lista, que mostra código e nome, por exemplo "159 - NOTA DE DEBITO IBS/CBS - MULTA E JUROS". A lista traz apenas as TOPs compatíveis com o subtipo: o assistente considera a finalidade e o modelo da nota de cada subtipo, por isso não há mensagem de erro de validação nessa escolha. Se a TOP que você procura não aparece na lista, ela não atende ao subtipo: a finalidade precisa ser de nota de débito (`finNFe` igual a 6) e o tipo de nota de débito (`tpNFDebito`) precisa ser igual ao do subtipo (04 para Multa e juros e 06 para Pagamento antecipado). Ajuste a TOP na tela **Tipos de Operação** ou escolha **Não, criar um novo**. Ao selecionar uma TOP, o assistente exibe uma faixa verde com "Tipo de Operação válido: [nome da TOP]".

### Não, criar um novo

Use esta opção quando ainda não existe uma TOP para a nota de débito. Você define o código e o nome da TOP, e o portal usa essa TOP para gerar as notas automaticamente. Os campos fiscais obrigatórios são preenchidos pelo assistente.

![Imagem 4: Use esta opção quando ainda não existe uma TOP para a nota de débito. Você define o código e o nome da TOP, e o portal…](https://ajuda.sankhya.com.br/hc/article_attachments/44410275617047)

- **Código da TOP** — a etiqueta ao lado do nome do campo mostra o modo de numeração, **Automática** ou **Manual**. Veja os detalhes no campo Código, mais abaixo.
- **Nome do Tipo de Operação** — vem sugerido para o subtipo, por exemplo "Nota de Debito IBS/CBS - Pagamento Antec", e pode ser editado. O botão **Próximo** fica desabilitado enquanto o campo estiver vazio.
- **CFOP de saída no estado** — vem sugerido o `5949` (Outra saída não especificada), e você pode alterar.
- **CFOP de saída fora do estado** — vem sugerido o `6949` (Outras saídas de mercadoria ou serviço), e você pode alterar.
- **Finalidade da Operação** — opcional. Selecione uma das finalidades cadastradas no Sankhya Om.
- **Preenchido automaticamente** — campos que o assistente define e que você não edita: `finNFe` igual a 6 (Nota de débito), `tpNFDebito` conforme o subtipo (por exemplo, 06 — Pagamento antecipado), Movimenta estoque igual a **Não**, Gera financeiro igual a **Não** e Numeração somente automática igual a **Sim**.

**⚠️ Atenção**

O assistente gera a TOP com um padrão pré-definido para a emissão de Notas de Débito IBS/CBS. Ajustes adicionais, como partidas contábeis, Livros Fiscais, comissões e integrações, precisam ser feitos diretamente no Cadastro da TOP.

#### Código

**O que faz**
Define o código da nova TOP.

**Quando usar**
Confira ou informe o código sempre que criar uma nova TOP.

**Como funciona**
O assistente segue o controle de numeração definido na tela **Tipos de Operação**. Se a numeração está como automática, o assistente assume o modo **Automática**; se está como manual, assume o modo **Manual**. Você não escolhe o modo no assistente. Para alterar, ajuste o controle de numeração na tela **Tipos de Operação**, antes de iniciar a configuração. No modo **Manual**, informe um código numérico, por exemplo `850`; o botão **Próximo** fica desabilitado enquanto o campo estiver vazio. Se o código informado já existir, o assistente não exibe mensagem: ele cria a TOP com o próximo número disponível a partir do código que você digitou. No modo **Automática**, o campo aparece bloqueado, já com o próximo código disponível, por exemplo `161`.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#sumario)

---

## Etapa 2: Empresas e séries

Nesta etapa você escolhe as empresas que emitem a nota de débito do subtipo e seleciona a série de cada uma. Você configura todas as empresas do grupo em uma única sessão. O título da etapa mostra quantas empresas já estão marcadas, no formato "X selecionada(s)".

![Imagem 5: Nesta etapa você escolhe as empresas que emitem a nota de débito do subtipo e seleciona a série de cada uma. Você…](https://ajuda.sankhya.com.br/hc/article_attachments/44410844431639)

### Seleção de empresas

A lista mostra as empresas com código, nome e CNPJ (Cadastro Nacional da Pessoa Jurídica).

- **Marcação da empresa** — marque a empresa para configurá-la e selecione a série na mesma linha. A marcação do cabeçalho da lista marca de uma vez todas as empresas que aparecem na grade e, ao ser desmarcada, desmarca todas elas.
- **Buscar empresa** — filtra a lista pelas empresas que contêm o texto digitado, como parte do nome ou do CNPJ. A grade mostra apenas as empresas que atendem ao que você digitou. As empresas marcadas continuam marcadas mesmo fora do filtro e entram na contagem.
- **Só selecionadas** — marque para listar apenas as empresas que você marcou na configuração em andamento.

Para avançar, marque ao menos uma empresa. Sem nenhuma marcada, o contador mostra "0 selecionada(s)" e o botão **Próximo** fica desabilitado.

### Séries de emissão

Cada empresa marcada precisa de uma série.

#### Série

**O que faz**
Define a série de emissão das notas de débito da empresa marcada.

**Quando usar**
Selecione a série de cada empresa marcada.

**Como funciona**
Selecione uma das séries disponíveis na lista. O campo só é habilitado depois que você marca a empresa. Na edição, as séries salvas vêm selecionadas e podem ser alteradas.

O assistente não permite a mesma série para empresas com o mesmo CNPJ. Quando você marca as empresas e escolhe a mesma série, ele exibe uma mensagem em vermelho, e o botão **Próximo** fica desabilitado: "As empresas {empresa 1}, {empresa 2} têm o mesmo CNPJ ({CNPJ}) e escolheram a mesma série ({série}). Séries repetidas entre empresas com o mesmo CNPJ podem misturar as faixas de numeração. Escolha uma série diferente para cada empresa." Para seguir, escolha uma série diferente para cada empresa. A mesma série pode ser usada em outro subtipo.

Se você marca uma empresa que não tem nenhuma série de NF-e cadastrada, a linha dela fica destacada em amarelo e o assistente exibe um aviso, sem bloquear o avanço: "{N} empresa(s) sem nenhuma série de NF-e cadastrada não vão entrar nesta configuração: {empresa}. Cadastre a numeração no Controle de Numeração e reconfigure depois para incluí-las."

**Impacto no sistema**
O controle de numeração da TOP é definido por empresa e série. Quando empresas com o mesmo CNPJ usam a mesma série, as faixas de numeração dessa série podem se misturar entre as empresas e quebrar a sequência. Por isso o assistente não permite a duplicidade: use uma série diferente para cada empresa.

**⚠️ Atenção**

A empresa sem série de NF-e cadastrada fica de fora da configuração. Para incluí-la, cadastre a numeração no Controle de Numeração e reconfigure o subtipo depois. Para cadastrar a numeração, você precisa ter permissão de acesso a essa opção no Controle de Acessos. Para saber mais, acesse [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#sumario)

---

## Etapa 3: Exceção de alíquota

Nesta etapa você define a exceção de alíquota IBS/CBS da TOP: a classificação tributária (CST e cClassTrib), as alíquotas de IBS e CBS e o início da vigência. O botão **Próximo** só é habilitado quando todos os campos estão preenchidos. Se faltar algum, o assistente destaca o campo em vermelho e exibe um aviso em amarelo com os campos que faltam, como "Preencha os campos obrigatórios para continuar: IBS do Município (%), Início da vigência."

**⚠️ Atenção**

Um aviso fixo no rodapé da etapa informa: "Esta exceção vale por Tipo de Operação e pode ser sobreposta por regra mais específica de alíquota. Ela só é aplicada quando os dados de imposto da nota de origem não puderem ser recuperados — quando existem, os dados da nota de origem prevalecem." O mesmo aviso reaparece no resumo da Etapa 4.

![Imagem 6: Um aviso fixo no rodapé da etapa informa: "Esta exceção vale por Tipo de Operação e pode ser sobreposta por regra mais…](https://ajuda.sankhya.com.br/hc/article_attachments/44410275618327)

### Classificação tributária

O CST (Código de Situação Tributária) e o cClassTrib (código de classificação tributária) se correlacionam: ao preencher um, o assistente ajusta o outro na hora.

#### CST de IBS/CBS

**O que faz**
Define o Código de Situação Tributária da exceção.

**Quando usar**
Selecione sempre; o campo é obrigatório.

**Como funciona**
A lista é carregada do Portal da Conformidade, por API, ao entrar na etapa. Cada opção mostra o código de 3 dígitos e a descrição, por exemplo "000 - TRIBUTAÇÃO INTEGRAL", e você pesquisa por código ou por trecho da descrição. O assistente não filtra a lista pelo tipo de nota: a escolha do CST é de responsabilidade sua. Na edição, o CST salvo vem selecionado.

#### Classificação Tributária (cClassTrib)

**O que faz**
Define a classificação tributária da exceção.

**Quando usar**
Selecione sempre; o campo é obrigatório.

**Como funciona**
Com um CST selecionado, a lista mostra só os cClassTrib cujo código começa com os 3 dígitos do CST. Por exemplo, ao selecionar o CST "000 - TRIBUTAÇÃO INTEGRAL", a lista traz apenas os códigos iniciados por 000, como "000001 - Situações tributadas integralmente pelo IBS e CBS." A lista também vem do Portal da Conformidade, por API, e você pesquisa por código ou por trecho da descrição. Se você selecionar um cClassTrib, o assistente preenche o CST automaticamente. Se você trocar o CST, o assistente mantém o cClassTrib anterior no campo, de propósito, para chamar a sua atenção para o campo que precisa de ajuste, e exibe a mensagem "Preencha os campos obrigatórios para continuar: Classificação Tributária (cClassTrib)." O botão **Próximo** fica bloqueado até você escolher o cClassTrib de novo, entre os códigos que correspondem ao novo CST, ou voltar o CST para um compatível com o cClassTrib. Na edição, os dois campos vêm preenchidos.

### Alíquotas e vigência

Estes valores formam a exceção de alíquota. Informe cada percentual entre 0 e 100, com até 4 casas decimais. Você pode usar ponto ou vírgula como separador decimal. Se você informar mais de 4 casas decimais, o assistente arredonda o valor. Com um valor inválido, o campo fica com borda vermelha e exibe a mensagem "Informe um percentual entre 0 e 100, com até 4 casas decimais."

- **IBS da UF (%)** — alíquota do IBS do estado.
- **IBS do Município (%)** — alíquota do IBS do município.
- **CBS (%)** — alíquota da CBS.
- **IBS total** — mostra a soma de **IBS da UF (%)** e **IBS do Município (%)**, calculada pelo assistente; você não edita este valor.
- **Início da vigência** — data a partir da qual a exceção passa a valer, no formato DD/MM/AAAA. O campo é obrigatório: sem a data, o assistente destaca o campo em vermelho, exibe "Preencha os campos obrigatórios para continuar: Início da vigência." e você não avança. Se você digitar uma data que não existe, o assistente a ajusta automaticamente: 30/02/2026, por exemplo, vira 02/03/2026. Data futura é permitida. Com data passada, o assistente exibe "A vigência informada é retroativa. A exceção passará a valer para os documentos a partir dessa data." e deixa você avançar.

Se um dos campos de alíquota ficar sem preenchimento, o assistente o destaca em vermelho e o inclui no aviso de campos obrigatórios. Quando os três campos de alíquota ficam com valor 0, o assistente exibe o aviso "Alíquota zero configurada." O aviso é apenas informativo e não bloqueia o botão **Próximo**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#sumario)

---

## Etapa 4: Resumo e conclusão

Esta é a revisão final antes de gravar. O resumo mostra, somente para consulta, tudo o que você configurou nas etapas anteriores, em dois grupos: **Resumo da configuração** e **Alíquotas e Empresas**. Nada é gravado enquanto você apenas revisa: a gravação só acontece quando você clica em **Finalizar**. Para ajustar algo, clique em **Voltar** até a etapa desejada.

![Imagem 7: Esta é a revisão final antes de gravar. O resumo mostra, somente para consulta, tudo o que você configurou nas etapas…](https://ajuda.sankhya.com.br/hc/article_attachments/44410275619351)

### Resumo da configuração

Este grupo mostra os dados da TOP: Finalidade NF-e (por exemplo, **6 — Nota de débito**), Subtipo (tpNFDebito), Modelo NF-e (**55 — NF-e**), Código da TOP, Nome da TOP, CFOP (saída no estado / fora do estado), Finalidade op. e Movimenta estoque. O CFOP (Código Fiscal de Operações e Prestações) aparece nos dois valores, como "5949 / 6949". Se você não escolheu a Finalidade da Operação na Etapa 1, o campo **Finalidade op.** mostra um traço (—).

### Alíquotas e Empresas

Este grupo mostra a Alíquota IBS UF, a Alíquota IBS Município, a Alíquota CBS, o CST, o cClassTrib, a Vigência, a quantidade de empresas, no formato "X empresa(s) selecionada(s)", e a série de cada empresa em **Empresa / Série**, no formato "161 — Série 1", com o código da empresa e a série escolhida. O aviso da exceção de alíquota aparece de novo abaixo desses valores.

### Finalizar a configuração

1. Revise os dois grupos do resumo. Se precisar ajustar algo, clique em **Voltar** até a etapa desejada.
2. Clique em **Finalizar**.
3. Aguarde a tela de conclusão. O assistente exibe a mensagem "Configuração concluída com sucesso." e o **Código da TOP** usada na configuração.
4. Clique em **Voltar ao painel** e confira o subtipo com o status **Configurado**.

![Imagem 8: Clique em Voltar ao painel e confira o subtipo com o status Configurado .](https://ajuda.sankhya.com.br/hc/article_attachments/44410275620503)

Se você sair do assistente antes de finalizar, nada é gravado e o painel mantém o status anterior.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#sumario)

---

## Pontos de atenção

O assistente prepara a configuração. O que acontece depois, na emissão das notas, fica em outras telas:

- A tela **Multa e Juros**, em **Movimentações › Receitas › Multa e Juros**, apenas gera o documento do subtipo 04 (Multa e juros) para o Portal de Vendas. A confirmação, a transmissão e o cancelamento da nota acontecem no Portal de Vendas. Para saber mais sobre a geração do documento, acesse [Como emitir Nota de Débito — Multa e Juros (Tipo 04)](https://ajuda.sankhya.com.br/hc/pt-br/articles/40099993722007-Como-emitir-Nota-de-D%C3%A9bito-Multa-e-Juros-Tipo-04). Para saber mais sobre a confirmação, a transmissão e o cancelamento, acesse [Tela Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Tela-Portal-de-Vendas).
- O assistente não configura a contabilidade nem a escrituração das TOPs no SPED (Sistema Público de Escrituração Digital).
- O assistente não atende Simples Nacional e MEI (Microempreendedor Individual).

**⚠️ Atenção**

O subtipo 06 (Pagamento antecipado) já pode ser configurado, mas ainda não oferece suporte à emissão: a tela específica para as notas desse subtipo está em desenvolvimento.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/44410252261527-Processo-Configura%C3%A7%C3%A3o-de-Notas-de-D%C3%A9bito-IBS-CBS#sumario)

---

## Perguntas frequentes

### Quais subtipos posso configurar?

Hoje, o 04 (Multa e juros) e o 06 (Pagamento antecipado) da Nota de Débito. Os demais aparecem no painel com a marca **Em breve**. O subtipo 06 já pode ser configurado, mas ainda não oferece suporte à emissão das notas.

### O que preciso informar para configurar um subtipo?

Você escolhe a TOP (existente ou nova), marca as empresas, seleciona a série de cada uma e informa a exceção de alíquota: CST, cClassTrib, alíquotas de IBS e CBS e início da vigência. O assistente preenche os campos fiscais obrigatórios da TOP criada.

### Posso usar uma TOP que já tenho?

Sim. Na Etapa 1, escolha **Sim, vincular um existente**. A lista mostra apenas as TOPs compatíveis com o subtipo. O assistente só cria uma nova TOP se você escolher **Não, criar um novo**.

### As alíquotas da Etapa 3 valem para todas as notas?

Não. A exceção só é aplicada quando os dados de imposto da nota de origem não podem ser recuperados; quando existem, os dados da nota de origem prevalecem. Uma regra de alíquota mais específica também pode se sobrepor à exceção.

### O que fazer se emiti uma nota com CST ou cClassTrib incorreto?

Cancele o documento no Portal de Vendas. Em seguida, clique em **Editar** no painel, corrija o CST e o cClassTrib na Etapa 3 e finalize. A nova configuração substitui a anterior, e o assistente não guarda as configurações anteriores: o reflexo delas fica nos documentos emitidos. Depois, gere o documento novamente na tela **Multa e Juros** e transmita a nota no Portal de Vendas.
