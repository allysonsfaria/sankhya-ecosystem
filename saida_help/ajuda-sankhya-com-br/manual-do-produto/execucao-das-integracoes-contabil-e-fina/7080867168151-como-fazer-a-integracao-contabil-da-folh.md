---
id: "7080867168151"
titulo: "Como fazer a integração contábil da folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7080867168151-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-folha"
trilha: "Manual do Produto > Pessoas+ > Integração Contábil e Financeira > Execução das Integrações Contábil e Financeira"
atualizado_em: "2026-10-15T17:19:56Z"
rotulos: ["Configuração", "Centro de Resultado", "Contabilidade", "Folha de Pagamento", "Configuração de Integração Contábil", "Integração Contábil", "br.com.sankhya.rh.GerenciadorFolha", "Gerenciador de Folhas", "Débito em despesas crédito em salários a pagar", "Aplique filtros gere e efetive lançamentos", "Use \"Integração Contábil\" no Gerenciador de Folhas"]
---

# Como fazer a integração contábil da folha

A **Integração Contábil** da folha de pagamento consiste em levar os valores dos eventos que integram com a contabilidade, onde devem realizar em conta de resultado e também em conta operacional.

Normalmente para as despesas com a remuneração é utilizado:

- Conta Débito: Despesas de folha (resultado);
- Conta Crédito: Salários a pagar (passivo).

Após ter sido realizada todas as configurações dos eventos com as contas contábeis, e realizado o cálculo da folha de pagamento, é possível a realização da integração da folha com a contabilidade.

| ℹ️ **Nota**  Quando um evento precisa ser contabilizado em contas diferentes da configuração principal para um **tipo de folha** ou um **departamento** específico, é possível criar uma **exceção de contabilização**.  Para isso, configure o parâmetro **Exceção para Contabilização (FPEXCECAOCTB)** na tela **Preferências**, com a opção **Por Tipo de Folha**, **Por Departamento** ou ambas. Depois, cadastre a exceção na tela **Configuração de Integração Contábil**, pelo botão **Visualizar Exceções**. Na integração, o sistema usa as contas da exceção no lugar da configuração principal do evento.  📚 Configure isso em: [Como configurar a integração contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/10137196517783) (seção Criando Exceções Contábeis). |
| --- |

Para realizá-la, acesse a tela [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247).

