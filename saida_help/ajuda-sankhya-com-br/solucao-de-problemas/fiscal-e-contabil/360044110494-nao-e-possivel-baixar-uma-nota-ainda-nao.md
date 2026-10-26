---
id: "360044110494"
titulo: "Não é possível baixar uma nota ainda não confirmada pela SEFAZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110494-N%C3%A3o-%C3%A9-poss%C3%ADvel-baixar-uma-nota-ainda-n%C3%A3o-confirmada-pela-SEFAZ"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:36Z"
rotulos: ["Fiscal", "NF-e", "SEFAZ", "ORA-20101", "Não é possível baixar notas não confirmadas pela SEFAZ.", "Verifique notas com status 'Aguardando Autorização' 'Aguardando Correção' 'Com erro' ou 'Pendente de Retorno'.", "Ajuste o status das notas e tente gerar os livros novamente.", "Erro", "Documentos Eletrônicos"]
---

# Não é possível baixar uma nota ainda não confirmada pela SEFAZ

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16595121243799) MENSAGEM:**

[ORA-20101]: Não é possível baixar uma nota ainda não confirmada pela SEFAZ.
[ORA-06512]: em "SANKHYA.TRG\_INC\_UPT\_TGFLIV\_STATUSNFE", line 31
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_UPT\_TGFLIV\_STATUSNFE'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16595076267927) SOLUÇÃO:**

Verifique para o período em que está sendo realizada a 'Geração ICMS/IPI' quais notas estão com o campo STATUS NF-e = 'Aguardando Autorização', 'Aguardando Correção', 'Com erro de Validação' ou 'Pendente de Retorno'. Para tal, siga as instruções abaixo:

![Imagem 3: Realize filtros nos Portais ( Venda » Compra » Mov.Interna ) para o período de geração dos livros fiscais.](https://ajuda.sankhya.com.br/hc/article_attachments/16595121252119) Realize filtros nos Portais (Venda » Compra » Mov.Interna) para o período de geração dos livros fiscais.

![Imagem 4: Selecione a coluna 'Status NF-e':](https://ajuda.sankhya.com.br/hc/article_attachments/16595121255575) Selecione a coluna 'Status NF-e':

![Imagem 5: Selecione a coluna 'Status NF-e':](https://ajuda.sankhya.com.br/hc/article_attachments/15185354139671)

![Imagem 6: Caso não localize esse campo, o mesmo pode ser inserido através do botão "Configuração da Grade" :](https://ajuda.sankhya.com.br/hc/article_attachments/16595076277527) Caso não localize esse campo, o mesmo pode ser inserido através do botão **"Configuração da Grade"**:

![Imagem 7: Caso não localize esse campo, o mesmo pode ser inserido através do botão "Configuração da Grade" :](https://ajuda.sankhya.com.br/hc/article_attachments/15185379382551)

Busque pelo campo **"Status NF-e"** em **"Colunas disponíveis"** e arraste para **"Colunas selecionadas"**.

![Imagem 8: Para notas fiscais eletrônicas com Status NF-e diferente de "Aprovada" , de acordo com o Status apresentado, proceda…](https://ajuda.sankhya.com.br/hc/article_attachments/16595076285335) Para notas fiscais eletrônicas com Status NF-e diferente de **"Aprovada"**, de acordo com o Status apresentado, proceda com as devidas tratativas:

- Aguardando Autorização: [Nota Fiscal Eletrônica com status 'Aguardando Autorização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)
- Aguardando Correção: [Nota Fiscal Eletrônica com status 'Aguardando Correção'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043231613)
- Pendente de Retorno: [Nota Fiscal Eletrônica com status 'Pendente de Retorno'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454)

![Imagem 9: Realizada a tratativa da respectiva nota de acordo com o seu status, teste a geração dos livros novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16595121263127) Realizada a tratativa da respectiva nota de acordo com o seu status, teste a geração dos livros novamente.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16595121269783) CAUSA:**

Ao tentar gerar os livros fiscais de determinado período, se existirem notas com Status NF-e = 'Aguardando Autorização', 'Aguardando Correção', 'Com erro de Validação' ou 'Pendente de Retorno', será apresentada a mensagem.
