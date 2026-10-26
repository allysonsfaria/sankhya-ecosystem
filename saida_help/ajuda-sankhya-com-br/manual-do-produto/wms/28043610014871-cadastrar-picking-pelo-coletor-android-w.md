---
id: "28043610014871"
titulo: "Cadastrar Picking pelo Coletor Android WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28043610014871-Cadastrar-Picking-pelo-Coletor-Android-WMS"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:13:11Z"
rotulos: ["Produtos", "Configuração", "Estoque", "coletor android", "wms", "desvincular", "vincular", "coletor", "picking", "coletor wms"]
---

# Cadastrar Picking pelo Coletor Android WMS

```
 Versão disponível: A partir da 4.32
```

---

É possível realizar o cadastro de endereços de picking diretamente pelo Coletor Android WMS da Sankhya.

Abaixo, você confere o passo a passo da jornada para efetuar esse cadastro, bem como as configurações necessárias para seu correto funcionamento.

**ATENÇÃO:** A tarefa **“Definir Vínculo de Produto”** apenas será exibida no coletor quando estiver devidamente habilitada no perfil do usuário no **TotalCross**.

Para liberar o acesso:

**(1)** Acesse a tela ''**Configurações por Usuário''** (WMS » Rotinas » Configurações por Usuário).

**(2)** Na aba **''Tarefas Permitidas''**, localize o campo **''Tarefa''**.

**(3)** Busque e habilite a tarefa **''36 – Definir Vínculo de Produto''** para o usuário utilizado no coletor.

- Caso essa configuração não esteja ativa, a tarefa não será exibida no coletor. Nesse cenário, não se trata de falha no sistema, mas sim de restrição de permissão.

**(1)** Na tela inicial de acesso ao Coletor Android WMS, está disponível a opção "Definir Vínculo de Produto", que dá início à rotina de cadastro de picking:

![Imagem 1: (1) Na tela inicial de acesso ao Coletor Android WMS, está disponível a opção "Definir Vínculo de Produto" , que dá…](https://ajuda.sankhya.com.br/hc/article_attachments/28043577509271)

**(1)** Ao clicar nesse botão, a tela **"Tarefa"** será exibida, contendo os campos **"Informe o Endereço"** e **"Situação Endereço"**, ambos disponíveis para preenchimento:

![Imagem 2: (1) Ao clicar nesse botão, a tela "Tarefa" será exibida, contendo os campos "Informe o Endereço" e "Situação Endereço"…](https://ajuda.sankhya.com.br/hc/article_attachments/28043577510423)

**OBSERVAÇÃO:** Serão aceitos apenas endereços de expedição (TGWEND.EXPEDICAO), que estejam ativos e com a marcação **"Permite** **expedição"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) da tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento)) habilitada, caso insira algum endereço diferente destes, a mensagem a seguir será apresentada:

**“Endereço inválido! Só é permitido endereços ativos e que permita expedição!”**

Após inserir um endereço válido no campo ''Informe o Endereço'', o campo ''Situação Endereço'' será preenchido automaticamente. Em seguida, as informações dos campos **"Tipo Endereço"**, **"Possui Estoque"**, **"SKU Vinculado"** e **"Qtde SKUs Vinculados"** serão exibidas automaticamente.

