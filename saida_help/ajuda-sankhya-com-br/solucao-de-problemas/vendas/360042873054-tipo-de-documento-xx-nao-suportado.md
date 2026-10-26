---
id: "360042873054"
titulo: "Tipo de Documento XX não suportado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042873054-Tipo-de-Documento-XX-n%C3%A3o-suportado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:12Z"
rotulos: ["CORE_E02734", "Configuração", "NF-e", "XML", "SEFAZ", "TOP", "CORE_E03971", "Verifique status NF-e ajuste 'Modelo do Documento' para 55", "Tipo de Documento XX não suportado", "Incidente com Modelo do Documento = 01 na geração do XML", "Erro"]
---

# Tipo de Documento XX não suportado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16109113269015) MENSAGEM:**

[CORE\_E02734] Tipo de Documento XX não suportado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16109147486871) SOLUÇÃO:**

![Imagem 3: Realize um filtro nos "Portais (Vendas/Compras/Mov.Interna)" para o respectivo período de geração dos arquivos XML, e…](https://ajuda.sankhya.com.br/hc/article_attachments/16109147495063) Realize um filtro nos **"Portais (Vendas/Compras/Mov.Interna)"** para o respectivo período de geração dos arquivos XML, e através da coluna Status NF-e identifique as notas com o **status DENEGADA**;

![Imagem 4: Verifique o Cód. 'Tipo de Operação' utilizado no lançamento denegado;](https://ajuda.sankhya.com.br/hc/article_attachments/16109663490711) Verifique o Cód. 'Tipo de Operação' utilizado no lançamento denegado;

![Imagem 5: Acesse a tela " Tipos de Operação - TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros) , vá até a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/16109113280791) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros), vá até a aba **"NF-e/NFC-e/CF-e"** observe o campo **'Modelo do Documento'**. Ele deve ser ajustado para **55- Nota Fiscal Eletrônica:**

![Imagem 6: Acesse a tela " Tipos de Operação - TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros) , vá até a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/14535251002647)

![Imagem 7: Vale ressaltar que o ajuste acima impedirá que esse incidente aconteça para os próximos lançamentos. Para o lançamento…](https://ajuda.sankhya.com.br/hc/article_attachments/16109147505943) **Vale ressaltar que** o ajuste acima impedirá que esse incidente aconteça para os próximos lançamentos. Para o lançamento atual, após correção da TOP, entre em contato com o Service Desk para ajuste dessa informação retroativa via banco.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16109147515799) CAUSA:**

Mensagem apresentada na geração do arquivo XML para lançamentos com Modelo do Documento = 01;
