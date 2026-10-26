---
id: "360042756634"
titulo: "O campo 'c39_camposExtras/campoExtra/codigo' está com o valor \" inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042756634-O-campo-c39-camposExtras-campoExtra-codigo-est%C3%A1-com-o-valor-inv%C3%A1lido"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:06:11Z"
rotulos: ["Configuração", "GNRE", "Estados", "Gerar novo lote após ajuste", "Código inválido no arquivo GNRE", "Ajustar \"Campos Extras GNRE\" na tela Estados", "Erro", "Documentos Eletrônicos"]
---

# O campo 'c39_camposExtras/campoExtra/codigo' está com o valor " inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16413718758807) MENSAGEM:**

Layout do arquivo de lote inválido! Causa do Erro: O campo 'c39\_camposExtras/campoExtra/codigo' está com o valor " inválido. O valor deve ser numérico até 2147483647!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16413718759319) SOLUÇÃO:**

![Imagem 3: Identifique a UF do Parceiro Destinatário;](https://ajuda.sankhya.com.br/hc/article_attachments/16413718759959) Identifique a UF do Parceiro Destinatário;

![Imagem 4: Acesse a tela " Estados" ( Caminho de acesso: Configurações » Cadastros » Endereços );](https://ajuda.sankhya.com.br/hc/article_attachments/16413718760471) Acesse a tela "[**Estados"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294) (Caminho de acesso: Configurações » Cadastros » Endereços);

![Imagem 5: Busque pela UF identificada no Item 1;](https://ajuda.sankhya.com.br/hc/article_attachments/16413718762391) Busque pela UF identificada no Item 1;

![Imagem 6: Se na aba " Geral" estiver marcada a opção " Gera Informação dos Campos Adicionais na GNRE" , acesse a aba " GNRE…](https://ajuda.sankhya.com.br/hc/article_attachments/16413731809815) Se na aba "**Geral"** estiver marcada a opção "**Gera Informação dos Campos Adicionais na GNRE"**, acesse a aba "**GNRE Unidade Federativa"** e preencha o campo "**Código (Campos Extras GNRE)"**:

![Imagem 7: Se na aba Geral não estiver marcada a opção Gera Informação dos Campos Adicionais na GNRE , acesse a aba Geral e…](https://ajuda.sankhya.com.br/hc/article_attachments/16413731810711) Se na aba Geral não estiver marcada a opção Gera Informação dos Campos Adicionais na GNRE, acesse a aba Geral e preencha o campo Código (Campos Extras GNRE).

(1)** CONCLUSÃO:** Quando a opção Gera Informação dos Campos Adicionais na GNRE estiver:

- Marcada: Buscará o código do campo na aba GNRE Unidade Federativa;
- Desmarcada: Buscará o código do campo que está na aba Geral da tela Estado.

![Imagem 8: Realizado o ajuste, gere um novo lote da GNRE.](https://ajuda.sankhya.com.br/hc/article_attachments/16413718768279) Realizado o ajuste, gere um novo lote da GNRE.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16413718768791) CAUSA:**

Mensagem retornada na geração de lote de GNRE quando o campo **"Código (Campos Extras GNRE)"** não é preenchido.
