---
id: "360043575614"
titulo: "A TOP não está ativa ou não pode ser utilizada aqui"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575614-A-TOP-n%C3%A3o-est%C3%A1-ativa-ou-n%C3%A3o-pode-ser-utilizada-aqui"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-09-16T14:08:30Z"
rotulos: ["#PUBLIFER", "#Revisadoclaudio", "CORE_E00865", "O.S1280651", "Configuração", "NF-e", "XML", "Importação", "TOP", "Problema com TOP na Importação", "Erro"]
---

# A TOP não está ativa ou não pode ser utilizada aqui

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16105378154391) MENSAGEM:**

[CORE\_E00865]  A TOP não está ativa ou não pode ser utilizada aqui.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16105378155287) SOLUÇÃO:**

![Imagem 3: Certifique-se que para o seu processo será válido trabalhar com a marcação "Validar TOP na importação do XML" :](https://ajuda.sankhya.com.br/hc/article_attachments/16105369720727) Certifique-se que para o seu processo será válido trabalhar com a marcação **"Validar TOP na importação do XML"**:

**(2)** Tela **"[Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)"** (Caminho de acesso: Comercial » Rotinas),  botão **"Outras Opções"**:

![Imagem 4: (2) Tela " Portal de Importação de XML " (Caminho de acesso: Comercial » Rotinas), botão "Outras Opções" :](https://ajuda.sankhya.com.br/hc/article_attachments/14499349376407)

Quando a opção Validar TOP na importação de XML estiver marcada, no campo **"Cód. Tipo Operação"** será possível selecionar apenas as TOP's pré-definidas no cadastro, não permitindo a utilização de qualquer outro código. Porém, quando desmarcada a opção, o sistema disponibilizará apenas as TOP's ativas, sendo que todas estas poderão ser utilizadas.

Caso a marcação acima não seja necessária, desmarque a mesma e refaça a importação.

![Imagem 5: Caso a marcação seja válida, certifique-se que o Tipo de Operação utilizado atende aos seguintes critérios, todas as…](https://ajuda.sankhya.com.br/hc/article_attachments/16105369721751) Caso a marcação seja válida, certifique-se que o Tipo de Operação utilizado atende aos seguintes critérios, todas as TOP's ativas que:

**(2)** Para quando o tipo de NF-e selecionada for diferente de **Devolução**, será pesquisado todas as TOP's que possuam o tipo de movimento igual **Compra** ou **Financeiro** e que modelo do documento seja: 08, 57 ou 67;

**(2)** Para quando o tipo de NF-e selecionada for igual a **Devolução de Mercadoria**, será pesquisado todas as TOP's que o Tipo de movimento seja igual **Devolução de venda**.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16105378159255) CAUSA:**

Mensagem será apresentada quando a opção Validar TOP na importação de XML estiver marcada e no campo Cód. Tipo Operação forem selecionadas TOP's inativas ou com configurações divergentes das pré-definidas no cadastro.
