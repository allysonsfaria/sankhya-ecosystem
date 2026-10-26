---
id: "360043363533"
titulo: "Não é possível excluir a nota, pois já foi enviada via EPEC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043363533-N%C3%A3o-%C3%A9-poss%C3%ADvel-excluir-a-nota-pois-j%C3%A1-foi-enviada-via-EPEC"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:20Z"
rotulos: ["#PUBLIFER", "CORE_E00894", "EPEC", "NF-e", "SEFAZ", "Consulte a nota e gere lote se necessário", "Nota não pode ser excluída após EPEC", "Exclusão não permitida para notas em Contingência EPEC", "Erro", "Documentos Eletrônicos"]
---

# Não é possível excluir a nota, pois já foi enviada via EPEC

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16108882602391) MENSAGEM:**

[CORE\_E00894] Não é possível excluir a nota, pois já foi enviada via EPEC.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108870652567) SOLUÇÃO:**

Caso a nota tenha sido recebida pela SEFAZ em Contingência (EPEC), sua exclusão não será permitida. Dessa forma siga com as orientações abaixo:

![Imagem 3: Através da chave NF-e gerada para a respectiva nota, acesse o site da Sefaz Nacional e realize a consulta dessa:…](https://ajuda.sankhya.com.br/hc/article_attachments/16108870655127) Através da chave NF-e gerada para a respectiva nota, acesse o site da Sefaz Nacional e realize a consulta dessa: [Consulta chave NF-e](http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=).

![Imagem 4: Repita a consulta através da opção “Portais Estaduais da NF-e” , selecionando o Estado da empresa emissora e buscando a…](https://ajuda.sankhya.com.br/hc/article_attachments/16108882607639) Repita a consulta através da opção **“Portais Estaduais da NF-e”**, selecionando o Estado da empresa emissora e buscando a opção de **"Consulta NF-e por chave de acesso"**.

![Imagem 5: De acordo com o resultado obtido na consulta acima, realize os procedimentos recomendados:](https://ajuda.sankhya.com.br/hc/article_attachments/16108882611223) De acordo com o resultado obtido na consulta acima, realize os procedimentos recomendados:

- Nota **"Enviada em EPEC"** na SEFAZ Estadual e Nacional ou apenas na SEFAZ Estadual: Através do botão NF-e no **"Portal de Vendas/Compras"**, gere o lote desta nota. Como consequência o STATUSNFE da nota será atualizado para "**APROVADA"**.
- Caso o status seja atualizado para **"Aguardando Correção"** e/ou mantenha-se como Enviada em EPEC, acesse o botão **"Outras Opções"** » **"Ver acompanhamento"** e verifique se existe alguma rejeição impedindo sua aprovação. Em caso positivo realize as tratativas para solução do respectivo erro de validação, realizando uma nova geração de lote após ajustes.

Para mais detalhes sobre conceito e informações importantes sobre o status Enviada em EPEC, verifique o artigo [Nota Fiscal Eletrônica status 'Enviada em Ambiente de Contingência'(EPEC).Como funciona?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626354)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16108882614295)CAUSA:**

Não é permitido exclusão de notas recebidas em Contingência EPEC pela SEFAZ.
