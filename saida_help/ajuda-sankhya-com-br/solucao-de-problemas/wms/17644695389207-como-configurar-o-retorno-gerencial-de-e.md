---
id: "17644695389207"
titulo: "Como configurar o retorno gerencial de estoque WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17644695389207-Como-configurar-o-retorno-gerencial-de-estoque-WMS"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-10-02T12:34:37Z"
rotulos: ["Configuração", "WMS", "NF-e", "Portal de Vendas", "TOP", "Estoque", "Tipo de movimento e estoque", "Processo específico", "Retorno Gerencial WMS", "Artigo atualizado KCS", "WMS - KCS"]
---

# Como configurar o retorno gerencial de estoque WMS

**SITUAÇÃO:**

Quando a separação do pedido de venda está com a situação 'Concluído' no WMS não há como cancelá-la. Sendo necessário realizar o retorno gerencial de estoque WMS, especialmente em casos de notas fiscais de saída denegadas pela Sefaz, onde o sistema precisa retornar o estoque sem gerar uma devolução fiscal indevida.

**SOLUÇÃO:**

Para configurar o retorno gerencial de estoque WMS, realize as configurações abaixo:

 Crie uma TOP, acesse: **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP).

 No tipo de movimento **"Devolução de Venda"**, acesse a aba **"Geral"** e no campo **"Exigir Nota de Venda"**, selecione **"Não exigir"**.

![Imagem 1: Para configurar o retorno gerencial de estoque WMS, realize as configurações abaixo: Crie uma TOP, acesse: "Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/17679534854807)

 Acesse a aba **"Estoque"** e configure os campos:

- **"Atualização do Estoque"**: **"Nenhuma"**.
- **"Atualização estoque MP"**: **"Nenhuma"**.
- **"Atualização do Bem"**: **"Não Atualizar"**.
- **"Validar estoque p/Reservar"**: **"Marcado"**.

![Imagem 2: Acesse a aba "WMS" e configure os campos:](https://ajuda.sankhya.com.br/hc/article_attachments/17679534856855)

 Acesse a aba **"WMS"** e configure os campos:

- **"Permite confirmação antes do envio para o WMS?"**: **"Parâmetro Global"**.
- **"Endereçamento no WMS"**: **"Manual"**.
- **"Atualização do WMS"**: **"Entrar"**.

![Imagem 3: Após concluir as configurações acima, crie um modelo de nota e pedido em "Modelo de Notas e Pedidos" (Comercial >>…](https://ajuda.sankhya.com.br/hc/article_attachments/17679534862615)

 Após concluir as configurações acima, crie um modelo de nota e pedido em **"Modelo de Notas e Pedidos"** (Comercial >> Consulta >> Modelo de Notas e Pedidos) e preencha os campos **"Empresa"**, **"Tipo Operação"**, **"Tipo de Negociação"** e **"Dt. de Alteração"**.

![Imagem 4: Após concluir as configurações acima, crie um modelo de nota e pedido em "Modelo de Notas e Pedidos" (Comercial >>…](https://ajuda.sankhya.com.br/hc/article_attachments/17679534871319)
![Imagem 5: Após concluir as configurações acima, crie um modelo de nota e pedido em "Modelo de Notas e Pedidos" (Comercial >>…](https://ajuda.sankhya.com.br/hc/article_attachments/17679534873239)

**OBSERVAÇÃO DE ERRO COMUM:**

É necessário informar um **"Tipo de Negociação"** no **"Modelo de Notas e Pedidos"** para o Retorno Gerencial de Estoque WMS. Caso o campo esteja com valor zero, será apresentada a mensagem:

**"Recebimento não gerado: ORA-20101: Campo Tipo de negociac?o obrigatorio para a nota de Nro Unico:X. ORA-06512: em SANKHYA.TRG\_INC\_TGFCAB, line 462. ORA-04088: erro durante a execução do gatilho SANKHYA.TRG\_INC\_TGFCAB. Código: CORE\_E05120"**.

![Imagem 6: Após concluir as configurações acima, crie um modelo de nota e pedido em "Modelo de Notas e Pedidos" (Comercial >>…](https://ajuda.sankhya.com.br/guide-media/01H532NS5KVBYNJ6CRSGDMZHCD) Após criar o modelo, informe o número no campo **"Modelo Retor. de Est. Gerencial WMS(Venda)"** em (Comercial >> Preferências >> Empresa aba WMS).

![Imagem 7: Após concluir as configurações acima, crie um modelo de nota e pedido em "Modelo de Notas e Pedidos" (Comercial >>…](https://ajuda.sankhya.com.br/hc/article_attachments/17679534888727)

 Acesse (Comercial >> Consulta >> Portal de Vendas), selecione a nota denegada, clique no botão **"Outras Opções"** e selecione a opção **"Retorno Gerencial de Estoque WMS"**.

Na tela de execução, informe a doca de recebimento no WMS. Confirme o processo para que o sistema gere o recebimento de mercadorias.

![Imagem 8: Após concluir as configurações acima, crie um modelo de nota e pedido em "Modelo de Notas e Pedidos" (Comercial >>…](https://ajuda.sankhya.com.br/hc/article_attachments/17677653153815)

**OBSERVAÇÕES E ALTERNATIVAS:**

- Somente será permitido retornar o estoque da nota ou pedido uma vez.
- Essa opção poderá ser utilizada para pedidos ou notas com status de WMS concluído.
- Em casos de pedidos ou notas que contenham separações **"Por produto"** e **"Por Pedido"**, ambas devem estar como concluídas.
- Em casos de NF-e canceladas, o pedido de venda volta a ser pendente. O sistema sugerirá marcar o pedido como não pendente, caso este não seja faturado.
- Ao gerar uma **"Nota de Devolução"** de venda utilizando este processo, não será possível confirmá-la após a conferência, pois o movimento é apenas para atualização de saldos no WMS.
- Alternativa: Utilize o **"Inventário de WMS"** para equalização dos saldos de estoque causados por cancelamentos ou denegações.
