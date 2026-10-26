---
id: "360045110853"
titulo: "Numeração da TOP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110853-Numera%C3%A7%C3%A3o-da-TOP"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:30:26Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Empresa", "Fiscal", "Numeração da TOP", "br.com.sankhya.com.cad.numeracaotop", "Numeração da TOP manual", "Notas Fiscais Eletrônicas", "Controle", "TOP", "Financeiro", "Modelo do Documento"]
---

# Numeração da TOP

```
 Módulo: Comercial > Arquivo > Cadastros
```

---

Esta tela serve para controlar todas as numerações de notas emitidas pela empresa, podendo ser por empresa, série, etc. Possibilita ainda, o controle da emissão de notas por impressora, para o caso de haver mais de uma série de notas em diferentes impressoras.

Ao definir o acesso por usuário a esta tela através da rotina [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos), o mesmo poderá realizar modificações sem que seja necessário conter acesso à rotina de [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP).

![Imagem 1: Ao definir o acesso por usuário a esta tela através da rotina Controle de Acessos , o mesmo poderá realizar…](https://ajuda.sankhya.com.br/hc/article_attachments/360087400294)

Na parte esquerda da tela, temos o menu que possibilita filtrar por categoria, o Tipo de Operação que você deseja alterar a numeração.

Após selecionar o Tipo de Operação, serão exibidos na parte superior, o botão de filtros, o Painel de Controle e o código da TOP selecionada, bem como a sua descrição.

[GIF animado: Imagem 2: Após selecionar o Tipo de Operação , serão exibidos na parte superior, o botão de filtros, o Painel de Controle e o…](https://ajuda.sankhya.com.br/hc/article_attachments/360087400754)

O campo **"Empresa"** trará o código e a descrição da empresa.

Se a numeração das notas da empresa possuir série, informe-a no campo **"Série"**.

No campo **"Mod.Doc.Fiscal"**, será indicado o modelo da nota fiscal. Este campo é uma forma a mais de se controlar a numeração das movimentações de venda. Para que este campo esteja habilitado, é necessário que o campo **"Base de numeração"** da TOP esteja selecionada como Venda.

**Nota:** Para que uma TOP possa fazer o controle de numeração pelo Mod.Doc.Fiscal, o **"Modelo do Documento"** da aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal) deve ser o mesmo do informado aqui.

Quando a opção do campo Mod.Doc.Fiscal for igual a 55, o sistema não permitirá alterar e nem excluir manualmente a numeração, emitindo a seguinte mensagem:

**"Mod.Doc.Fiscal 55 não pode alterar o campo "Numeração Automática" e nem o campo "Último Código."**

**Importante:** A validação acima não valerá para o usuário SUP.

A marcação **"Numeração Automática"**, quando acionada, indica que a numeração será gerada automaticamente pelo sistema.

O último código de numeração gerado pelas movimentações lançadas com esta empresa, com a Base de numeração da TOP será apresentado no campo **"Último Código"**.

O campo **"Último Número do Talão"** comporta o último número de nota disponível para impressão no formulário manual.

Se o número da nota for maior que o Último número do talão, a seguinte mensagem será exibida:

**"Números disponíveis para numeração automática acabaram!"**

Se o último número do talão menos a quantidade de aviso para poucas notas for menor que o número da nota, será exibida a mensagem referente à quantidade de notas que ainda restam. Trouxemos abaixo um exemplo:

- Preenchendo o campo Último Código com o valor 1, o campo Último Número do Talão com o valor 11 e o campo **"Qtd. p/ Aviso Poucas Notas"** com o valor 10, caso o número da nota seja igual a 2, será apresentada uma mensagem alertando que restam 9 notas. No caso de o número da nota ser igual a 12, será apresentada a seguinte mensagem:

**"Números disponíveis para numeração automática acabaram!".**

Informe no campo Qtd. p/Aviso de Poucas Notas a quantidade de notas que o sistema deverá emitir um aviso informando que o talão de notas está acabando.

Através dos campos **"Quantidade de itens na nota"** e **"Quantidade de serviços da nota"** você aponta o valor limite de itens e serviços permitidos no lançamento da nota.

Quando o faturamento de um pedido de venda ultrapassa o limite definido no campo **"Quantidade de itens na nota"**, o sistema divide automaticamente os itens em notas separadas. O financeiro de cada nota gerada é calculado conforme o tipo de negociação configurado no pedido.

**Importante:** caso o financeiro do pedido de venda tenha sido **alterado manualmente** antes do faturamento, essas alterações não serão consideradas na divisão das notas. Nessa situação, o sistema ignora os ajustes manuais e segue apenas as regras do tipo de negociação para calcular o financeiro de cada nota gerada. Para evitar inconsistências, recomenda-se não realizar alterações manuais no financeiro do pedido quando a configuração de limite de itens por nota estiver em uso.

O modelo a ser empregado no campo **"Código do Modelo"** necessita estar previamente cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).

A categoria da impressora a ser utilizada na impressão da nota é informado no campo **"Tipo Impressora"**.

Indique no campo **"Impressora"** o caminho da impressora responsável pela impressão da nota.

No campo **"Dias para Aviso"** aponte em quantos dias antes da data de validade dos formulários de Notas, o sistema emitirá no momento da confirmação da Nota uma mensagem informando que o prazo de validade do talão de Notas está acabando ou já encerrou.

A data de validade do talão de notas é discriminada no campo **"Dt. Validade"**. Sendo assim, se o talão tem seu vencimento em 31/12/2012, indicado no campo **"Data de Validade"** e você deseja que o sistema emita um aviso de que este talão vencerá 05 dias antes desta data, informe o valor **"05"** no campo Dias para Aviso. Assim, a partir do dia 26/12/2012, o sistema emitirá a seguinte mensagem no momento da confirmação da Nota:

**"A Validade do Talão está acabando. Resta(m) 05 Dia(s)."**

Se após a data de validade (31/12/2012) da TOP, ocorrer o lançamento de uma Nota com esta TOP no dia 03/01/2013, ao confirmá-la, o sistema emitirá uma mensagem avisando que a validade do talão já acabou.