![Imagem 3: Após inserir um endereço válido no campo ''Informe o Endereço'' , o campo ''Situação Endereço'' será preenchido…](https://ajuda.sankhya.com.br/hc/article_attachments/28043577511703)

Após o preenchimento dos campos mencionados, será possível selecionar uma das opções disponíveis, conforme a necessidade:

- **Vincular**: abre a tela **"Vincular Produto"** para adicionar produtos ao endereço;
- **Desvincular**: direciona para a tela **"Desvincular Produto"** para remover um produto específico do endereço;
- **Remover Existentes**: desvincula todos os produtos atualmente vinculados ao endereço.

**![Imagem 4: Informações adicionais sobre as opções Vincular , Desvincular e Remover Existentes :](https://ajuda.sankhya.com.br/hc/article_attachments/28043610004375) Informações adicionais sobre as opções Vincular, Desvincular e Remover Existentes:**

A tela ''Vincular Produto'' apresenta o campo **"Informe o Produto"**:

![Imagem 5: A tela ''Vincular Produto'' apresenta o campo "Informe o Produto" :](https://ajuda.sankhya.com.br/hc/article_attachments/28043610004887)

Neste campo, somente produtos válidos, ativos e reconhecidos pelo sistema podem ser utilizados. Caso seja informado um produto que não esteja ativo ou não seja reconhecido, uma das seguintes mensagens será exibida:

**"Este produto não pode ser usado aqui!".**

 Ou

**"O código de barras informado não é reconhecido pelo sistema".**

Na tela, o botão ![Imagem 6: Na tela, o botão "Continuar" permanecerá desativado por padrão até que um produto ativo seja inserido.](https://ajuda.sankhya.com.br/hc/article_attachments/28043810318103) **"Continuar"** permanecerá desativado por padrão até que um produto ativo seja inserido.

A descrição dos campos **"Produto"** e **"Controle"** será preenchida automaticamente, conforme a configuração prévia do produto.

**Observação:** caso o produto seja controlado por lista, será necessário informar o controle correspondente à lista.

Após essa etapa, a seção **"Regra do Endereço"** estará disponível. Nela, será possível selecionar uma das seguintes opções: **"Permitir"**, **"Exclusivo"** ou **"Proibir"**.

Os campos **"Estoque Mínimo"** e **"Estoque Máximo"** devem ser preenchidos e podem ser ajustados conforme necessário.

Preencha o campo **"Unidade Estoque"**, com uma das opções da lista de unidades cadastradas para o produto (UN, CX, PC), priorizando a unidade padrão na primeira posição. Caso seja inserida uma unidade não compatível com o produto, a seguinte mensagem será exibida:

**"Unidade XX não pode ser usada para este produto!"**

A marcação **"Ativo"** também poderá ser habilitada, conforme necessário.

Após preencher os campos necessários, pressione o botão ![Imagem 7: Após preencher os campos necessários, pressione o botão "Vincular" para concluir o vínculo do produto. Uma mensagem de…](https://ajuda.sankhya.com.br/hc/article_attachments/28043610005527) **"Vincular"** para concluir o vínculo do produto. Uma mensagem de sucesso será exibida, e, em seguida, a tela **"Vincular Produto"** será reaberta, com o foco preparado para o cadastro de um novo produto.

No entanto, caso a opção Desvincular seja selecionada na tela Tarefa, o Coletor WMS redirecionará para a tela Desvincular Produto, onde será exibido o campo para a leitura do produto a ser desvinculado.

![Imagem 8: No entanto, caso a opção Desvincular seja selecionada na tela Tarefa , o Coletor WMS redirecionará para a tela…](https://ajuda.sankhya.com.br/hc/article_attachments/28043610006679)

Ao inserir manualmente o código do produto neste campo, o botão ![Imagem 9: Ao inserir manualmente o código do produto neste campo, o botão "Desvincular" será ativado.](https://ajuda.sankhya.com.br/hc/article_attachments/28043610008087) **"Desvincular"** será ativado.

![Imagem 10: Somente produtos válidos serão aceitos, ou seja, produtos previamente vinculados ao endereço especificado. Caso o…](https://ajuda.sankhya.com.br/hc/article_attachments/28043610008983) Somente produtos válidos serão aceitos, ou seja, produtos previamente vinculados ao endereço especificado. Caso o código informado não seja reconhecido ou não esteja vinculado ao endereço, serão exibidas mensagens apropriadas, como:

**"Aviso**

**Produto não existe ou não pode ser usado aqui."**

Ou

**"Aviso**

**Produto informado não está vinculado neste endereço."**

Por outro lado, ao informar um produto válido e realizar o desvinculamento, o produto será desassociado do endereço, e uma mensagem de sucesso será exibida.

---

Ao final, quando um endereço e um produto já vinculados forem identificados, o botão Vincular será alterado para ![Imagem 11: Ao final, quando um endereço e um produto já vinculados forem identificados, o botão Vincular será alterado para…](https://ajuda.sankhya.com.br/hc/article_attachments/28043577521303) **"Atualizar"**.

Ao pressioná-lo, as informações existentes no endereço relacionadas ao produto serão carregadas automaticamente.

![Imagem 12: Se o produto for controlado por lista, essa lista deverá ser exibida na seção geral de descrição do "Produto" , no…](https://ajuda.sankhya.com.br/hc/article_attachments/28043910871319) Se o produto for controlado por lista, essa lista deverá ser exibida na seção geral de descrição do **"Produto"**, no campo **"Controle"** na aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto) da tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento). Caso não exista uma lista associada, o campo Controle não será exibido, sendo apresentada apenas a descrição do produto.
