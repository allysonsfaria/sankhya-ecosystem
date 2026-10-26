---
id: "360052601713"
titulo: "Nota Fiscal de Acompanhamento !  Veja orientações:"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052601713-Nota-Fiscal-de-Acompanhamento-Veja-orienta%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:29:41Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Impostos", "TOP", "CFOP", "Referência ao Cupom Fiscal; necessária para PJ", "Tipo \"Venda\"; atualiza Livro Fiscal e impostos", "Sequência controlada; buscar NF origem; cadastro se Consumidor Final"]
---

# Nota Fiscal de Acompanhamento !  Veja orientações:

| - Após emissão do Cupom Fiscal, determinado parceiro poderá solicitar que seja emitida uma **nota fiscal de acompanhamento**, referenciando o CF emitido. - Essa solicitação pode ocorrer em função da necessidade de Nota Fiscal para comprovação da garantia do produto, ou em casos onde trata-se de um parceiro "Pessoa Jurídica",visto que PJ não pode escriturar Cupons Fiscais. - Para tal, é possível seguir algumas configurações padrão, conforme detalhado a seguir. De toda forma, vale ressaltar que toda e qualquer configuração deve considerar as especificações de sua empresa, **alinhamentos com o Contador responsável**, e principalmente **validadas com um consultor de sua Franquia**. |
| --- |

![Imagem 1: O tipo de movimento para essa TOP é "Venda", para que as notas emitidas fiquem armazenadas em conjunto com outras…](https://ajuda.sankhya.com.br/hc/article_attachments/15935685170839)  O tipo de movimento para essa TOP é "Venda", para que as notas emitidas fiquem armazenadas em conjunto com outras operações de Saída;

![Imagem 2: O tipo de movimento para essa TOP é "Venda", para que as notas emitidas fiquem armazenadas em conjunto com outras…](https://ajuda.sankhya.com.br/hc/article_attachments/15935433320471)

![Imagem 3: Esse 'Tipo de Operação' não deve atualizar o financeiro, estoque, comissão, e apoio à decisão. Visto que todas estas…](https://ajuda.sankhya.com.br/hc/article_attachments/15935722946327) Esse 'Tipo de Operação' não deve atualizar o financeiro, estoque, comissão, e apoio à decisão. Visto que todas estas atualizações já foram anteriormente geradas a partir do Cupom Fiscal;

![Imagem 4: Não deve permitir alteração após a confirmação, para evitar que o registro da nota Fiscal no sistema seja diferente da…](https://ajuda.sankhya.com.br/hc/article_attachments/15935722947479) Não deve permitir alteração após a confirmação, para evitar que o registro da nota Fiscal no sistema seja diferente da nota Fiscal emitida e entregue ao cliente:

![Imagem 5: Não deve permitir alteração após a confirmação, para evitar que o registro da nota Fiscal no sistema seja diferente da…](https://ajuda.sankhya.com.br/hc/article_attachments/15935459067799)

![Imagem 6: Configurar o campo "Usar como Preço" com a opção "Preço de Venda", pois o valor unitário a ser praticado nas vendas é o…](https://ajuda.sankhya.com.br/hc/article_attachments/15935685174295) Configurar o campo "Usar como Preço" com a opção "Preço de Venda", pois o valor unitário a ser praticado nas vendas é o Preço de Venda calculado pelo sistema, a exemplo das demais operações deste processo;

![Imagem 7: Deve atualizar o Livro Fiscal de Saída, com os CFOP 5929 e 6929 - NF Ref. Oper. Registr. em CF;](https://ajuda.sankhya.com.br/hc/article_attachments/15935722949655) Deve atualizar o Livro Fiscal de Saída, com os CFOP 5929 e 6929 - NF Ref. Oper. Registr. em CF;

![Imagem 8: Deve atualizar o Livro Fiscal de Saída, com os CFOP 5929 e 6929 - NF Ref. Oper. Registr. em CF;](https://ajuda.sankhya.com.br/hc/article_attachments/15935466007575)

![Imagem 9: Deve calcular impostos incidentes sobre os produtos (ICMS, ST, PIS e COFINS) para que a empresa realize a emissão da…](https://ajuda.sankhya.com.br/hc/article_attachments/15935685177239) Deve calcular impostos incidentes sobre os produtos (ICMS, ST, PIS e COFINS) para que a empresa realize a emissão da Nota Fiscal com todos os impostos incidentes na operação. Mesmo havendo o destaque do imposto, que concede ao cliente o direito de se creditar dos impostos destacados, o mesmo não será pago "duas vezes", pois a escrituração desta Nota se dá de forma específica nos Livros, não considerando valor contábil nem impostos;

![Imagem 10: Todas as notas Fiscais emitidas pela empresa devem seguir a mesma sequência de numeração independente do movimento, e…](https://ajuda.sankhya.com.br/hc/article_attachments/15935685177879) Todas as notas Fiscais emitidas pela empresa devem seguir a mesma sequência de numeração independente do movimento, e esta sequência deve ser controlada pelo sistema:

- Como a Nota Fiscal de Acompanhamento de Cupom Fiscal será emitida pela empresa, deve ser configurada nesta TOP a **base de Numeração "Venda"**. Deve ser definido o Tipo de Numeração igual a **"Empresa/Série"**;
- Cadastrar no **"Controle de Numeração"** uma linha para a empresa, com a série que será utilizada nas Notas Fiscais emitidas pela empresa, caso não exista.
- Nos lançamentos realizados com esta TOP, o usuário deverá se lembrar de utilizar a mesma série informada no controle de Numeração da mesma.

![Imagem 11: Opção "Buscar NF de origem p/ referenciar na NFe:" deverá estar marcada:](https://ajuda.sankhya.com.br/hc/article_attachments/15935685178391)Opção "Buscar NF de origem p/ referenciar na NFe:" deverá estar marcada:

![Imagem 12: Opção "Buscar NF de origem p/ referenciar na NFe:" deverá estar marcada:](https://ajuda.sankhya.com.br/hc/article_attachments/15935482095255)

**![Imagem 13: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15935685180439) OBSERVAÇÃO:**

Para lançamento da nota de acompanhamento, é necessário localizar o documento de origem na retaguarda (Sankhya Om), selecionar "outras opções": **Gerar nota de acompanhamento p/Cupom Fiscal.**

![Imagem 14: Para lançamento da nota de acompanhamento, é necessário localizar o documento de origem na retaguarda (Sankhya Om),…](https://ajuda.sankhya.com.br/hc/article_attachments/15935722809367)

Feito isso, informe a TOP e série a serem utilizadas, valide as informações geradas no respectivo lançamento e confirme a nota.

![Imagem 15: Caso o Parceiro da Cupom/NFC-e de origem seja 'Consumidor Final', será preciso cadastrar o Parceiro para emissão da…](https://ajuda.sankhya.com.br/hc/article_attachments/15935685180439) Caso o Parceiro da Cupom/NFC-e de origem seja 'Consumidor Final', será preciso cadastrar o Parceiro para emissão da NF-e ( Modelo 55) pois a Sefaz valida os dados do CNPJ/CPF do Parceiro para emissão da nota.
