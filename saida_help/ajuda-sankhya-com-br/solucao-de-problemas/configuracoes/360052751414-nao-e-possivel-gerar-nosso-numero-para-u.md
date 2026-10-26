---
id: "360052751414"
titulo: "Não é possivel gerar nosso numero para uma nota ainda não aprovada pela Prefeitura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052751414-N%C3%A3o-%C3%A9-possivel-gerar-nosso-numero-para-uma-nota-ainda-n%C3%A3o-aprovada-pela-Prefeitura"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:28:54Z"
rotulos: ["Configuração", "Financeiro", "Prefeituras", "NFS-e", "Erro ao Gerar Nosso Número para Nota Não Aprovada"]
---

# Não é possivel gerar nosso numero para uma nota ainda não aprovada pela Prefeitura

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18613450261271) MENSAGEM**:

Não é possível gerar nosso numero para uma nota ainda não aprovada pela Prefeitura. NUNOTA XXXX. Financeiro de Nro unico XXXXX.

![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18613444807063) **CAUSA:**

Mensagem de validação causada pela configuração inadequada da opção NFS-e (Convencional ou NFS-e), ou tentativa de baixa para NFS-e não aprovada pela Prefeitura.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613444815639) **SOLUÇÃO:**

![Imagem 4: Localize no respectivo Portal a nota que gerou esse financeiro. (Verifique o NUNOTA citado na mensagem, para facilitar…](https://ajuda.sankhya.com.br/hc/article_attachments/18613444824599) Localize no respectivo Portal a nota que gerou esse financeiro. (Verifique o NUNOTA citado na mensagem, para facilitar a busca).

- Caso seja a EMISSÃO de uma **nota fiscal de serviço eletrônica**, que será devidamente transmitida para a Prefeitura, a mensagem de validação menciona que essa não está aprovada. Dessa forma será necessário verificar o seu 'Status NFS-e' e proceder com as tratativas até que a aprovação seja efetiva.
- Outra análise válida : Certifique-se que os itens lançados foram cadastrados na tela 'Serviços' (Configurações » Cadastros » Produtos » Serviço) e não na tela 'Produtos'.

![Imagem 5: Caso não seja uma NFS-E , a ser transmitida para a Prefeitura:](https://ajuda.sankhya.com.br/hc/article_attachments/18613450315671) Caso **não seja uma NFS-E**, a ser transmitida para a Prefeitura:

Verifique o Tipo de Operação utilizado no lançamento dessa nota, e atente-se a configuração do campo NFS-e (Aba NFS-e):

![Imagem 6: Verifique o Tipo de Operação utilizado no lançamento dessa nota, e atente-se a configuração do campo NFS-e (Aba NFS-e):](https://ajuda.sankhya.com.br/hc/article_attachments/18613450321815)

- **Convencional (Não usa NFS-e)**: Se selecionado, indicará que a top não será utilizada para nota fiscal eletrônica de serviços;
- **Normal:** Se selecionado, indicará que a top será utilizada para Nota Fiscal Eletrônica de serviços;"

Não sendo uma NFS-e, ajuste a configuração para "Convencional (Não usa NFS-e), exclua a nota e refaça o lançamento.
