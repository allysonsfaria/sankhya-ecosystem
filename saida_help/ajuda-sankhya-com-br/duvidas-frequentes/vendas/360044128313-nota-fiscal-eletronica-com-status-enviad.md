---
id: "360044128313"
titulo: "Nota Fiscal Eletrônica com status 'Enviada'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044128313-Nota-Fiscal-Eletr%C3%B4nica-com-status-Enviada"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-09-29T18:19:47Z"
rotulos: ["ERRONF", "DUVIDANF", "#PUBLIFER", "#revisadoclaudio", "Consulta", "NF-e", "Portal de Vendas", "SEFAZ", "Consulte a situação na SEFAZ", "Se o status não mudar contate o suporte", "Status \"Enviada\" na NF-e", "Erro", "Documentos Eletrônicos"]
---

# Nota Fiscal Eletrônica com status 'Enviada'

Esse documento tem por objetivo detalhar a causa/tratativa de Nota Fiscal Eletrônica onde a coluna **"STATUS NF-E"** no [**"Portal de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) encontra-se como **"Enviada"** (STATUSNFE = I).

![Imagem 1: Através da chave NF-e gerada para a respectiva nota, acesse o site da SEFAZ NACIONAL e realize a Consulta dessa:](https://ajuda.sankhya.com.br/hc/article_attachments/16105954913687) Através da chave NF-e gerada para a respectiva nota, acesse o site da SEFAZ NACIONAL e realize a Consulta dessa:

- [Link consulta chave NF-e](http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=)

![Imagem 2: Repita a consulta através da opção “Portais Estaduais da NF-e” , selecionando o Estado da empresa emissora e buscando a…](https://ajuda.sankhya.com.br/hc/article_attachments/16105954918167) Repita a consulta através da opção **“Portais Estaduais da NF-e”**, selecionando o Estado da empresa emissora e buscando a opção de consulta NF-e por chave de acesso.

![Imagem 3: Caso a respectiva NF-e esteja AUTORIZADA nos ambientes acima:](https://ajuda.sankhya.com.br/hc/article_attachments/16105954920215) Caso a respectiva NF-e esteja AUTORIZADA nos ambientes acima:

- Selecione a nota no Portal de Vendas, no botão **"NF-e"** selecione a opção “**Consulta situação atual da nota**”, será exibida uma caixa de diálogo, informando que a situação da nota no sistema está diferente da situação atual da SEFAZ, clique em sim e confira a mudança do Status Enviada para APROVADA.

![Imagem 4: Caso a respectiva NF-e esteja 'INEXISTENTE' nos ambientes citados.](https://ajuda.sankhya.com.br/hc/article_attachments/16105984948887) Caso a respectiva NF-e esteja 'INEXISTENTE' nos ambientes citados.

- Através do Botão NF-e » **“Consulta status do serviço”** verifique se é retornado algum erro, em caso positivo busque por esse em nossa Central de Ajuda e siga com as orientações para solução. Em caso negativo, siga com as orientações a seguir.
- Após as verificações acima será necessário executar uma das duas ações abaixo para verificar se esse status nota é atualizado.

1. NF-E » Consulta situação atual da nota.
2. NF-e » Gerar Lote.

A primeira opção pode ser utilizada, pois quando realizada a consulta de situação de uma nota marcada no sistema como ENVIADA o sistema tentará enviar a nota à SEFAZ.

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17854518410775) IMPORTANTE:**

Após 24 horas, se diante geração de lote e/ou consulta situação atual da nota, mantido esse Status ENVIADA, acione o Service Desk Sankhya para análise do log de envio dessa nota.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16105954925719) CAUSA:**

Caso tenha sido gerado o lote de uma nota e houver alguma falha na comunicação com a SEFAZ, a nota não será processada, logo sua situação ficará como ENVIADA. O que difere esse STATUS do Status NF-e Aguardando Autorização é que para 'Enviada' não temos nenhuma evidência (nRec) de que a SEFAZ recebeu esse documento.
