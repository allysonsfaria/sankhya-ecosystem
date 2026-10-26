---
id: "16645154941591"
titulo: "Erro na geração/envio do evento S-2240"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16645154941591-Erro-na-gera%C3%A7%C3%A3o-envio-do-evento-S-2240"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:17:37Z"
rotulos: ["Eventos", "Fiscal", "eSocial", "Configuração Funcionários", "Finalize o ambiente anterior antes de cadastrar o novo", "Funcionários cadastrados em múltiplos ambientes no mesmo período", "Erro na geração do evento S-2240 do eSocial", "Erro 1829", "Ambiente de Trabalho", "Erro na geração/envio", "Erro", "Central de Projetos"]
---

# Erro na geração/envio do evento S-2240

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16645111767959) MENSAGEM:**

Erro 1829 - Somente é permitido informar mais de um grupo de ambiente de trabalho [infoAmb] no caso de trabalhador avulso (código de categoria no RET igual a [2XX]). Elemento: /eSocial/evtExpRisco/infoExpRisco [] -----------------------------------Erro 632 - Já existe no evento um grupo com mesma chave de identificação. Elemento: /eSocial/evtExpRisco/infoExpRisco/infoAmb[2] [ nao localizado ]

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33229316703511) SITUAÇÃO:**

Ao tentar enviar o evento S-2240 (Condições Ambientais do Trabalho – Fatores de Risco), ocorre um erro durante o processo de envio

![Imagem 3: Ao tentar enviar o evento S-2240 (Condições Ambientais do Trabalho – Fatores de Risco), ocorre um erro durante o…](https://ajuda.sankhya.com.br/hc/article_attachments/33229287852695)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16645126548247) CAUSA:**

O erro ocorre devido a uma configuração incorreta na tela **"Configuração Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários), especificamente na aba **"Ambiente de Trabalho"**, onde foram atribuídos dois ambientes simultaneamente ao mesmo colaborador.

Conforme as diretrizes do Manual de Orientação do eSocial (**MOS**), cada trabalhador deve estar vinculado a apenas um ambiente de trabalho por vez. A duplicidade de registros nessa aba viola essa regra, gerando uma inconsistência que impede o correto processamento das informações pelo sistema e, consequentemente, o envio do evento ao eSocial.

![Imagem 5: Conforme as diretrizes do Manual de Orientação do eSocial ( MOS ), cada trabalhador deve estar vinculado a apenas um…](https://ajuda.sankhya.com.br/hc/article_attachments/33229287855895)

**![Imagem 6: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16674213366679) SOLUÇÃO:**

É necessário revisar e corrigir a configuração do funcionário, mantendo apenas um único ambiente de trabalho ativo na aba Ambientes de Trabalho, conforme estabelecido pela legislação vigente e pelas diretrizes do Manual de Orientação do eSocial (MOS).
