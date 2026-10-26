---
id: "30873703633431"
titulo: "Ocorreu um erro no servidor do governo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30873703633431-Ocorreu-um-erro-no-servidor-do-governo"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:34:35Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "FIN_E00502", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Ocorreu um erro no servidor do governo", "URLs para Serviços", "Cód. Unidade Federativa", "Erro", "Documentos Eletrônicos"]
---

# Ocorreu um erro no servidor do governo

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30873711886871) **MENSAGEM:**

[FIN\_E00502] Ocorreu um erro no servidor do governo.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30873711887255)SOLUÇÃO:**

Verifique na tela **"URLs para Serviços"** (Caminho: Livros Fiscais » Conexão » URLs para Serviços) se há um cadastro com o código **0 (zero),** no campo **"Cód. Unidade Federativa"** e se a configuração está correta. O sistema interpreta o código 0 (zero) como uma definição válida para todas as unidades federativas (UFs).

![Imagem 3: Verifique na tela " URLs para Serviços" ( Caminho: Livros Fiscais » Conexão » URLs para Serviços ) se há um cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/30873703630231)

As URLs a serem utilizadas são as seguintes:

**Homologação**

- **Recepção:** <https://www.testegnre.pe.gov.br/gnreWS/services/GnreLoteRecepcaoConsulta>
- **Consulta:** <https://www.testegnre.pe.gov.br/gnreWS/services/GnreResultadoLote>

**Produção**

- **Recepção:** <https://www.gnre.pe.gov.br/gnreWS/services/GnreLoteRecepcaoConsulta>
- **Consulta:** <https://www.gnre.pe.gov.br/gnreWS/services/GnreResultadoLote>

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30873711888279)CAUSA:**

Ocorre quando não existe uma configuração com o código **0** na tela Urls para Serviços ou quando a Url inserida está incorreta.
