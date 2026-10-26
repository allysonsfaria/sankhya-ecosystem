---
id: "360044596014"
titulo: "Cadastro Benefícios"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596014-Cadastro-Benef%C3%ADcios"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-10-01T12:40:02Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Fiscal", "Parceiro", "NF-e", "br.com.sankhya.mgeliv.cad.cadastrobeneficios", "Cadastro Benefícios manual", "Impostos", "Cadastro de benefícios fiscais", "Vinculação de códigos à nota", "Configurações e funcionalidades detalhadas"]
---

# Cadastro Benefícios

```
 Módulo: Livros Fiscais > Arquivos
```

---

Esta tela possui algumas funcionalidades que permitem localizar códigos de benefícios, resultando desta forma no preenchimento do campo **"Cód. Benefício Fiscal na UF"** encontrado na grade **"Itens"** das Centrais de Notas, reduzindo assim o percentual de possíveis erros de lançamentos.

![Imagem 1: Esta tela possui algumas funcionalidades que permitem localizar códigos de benefícios, resultando desta forma no…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003091561)

Neste contexto, acione o botão ![Imagem 2: Neste contexto, acione o botão "Cadastrar Benefícios" para realizar um novo cadastro de benefício.](https://ajuda.sankhya.com.br/hc/article_attachments/360104088653) **"Cadastrar Benefícios"** para realizar um novo cadastro de benefício.

Ao realizar a confirmação do cadastro, o campo **"Número de Benefício"** será preenchido de forma automática.

Informe o **"Código da Empresa"** correspondente às notas que serão utilizadas na regra.

Insira o código que será vinculado à nota no campo **"Código do Benefício**".

No campo **"Descrição"**, registre a informação sobre o benefício que estará relacionado à nota.

As informações dos campos **"Grupo de ICMS"** e **"Grupo de ICMS 2"** estão vinculadas à tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostosinformaesporempresa), sendo que o primeiro campo será utilizado para realizar a distinção entre os produtos, visto que, em uma mesma nota poderão ser lançados produtos com códigos de benefícios distintos. Em relação ao campo Grupo de ICMS 2, tem-se que este buscará por exceções que poderão existir dentro do Grupo de ICMS.

**Nota:** o campo Grupo de ICMS 2 também poderá ser utilizado de forma independente.

Em relação ao campo **"Finalidade da Operação"**, tem-se que este estará vinculado aos itens ou ao cabeçalho da nota. Deste modo, este campo é utilizado, pois existem algumas situações em que, dependendo do registro inserido no campo Finalidade da Operação, a informação contida no campo Código do Benefício será alterada.

**Observação:** no faturamento de um pedido de venda, caso o parâmetro **"Atualiza finalidade da operação no faturamento - ATUALFINFAT"** esteja ativado e o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de destino (correspondente a nota a ser gerada) possuir uma finalidade de operação (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), campo **"Finalidade da Operação"**), esta será considerada e consequentemente inserida no cabeçalho da nota de destino em seu campo correspondente.

Porém, caso o campo Finalidade da Operação do Tipo de Operação - TOP não esteja preenchido, será considerada a configuração realizada no campo **"Finalidade da Operação"** localizado no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal).

O campo **"Classificação de ICMS"** também relaciona-se com a tela Cadastro de Parceiros, aba Fiscal, e/ou com a tela Tipos de Operação - TOP, aba Impostos, tendo o objetivo de identificar para qual tipo de Parceiro a nota está sendo emitida. Dentro deste campo temos as seguintes opções:

- Produtor Rural;
- Revendedor;
- Consumidor Final Contribuinte;
- Consumidor Final Não Contribuinte;
- Isento de ICMS.

A marcação **"Simples Nacional"** deverá ser habilitada caso a nota que está sendo emitida seja para um parceiro optante por este regime de tributação.

Quando habilitada, a marcação **"Operação Interestadual"** identificará se a nota está sendo emitida para dentro ou fora do Estado, no qual a empresa encontra-se situada.

No campo **"UF do Destinatário"** insira a UF para identificar qual Código de Benefício deverá ser vinculado ao Item da Nota. Para que esta funcionalidade seja considerada, deve-se, antes de efetuar o lançamento do Pedido, realizar as configurações abaixo:

- Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), sub-aba [NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaNF-e) (aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)), a marcação **"Considerar benefícios ao alterar item da nota?"** deverá encontrar-se habilitada;
- O documento deverá ser um Pedido de Venda, uma Venda ou uma Devolução de Venda, e;
- Deverá tratar-se de uma NF-e.

---

![Imagem 3: Informações adicionais sobre o campo UF do Destinatário:](https://ajuda.sankhya.com.br/hc/article_attachments/17432533424023) **Informações adicionais sobre o campo** **UF do Destinatário:**

- O campo UF do destinatário verifica o campo **"UF do Parceiro"** do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros);
- Caso seja informado um endereço de contato ou endereço de entrega na aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacontatos) do Cadastro de Parceiros, o sistema não irá associar a UF de destino para o código do beneficiário como UF informada no contato;
- Se for necessário editar o **"Código do Benefício"** manualmente na emissão da nota, desabilite a marcação Considerar Benefícios ao alterar item da nota presente na aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos) da tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

---

Selecione no campo **"Tributação"** o Código da Situação Tributária existente para o ICMS.

![Imagem 4: Para conhecer os detalhes das opções do campo Tributação , acesse o artigo Alíquotas de ICMS, aba Geral .](https://ajuda.sankhya.com.br/hc/article_attachments/16256080155415) Para conhecer os detalhes das opções do campo Tributação, acesse o artigo Alíquotas de ICMS, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#tributa%C3%A7%C3%A3o).

Em relação à marcação **"Levar benefício nulo para o XML da NF-e"**, quando esta estiver selecionada, fará com que a tag **<cBenef>** seja encaminhada para o XML da NF-e, porém, sem valor.

**Observação:** caso a marcação acima esteja habilitada, o campo Código do Benefício será desabilitado para preenchimento

**Importante:** o registro não será salvo caso a marcação não seja efetuada e o campo Código do Benefício encontre-se vazio.

Através do botão ![Imagem 5: Através do botão "Filtro Personalizado" será possível realizar a busca de informações relacionadas ao Cabeçalho da Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003091601) **"Filtro Personalizado"** será possível realizar a busca de informações relacionadas ao Cabeçalho da Nota (de todas as notas que forem NF-e's de emissão própria), bem como possuirá as mesmas funcionalidades de um campo da tela, tratando-se de uma condição para o benefício ser preenchido.

**Nota:** não será possível utilizar condições variáveis nos Filtros Personalizados.

**Observação:** sempre que houver a emissão própria de um documento, como por exemplo, Pedido de Venda, Venda, Devolução de Venda, Devolução de Compra e etc, a tag **<cBenef>** do Benefício Fiscal será preenchida.

**Importante:** a tag acima mencionada não será preenchida quando o campo **"Base de numeração"** (aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114#abaimpresso), tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)) encontrar-se selecionado com as opções **"Manual (Informada pelo Usuário)"** ou **"Pedido de Compra"**.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596014-Cadastro-Benef%C3%ADcios#top)
