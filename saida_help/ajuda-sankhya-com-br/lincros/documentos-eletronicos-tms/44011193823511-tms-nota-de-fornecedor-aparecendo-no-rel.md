---
id: "44011193823511"
titulo: "[TMS] - Nota de Fornecedor Aparecendo no Relatório de Entrega com Status \"Em transporte\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011193823511--TMS-Nota-de-Fornecedor-Aparecendo-no-Relat%C3%B3rio-de-Entrega-com-Status-Em-transporte"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T18:57:23Z"
rotulos: ["sync_hc", "lincros", "lincros_13439143", "sync_hash_676886da94ba"]
---

# [TMS] - Nota de Fornecedor Aparecendo no Relatório de Entrega com Status "Em transporte"

## 1 - Problema Relatado pelo Cliente:

O cliente relatou que uma nota de fornecedor está sendo exibida no relatório de entrega com o status "Em transporte", o que indica que a finalização da nota não foi concluída corretamente. O cliente solicitou uma verificação sobre como a nota de fornecedor foi integrada ao sistema e por que ela aparece no relatório de entrega.

## 2 - Passo a Passo para Resolver o Problema:

## 1.Verificar o Certificado Digital Instalado:

O certificado digital é responsável por buscar as notas fiscais emitidas contra a empresa. Se o certificado estiver configurado corretamente, a nota de fornecedor será integrada automaticamente ao sistema.

Você pode verificar o certificado através de:

Cadastros gerais>configurações da empresa> Gerais>Certificado digital

## 2.Funcionalidade do Certificado Digital:

Verifique que a funcionalidade do certificado digital é de buscar e integrar notas fiscais emitidas contra a empresa para o sistema. Caso o certificado digital tenha sido instalado corretamente, a nota do fornecedor deve ser exibida no sistema, como mencionado no relatório.

## 3.Entender a Falta de Filtro no Sistema:

O TMS atualmente não aplica filtro na tela de NF-s  para distinguir entre notas fiscais de entrada (fornecedor) e notas fiscais de saída (vendas). Como resultado, a nota de fornecedor é apresentada no relatório de entregas, mesmo que a operação não se refira à entrega de mercadorias.

O relatório que é apresentado dessa forma pode ser acessado pelo caminho: Documentos eletrônicos> NF-es>

## 4.Verificar o Tipo de Operação da Nota Fiscal:

Embora a nota de fornecedor apareça na tela de NF-es, o sistema não está realizando a filtragem automática para identificar que se trata de uma nota fiscal de entrada, o que explica o motivo pelo qual a nota esta sendo exibida na tela de NF-es.

## 5. Podemos identificar que essa nota de entrada esta com situação de "em aberto" quando na coluna de "situação" da tela de NF-es, a situação dela fica como "em transporte", conforme imagem abaixo de exemplo:

![Imagem 1: 5. Podemos identificar que essa nota de entrada esta com situação de " em aberto " quando na coluna de " situação " da…](https://ajuda.sankhya.com.br/hc/article_attachments/44011185001239)

Com o certificado instalado, a nota de entrada é integrada normalmente ao sistema Lincros e permanecerá com o status "em transporte" até sua finalização.
