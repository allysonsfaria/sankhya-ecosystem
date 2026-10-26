---
id: "9190431805719"
titulo: "Versão NF-e '0' não suportada no Sankhya-W. Versões suportada 401, 502, 503, 598, 599 e 600"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9190431805719-Vers%C3%A3o-NF-e-0-n%C3%A3o-suportada-no-Sankhya-W-Vers%C3%B5es-suportada-401-502-503-598-599-e-600"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:33Z"
rotulos: ["Configuração", "NF-e", "TOP", "CFOP", "Preferências", "CORE_E02732", "Versão", "Erro"]
---

# Versão NF-e '0' não suportada no Sankhya-W. Versões suportada 401, 502, 503, 598, 599 e 600

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18666951886999) MENSAGEM:**

[CORE\_E02732] Versão NF-e '0' não suportada no Sankhya-W. Versões suportada 401, 502, 503, 598, 599 e 600.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18666951898647) SITUAÇÃO:**

Ao tentar dar entrada na NF-e a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18791442814999) SOLUÇÃO:**

![Imagem 4: Confira se o campo Versão NF-e/NFC-e nas preferências da Empresa ( Comercial » Preferências » Empresa) está devidamente…](https://ajuda.sankhya.com.br/hc/article_attachments/18666910905879) Confira se o campo Versão NF-e/NFC-e nas preferências da **Empresa** (Comercial » Preferências » Empresa) está devidamente preenchido.

![Imagem 5: Confira se o campo Versão NF-e/NFC-e nas preferências da Empresa ( Comercial » Preferências » Empresa) está devidamente…](https://ajuda.sankhya.com.br/hc/article_attachments/18666910939543)

![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18924352711959) **OBSERVAÇÃO:**

A partir da versão 4.23 do sistema, houve uma alteração na localização do campo.

Acesse: Comercial » Preferências » Empresa.  Aba Documentos Fiscais Eletrônicos - sub aba: NF-e/NFC-e:

![Imagem 7: Acesse: Comercial » Preferências » Empresa. Aba Documentos Fiscais Eletrônicos - sub aba: NF-e/NFC-e:](https://ajuda.sankhya.com.br/hc/article_attachments/18924357184663)

![Imagem 8: Caso esteja utilizando uma TOP nova será necessário verificar a configuração do campo](https://ajuda.sankhya.com.br/hc/article_attachments/18666951951383) Caso esteja utilizando uma TOP nova será necessário verificar a configuração do campo

"**Atualização de Livros ICMS**" da TOP, caso definido para não atualizar, teoricamente não seria um documento fiscal e com isso não tem necessidade de enviar a CFOP. Portanto, é necessário ajustar esse campo e realizar o lançamento novamente. Para TOP de venda esse campo é definido como Livro de saída.

![Imagem 9: " Atualização de Livros ICMS " da TOP, caso definido para não atualizar, teoricamente não seria um documento fiscal e…](https://ajuda.sankhya.com.br/hc/article_attachments/18666910956055)

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18666910900503) CAUSA:**

Ocorre se nas preferências da **Empresa** (Comercial » Preferências » Empresa) o campo Versão NF-e/NFC-e não estiver devidamente configurado ou usar uma TOP com configuração incorreta.
