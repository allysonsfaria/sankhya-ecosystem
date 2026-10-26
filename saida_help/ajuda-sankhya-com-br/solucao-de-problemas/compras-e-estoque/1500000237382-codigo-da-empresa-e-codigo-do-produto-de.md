---
id: "1500000237382"
titulo: "Código da Empresa e Código do Produto devem ser informados para obter o uso do produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000237382-C%C3%B3digo-da-Empresa-e-C%C3%B3digo-do-Produto-devem-ser-informados-para-obter-o-uso-do-produto"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:26:22Z"
rotulos: ["#criadoRoger", "CT-e", "Configuração", "Código da Empresa", "XML", "Importação", "Preferências", "CORE_E04469", "#publicadoHyago", "Código do Produto", "Uso do Produto", "Erro"]
---

# Código da Empresa e Código do Produto devem ser informados para obter o uso do produto

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16274228833943) MENSAGEM**:

[CORE\_E04469] Código da Empresa e Código do Produto devem ser informados para obter o uso do produto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16274200159895) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse as Preferências para Importar CT-e em: Comercial » Rotinas » Portal de importação de XML . Clique em Outras…](https://ajuda.sankhya.com.br/hc/article_attachments/16274200161175) Acesse as Preferências para Importar CT-e em: Comercial » Rotinas » Portal de importação de XML.  Clique em Outras Opções » Preferências para importar CT-e Opção:

- Importar CT-e com cabeçalho: marcado
- Tipo de Importação:  Central de Compras
- Top p/ cabeçalho CT-e: Top do tipo compra / Não calcula e digita
- Serviço Padrão: informar um código do serviço de Frete valido
- Exige vínculo com notas: diferente de Não exige

![Imagem 4: Exige vínculo com notas: diferente de Não exige](https://ajuda.sankhya.com.br/hc/article_attachments/14679406132503)

Ao informar o serviço, a mensagem não é mais apresentada.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16274200164503) CAUSA:**

A mensagem ocorre pois nas preferências para importar o CT-e, foi marcada a opção para criar um cabeçalho de uma nota de compra e não foi informado o serviço de frete que deve ser inserido na nota no portal de compras.
