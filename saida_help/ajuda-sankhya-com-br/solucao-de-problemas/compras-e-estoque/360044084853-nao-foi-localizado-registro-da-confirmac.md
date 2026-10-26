---
id: "360044084853"
titulo: "Não foi localizado registro da confirmação da operação no MD-e para esta chave da NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044084853-N%C3%A3o-foi-localizado-registro-da-confirma%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-no-MD-e-para-esta-chave-da-NF-e"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:22Z"
rotulos: ["#PUBLIFER", "#RevisadoGilmar", "CORE_E02963", "Configuração", "NF-e", "SEFAZ", "TOP", "MD-e", "Problema de Confirmação de Operação no MD-e não Encontrada para NF-e", "Manifesto do Destinatário (MD-e)", "Erro"]
---

# Não foi localizado registro da confirmação da operação no MD-e para esta chave da NF-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16191317022743) MENSAGEM:**

[CORE\_E02963] Não foi localizado registro da confirmação da operação no MD-e para esta chave da NF-e.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16191332203671) SOLUÇÃO:**

![Imagem 3: Caso não trabalhe com validação dos eventos de MD-e (Manifesto do Destinatário), verifique a configuração abaixo no…](https://ajuda.sankhya.com.br/hc/article_attachments/16191317026583) Caso **não trabalhe** com validação dos eventos de MD-e (Manifesto do Destinatário), verifique a configuração abaixo no cadastro do 'Tipo de Operação' utilizado para o respectivo lançamento:

- Tela **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros), Aba **CT-e/MD-e**,  Campo **"Exigir confirmação do MD-e antes da confirmação":** desmarcado

![Imagem 4: Tela "Tipos de Operação - TOP" (Caminho de acesso: Comercial » Arquivo » Cadastros), Aba CT-e/MD-e , Campo "Exigir…](https://ajuda.sankhya.com.br/hc/article_attachments/14686213116439)

![Imagem 5: Realizado o ajuste acima, refaça o lançamento (essa é uma marcação histórica, assim exclua o lançamento atual e realize…](https://ajuda.sankhya.com.br/hc/article_attachments/16191317036055) Realizado o ajuste acima, refaça o lançamento (essa é uma marcação histórica, assim exclua o lançamento atual e realize outro).

![Imagem 6: Caso trabalhe com esta validação do MD-e, mantenha a configuração acima e verifique se o evento de Ciência da Operação…](https://ajuda.sankhya.com.br/hc/article_attachments/16191332206103) Caso trabalhe com esta validação do MD-e, mantenha a configuração acima e verifique se o evento de Ciência da Operação (Botão **"MD-e"** » **"Ciência da Operação"**) foi devidamente realizado para essa chave NF-e. Em caso de erros para executar essa confirmação da operação, busque possíveis soluções em nossa Central de Ajuda, persistindo acione o Service Desk Sankhya.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16191332207511) CAUSA:**

Mensagem apresentada quando configurado o 'Tipo de Operação' para exigir confirmação do MD-e antes da confirmação e essa não for executada.
