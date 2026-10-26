---
id: "12772062614167"
titulo: "cvc-enumeration-valid: O valor '1' não tem um aspecto válido em relação à enumeração '[2, 3, 4, 5, 6, 7, 9]'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12772062614167-cvc-enumeration-valid-O-valor-1-n%C3%A3o-tem-um-aspecto-v%C3%A1lido-em-rela%C3%A7%C3%A3o-%C3%A0-enumera%C3%A7%C3%A3o-2-3-4-5-6-7-9"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:17:08Z"
rotulos: ["Carga Horária", "eSocial", "Configuração Funcionários", "Central do eSocial", "Valide o código da carga horária", "Deletar campo \"INDSITREMUNDESLIG\" se indevidamente preenchido", "Corrija o Tipo de Jornada", "Erro"]
---

# cvc-enumeration-valid: O valor '1' não tem um aspecto válido em relação à enumeração '[2, 3, 4, 5, 6, 7, 9]'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16365376032023) MENSAGEM:**

cvc-enumeration-valid: O valor '1' não tem um aspecto válido em relação à enumeração '[2, 3, 4, 5, 6, 7, 9]'. Deve ser um valor da enumeração.
cvc-type.3.1.3: O valor '1' do elemento 'tpJornada' não é válido.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16365407561879) CAUSA:**

- Esse erro ocorre quando não foi preenchido o Tipo de Jornada da carga horária; ou
- Preencher o campo "**INDSITREMUNDESLIG**" indevidamente, este campo normalmente só é preenchido em caso de aposentadoria.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16365376042007) SOLUÇÃO:**

**Para resolução da primeira causa, siga o passo a passo abaixo:**

**MGE**

Para a correção desse erro, verifique no cadastro do funcionário qual é o código da carga horária que ele está vinculado.
 
![cvc-enumeration-valid](https://ajuda.sankhya.com.br/hc/article_attachments/15830437050391)
 
Em seguida, acesse o cadastro da carga horária em Arquivos/Cadastros/Carga Horária e valide o campo Tipo de Jornada.
 
![cvc-enumeration-valid](https://ajuda.sankhya.com.br/hc/article_attachments/15830437053719)
 
 
Selecione o tipo que melhor se enquadrar na carga horária em questão. É obrigatório o preenchimento do tipo de jornada para envio ao eSocial. Após esse ajuste, realize uma nova geração e envie o evento.

**Pessoal +**

Verifique no cadastro do funcionário qual é o código da carga horária que ele está vinculado.

![Imagem 6: Verifique no cadastro do funcionário qual é o código da carga horária que ele está vinculado.](https://ajuda.sankhya.com.br/hc/article_attachments/18362460414615)

Em seguida, acesse o cadastro da carga horária em Arquivos/Cadastros/Carga Horária e valide o campo Tipo de Jornada.

![Imagem 7: Em seguida, acesse o cadastro da carga horária em Arquivos/Cadastros/Carga Horária e valide o campo Tipo de Jornada.](https://ajuda.sankhya.com.br/hc/article_attachments/18362460418583)

Selecione o tipo que melhor se enquadrar na carga horária em questão.
É obrigatório o preenchimento do tipo de jornada para envio ao eSocial. 
Após esse ajuste, realize uma nova geração e envie o evento.

**Para resolução da sua causa siga a orientação abaixo:**

Caso o campo "**INDSITREMUNDESLIG**" esteja preenchido indevidamente basta deletar o campo e enviar o evento de rescisão novamente.

Esse campo normalmente só é preenchido em caso de aposentadoria, após deletar o campo o evento de rescisão será finalizado com sucesso.

![Imagem 8: Esse campo normalmente só é preenchido em caso de aposentadoria, após deletar o campo o evento de rescisão será…](https://ajuda.sankhya.com.br/hc/article_attachments/18362497457303)
