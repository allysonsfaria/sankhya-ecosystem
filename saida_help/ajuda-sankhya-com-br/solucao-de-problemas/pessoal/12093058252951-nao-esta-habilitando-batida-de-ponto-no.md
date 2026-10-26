---
id: "12093058252951"
titulo: "Não está habilitando batida de ponto no App e no portal Pessoas +"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12093058252951-N%C3%A3o-est%C3%A1-habilitando-batida-de-ponto-no-App-e-no-portal-Pessoas"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:17:02Z"
rotulos: ["Configuração", "Folha", "Sindicato", "Habilitação de Batida de Ponto no App e Portal", "Pessoal+", "Ponto Eletrônico"]
---

# Não está habilitando batida de ponto no App e no portal Pessoas +

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19276767204759) SITUAÇÃO:**

Não esta habilitando batida de ponto no App Pessoas + e nem no Portal Pessoas +.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19276767208727) CAUSA:**

Trata-se do comportamento do sistema com a configuração da opção "Utiliza Registro Eletrônico de Ponto Alternativo" (PONTOANTERNATIVO) do sindicato do funcionário (TFPSIN) desabilitada.
esse comportamento foi implementado na OS: 3584108 - Validação para liberação de Batidas de Ponto - Portaria 671 - Implementação, onde se encontra a documentação.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19276767211543) SOLUÇÃO:**

Verifique qual o SINDICATO do colaborador
Entre no cadastro do SINDICATO e verifique o campo **'Utiliza Registro Eletrônico de Ponto Alternativo'** este campo tem que estar marcado para que seja habilitado a opção de bater o ponto no portal e no APP Pessoas +.

No Pessoal +/W>> Pessoal+ » Cadastros » Sindicato

![Imagem 4: No Pessoal +/W>> Pessoal+ » Cadastros » Sindicato](https://ajuda.sankhya.com.br/hc/article_attachments/19276773354391)

No MGE Pessoal >> Arquivos/ Cadastros/ Sindicatos

![Imagem 5: No MGE Pessoal >> Arquivos/ Cadastros/ Sindicatos](https://ajuda.sankhya.com.br/hc/article_attachments/19276767223575)