![integracao](https://ajuda.sankhya.com.br/hc/article_attachments/15908976449431)

As folhas que estão prontas para serem integradas com a contabilidade estarão sinalizadas com o ícone de calculadora. Isso quer dizer que já foram realizadas todas as conferências, integradas com o financeiro e agora está pronto para enviar os dados para a contabilização.

No menu lateral, clique no botão**"Integração Contábil Folha de Pagamento"** para que seja exibida uma nova janela para preenchimento das informações:

![pop](https://ajuda.sankhya.com.br/hc/article_attachments/15909028180631)

Informe o código da **"Empresa"** e a **"Referência"** nos respectivos campos.

Selecione os **"Tipos de Folha"** que foram calculadas na referência, informe o **"Lote Contábil"** (que normalmente é indicado pela Contabilidade) e também a **"Data Movimento Contábil"**.

Na seção **"Contabilizar por"** selecione como será realizada a contabilização, se por **"Empresa"**, **"Funcionário"**, **"Departamento"** ou **"Centro de Resultado"**. Normalmente é utilizada a opção Centro de Resultado.

| ℹ️ **Nota**  Antes de gerar a integração, confirme que o **Centro de Resultado** vinculado à empresa, ao evento e ao departamento está marcado como **Ativo** e **Analítico**. Se algum desses cadastros estiver vinculado a um Centro de Resultado inativo ou sintético (não analítico), a contabilização da folha falha. |
| --- |

![Imagem 3: Caso a empresa utilize rateios , ao realizar a contabilização por Empresa , os centros de resultados serão exibidos…](https://ajuda.sankhya.com.br/hc/article_attachments/35622390967447) Caso a empresa utilize [rateios](https://ajuda.sankhya.com.br/hc/pt-br/articles/7092297445911), ao realizar a contabilização por **Empresa**, os centros de resultados serão exibidos devido à aplicação do critério de rateio, que impacta diretamente as rotinas financeiras e contábeis.

Em seguida, na seção de **"Composição do Histórico Contábil"**, faça as marcações que irão compor o histórico contábil. Considerando o seguinte:

- Se definida a contabilização por Empresa ou Centro de Resultado, a composição do histórico será permitida apenas para **"Histórico Padrão"**, **"Referência"** e **"Descrição Evento"**.
- Se definida por Funcionário, é permitido marcar todas as composições.
- Definida por Departamento, pode marcar todas as composições, exceto por **"Nome do Funcionário"**.

Através do botão **"Filtros"**é possível definir como e quais dados serão contabilizados. Tem-se os filtros por **"Departamentos"**, **"Cargos"**, **"Vínculos"** e **"Funcionários"**.

![Imagem 4: Através do botão "Filtros" é possível definir como e quais dados serão contabilizados. Tem-se os filtros por…](https://ajuda.sankhya.com.br/hc/article_attachments/7080769784727)

Se por exemplo, for para contabilizar funcionários específicos, selecione o tipo de filtro Funcionários e clique no botão de adicionar:

[GIF animado: Imagem 5: Se por exemplo, for para contabilizar funcionários específicos, selecione o tipo de filtro Funcionários e clique no…](https://ajuda.sankhya.com.br/hc/article_attachments/7080799594903)

Em seguida, selecione os funcionários que participaram do filtro e clique em **"Aplicar Filtros"**.

**Observação:** é possível incluir filtros diversos ou até mesmo não necessariamente fazer um filtro.

Após definir os filtros, clique em **"Voltar"**, e em seguida, em **"Gerar"**.

Ao clicar no botão Gerar, será apresentado um resumo em tela, com todos os lançamentos, para que seja feita a conferência:

![Imagem 6: Ao clicar no botão Gerar , será apresentado um resumo em tela, com todos os lançamentos, para que seja feita a…](https://ajuda.sankhya.com.br/hc/article_attachments/7080803471127)

| **⚠️** **Atenção**  Antes de clicar em **Efetivar**, confira no resumo se existem lançamentos com valor de **débito** ou de **crédito** zerado. Lançamentos zerados podem impedir a efetivação da integração contábil.  Se encontrar lançamentos zerados, revise a configuração contábil dos eventos envolvidos, inclusive as exceções de contabilização, e gere a integração novamente. |
| --- |

Se estiver tudo certo, basta que você clique em **Efetivar**.

A partir daí, a área contábil realizará as conferências através da tela [Consulta Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607374) e emitirá os relatórios, como o Razão Analítico.

Para realizar a emissão do **"Resumo da Folha"**, retorne à tela principal do Gerenciador de Folhas e clique no ícone ![Imagem 7: Para realizar a emissão do "Resumo da Folha" , retorne à tela principal do Gerenciador de Folhas e clique no ícone :](https://ajuda.sankhya.com.br/hc/article_attachments/16951242847127):

[GIF animado: Imagem 8: Para realizar a emissão do "Resumo da Folha" , retorne à tela principal do Gerenciador de Folhas e clique no ícone :](https://ajuda.sankhya.com.br/hc/article_attachments/7080794657175)

Selecione a(s) **"Empresa(s)"** e depois clique na aba **"Geração"** para definir o **"Tipo de Folha"** e as demais marcações você pode utilizar a estabelecida pelo sistema. Em seguida, selecione os **"Funcionários"** para a conferência e clique em **"Gerar Resumo da Folha"**:

[GIF animado: Imagem 9: Selecione a(s) "Empresa(s)" e depois clique na aba "Geração" para definir o "Tipo de Folha" e as demais marcações você…](https://ajuda.sankhya.com.br/hc/article_attachments/7080795912855)

Caso queira imprimir, basta clicar no ícone ![Imagem 10: Caso queira imprimir, basta clicar no ícone .](https://ajuda.sankhya.com.br/hc/article_attachments/16951280107287).

![Imagem 11: A conferência é de responsabilidade da área contábil.](https://ajuda.sankhya.com.br/hc/article_attachments/16951280110103) A conferência é de responsabilidade da área contábil.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7080867168151-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-folha#top)
