---
id: "27794302464023"
titulo: "Impressão de etiqueta/relatório pelo navegador Sankhya está com resolução ruim, veja como resolver"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27794302464023-Impress%C3%A3o-de-etiqueta-relat%C3%B3rio-pelo-navegador-Sankhya-est%C3%A1-com-resolu%C3%A7%C3%A3o-ruim-veja-como-resolver"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:39:18Z"
rotulos: ["Configuração", "Impressão", "Relatórios", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "resolução ruim", "Impressão de etiqueta/relatório", "navegador Sankhya", "Erro"]
---

# Impressão de etiqueta/relatório pelo navegador Sankhya está com resolução ruim, veja como resolver

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27794302455319)SOLUÇÃO:**

Caso outro navegador  imprima corretamente, coloque o comando <property name="forceDownloadElectron" value="true"/> no modelo de etiqueta/relatório, conforme print abaixo.

Após essa alteração, o sistema irá utilizar o visualizador nativo do sistema operacional para pré-visualizar os boletos, sendo que o mesmo comportamento ocorre quando for utilizado o navegador Google Chrome. Para esse caso, o parâmetro **"UTZJASPERWC"** precisa ser desligado.

![Imagem 2: Após essa alteração, o sistema irá utilizar o visualizador nativo do sistema operacional para pré-visualizar os…](https://ajuda.sankhya.com.br/hc/article_attachments/27794302456983)

Depois de inserida a propriedade acima, a impressão usará esse preview.

![Imagem 3: Depois de inserida a propriedade acima, a impressão usará esse preview.](https://ajuda.sankhya.com.br/hc/article_attachments/27798883021591)

Sem a propriedade a impressão fica assim:

![Imagem 4: Sem a propriedade a impressão fica assim:](https://ajuda.sankhya.com.br/hc/article_attachments/27798846326295)

E com o parâmetro UTZJASPERWC  ligado, o sistema vai levar por padrão esse preview.

Vale destacar que de forma nativa esse parâmetro vai desligado nas bases.

![Imagem 5: Vale destacar que de forma nativa esse parâmetro vai desligado nas bases.](https://ajuda.sankhya.com.br/hc/article_attachments/27798883025431)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27794302458391)CAUSA:**

Problema ocorre pois ao visualizar a etiqueta pelo preview do navegador Sankhya e clicar no botão de impressão, pode haver perda de resolução ao imprimir a etiqueta/relatório.

Para mais informações sobre visualização de relatórios e sobre o parâmetro UTZJASPERWC, leia o artigo: [Pré-visualizar notas e boletos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404333601175-Pr%C3%A9-visualizar-notas-e-boletos)
