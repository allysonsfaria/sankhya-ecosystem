---
id: "360042507654"
titulo: "O valor 'XXXX' do elemento 'NCM' não é válido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507654-O-valor-XXXX-do-elemento-NCM-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:16Z"
rotulos: ["ERRONF", "#criadoRoger", "Produtos", "Configuração", "NF-e", "XML", "SEFAZ", "Valor Inválido no Código NCM", "Erro"]
---

# O valor 'XXXX' do elemento 'NCM' não é válido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16315057492631) MENSAGEM:**

ERRO NA VALIDAÇÃO. Número Único: 'X'
Validação básica Sefaz: Erros encontrados:
cvc-pattern-valid: O valor 'XXXX' não tem um aspecto válido em relação ao padrão '[0-9]{2}|[0-9]{8}' do tipo '#AnonType\_NCMproddetinfNFeTNFe'.
cvc-type.3.1.3: O valor 'XXXX' do elemento 'NCM' não é válido. erro.handshake=true

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16315057495191) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela " Produtos " ( Arquivos » Produtos ), Aba "Propriedades" - Campo 'Cód.NCM': informe um NCM válido.](https://ajuda.sankhya.com.br/hc/article_attachments/16315057497751) Acesse a tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** (Arquivos » Produtos),  Aba **"Propriedades"** - Campo **'Cód.NCM':** informe um NCM válido.

![Imagem 4: Na mensagem de erro é retornado o NCM rejeitado. Caso não saiba a qual produto esse NCM está vinculado, gere o XML em…](https://ajuda.sankhya.com.br/hc/article_attachments/16315047061783) Na mensagem de erro é retornado o NCM rejeitado. Caso não saiba a qual produto esse NCM está vinculado, gere o XML em conferência conforme abaixo para análises detalhadas:

**(2)** Selecione a nota rejeitada » Lançamento » Botão direito » **"Gerar XML da NF-e em arquivo para Conferência"**.

**(2)** Abra o XML gerado pelo Internet Explorer e/ou Bloco de Notas.

**(2)** Aperte ctrl+f do teclado, será aberto um campo de busca, faça a busca pelo código do NCM apresentado na mensagem de erro, até que seja localizado o código do produto (<cProd>) referenciado na rejeição apresentada.

**![Imagem 5: CASO DE USO:](https://ajuda.sankhya.com.br/hc/article_attachments/16315057505559) CASO DE USO:**

Validação básica Sefaz: Erros encontrados:
cvc-pattern-valid: O valor**'33043000'** não tem um aspecto válido em relação ao padrão '[0-9]{2}|[0-9]{8}' do tipo '#AnonType\_NCMproddetinfNFeTNFe'.
cvc-type.3.1.3: 
O valor **'33043000'** do elemento 'NCM' não é válido. erro.handshake=true

Identificado o item rejeitado, realize os ajustes no campo citado, conforme item 1 desse artigo.

**![Imagem 6: ATENÇÃO: É possível realizar a consulta de NCM por Descrição ou Código, através do seguinte link:](https://ajuda.sankhya.com.br/hc/article_attachments/16315057507991) ATENÇÃO:** É possível realizar a consulta de NCM por Descrição ou Código, através do seguinte link:

**[Consulta NCM](https://efisco.sefaz.pe.gov.br/sfi_com_tge/PRConsultarNCM)**

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16315047068567) CAUSA:**

Ocorre quando uma NF-e for transmitida,  onde o NCM de um ou mais itens, não existir na Tabela de NCM publicado pelo MDIC²-Ministério do Desenvolvimento, Indústria e Comércio Exterior.
