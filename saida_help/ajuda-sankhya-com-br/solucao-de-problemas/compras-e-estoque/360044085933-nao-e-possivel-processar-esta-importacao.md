---
id: "360044085933"
titulo: "Não é possível processar esta importação, pois ela não possui XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044085933-N%C3%A3o-%C3%A9-poss%C3%ADvel-processar-esta-importa%C3%A7%C3%A3o-pois-ela-n%C3%A3o-possui-XML"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:06Z"
rotulos: ["#criadoRoger", "#revisadohugo", "CORE_E00237", "Configuração", "NF-e", "XML", "Importação", "SEFAZ", "CORE_E00240", "Configuração MD-e/DF-e", "Problema na Importação sem XML", "Erro"]
---

# Não é possível processar esta importação, pois ela não possui XML

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16107921883031) MENSAGEM**:

[CORE\_E00237] Não é possível processar esta importação, pois ela não possui XML.

[CORE\_E00240] Não é possível processar esta importação, pois ela não possui XML.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16107942708759) SOLUÇÃO**:

Considere o Comportamento da Aplicação, conforme abaixo:

![Imagem 3: Acesse a tela " Configuração MD-e/DF-e " (Caminho de acesso: Comercial » Rotinas » Configuração MD-e/DF-e)](https://ajuda.sankhya.com.br/hc/article_attachments/17854422541847) Acesse a tela **"[Configuração MD-e/DF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599234)"** (Caminho de acesso: Comercial » Rotinas » Configuração MD-e/DF-e)

Revise as configurações de MD-e/DF-e, se atentando para a marcação **"Baixar o XML ao dar ciência da operação"**.

- **Realize ciência automática**- Quando este estiver **"desmarcado"** será preciso **"Dar ciência"** em todos os XMLs baixados, de forma manual, através do Portal de Importação de XML. Considere deixá-lo marcado.

(1)** IMPORTANTE:**

Mesmo após realizar a marcação acima, para que o sistema busque o xml dos arquivos que já foram importados pela rotina, siga o processo conforme abaixo:

- Selecione o documento no Portal de Importação de XML;
- Feito isso, clique em MD-e > Ciência da Operação;
- MD-e > Download NF-e
- Realize o processamento do Arquivo

Caso existam muitos lançamentos desse tipo, o Portal de Importação de XML permite selecionar mais de uma linha e fazer as operações acima.

**NOTA**: Lembrando que a SEFAZ reserva o direito de permitir o download do XML pelo destinatário, apenas um percentual mensal. Verifique esta informação com a SEFAZ do seu Estado.

**![Imagem 4: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16107942715031) CAUSA**:

Ocorre quando se extrapola o percentual mensal de download de XML, estipulado pela SEFAZ, ou a Ciência da Operação não está automatizada, fazendo com que não seja possível processar a importação, antes de dar a ciência.
