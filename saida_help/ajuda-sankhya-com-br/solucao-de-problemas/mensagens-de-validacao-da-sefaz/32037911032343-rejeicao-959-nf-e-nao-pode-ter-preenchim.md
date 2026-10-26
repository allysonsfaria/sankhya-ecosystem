---
id: "32037911032343"
titulo: "Rejeição 959: NF-e não pode ter preenchimento de Grupo de Tributação do ICMS monofásica sobre combustíveis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32037911032343-Rejei%C3%A7%C3%A3o-959-NF-e-n%C3%A3o-pode-ter-preenchimento-de-Grupo-de-Tributa%C3%A7%C3%A3o-do-ICMS-monof%C3%A1sica-sobre-combust%C3%ADveis"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:32:10Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Rejeição 959", "sobre combustíveis", "NF-e não pode ter preenchimento", "Grupo de Tributação do ICMS monofásica", "CST Monofásico", "02 15 53 ou 61", "CST Monofásico 02 15 53 ou 61"]
---

# Rejeição 959: NF-e não pode ter preenchimento de Grupo de Tributação do ICMS monofásica sobre combustíveis

![Imagem 1: MENSAGEM](https://ajuda.sankhya.com.br/hc/article_attachments/32037916289175) **MENSAGEM**

Rejeição 959: NF-e não pode ter preenchimento de Grupo de Tributação do ICMS monofásica sobre combustíveis

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/32377347945495) SITUAÇÃO**

Foi transmitida uma NF-e com o CST - ''53  que faz parte do grupo de tributação monofásico, **''COMBUSTÍVEIS''** e o produto não está na tabela de códigos de combustíveis ou a aba **"Combustível"** da tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) não está habilitada e ou preenchida.

**![Imagem 3: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/32377363398935)SOLUÇÃO**

**(1)** **Verifique se o produto informado com código e CST Monofásico (02, 15, 53 ou 61) está devidamente cadastrado na tabela de produtos monofásicos disponibilizada pela SEFAZ**

**OBSERVAÇÃO**: A tabela de códigos de combustíveis sujeitos à tributação monofásica de ICMS está publicada no [**''Portal Nacional da NF-e''**](https://www.nfe.fazenda.gov.br) no menu **"Documentos"**, **"Diversos"**, **"Vigentes".**

(2)** Caso o produto esteja devidamente cadastrado.**Certifique-se de que esse produto está com as informações de combustível preenchidas.

**(3)** Acesse a tela **"Preferências"**(Configurações » Avançado » Preferências) e habilite o parâmetro "Combustível":

![Imagem 4: (1) Verifique se o produto informado com código e CST Monofásico (02, 15, 53 ou 61) está devidamente cadastrado na…](https://ajuda.sankhya.com.br/hc/article_attachments/32037911024535)

**(4)** Ao ativar este parâmetro, o sistema libera a aba ''Combustível'', na tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos).  **Então, faça os devidos preenchimentos desta aba.**Se ela **já estiver habilitada, garanta que esteja preenchida com as informações necessárias.**

![Imagem 5: (4) Ao ativar este parâmetro, o sistema libera a aba ''Combustível'' , na tela ''Produtos'' (Configurações » Cadastros…](https://ajuda.sankhya.com.br/hc/article_attachments/32378301057943)

**(5)** Caso o produto não esteja cadastrado na tabela oficial e não esteja sujeito à tributação monofásica, revise o CST utilizado, substituindo por código compatível com a natureza da operação.

**(6)** Acesse a tela **"Alíquotas de ICMS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS) e selecione a alíquota utilizada na operação para alterar o CST.

**(7)** Na aba **"Geral"**, altere o campo **"Tributação"** (CST) para um código adequado ao produto e à operação que não seja específico para tributação monofásica de combustíveis.

**![Imagem 6: (4) Ao ativar este parâmetro, o sistema libera a aba ''Combustível'' , na tela ''Produtos'' (Configurações » Cadastros…](https://ajuda.sankhya.com.br/hc/article_attachments/32378122850967)CAUSA**

Quando tem um **produto com código de tributação monofásica** do ICMS sobre combustíveis, esse **produto está cadastrado** **na Tabela** de códigos de combustíveis sujeitos à tributação monofásica de ICMS, **mas a aba Combústível não está habilitada e ou preenchida**.

Também quando há um **produto com código de tributação monofásica** do ICMS, porém esse produto **não está presente na Tabela** de códigos de combustíveis sujeitos à tributação monofásica de ICMS. Nestes casos não devem ser utilizados os CST de tributação monofásica sobre combustíveis (CST 02, 15, 53, 61).
