---
id: "360044618273"
titulo: "O valor do elemento 'grauInstr' não é válido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044618273-O-valor-do-elemento-grauInstr-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:34:16Z"
rotulos: ["Fiscal", "eSocial", "Configuração Funcionários", "Central do eSocial", "Valor Inválido no Campo 'grauInstr'", "Erro"]
---

# O valor do elemento 'grauInstr' não é válido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16425686252311) MENSAGEM:**

"Campo obrigatório com valor nao informado. [grauInstr]
cvc-pattern-valid: O valor '' não tem um aspecto válido em relação ao padrão '\d{2}' do tipo '#AnonType\_grauInstrtrabalhadorevtTSVInicioeSocial'.
cvc-type.3.1.3: O valor '' do elemento 'grauInstr' não é válido."

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16425686256791) SITUAÇÃO:**

Ao tentar transmitir o arquivo do eSocial apresenta a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16425686258967) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 4: Acesse MGEPessoal » Arquivos » Funcionários , aba Pessoais e no campo "Escolaridade" preencha corretamente, conforme o…](https://ajuda.sankhya.com.br/hc/article_attachments/16425663633431) Acesse MGEPessoal » Arquivos » Funcionários, aba **Pessoais** e no campo **"Escolaridade"** preencha corretamente, conforme o grau de instrução do Funcionário e salve o registro.

![Imagem 5: Acesse MGEPessoal » Avançado » Central do eSocial e transmita novamente as obrigações.](https://ajuda.sankhya.com.br/hc/article_attachments/15642595206807) Acesse MGEPessoal » Avançado » Central do eSocial e transmita novamente as obrigações.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16425686269719) CAUSA:**

Ocorre quando os dados de Grau de Escolaridade do cadastro de funcionário está em branco.

**![Imagem 7: OBSERVAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16425663638423) OBSERVAÇÃO:**

Evento: S-2300
[Manual Orientação do eSocial](https://drive.google.com/file/d/1fe79_YXu_a1a6xzvBf97pmBNN5_QPQHu/view)
