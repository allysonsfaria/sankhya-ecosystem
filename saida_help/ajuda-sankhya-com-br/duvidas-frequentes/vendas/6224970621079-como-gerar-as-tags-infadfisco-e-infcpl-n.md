---
id: "6224970621079"
titulo: "Como gerar as tags INFADFISCO e INFCPL nas notas fiscais eletrônicas?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6224970621079-Como-gerar-as-tags-INFADFISCO-e-INFCPL-nas-notas-fiscais-eletr%C3%B4nicas"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-08-04T12:27:11Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "#validadoSilvio", "Gerar tags INFADFISCO e INFCPL", "Início e fim", "Preferências e observações", "Documentos Eletrônicos"]
---

# Como gerar as tags INFADFISCO e INFCPL nas notas fiscais eletrônicas?

As **Tags** são rótulos identificados por uma chave (<), indicando a inicialização de uma função no software. Por conseguinte, o encerramento de algumas tags é demarcado com o fechamento da chave (>). Ainda assim, existem as que não são encerradas com esse caractere, pois o próprio método já declara o fim da função.

Para gerar as tags INFADFISCO e INFCPL, siga o demostrado abaixo: 

- Para **INFADFISCO,** habilite o parâmetro **"ENVOBSPADNFE"** na tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)**" e informe o seu conteúdo no campo **"Observação padrão"**  (seja no cabeçalho da nota ou no próprio item);
- Para **INFCPL,** habilite o parâmetro **"ENVOBSNFE"** na tela Preferências e informe o seu conteúdo no campo **"Observação"** (seja no cabeçalho da nota ou no próprio item);

O grupo da tag <infAdic> recebe a tag <infAdFisco>, acolhe o conteúdo das observações padrão informada no cabeçalho do documento, que é previamente cadastrado na tela **"[Observações da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474)"**: (Caminho de acesso: Comercial » Arquivo » Cadastros » Observações para Notas), informação padrão apresentada nos itens de documento que tem origem na **"[Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)"**: (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS) e o modelo vinculado na Top é utilizado no preenchimento da tag infCPL, campo **"Modelo para Dados Adicionais de NF-e",** na tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

Deve atentar-se também a modelos personalizados pré-existentes.
