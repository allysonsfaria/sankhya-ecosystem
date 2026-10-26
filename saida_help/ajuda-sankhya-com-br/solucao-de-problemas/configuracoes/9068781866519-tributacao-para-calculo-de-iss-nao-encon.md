---
id: "9068781866519"
titulo: "Tributação para cálculo de ISS não encontrada para o serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9068781866519-Tributa%C3%A7%C3%A3o-para-c%C3%A1lculo-de-ISS-n%C3%A3o-encontrada-para-o-servi%C3%A7o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:10:57Z"
rotulos: ["ISS", "Configuração", "Faturamento", "Contrato", "Faturamento de Contratos", "Impostos", "CORE_E04488", "NFS-e", "Configurações de Serviço", "Tributação de ISS", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Tributação para cálculo de ISS não encontrada para o serviço.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18882674132631) MENSAGEM:**

[CORE\_E04488] Tributação para cálculo de ISS não encontrada para o serviço.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18882681252375) SITUAÇÃO:**

Ao tentar faturar um contrato a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18882681257239) SOLUÇÃO:**

Verifique as configurações a seguir:

![Imagem 4: Acesse a tela ' Faturamento de Contratos' ( Contratos e Serviços » Rotinas » Faturamento de Contratos ) clique na opção…](https://ajuda.sankhya.com.br/hc/article_attachments/18882674151319) Acesse a tela '**Faturamento de Contratos'** (Contratos e Serviços » Rotinas » Faturamento de Contratos) clique na opção ' Configurações' e o campo 'Calcular ISS/IRF pelo Contrato' deve estar marcado (para ativar esta opção, o parâmetro IMPOSTCON deve estar habilitado);

![Imagem 5: Acesse a tela 'Cadastro de produtos' ( Configurações » Cadastros » Produtos » Serviço ) e marque o produto como…](https://ajuda.sankhya.com.br/hc/article_attachments/18882681266199) Acesse a tela **'Cadastro de produtos'** (Configurações » Cadastros » Produtos » Serviço) e marque o produto como 'SERVIÇO'.

![Imagem 6: Acesse a tela de ' Preferências da empresa' ( Comercial » Preferências » Empresa ) e confira se a aba CNAE está…](https://ajuda.sankhya.com.br/hc/article_attachments/18882681267863) Acesse a tela de '**Preferências da empresa'** (Comercial » Preferências » Empresa) e confira se a aba CNAE está preenchida com os dados da cidade.

![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/18882674169495) **IMPORTANTE:**

O parâmetro 'Buscar retenção de ISS pelo contrato?? Chave ISSRETCONTRATO' quando ativado faz a retenção de ISS sempre de acordo com a definição indicada no campo Retém ISS do contrato e nunca de acordo com a configuração indicada no cadastro do parceiro.

Na Central: Quando este parâmetro 'ISSRETCONTRATO?' estiver ligado e o parceiro de um documento for alterado, caso a nota possua um contrato vinculado, o ISS será retido ou não de acordo com o campo RETEM ISS do cadastro do contrato. Caso esteja desligado, funciona verificando o campo RETEM ISS do cadastro do parceiro.

![Imagem 8: OBSERVAÇÃO: Para mais informações sobre a rotina acesse: Faturamento de Contratos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/article_attachments/18882674179095) **OBSERVAÇÃO:**
Para mais informações sobre a rotina acesse: [Faturamento de Contratos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18882674181143)CAUSA:**

Ocorre quando as configurações do ISS não estão devidamente configuradas.
