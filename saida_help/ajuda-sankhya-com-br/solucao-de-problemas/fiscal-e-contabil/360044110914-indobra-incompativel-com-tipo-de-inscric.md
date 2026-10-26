---
id: "360044110914"
titulo: "IndObra incompatível com tipo de inscrição do estabelecimento (tpInscEstab)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110914-IndObra-incompat%C3%ADvel-com-tipo-de-inscri%C3%A7%C3%A3o-do-estabelecimento-tpInscEstab"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:52Z"
rotulos: ["Configuração", "Impostos", "EFD", "NFS-e", "Incompatibilidade inscrição e obra", "Erro tpInscEstab e indObra", "Configurar serviço corretamente", "Reinf"]
---

# IndObra incompatível com tipo de inscrição do estabelecimento (tpInscEstab)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17003586274711) MENSAGEM:**

MS1036 - IndObra incompatível com tipo de inscrição do estabelecimento (tpInscEstab). Se tpInscEstab = 1, indObra deve ser 0. Se tpInscEstab = 4, indObra deve ser 1 ou 2. Localização:Registro:

ideEstabObra - XPATH: /Reinf/evtServTom/infoServTom/ideEstabObra.

**![Imagem 2: SITUAÇÃO: Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.](https://ajuda.sankhya.com.br/hc/article_attachments/17003586271383) SITUAÇÃO:**
Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17003564245655) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Configurações » Cadastros » Produtos » Serviço](https://ajuda.sankhya.com.br/hc/article_attachments/17003586283671) Acesse: Configurações » Cadastros » Produtos » Serviço

Aba: **"Impostos"**.

Campo **"Tipo de Serviço"**: vincule o Tipo de serviço, cadastrado anteriormente

Campo **"Obra de Construção Civil"**: preencha o campos com um dos valores validos

- Quando seu conteúdo está vazio, o 'Indicativo de Prestação de Serviço em Obra' é igual a '0 - Não é obra de construção civil ou não está sujeita a matrícula de obra';
- Quando seu conteúdo está preenchido, o 'Indicativo de Prestação de Serviço em Obra' é igual ao conteúdo informado no campo e pode ser '1 - Obra de Construção Civil - Empreitada Total' e ou '2 - Obra de Construção Civil - Empreitada Parcial';

![Imagem 5: Acesse: Portal de Vendas >>Notas de Vendas](https://ajuda.sankhya.com.br/hc/article_attachments/17003564251415) Acesse: Portal de Vendas >>Notas de Vendas

No lançamento de uma nota de serviço, com o serviço configurado anteriormente, preencha o campo "**Cód. da Obra**" e **"Cód. Art**"  no cabeçalho da nota. Caso não esteja visualizando o campo, disponibilize o campo através do Configurador de layout de nota.

- Quando seu conteúdo está vazio, o 'Tipo de Inscrição do Estabelecimento' é igual a '1-CNPJ';
- Quando seu conteúdo está preenchido, o 'Tipo de Inscrição do Estabelecimento' é igual a '4-CNO';

**Observação:** para os lançamentos de NFS-e's já confirmados e que não possuem o Cod. da Obra preenchidos, não é possível ajustar via sistema.

![Imagem 6: Acesse: Livros Fiscais » Conexão » Reinf » EFD - Reinf e após os ajustes, transmita novamente o Reinf.](https://ajuda.sankhya.com.br/hc/article_attachments/17003586287639) Acesse: Livros Fiscais » Conexão » Reinf » EFD - Reinf e após os ajustes, transmita novamente o Reinf.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17003564254743)CAUSA:**

Ocorre quando temos as seguintes situações:

![Imagem 8: Campo "Tipo de Inscrição do Estabelecimento" igual a '1-CNPJ' e campo "Indicativo de Prestação de Serviço em Obra"…](https://ajuda.sankhya.com.br/hc/article_attachments/17003586283671) Campo **"Tipo de Inscrição do Estabelecimento"** igual a '1-CNPJ' e campo **"Indicativo de Prestação de Serviço em Obra"** igual a '1 - Obra de Construção Civil - Empreitada Total' ou '2 - Obra de Construção Civil - Empreitada Parcial'.

![Imagem 9: Campo Tipo de Inscrição do Estabelecimento igual a '4-CNO' e campo Indicativo de Prestação de Serviço em Obra igual a…](https://ajuda.sankhya.com.br/hc/article_attachments/17003564251415) Campo Tipo de Inscrição do Estabelecimento igual a '4-CNO' e campo Indicativo de Prestação de Serviço em Obra igual a '0 - Não é obra de construção civil ou não está sujeita a matrícula de obra'.

**![Imagem 10: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17003586292631) OBSERVAÇÃO:**

Incidência nos eventos:

R-2010 - Retenção Contribuição Previdenciária - Serviços Tomados

R-2020 - Retenção Contribuição Previdenciária - Serviços Prestados
