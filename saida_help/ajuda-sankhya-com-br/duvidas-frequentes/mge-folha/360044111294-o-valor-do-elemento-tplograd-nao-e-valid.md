---
id: "360044111294"
titulo: "O valor '' do elemento 'tpLograd' não é válido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111294-O-valor-do-elemento-tpLograd-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:32:51Z"
rotulos: ["Configuração", "Eventos", "eSocial", "Central do eSocial", "Erro de Valor Inválido no Campo 'tpLograd'", "Erro", "S-2200"]
---

# O valor '' do elemento 'tpLograd' não é válido.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16424639169559) MENSAGEM:**

"Campo obrigatorio com valor nao informado. [observacao]
cvc-minLength-valid: O valor '' com tamanho = '0' não tem um aspecto válido em relação ao minLength '1' do tipo '#AnonType\_tpLogradTEnderecoBrasil'.
cvc-type.3.1.3: O valor '' do elemento 'tpLograd' não é válido."

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16424623304599) SITUAÇÃO:**

Ao tentar transmitir o arquivo do eSocial apresenta a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16424639175575) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 4: Acesse MGEConfigurações » Arquivos » Endereços » Endereços , pesquise pelo endereço vinculado ao funcionário e preencha…](https://ajuda.sankhya.com.br/hc/article_attachments/16424623307927) Acesse MGEConfigurações » Arquivos » Endereços » Endereços, pesquise pelo endereço vinculado ao funcionário e preencha o campo "**Cód. Logradouro p/E-social"**. Depois salve as alterações feitas.

![Imagem 5: Acesse MGEPessoal » Avançado » Central do eSocial e transmita novamente as obrigações.](https://ajuda.sankhya.com.br/hc/article_attachments/16424623310231) Acesse MGEPessoal » Avançado » Central do eSocial e transmita novamente as obrigações.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16424639188631) CAUSA:**

Ocorre quando os endereços vinculados ao cadastros dos funcionários não estão com o campo Cod. Logradouro p/eSocial preenchido.

**![Imagem 7: OBSERVAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16424639190295)OBSERVAÇÃO:**

Evento: S-2200
[Manual Orientação do ESocial](https://drive.google.com/file/d/1fe79_YXu_a1a6xzvBf97pmBNN5_QPQHu/view)
