---
id: "4403485020695"
titulo: "Como gerar registro 0220 do EFD ICMS/IPI?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403485020695-Como-gerar-registro-0220-do-EFD-ICMS-IPI"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:23:52Z"
rotulos: ["Produtos", "Configuração", "IPI", "ICMS", "Impostos", "EFD", "Estoque", "#validadoThiagoArantes", "Gerar EFD corretamente", "Registro 0220 do EFD ICMS/IPI", "Configurar unidades de produtos"]
---

# Como gerar registro 0220 do EFD ICMS/IPI?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16345071002007) SITUAÇÃO:**

O Registro 0220 do EFD FISCAL é gerado quando há compra de produto em uma unidade padrão, mas na venda, a mesma foi feita com unidade alternativa.

Abaixo trecho do Guia prático:

<http://sped.rfb.gov.br/estatico/30/5EC21565F41BC9D392045D71E5706429186705/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.6.pdf>

**Registro 0220: Fatores de conversão de unidades**

Este registro tem por objetivo informar os fatores de conversão dos itens descriminados na Tabela de Identificação do Item (Produtos e Serviços) entre a unidade informada no registro 0200 e as unidades informadas nos registros dos documentos fiscais ou nos registros do controle da produção e do estoque - Bloco K. Nos documentos eletrônicos de emissão própria quando a unidade comercial for diferente da unidade do inventário, este registro deverá ser informado. Quando for utilizada unidade de inventário (bloco H) ou unidade de medida de controle de estoque (bloco K), diferente da unidade comercial do produto, é necessário informar o registro 0220 para informar os fatores de conversão entre as unidades.

No exemplo abaixo, foi comprado um produto com a unidade Padrão UN(unidade) e vendido na Unidade Alternativa CX(caixa).

Essas configurações ficam no cadastro de Produtos.

**Aba Geral> campo Unidade Padrão**

![Imagem 2: Aba Geral> campo Unidade Padrão](https://ajuda.sankhya.com.br/hc/article_attachments/15081406441879)

E aba **Unidade Alternativa> Inserida Unidade alternativa.**

![Imagem 3: E aba Unidade Alternativa> Inserida Unidade alternativa.](https://ajuda.sankhya.com.br/hc/article_attachments/4403499137559)

No exemplo

-Unidade alternativa cadastrada.

![Imagem 4: -Unidade alternativa cadastrada. -Nota de entrada lançada com unidade padrão. -Venda feita com unidade alternativa.](https://ajuda.sankhya.com.br/hc/article_attachments/15081428579991)

-Nota de entrada lançada com unidade padrão.

![Imagem 5: -Unidade alternativa cadastrada. -Nota de entrada lançada com unidade padrão. -Venda feita com unidade alternativa.](https://ajuda.sankhya.com.br/hc/article_attachments/15081424341655)

-Venda feita com unidade alternativa.

![Imagem 6: -Unidade alternativa cadastrada. -Nota de entrada lançada com unidade padrão. -Venda feita com unidade alternativa.](https://ajuda.sankhya.com.br/hc/article_attachments/15081477753751)

-Nas preferências da empresa devem estar cadastrados os registros do bloco 0 e o bloco marcado pra gerar.

![Imagem 7: -Nas preferências da empresa devem estar cadastrados os registros do bloco 0 e o bloco marcado pra gerar. - As notas…](https://ajuda.sankhya.com.br/hc/article_attachments/15081440180503)

- As notas devem ser geradas no livro ( Tela Geração de ICMS/IPI).

- Na tela de geração do EFD ICMS/IPI  > EFD - Escrituração Fiscal Digital - ICMS/IPI >Aba opções **"Gerar a opção"** > Item da Nota com a Unidade Comercializada> Deve estar Marcado.

- Faça uma cópia de estoque, se a empresa gera Bloco K / Bloco H para informar a data da cópia ou contagem no campo Data do inventário.
