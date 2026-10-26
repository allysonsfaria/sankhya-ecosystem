---
id: "360045111233"
titulo: "Criação de Relatórios para Docx"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111233-Cria%C3%A7%C3%A3o-de-Relat%C3%B3rios-para-Docx"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:40Z"
rotulos: ["Configuração", "Relatórios Formatados", "Relatórios", "jrxml", "iReport", "Word", "Criação de Relatórios para Docx manual", "Desenvolvimento de Relatórios em Docx: Considerações e Propriedades", "Documentos Eletrônicos", "JasperReports"]
---

# Criação de Relatórios para Docx

Ao realizar a criação de relatórios visando que estes sejam exportados para o formato **".docx"**, algumas características devem ser observadas. A saber:

Algumas particularidades de visualização não podem ser reproduzidas à risca, em consequência do mecanismo utilizado para posicionar os elementos na tela. O exportador cria uma grande tabela no documento. Cada célula dessa tabela, também pode conter uma tabela, possibilitando assim o posicionamento visual semelhante ao pretendido no relatório. Em decorrência a esse comportamento, documentos exportados em PDF e docx, partindo do mesmo jrxml (mesmo relatório), podem gerar saídas consideravelmente diferentes.

Os objetos padrão existentes no Word, como por exemplo, cabeçalhos e rodapés, não são criados ao se exportar nesse formato. Se existirem elementos que seriam usados como tal, eles também são criados em células de tabela, seguindo o comportamento de todo o documento gerado.

Características como largura de página e largura de coluna, podem levar o documento a não ser visualizado corretamente na tela, pois ao abrir o documento no Word, este deve seguir as configurações vigentes de largura e altura de página. Esta situação, pode levar a quebras inesperadas de página, e elementos que ficaram "invisíveis", por não caberem na página. Isso também torna distintos os documentos abertos em diferentes versões do Word, ou mesmo, uma similar versão com desiguais configurações de visualização.

Elementos que se sobrepõe naturalmente, não são exibidos em relatórios exportados em formatos baseados em grades (tabelas), tal como o docx. Deve-se atentar a este detalhe ao criar o relatório, ou alguns elementos serão perdidos ao gerar a visualização para este formato.

Vejamos algumas propriedades relevantes:

**net.sf.jasperreports.export.docx.flexible.row.height**

O valor falso é o padrão para esta propriedade, o que significa que os relatórios são exportados em tabelas de altura fixa, e com isso, ao editar o documento o usuário deve redimensionar manualmente a altura das células.

**net.sf.jasperreports.export.docx.frames.as.nested.tables**

O valor padrão para essa propriedade é verdadeiro. Isso significa, que por padrão, cada frame gerado no documento é renderizado (obtenção do resultado final) como uma tabela aninhada na tabela principal do documento.

**net.sf.jasperreports.export.docx.hidden.text**

Essa propriedade tem escopo de elemento, e significa que o elemento será renderizado como um texto oculto.

**net.sf.jasperreports.allow.element.overlap**

O padrão para essa propriedade é falso; o que representa que o gerador de relatório não efetua verificações de sobreposição de elementos. Ou seja, você pode criar um relatório com elementos que se sobrepõem, e esses componentes não serão exibidos ao exportar o relatório. Ao mudar o valor da propriedade para falso, o compilador de relatório irá verificar a sobreposição e não permitirá tal situação.
