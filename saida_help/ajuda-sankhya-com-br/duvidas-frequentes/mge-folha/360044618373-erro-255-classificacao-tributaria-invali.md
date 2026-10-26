---
id: "360044618373"
titulo: "Erro 255 - Classificação tributária inválida. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044618373-Erro-255-Classifica%C3%A7%C3%A3o-tribut%C3%A1ria-inv%C3%A1lida-Como-resolver"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:34:23Z"
rotulos: ["Configuração", "Fiscal", "eSocial", "Central do eSocial", "Campo em branco no Evento S-1000", "Classificação Tributária inválida (Código 401)", "Preencha o campo com valor da Tabela 8", "Erro"]
---

# Erro 255 - Classificação tributária inválida. Como resolver?

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16981421980439) MENSAGEM:**

401 - Conteúdo do evento inválido. Erro 255 - Classificação tributária inválida.

Ação Sugerida: O valor informado no campo deverá existir na Tabela 8 (Classificação Tributária). Elemento:/eSocial/evtInfoEmpregador/infoEmpregador/inclusao/infoCadastro/classTrib [00]

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16981421981847) SITUAÇÃO:**

Ao tentar Transmitir o arquivo do eSocial, apresenta a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16981403006615) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 4: Acesse: MGEPessoal » Arquivos » Cadastros » Empresas (Dados Básicos) Aba: "Informações Fiscais"](https://ajuda.sankhya.com.br/hc/article_attachments/16981421985687) Acesse: MGEPessoal » Arquivos » Cadastros » Empresas (Dados Básicos)
Aba: **"Informações Fiscais"**

Campo **"Classificação Tributária":**preencha com um valor válido. Para isso, busque orientações com o Contador.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16981421989783)CAUSA:**

Essa mensagem de erro de validação ocorre no retorno do Evento S-1000, quando a informação de Classificação Tributária está em branco.

**![Imagem 6: OBSERVAÇÃO: Manual Orientação do eSocial](https://ajuda.sankhya.com.br/hc/article_attachments/16981403016855) OBSERVAÇÃO:**
[Manual Orientação do eSocial](https://portal.esocial.gov.br/manuais/mos-v-2-4-02-publicada-cg.pdf)
