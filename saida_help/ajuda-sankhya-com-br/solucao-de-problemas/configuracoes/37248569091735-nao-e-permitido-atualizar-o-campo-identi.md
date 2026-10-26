---
id: "37248569091735"
titulo: "Não é permitido atualizar o campo Identificação PDV quando ele já possui valor."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37248569091735-N%C3%A3o-%C3%A9-permitido-atualizar-o-campo-Identifica%C3%A7%C3%A3o-PDV-quando-ele-j%C3%A1-possui-valor"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:13:36Z"
rotulos: ["Segurança", "PDV", "ORA-06512", "Cadastro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Não é permitido atualizar o campo Identificação PDV", "campo Identificação PDV quando ele já possui valor", "Cadastro de PDV", "identificador único do equipamento"]
---

# Não é permitido atualizar o campo Identificação PDV quando ele já possui valor.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/37248569087639) **MENSAGEM:**

ORA-20002: Não é permitido atualizar o campo Identificação PDV quando ele já possui valor.
ORA-06512: em "SANKHYA.TRG\_INC\_UPD\_TGFPDV\_BEFORE", line 6
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_UPD\_TGFPDV\_BEFORE'

**SITUAÇÃO:**

Ao tentar alterar o cadastro do PDV, o sistema pode impedir a gravação das alterações e exibir uma das seguintes mensagens:

- “Não é permitido atualizar o campo Identificação PDV quando ele já possui valor.”
- “O campo Identificação PDV não pode ser alterado para vazio.”
- “Já existe um registro com a Identificação PDV informada.”

Esse comportamento é esperado e faz parte das regras de segurança do sistema, que não permitem alterar a Identificação do PDV após o cadastro.

**SOLUÇÃO:**

Caso seja necessário utilizar o PDV em **outro equipamento**, o procedimento correto é:

- **Criar um novo cadastro de PDV** para a nova máquina

**OBSERVAÇÃO:** A alteração direta da Identificação do PDV **não é suportada**, nem via tela nem por comandos no banco de dados, pois pode causar inconsistências no sistema.

##### Posso usar o mesmo PDV para mais de um usuário?

É possível cadastrar mais de um usuário para o mesmo PDV, desde que a utilização ocorra em momentos distintos. O sistema não permite que dois usuários utilizem o mesmo PDV simultaneamente. Caso seja necessário o uso simultâneo de usuários caixa, cada usuário deverá possuir seu próprio cadastro de PDV e sua própria máquina.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/37248552207255)CAUSA:**

Esse erro ocorre porque o campo **''Identificação do PDV''** possui validações internas de segurança que impedem sua alteração após o cadastro inicial.

A Identificação do PDV é utilizada pelo sistema como um **identificador único do equipamento**, garantindo integridade, rastreabilidade e controle das operações do ponto de venda.

Por esse motivo, o sistema bloqueia alterações do valor já informado, limpeza do campo e reutilização da mesma identificação em outro PDV.
