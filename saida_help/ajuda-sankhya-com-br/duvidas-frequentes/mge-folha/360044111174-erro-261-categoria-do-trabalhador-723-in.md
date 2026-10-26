---
id: "360044111174"
titulo: "Erro 261-Categoria do trabalhador '723' incompatível com a lotação do tipo '04' e classificação tributária do empregador '99'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111174-Erro-261-Categoria-do-trabalhador-723-incompat%C3%ADvel-com-a-lota%C3%A7%C3%A3o-do-tipo-04-e-classifica%C3%A7%C3%A3o-tribut%C3%A1ria-do-empregador-99"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:32:46Z"
rotulos: ["#RevisadoLorrana", "Parceiro", "Folha", "eSocial", "Configuração Funcionários", "Categoria incompatível; lotação e tributação", "Ajuste vínculo; recalcular folha; reenviar S-1200", "Diretores estagiários e aprendizes não em tomadores", "Erro"]
---

# Erro 261-Categoria do trabalhador '723' incompatível com a lotação do tipo '04' e classificação tributária do empregador '99'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16813981371543) MENSAGEM:**

[Erro 261]: Categoria do trabalhador '723' incompatível com a lotação do tipo '04' e classificação tributária do empregador '99'.
Ação Sugerida: O valor informado no campo deverá ser compatível com a Lotação e classificação tributária do CONTRIBUINTE informada no Evento de "Informações Cadastrais do Empregador", conforme Tabela 11 (Compatibilidade entre Categoria de Trabalhadores, Classificação Tributária e Tipos de Lotação)
Elemento: /eSocial/evtRemun/dmDev/codCateg

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16814006336919) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: MGEPessoal » Lançamentos » Movimentação de Tomadores de Serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/16813981389207)  Acesse: MGEPessoal » Lançamentos » Movimentação de Tomadores de Serviço.

Para esse tipo de vínculo, retire o diretor de lotação ou use o mesmo parceiro da empresa (arquivos » cadastros » Empresas (Dados básicos), na aba **"Cadastro"**, campo **"Parceiro"**).

![Imagem 4: Posteriormente na tela de cálculo da folha, desmarque a opção "Liberado p/ envio ao E-Social" e, em seguida, marque…](https://ajuda.sankhya.com.br/hc/article_attachments/16814006343063) Posteriormente na tela de cálculo da  folha, desmarque a opção **"Liberado p/ envio ao E-Social"** e, em seguida, marque novamente. Depois gere nova transmissão do evento S-1200 para o E-social.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16813981403671) CAUSA:**

Diretores, estagiários e menor aprendiz são vínculos que não podem ser alocados em tomadores de serviços, conforme determina o manual do e-social. Dessa forma, para que o erro acima seja sanado, tais vínculos precisam ser retirados dos tomadores, ou ainda podem colocá-los no parceiro/tomador da própria empresa.
