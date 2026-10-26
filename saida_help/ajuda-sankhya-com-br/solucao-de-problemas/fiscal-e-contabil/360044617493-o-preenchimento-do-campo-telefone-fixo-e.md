---
id: "360044617493"
titulo: "O preenchimento do campo telefone fixo é obrigatório se o campo telefone celular não for preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617493-O-preenchimento-do-campo-telefone-fixo-%C3%A9-obrigat%C3%B3rio-se-o-campo-telefone-celular-n%C3%A3o-for-preenchido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:50Z"
rotulos: ["Configuração", "Parceiro", "Telefone fixo é obrigatório se celular não for preenchido.", "Rejeição ocorre na transmissão do EFD-Reinf.", "Preencha dados de telefone e celular corretamente.", "Detalhe do erro", "Erro", "EFD-REINF", "R1000"]
---

# O preenchimento do campo telefone fixo é obrigatório se o campo telefone celular não for preenchido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17003847300375) MENSAGEM:**

MS1018 - O preenchimento do campo telefone fixo é obrigatório se o campo telefone celular não for preenchido. Localização:Registro: contato - XPATH: /Reinf/evtInfoContri/infoContri/alteracao/infoCadastro/contato.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17003877265687) SITUAÇÃO:**

Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17003847302423) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Comercial » Preferências » Empresa:](https://ajuda.sankhya.com.br/hc/article_attachments/17003877284375) Acesse: Comercial » Preferências » Empresa:

- Aba: **"EFD-Reinf"**
- Campo **"Responsável pela entrega":**informe o código do parceiro

![Imagem 5: Acesse: Configurações » Cadastros » Parceiros:](https://ajuda.sankhya.com.br/hc/article_attachments/17003877287191)  Acesse: Configurações » Cadastros » Parceiros:

- Aba: **"Endereço"**
- Busque o código do parceiro e preencha corretamente dados do  **"Telefone"** e **"Celular/Fax".**

![Imagem 6: Acesse: Livros Fiscais » Conexão » Reinf » EFD - Reinf e gere novamente os movimentos através do botão "Gerar Eventos"…](https://ajuda.sankhya.com.br/hc/article_attachments/17003847310487) Acesse: Livros Fiscais » Conexão » Reinf » EFD - Reinf e gere novamente os movimentos através do botão **"Gerar Eventos"**. Realize uma nova transmissão do evento R1000 através do botão **"Enviar Eventos".**

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17003877294487) CAUSA:**

O responsável pela entrega precisa ter os dados de telefones devidamente preenchidos no cadastro de Parceiro vinculado à empresa. Quando este não está devidamente preenchido, ocorre a rejeição.
