---
id: "9300975768471"
titulo: "Local de Destino deve ser informado para o produto XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9300975768471-Local-de-Destino-deve-ser-informado-para-o-produto-XXXX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-01T14:03:44Z"
rotulos: ["Produtos", "Configuração", "XML", "TOP", "Estoque", "CORE_E00779", "Erro [CORE_E00779]: Corrigindo Falta de Local de Destino", "Erro"]
---

# Local de Destino deve ser informado para o produto XXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18604459640343) MENSAGEM:**

[CORE\_E00779] Local de Destino deve ser informado para o produto XXXX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18604459653271) SITUAÇÃO:**

Ao lançar uma nota ou processar o Arquivo XML na tela Portal de Importação de XML a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18604499454999) CAUSA:**

Quando existirem itens configurados com controle de estoque por local, e esse local não foi informado no respectivo lançamento ou existir uma customização relacionada ao parâmetro **Módulos Java para regras da central -MODREGCENTRAL.**

**SOLUÇÃO:**

![Imagem 4: Na tela 'Produtos' (Configurações » Cadastros » Produtos) verificar dentre os itens do lançamento realizado, quais…](https://ajuda.sankhya.com.br/hc/article_attachments/18604499464727) Na tela **'Produtos'**(Configurações » Cadastros » Produtos)verificar dentre os itens do lançamento realizado, quais possuem a marcação "Usa Local":

- Aba Medidas e Estoque >> Sub-Aba 'Estoque' >> Campo **'Usa Local'**:

![Imagem 5: Aba Medidas e Estoque >> Sub-Aba 'Estoque' >> Campo 'Usa Local' :](https://ajuda.sankhya.com.br/hc/article_attachments/18604459671831)

![Imagem 6: Para os itens que possuem a marcação acima, o campo LOCAL da grade de itens deverá ser preenchido no lançamento…](https://ajuda.sankhya.com.br/hc/article_attachments/18604499477911) Para os itens que possuem a marcação acima, o campo LOCAL da grade de itens deverá ser preenchido no lançamento realizado na respectiva 'Central':

![Imagem 7: Preenchido o campo acima, será possível salvar o lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/18604499486231) Preenchido o campo acima, será possível salvar o lançamento.

Será necessário ainda verificar se existe alguma informação inserida no parâmetro **MODREGCENTRAL-Módulos Java para regras da central,** para consultar esse parâmetro é necessário acessar a tela **Preferências** (Configurações » Avançado » Preferências), caso tenha alguma informação nesse parâmetro significa que uma personalização está envolvida, sendo assim, é necessário solicitar o criador dessa personalização revise a mesma que está gerando o erro.

Temos ainda uma última situação onde essa mensagem será apresentada, que é:

- Analisar o XML da operação e verificar qual o CFOP informado, segue um exemplo: XML se trata de uma operação: "**CFOP 5907 - Retorno simbólico de mercadoria depositada em depósito fechado ou armazém geral**"

![Imagem 8: Analisar o XML da operação e verificar qual o CFOP informado, segue um exemplo: XML se trata de uma operação: " CFOP…](https://ajuda.sankhya.com.br/hc/article_attachments/18604499492631)

NF de Origem, foi gerada por uma empresa, com isso o tipo de Movimento da TOP 706 está igual "**Transferência**" , e o sistema não possuí os dados de locais de Origem e Destino para definir nesse processo como está sendo tratado como uma possível "**Transferência**".

![Imagem 9: NF de Origem, foi gerada por uma empresa, com isso o tipo de Movimento da TOP 706 está igual " Transferência " , e o…](https://ajuda.sankhya.com.br/hc/article_attachments/18604459694487)

Na entrada dessa NF via portal de Importação de XML, deveria ser usado uma TOP do tipo de Movimento de Compras, pois dessa forma o sistema não tentará encontrar a NF de origem na mesma base e também não vai solicitar local Destino.  **Observação:** Quando é gerado uma Transferência, onde ambas empresas estão na mesma base, o sistema já trata essa questão dos locais e gera duas linha na TGFITE para o mesmo produto diferenciando movimentação de ENTRADA com SAIDA do estoque.
