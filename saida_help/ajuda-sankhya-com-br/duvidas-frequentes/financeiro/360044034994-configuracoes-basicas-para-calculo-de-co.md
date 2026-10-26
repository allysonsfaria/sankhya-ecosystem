---
id: "360044034994"
titulo: "Configurações básicas para cálculo de comissão por 'Contratos'!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044034994-Configura%C3%A7%C3%B5es-b%C3%A1sicas-para-c%C3%A1lculo-de-comiss%C3%A3o-por-Contratos"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:55:54Z"
rotulos: ["#PUBLIFER", "O.S1395591", "Configuração", "Parceiro", "Contrato", "Comissão", "Financeiro", "Faturamento contrato: Vendedor exibido", "Contratos: Configurar comissões", "Configurar parceiro: Vendedor preferencial"]
---

# Configurações básicas para cálculo de comissão por 'Contratos'!

### Comissão por 'Valor do Contrato':

![Imagem 1: Acesse Parceiros (Configurações » Cadastros » Parceiros)](https://ajuda.sankhya.com.br/hc/article_attachments/18970115276439) Acesse **Parceiros** (Configurações » Cadastros » Parceiros)

- Selecione parceiro vinculado ao respectivo 'Contrato'.
- Aba 'Identificação': Informe no campo **'Vend.Preferencial'** o vendedor responsável pelo 'Contrato' [Vendedor a ser comissionado].

Com as configurações acima, após realizar o 'Faturamento de contrato', no portal será apresentado o vendedor cadastrado no parceiro [TGFCAB].

![Imagem 2: Acesse Vendedores/Compradores (Configurações » Cadastros » Vendedores/Compradores) e realize as devidas configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/18970115282327) Acesse **Vendedores/Compradores** (Configurações » Cadastros » Vendedores/Compradores) e realize as devidas configurações para cálculo de comissão do 'Vendedor Preferencial' definido no item 1.

![Imagem 3: Acesse Contratos (Contratos e Serviços » Arquivos » Contratos)](https://ajuda.sankhya.com.br/hc/article_attachments/18970115286039) Acesse **Contratos** (Contratos e Serviços » Arquivos » Contratos)

- **NÃO** configurar as informações da **sub-aba 'Comissões'** (aba Produtos/Serviços):

### Comissão por 'Produto/Serviço' faturando contrato pagando comissão para vários vendedores:

![Imagem 4: Acesse o cadastro de Vendedores/Compradores (configurações > cadastros > Vendedores/Compradores) no cadastro dos…](https://ajuda.sankhya.com.br/hc/article_attachments/18970115276439)  Acesse o cadastro de **Vendedores/Compradores** (configurações > cadastros > Vendedores/Compradores) no cadastro dos vendedores defina o parceiro, a fórmula e o campo Recebe comissão em CM.

![Imagem 5: Acesse o cadastro de Vendedores/Compradores (configurações > cadastros > Vendedores/Compradores) no cadastro dos…](https://ajuda.sankhya.com.br/hc/article_attachments/29739049143063)

![Imagem 6: Acesse o cadastro de Vendedores/Compradores (configurações > cadastros > Vendedores/Compradores) no cadastro dos…](https://ajuda.sankhya.com.br/hc/article_attachments/29739049149207)

![Imagem 7: Ligue os parâmetros "Calcular comissão p/ gerente do vendedor - CALCCOMGER"](https://ajuda.sankhya.com.br/hc/article_attachments/29739072110743) Ligue os parâmetros **"Calcular comissão p/ gerente do vendedor - CALCCOMGER"**

**"Lançar Comissão p/Múltiplos Vendedores? - LANCCOMMULT".**

**"Comissão para Gerente de Contas em Contrato de Manutenção - COMCMGC: ?**

**"Comissão para Apresentação em Contrato de Manutenção - COMCMAPR": ?**

**Período(meses) Máximo p/ pgto de Comissão em CM <=> PERMAXCM = ?
% Máximo de Comissão em CM <=> COMMAXCM = ?**

**(1)** O campo Nro. Único Pedido será preenchido pelo pedido selecionado na tela.
**(1)** Vendedor: Só é possível incluir vendedores ativos e que estejam com o campo ?Recebe comissão em CM? (onde CM = Contrato de Manutenção) marcado.

![Imagem 8: No portal de venda, para o contrato em questão será lançado um pedido com os dois vendedores.](https://ajuda.sankhya.com.br/hc/article_attachments/18970115286039) No portal de venda, para o contrato em questão será lançado um pedido com os dois vendedores.

![Imagem 9: Verifique se no cadastro da TOP utilizada no faturamento de contrato a opção comissão está definida para "calcular".](https://ajuda.sankhya.com.br/hc/article_attachments/29739049153175) Verifique se no cadastro da TOP utilizada no faturamento de contrato a opção comissão está definida para "calcular".

![Imagem 10: Verifique se no cadastro da TOP utilizada no faturamento de contrato a opção comissão está definida para "calcular".](https://ajuda.sankhya.com.br/hc/article_attachments/29739072118935)

![Imagem 11: Acesse Contratos (Contratos e Serviços » Arquivos » Contratos)](https://ajuda.sankhya.com.br/hc/article_attachments/29739072121111) Acesse **Contratos** (Contratos e Serviços » Arquivos » Contratos)

Configure as informações da **sub-aba 'Comissões'** (aba Produtos/Serviços).

**(1)**Botão configuração, gerar financeiro pelo tipo de negociação usando Venc da tela +(mais) prazo das parcelas.

**(1)** Faturar >> gerar faturas >> Sim.

![Imagem 12: Na tela Cálculo de comissão por fórmula (Comercial » Avançado » Cálculo de Comissão por Fórmula) informe o período de…](https://ajuda.sankhya.com.br/hc/article_attachments/29739072122391) Na tela **Cálculo de comissão por fórmula** (Comercial » Avançado » Cálculo de Comissão por Fórmula) informe o período de negociação, a opção vendedor da comissão múltipla marcada e clique em aplicar.

**OBSERVAÇÃO:** Esse é o comportamento do sistema para calculo de comissão por contrato.

É possível inseri-lo diretamente na aba Produtos/Serviços do contrato, adicionando os produtos e vendedores. Alternativamente, pode-se lançar um pedido com vários produtos e, em seguida, importar esse pedido para o contrato utilizando o botão Outras opções e selecionando a opção Selecionar Produtos/Serviços do pedido.
