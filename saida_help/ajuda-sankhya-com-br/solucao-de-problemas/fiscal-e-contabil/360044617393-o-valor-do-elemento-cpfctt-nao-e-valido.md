---
id: "360044617393"
titulo: "O valor \"do elemento 'cpfCtt\" não é válido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617393-O-valor-do-elemento-cpfCtt-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:01Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "EFD", "Erro de CPF inválido: Valor do elemento 'cpfCtt' não é válido", "Solução: Preencha corretamente o campo \"Responsável pela Entrega\" em Comercial » Preferências.", "Causa: Informações do 'Responsável pela Entrega' estão incompletas", "Erro", "Reinf"]
---

# O valor "do elemento 'cpfCtt" não é válido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16415300075799) MENSAGEM:**

cvc-pattern-valid: O valor " não tem um aspecto válido em relação ao padrão '[0-9]{11}' do tipo '#AnonType\_cpfCttcontatoinfoCadastroalteracaoinfoContrievInfoContReinf'. cvc-type.3.1.3: O valor " do elemento 'cpfCtt' não é válido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16415300077335) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse Comercial » Preferências » Empresa Aba: "REINF" Preencha o campo "Responsável pela Entrega:" com o Cod.Parceiro,…](https://ajuda.sankhya.com.br/hc/article_attachments/16415300078487) Acesse Comercial » Preferências » Empresa
Aba: **"REINF"**
Preencha o campo **"Responsável pela Entrega:"** com o Cod.Parceiro, previamente cadastrado em Configurações » Cadastros » Parceiros, com os campos de **"CPF/CNPJ"** devidamente preenchidos.

![Imagem 4: Ajustadas ambas configurações, repita a transmissão do Reinf.](https://ajuda.sankhya.com.br/hc/article_attachments/16415283739927) Ajustadas ambas configurações, repita a transmissão do Reinf.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16415283740823) CAUSA:**

Ocorre quando as informações do 'Responsável pela Entrega:' da empresa da transmissão do EFD-Reinf não estão devidamente preenchidas, principalmente o CPF.
