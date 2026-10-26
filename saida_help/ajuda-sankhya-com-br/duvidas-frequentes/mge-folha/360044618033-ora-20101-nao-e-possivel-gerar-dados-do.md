---
id: "360044618033"
titulo: "ORA-20101: Não é possível gerar dados do e-social se existir eventos em processo de envio. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044618033-ORA-20101-N%C3%A3o-%C3%A9-poss%C3%ADvel-gerar-dados-do-e-social-se-existir-eventos-em-processo-de-envio-Como-resolver"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:56Z"
rotulos: ["Eventos", "eSocial", "ORA-20101", "Central do eSocial", "Erro ORA-20101: Eventos Pendentes de Envio", "Erro"]
---

# ORA-20101: Não é possível gerar dados do e-social se existir eventos em processo de envio. Como resolver?

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18666237352983) MENSAGEM:**

Erro na geração dos eventos para o E-social. General SQL error. ORA-20101: ORA-20101: Não é possível gerar dados do e-social se existir eventos em processo de envio.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18666259709975) SITUAÇÃO:**

Ao tentar transmitir o E-social, apresenta a rejeição a seguir.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18666237366167) CAUSA:**

Ocorre quando algum evento foi liberado para transmissão, mas ainda está pendente em processo de envio.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18666259724695) SOLUÇÃO:**

![Imagem 5: Acesse MGEPessoal>>Avançado>>Central do E-social](https://ajuda.sankhya.com.br/hc/article_attachments/18666259732375) Acesse MGEPessoal>>Avançado>>Central do E-social

Aba "Eventos pendentes de envio p/E-social"

Identifique nesta aba, se existe algum evento pendente de envio para retransmiti-lo.

Confira na aba "Acompanhamento", se existe algum evento com o campo "Situação" como "Iniciado" ou "Aguardando processamento".

Caso não tenha acesse o Console do San E-social.

![Imagem 6: O acesso ao SanE-social e feito através do endereço http://localhost:8778/index.html, ou pode ser definido o IP do…](https://ajuda.sankhya.com.br/hc/article_attachments/18666237380247) O acesso ao SanE-social e feito através do endereço **<http://localhost:8778/index.html,>**ou pode ser definido o IP do Servidor ou nome do host diferente de 'Localhost'.

Logar com usuário e senha: admin - admin

E clicar em 'Cancelar Envio'.

![Imagem 7: Posteriormente acesse novamente a 'Central do E-social' e gere os eventos necessários.](https://ajuda.sankhya.com.br/hc/article_attachments/18666237382423) Posteriormente acesse novamente a 'Central do E-social' e gere os eventos necessários.
