---
id: "360044602634"
titulo: "Tela Configurador de Layout da Nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-08-18T22:13:17Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Portal de Compras", "Central de Notas", "Portal de Mov. Internas", "Layout", "Portal de Vendas", "Configurador de layout da nota", "Personalização de Layout", "Valor padrão", "Vincular layout de nota à TOP", "br.com.sankhya.mge.comercial.conf.layoutnota", "Configurador de Layout da Nota manual", "Notas", "Padrão", "Nota Fiscal", "TOP", "PDV Web", "Ajuste de configurações", "Comercial"]
---

# Tela Configurador de Layout da Nota

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#antes-de-comecar)
- [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#como-usar)
- [↳ Atributos da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#atributos)
- [↳ Exportar e importar via XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#xml)
- [↳ Usar PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#pdv-web)
- [↳ Ferramentas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#ferramentas)
- [↳ Campos disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#campos-disponiveis)
- [↳ Grades disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#grades-disponiveis)
- [↳ Outros controles](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#outros-controles)
- [Inserindo um novo layout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#inserindo-layout)
- [↳ Criar um layout vazio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#layout-vazio)
- [↳ Criar usando um modelo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#layout-modelo)
- [↳ Duplicar um layout existente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#layout-duplicar)
- [Vinculando um layout nas TOPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#vincular-tops)
- [Ajustes dos campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#ajustes-campos)
- [↳ Configurar o painel](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#configurar-painel)
- [↳ Configurar o item selecionado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#configurar-item)
- [↳ Tipo de valor padrão e Valor padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#valor-padrao)

Comercial › Configuração

---

## O que é e para que serve

O **Configurador de Layout da Nota** é a tela do Sankhya Om onde você define a estrutura visual das notas e pedidos exibidos nas Centrais — Compras, Vendas e Movimentações Internas. Por meio dela, você cria modelos personalizados de tela, organiza campos, painéis e abas, e associa cada layout a Tipos de Operação (TOPs) específicas, garantindo que cada fluxo operacional exiba exatamente as informações que o usuário precisa.

Quando nenhum layout personalizado for configurado, o sistema aplica automaticamente o layout padrão do Sankhya Om. A tela não gera nem altera registros de nota — ela configura apenas a estrutura de exibição.

![Imagem 1: Quando nenhum layout personalizado for configurado, o sistema aplica automaticamente o layout padrão do Sankhya Om. A…](https://ajuda.sankhya.com.br/hc/article_attachments/41436223776279)

**⚠️ Atenção**

As configurações de valor padrão, obrigatoriedade e editabilidade de campos funcionam **apenas para documentos gerados pelos Portais** (Portal de Compras, Vendas e Movimentações Internas). Para documentos originados em outras telas, essas configurações não são aplicadas.

---

## Antes de começar

Para usar os layouts nas Centrais, é necessário vinculá-los a TOPs ou defini-los como padrão para um tipo de movimento. Sem esse vínculo, o sistema continua exibindo o layout padrão.

O acesso à tela é controlado pelo identificador `br.com.sankhya.mge.comercial.conf.layoutnota`. Usuários que precisam configurar layouts devem ter esse acesso habilitado pelo administrador do sistema em **Controle de Acessos**.

**ℹ️ Nota**

Se você utiliza o módulo Call Center / Central de Atendimento, um layout de nota é obrigatório para iniciar um atendimento que gere notas. Sem um layout configurado, o sistema exibe a mensagem: "O pedido não pode ser inicializado, pois necessita da configuração de layout da nota."

---

## Como usar a tela

Ao acessar o Configurador, a grade exibe todos os layouts já cadastrados. A partir daí, você pode criar um novo layout, editar um existente ou excluir layouts que não são mais utilizados.

O fluxo básico de configuração é:

1. Crie ou selecione um layout existente.
2. Configure os campos, painéis e abas usando as ferramentas disponíveis.
3. Vincule o layout a uma ou mais TOPs pelo botão **Visualizar TOPs**.
4. Se necessário, defina o layout como padrão para o tipo de movimento.
5. Clique em **Salvar**.

### Atributos da tela

Os campos a seguir definem as propriedades do layout que está sendo criado ou editado.

- **Código** — chave de identificação do layout, preenchida automaticamente pelo sistema.
- **Descrição** — nome do layout. Preencha com um nome que identifique claramente o tipo de nota ou operação ao qual o layout se destina.
- **Tipo de movimento** — define a qual tipo de nota o layout se aplica: Venda (V), Compra (C), Pedido de Venda (P), Devolução de Venda (D), entre outros.
- **Usar descrição como título da Central?** — quando marcada, o nome do layout é exibido como título da Central correspondente ao abrir uma nota com esse layout.
- **Usar como padrão para este tipo de movimento?** — define o layout como padrão para o tipo de movimento selecionado. Sempre que uma nota for aberta com uma TOP sem layout específico vinculado, o sistema aplica este layout automaticamente.

**ℹ️ Nota**

Somente um layout pode ser marcado como padrão por tipo de movimento. Se você marcar um segundo layout como padrão, ajuste manualmente o layout anterior.

Ao duplicar uma TOP que já possui um layout padrão configurado, a nova TOP adota automaticamente esse mesmo layout. Por esse motivo, o layout não é exibido em outros tipos de movimento.

### Exportar e importar via XML

Os botões **Visualizar layout em XML** e **Carregar layout em XML** permitem exportar e importar a estrutura completa de um layout entre registros ou bases de dados diferentes.

Para exportar: clique em **Visualizar layout em XML**. O sistema exibe o código XML do layout em uma tela separada. Copie o conteúdo para a área de transferência.

![Tela de visualização do XML do layout com o código gerado e botão de cópia](https://ajuda.sankhya.com.br/hc/article_attachments/13046667268119)

Para importar: clique em **Carregar layout em XML**, cole o XML copiado na tela exibida e clique em **Carregar XML**. Se não houver erros de sintaxe, o sistema importa e salva o layout automaticamente.

![Tela de carregamento de XML com campo para colar o código](https://ajuda.sankhya.com.br/hc/article_attachments/13046720519319)

### Usar PDV Web

O atributo **Usar PDV Web** habilita funcionalidades específicas para configuração do layout de **Pedido de Venda (P)** e **Venda (V)**. Ele não está disponível para layouts criados a partir de layout vazio — apenas para layouts padrão existentes ou criados a partir de modelo.

![Campo Usar PDV Web habilitado na tela de atributos do layout](https://ajuda.sankhya.com.br/hc/article_attachments/8050939838487)

Ao habilitar a opção, apenas as TOPs cujo campo **Modelo do Documento** (aba **NF-e/NFC-e/CF-e**) esteja configurado como uma das opções abaixo ficam disponíveis para vinculação:

- 55 – Nota Fiscal Eletrônica;
- 59 – Cupom Fiscal Eletrônico;
- 65 – Nota Fiscal Eletrônica de Venda a Consumidor.

O botão ![Botão Configurar layout do PDV Web](https://ajuda.sankhya.com.br/hc/article_attachments/16090288748055) **Configurar layout do PDV Web** abre a tela de configuração dos itens da nota. Para adicionar um campo, arraste-o da lista de campos disponíveis para uma das células da lista de produtos.

![Tela de configuração de itens do PDV Web com campos disponíveis e células da lista de produtos](https://ajuda.sankhya.com.br/hc/article_attachments/21134359877783)

No lado direito de cada célula, o botão ![Botão Remover campo](https://ajuda.sankhya.com.br/hc/article_attachments/360060998954) **Remover campo** retira o campo da célula.

**ℹ️ Nota**

Os campos **Quantidade** e **Unidade** são obrigatórios e não podem ser removidos do layout.

Ao posicionar o cursor sobre uma célula, o botão ![Botão Configurações do campo](https://ajuda.sankhya.com.br/hc/article_attachments/360061921953) **Configurações do campo** fica disponível. Ao acioná-lo, o pop-up **Configurações** exibe o campo **Exibir na célula** com as opções:

- **Apenas valor** — exibe somente o conteúdo do campo na célula.
- **Descrição e valor** — exibe o nome do campo e seu conteúdo.

![Pop-up Configurações do campo com opções Apenas valor e Descrição e valor](https://ajuda.sankhya.com.br/hc/article_attachments/21134359890711)

Na aba **Detalhes da venda** você define os campos que compõem o cabeçalho do pedido ou nota no PDV Web.

![Aba Detalhes da venda com campos do cabeçalho disponíveis para configuração](https://ajuda.sankhya.com.br/hc/article_attachments/21134359905687)

Para os campos do cabeçalho, os seguintes são obrigatórios para criar a nota no PDV Web: **Empresa**, **Parceiro**, **Tipo de Operação - TOP** e **Tipo de Negociação**. Quando todos esses campos forem definidos como obrigatórios e tiverem valor padrão preenchido, a tela de **Identificação (F2)** não é exibida ao confirmar a venda.

Se houver campo obrigatório sem valor padrão, a tela de Identificação é exibida na confirmação com a mensagem: "O valor do campo XXXX é incorreto, verifique no cadastro do Layout do PDV a configuração correta."

**ℹ️ Nota**

Pelo atalho **F2**, você pode abrir a tela de Identificação para editar campos configurados como **Editável** a qualquer momento durante o lançamento.

Ao incluir o campo **Controle do Indicador de Destinatário** no cabeçalho do layout, o sistema passa a validar automaticamente os dados para emissão de NFS-e:

- Com a opção **"1 - Destinatário não é o tomador"** e um Parceiro Destinatário informado, o sistema gera o grupo de tags correspondente no XML, permitindo envio de endereços de entrega distintos do tomador — inclusive para parceiros estrangeiros.
- Com **"0 - Destinatário próprio tomador"** ou sem Parceiro Destinatário preenchido, o sistema mantém o comportamento padrão, gerando apenas os dados do tomador.

Na aba **Preferências PDV Web**, o campo **Tipo Recebimento** define como o pagamento é processado:

![Aba Preferências PDV Web com campo Tipo Recebimento](https://ajuda.sankhya.com.br/hc/article_attachments/21134359918999)

- **Tipo de Título** — o recebimento segue o Tipo de Título configurado.
- **Tipo de Negociação** — o sistema realiza o recebimento conforme o Tipo de Negociação informado no cabeçalho da nota.
- **Ambos** — você escolhe a forma de pagamento no momento em que acionar **Receber** no PDV Web.

Para personalizar o layout do PDV Web com a logomarca da empresa, acione o botão **Logomarca da Empresa**. A imagem será exibida como plano de fundo nas telas de **Itens da Nota** e **Recebimento**.

**💡 Dica**

Para saber mais sobre o funcionamento do PDV Web, acesse [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web).

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#o-que-e)

### Ferramentas

O painel **Ferramentas** reúne os botões e abas usados para manipular as colunas do layout. Os botões operam sobre a coluna selecionada no momento.

- **Desfazer a última ação** — anula a última ação executada.
- **Excluir a coluna selecionada** — remove a coluna posicionada.
- **Colar uma coluna da área de transferência** — replica a coluna copiada anteriormente.
- **Recortar a coluna selecionada** — recorta a coluna para a área de transferência.
- **Copiar a coluna selecionada** — copia a coluna para a área de transferência.
- **Limpar a coluna selecionada** — remove todas as configurações da coluna, mantendo sua estrutura.
- **Definir coluna selecionada como área de destaque** — torna a coluna alvo dos painéis destacáveis. Colunas definidas como área de destaque são apresentadas com borda verde.
- **Mesclar a coluna selecionada** — une todas as células da coluna em uma única.

As abas **Dividir** e **Inserir** complementam o painel de ferramentas:

Na aba **Dividir**, selecione a coluna desejada, informe a quantidade de colunas no campo **Qtd. Colunas** e escolha a direção da divisão: vertical ou horizontal.

![Aba Dividir com campo Qtd. Colunas e botões de divisão vertical e horizontal](https://ajuda.sankhya.com.br/hc/article_attachments/13046810085015)

Na aba **Inserir**, informe a quantidade de colunas e defina a posição — antes ou depois da coluna selecionada — pelo botão **Posição**.

![Aba Inserir com campo Qtd. Colunas e seletor de posição](https://ajuda.sankhya.com.br/hc/article_attachments/13046847314839)

**ℹ️ Nota**

A inserção de colunas só é permitida após a coluna principal já ter sido dividida.

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#o-que-e)

### Campos disponíveis

Este quadrante lista os campos que podem ser inseridos nas grades que estruturam a nota. Use o campo de busca para localizar rapidamente um campo específico.

O botão **Mostrar somente campos obrigatórios** filtra a lista exibindo apenas os campos que o sistema exige no layout.

![Quadrante Campos disponíveis com campo de busca e botão de filtro de obrigatórios](https://ajuda.sankhya.com.br/hc/article_attachments/13046869703703)

**⚠️ Atenção**

Os campos obrigatórios do sistema devem estar presentes no layout para preenchimento. Se você optar por não incluir um campo obrigatório, é necessário cadastrar um valor padrão para ele — caso contrário, o sistema impedirá o lançamento da nota.

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#o-que-e)

### Grades disponíveis

O quadrante **Grades disponíveis** apresenta as grades que podem compor o layout. O comportamento da configuração de cada grade depende do parâmetro **SELAYCONFFORM** (**Separa por layout as conf. dos form. na Central**):

![Quadrante Grades disponíveis com lista de grades para arrastar ao layout](https://ajuda.sankhya.com.br/hc/article_attachments/360075339513)

- **Parâmetro desligado** — a configuração da grade é compartilhada entre todos os lançamentos com o mesmo tipo de movimento (TIPMOV). Alterar o layout da grade em uma TOP com TIPMOV = P, por exemplo, pode refletir em outras TOPs com o mesmo TIPMOV.
- **Parâmetro ligado** — a configuração da grade é salva considerando também o número do layout. Lançamentos com layouts diferentes mantêm configurações independentes, mesmo compartilhando o mesmo TIPMOV.

#### Grades de rodapé para NFS-e (Reforma Tributária)

O sistema disponibiliza grades específicas para registrar informações complementares de Notas Fiscais de Serviço Eletrônica (NFS-e) no Padrão Nacional, conforme as Normas Técnicas da Reforma Tributária. Você adiciona essas grades à aba **Referências e ajustes da NFS-e** do layout para que os campos correspondentes fiquem disponíveis na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

- **Deduções da Base IBS/CBS** — registra deduções e reduções da base de cálculo do IBS e da CBS conforme a NT 005 v1.1. Use quando o documento envolver tributos, emolumentos, condomínio ou glosa que não devem compor a base tributável.
- **Repasses e reembolsos de terceiros (gReeRepRes)** — registra valores recebidos pelo prestador relacionados a operações de terceiros, como reembolsos, repasses ou ressarcimentos já tributados anteriormente, conforme a NT 004 v2.0. Use em operações de intermediação imobiliária, agências de turismo ou agências de publicidade.

Para tornar essas abas disponíveis na Central, arraste um **Controle de abas** para a grade de rodapé **Referências e ajustes da NFS-e**, crie as abas **Deduções da Base IBS/CBS** e **Repasses e reembolsos de terceiros** e arraste a grade correspondente do quadrante **Grades disponíveis** para cada aba. Em seguida, vincule o layout à TOP pelo botão **Visualizar TOPs** e salve.

**ℹ️ Nota**

As grades de deduções e de repasses/reembolsos são específicas para NFS-e no Padrão Nacional e não afetam a emissão de NF-e ou outras modalidades. Para detalhes de preenchimento e estrutura, consulte os artigos [Processo Emissão da NFS-e Padrão Nacional via Micro Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/22378207317783) e [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

**⚠️ Atenção**

Se o layout B tiver colunas configuradas que não existam no layout A, essas colunas podem ficar ocultas quando usadas em uma nota com o layout A.

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#o-que-e)

### Outros controles

O quadrante **Outros controles** disponibiliza os componentes **Controle de abas** e **Aba**, usados para criar estruturas de abas dentro do layout. O uso desses componentes está descrito na seção [Criar um layout vazio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#layout-vazio).

![Quadrante Outros controles com componentes Controle de abas e Aba disponíveis para arrastar](https://ajuda.sankhya.com.br/hc/article_attachments/13046889563543)

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#o-que-e)

---

## Inserindo um novo layout

Clique no botão ![Botão Adicionar](https://ajuda.sankhya.com.br/hc/article_attachments/16090272687255) **Adicionar** na barra de ferramentas para abrir o assistente de criação. Ele oferece dois caminhos:

![Assistente de criação de layout com as opções Criar um layout vazio e Criar usando um modelo](https://ajuda.sankhya.com.br/hc/article_attachments/13046892654871)

### Criar um layout vazio

Um layout vazio parte do zero, sem campos ou configurações predefinidas. Ao escolher esta opção, informe a **Descrição** e o **Tipo de movimento** e, se desejar, marque **Usar como padrão para esse tipo de movimento?**. Clique em **Concluir** para abrir a tela de configuração.

![Passo de configuração do layout vazio com campos Descrição, Tipo de movimento e marcação de padrão](https://ajuda.sankhya.com.br/hc/article_attachments/13046913422359)

A área de configuração do layout é exibida inicialmente apenas com a coluna principal.

![Área de configuração do layout com a coluna principal vazia](https://ajuda.sankhya.com.br/hc/article_attachments/13046945555095)

Para construir o layout, siga os passos abaixo usando como exemplo um layout para Pedidos de Venda com duas colunas, sendo uma delas subdividida em duas células:

1. Selecione a coluna principal clicando sobre ela.
2. Na aba **Dividir**, informe **2** em **Qtd. Colunas** e acione **Dividir verticalmente a coluna selecionada**.

![Layout com coluna principal dividida verticalmente em duas colunas](https://ajuda.sankhya.com.br/hc/article_attachments/13046952171671)

3. Para subdividir a coluna superior em duas células, selecione-a e acione **Dividir horizontalmente a coluna selecionada**.

![Layout com coluna superior subdividida horizontalmente em duas células](https://ajuda.sankhya.com.br/hc/article_attachments/13046972426775)

4. Para inserir uma grade, clique sobre ela no quadrante **Grades disponíveis**, mantenha o clique e arraste-a até a célula desejada.

![Grade sendo arrastada do quadrante Grades disponíveis para uma célula do layout](https://ajuda.sankhya.com.br/hc/article_attachments/13047004586263)

5. Na janela exibida, informe o nome do painel e clique em **OK**.
6. Para criar abas, arraste um **Controle de abas** do quadrante [Outros controles](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#outros-controles) para a célula desejada e configure o painel na janela exibida.
7. Com o controle de abas inserido, arraste os componentes **Aba** para dentro do controle. O sistema solicita um nome para cada aba inserida.

**ℹ️ Nota**

Para renomear uma aba após a criação, dê um duplo clique sobre o nome da aba. Para reordenar, clique, mantenha e arraste a aba para a posição desejada. O botão ![Remover aba](https://ajuda.sankhya.com.br/hc/article_attachments/360061922293) **Remover aba**, ao lado do nome, exclui a aba do layout.

8. Arraste as grades para as abas correspondentes — ao soltar dentro de um painel já existente, o sistema não solicitará uma nova configuração.
9. Arraste os campos do quadrante [Campos disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#campos-disponiveis) para as células e grades criadas. Para remover um campo do layout, selecione-o e pressione **Delete** ou arraste-o de volta para a lista de campos disponíveis.
10. Clique em **Salvar**.

![Layout em construção com grades, abas e campos posicionados nas células](https://ajuda.sankhya.com.br/hc/article_attachments/13047035762967)

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#inserindo-layout)

### Criar usando um modelo

Ao escolher esta opção, o assistente exibe os modelos de layout padrão do sistema. Selecione o modelo compatível com o tipo de movimento para o qual o layout será criado.

![Lista de modelos de layout padrão do sistema disponíveis para seleção](https://ajuda.sankhya.com.br/hc/article_attachments/13047082434839)

Em seguida, informe a **Descrição**, o **Tipo de movimento** e, se aplicável, marque **Usar como padrão para esse tipo de movimento?**.

![Passo de dados do layout com campos Descrição e Tipo de movimento preenchidos](https://ajuda.sankhya.com.br/hc/article_attachments/13047083758231)

Ao finalizar, o sistema exibe o modelo selecionado já carregado para que você faça as modificações desejadas.

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#inserindo-layout)

### Duplicar um layout existente

Para criar um novo layout a partir de um já configurado, selecione o layout desejado na grade e clique em **Duplicar**. O sistema abre o layout copiado para que você faça as modificações necessárias.

![Botão Duplicar na barra de ferramentas da tela de layout](https://ajuda.sankhya.com.br/hc/article_attachments/13047091019543)

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#inserindo-layout)

---

## Vinculando um layout nas TOPs

Clique em **Visualizar TOPs** para abrir a tela de vinculação. O sistema exibe as TOPs disponíveis de acordo com o tipo de movimento configurado no layout. Para vincular, dê um duplo clique sobre a TOP desejada ou selecione-a e clique em ![Mover para direita](https://ajuda.sankhya.com.br/hc/article_attachments/360060999314) **Mover para direita**.

![Tela Visualizar TOPs com painéis de TOPs disponíveis e TOPs vinculadas ao layout](https://ajuda.sankhya.com.br/hc/article_attachments/13047106411031)

Após vincular uma TOP, sempre que um título for lançado na Central — Compras, Vendas ou Mov. Internas — com essa TOP, o layout configurado será aplicado automaticamente.

**ℹ️ Nota**

Ao tentar alterar o **Tipo de movimento** de um layout que já possui TOPs vinculadas, o sistema exibe uma confirmação perguntando se deseja desvincular as TOPs. Se confirmar, as TOPs são removidas e o tipo de movimento é atualizado.

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#o-que-e)

---

## Ajustes dos campos

No canto superior direito de cada painel do layout e do quadrante **Campos disponíveis** há dois botões de configuração:

![Botões de configuração no canto superior direito de um painel do layout](https://ajuda.sankhya.com.br/hc/article_attachments/13047108656407)

### Configurar o painel

Clique em **Configurar o painel**, altere o nome no pop-up exibido e clique em **OK** para salvar.

### Configurar o item selecionado

O botão **Configurar o item selecionado** abre as configurações do campo ou da grade selecionada no momento.

**Quando o item for um campo:** o pop-up **Editando o campo 'nome\_do\_campo'** é exibido. Por ele, você pode alterar o nome do campo, torná-lo **Obrigatório** e/ou **Editável**, e definir o valor padrão.

![Pop-up Editando o campo com opções de nome, obrigatoriedade, editabilidade e valor padrão](https://ajuda.sankhya.com.br/hc/article_attachments/13047147020183)

**Quando o item for uma grade:** o pop-up **Editando o grid 'nome\_da\_grade'** é exibido. Por ele, você seleciona os campos que ficarão visíveis na grade e define a ordem de exibição.

![Pop-up Editando o grid com colunas Campos Disponíveis e Campos Selecionados](https://ajuda.sankhya.com.br/hc/article_attachments/13047207756439)

Para grades do tipo **Itens**, o comportamento dos campos configurados nas colunas **Campos Disponíveis** e **Campos Selecionados** é:

- **Com campos selecionados** — apenas esses campos
  ficam disponíveis para inclusão no **Modo Grade**
  ou **Modo Formulário** nas Centrais.
- **Sem campos selecionados** — todos os campos
  ficam
  disponíveis para inclusão nas Centrais.

**⚠️ Atenção**

Existe uma exceção a esse comportamento: o campo
**Referência do Fornecedor** é de exibição permanente
nas
Centrais. Ele permanece disponível para utilização independentemente
de estar ou não entre os campos selecionados no layout. Alterar
sua configuração
nesta tela não afeta sua disponibilidade na grade de itens
da Central.
Este é o comportamento padrão do sistema.

Se o usuário já tiver distribuído campos entre as colunas nas Centrais e novos campos forem inseridos no layout, esses novos campos aparecem na coluna **Campos Disponíveis**.

No quadrante **Campos disponíveis**, o botão **Configurar o campo selecionado** fica habilitado ao selecionar um item da lista. Ao clicar, o pop-up é aberto permitindo apenas o cadastro de um valor padrão — as demais configurações do campo não ficam disponíveis neste contexto.

O botão **Restaurar nome do sistema** retorna o nome do campo para a nomenclatura padrão do Sankhya Om.

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#ajustes-campos)

### Tipo de valor padrão e Valor padrão

Quando um campo estiver definido como **Obrigatório** com a marcação **Editável** desabilitada, é necessário preencher o **Tipo de valor padrão** e o **Valor padrão** correspondente. O sistema utiliza esse valor ao abrir uma nota com o layout.

O campo **Tipo de valor padrão** apresenta duas opções:

- **Literal** — use quando o valor padrão for uma palavra ou número fixo.
- **Variáveis** — use quando o valor padrão for determinado por uma variável do sistema. As variáveis disponíveis são: Data Atual; Data e Hora Atuais; Código do Usuário Logado; Parceiro do Usuário Logado; Empresa do Usuário Logado; Vendedor para o Usuário Logado; Centro de Resultado do Usuário Logado.

**⚠️ Atenção**

As variáveis devem ser utilizadas de forma coerente com o tipo do campo. Por exemplo: **Data Atual** e **Data e Hora Atuais** devem ser usadas em campos de data; **Centro de Resultado do Usuário Logado** deve ser usada no campo **Centro de Resultado**. Usar uma variável em um campo incompatível — como **Vendedor para o Usuário Logado** no campo **Centro de Resultado** — gera erro ao abrir a nota, pois o código do vendedor difere do código do Centro de Resultado.

Quando o **Tipo de valor padrão** estiver configurado como **Variáveis**, o campo **Valor padrão** se transforma em um menu de lista para seleção da variável desejada.

Os campos do tipo opções ou do tipo Sim/Não exibem no valor padrão apenas as opções válidas para aquele campo, evitando o registro de uma opção inexistente que geraria erro ao abrir a Central. Veja o exemplo do campo CIF/FOB:

![Campo CIF/FOB no pop-up de configuração com as opções válidas listadas no campo Valor padrão](https://ajuda.sankhya.com.br/hc/article_attachments/13047206227095)

**ℹ️ Nota**

O campo **Finalidade da Operação** já possui um valor predefinido pelo sistema. Não é necessário configurar um valor padrão para ele nesta tela. Para mais detalhes, acesse [Finalidade da Operação - Onde informar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596074-Finalidade-da-Opera%C3%A7%C3%A3o-Onde-informar-).

Quando um Parceiro possui uma **Empresa Preferencial** vinculada, preencha o campo **Parceiro** do cabeçalho da nota antes do campo **Empresa**. Dessa forma, o campo Empresa é preenchido automaticamente com a empresa vinculada ao parceiro — sem essa ordem, o campo Empresa será populado com o valor padrão definido no layout.

Ao iniciar uma nota sem layout e salvá-la, o sistema troca o layout mas não carrega os valores padrão. Os valores padrão só são aplicados no momento da inclusão com o layout já definido. Exemplo: ao salvar a nota A sem layout e faturá-la para a nota B com layout, os valores padrão de B não são considerados.

[↑ voltar ao sumário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Tela-Configurador-de-Layout-da-Nota#ajustes-campos)
