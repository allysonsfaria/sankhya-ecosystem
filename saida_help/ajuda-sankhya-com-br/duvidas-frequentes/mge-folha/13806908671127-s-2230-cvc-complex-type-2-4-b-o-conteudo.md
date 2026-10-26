---
id: "13806908671127"
titulo: "S-2230 cvc-complex-type.2.4.b: O conteúdo do elemento 'evtAfastTemp' não está completo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13806908671127-S-2230-cvc-complex-type-2-4-b-O-conte%C3%BAdo-do-elemento-evtAfastTemp-n%C3%A3o-est%C3%A1-completo"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:30:59Z"
rotulos: ["XML", "eSocial", "S-2230", "Configuração Funcionários", "Erro em Elemento 'evtAfastTemp' do S-2230", "Erro", "Central de Projetos"]
---

# S-2230 cvc-complex-type.2.4.b: O conteúdo do elemento 'evtAfastTemp' não está completo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16922885013527) MENSAGEM:**

S-2230 cvc-complex-type.2.4.b: O conteúdo do elemento 'evtAfastTemp' não está completo.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16922885016855) SOLUÇÃO:**

Acesse o lançamento do afastamento e verifique o preenchimento conforme informação abaixo:

![Imagem 3: Não pode estar preenchido a "Data fim" com data futura;](https://ajuda.sankhya.com.br/hc/article_attachments/16922832209559) Não pode estar preenchido a "Data fim" com data futura;

![Imagem 4: Esse campo só deve ser preenchido quando de fato o afastamento for finalizado e o funcionário tiver retornado;](https://ajuda.sankhya.com.br/hc/article_attachments/16922832216343) Esse campo só deve ser preenchido quando de fato o afastamento for finalizado e o funcionário tiver retornado;

![Imagem 5: Esse campo só deve ser preenchido quando de fato o afastamento for finalizado e o funcionário tiver retornado;](https://ajuda.sankhya.com.br/hc/article_attachments/16922832219159)

![Imagem 6: Retifique o afastamento, deixando a data fim sem preenchimento. (Pode preencher a data no campo Dt.Prev.Retorno para…](https://ajuda.sankhya.com.br/hc/article_attachments/16922885026711) Retifique o afastamento, deixando a data fim sem preenchimento. (Pode preencher a data no campo Dt.Prev.Retorno para controle);

![Imagem 7: Após ter ajustado o afastamento, gere novamente o evento S-2230 e envie.](https://ajuda.sankhya.com.br/hc/article_attachments/16922832224535) Após ter ajustado o afastamento, gere novamente o evento S-2230 e envie.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16922832227479) CAUSA:**

Ocorre quando é preenchido a data fim indevidamente, antes do afastamento ter finalizado. O eSocial não aceita evento com data futura.
