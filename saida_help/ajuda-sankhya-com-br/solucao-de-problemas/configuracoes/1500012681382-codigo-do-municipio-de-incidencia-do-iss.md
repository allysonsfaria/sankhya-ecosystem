---
id: "1500012681382"
titulo: "Código do município de incidência do ISSQN inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012681382-C%C3%B3digo-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:24:32Z"
rotulos: ["Configuração", "Cidades", "Impostos", "não apagar", "#publicadoHyago", "[E309]", "#validadoSheyla", "Prefeituras", "NFS-e", "Problema com Código de Município do ISSQN", "Erro"]
---

# Código do município de incidência do ISSQN inválido

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16337229304087) MENSAGEM**:

Ao gerar lote NFS-e para Vitória - ES apresenta erro, E309: Código do município de incidência do ISSQN inválido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16337207881495) SOLUÇÃO:**

Informe o código do município de incidência do ISSQN com sete caracteres, conforme a tabela de municípios do IBGE.

Para o município de Vitória-ES a tag 'MunicipioIncidencia' deve constar com as mesmas informações da tag 'CodigoMunicipio'.

- A tag 'CodigoMunicipio' é configurado no cadastro de cidade em "Mun. Domicílio fiscal".

- A tag 'MunicipioIncidencia' é obtida no sistema pela seguinte regra:

![Imagem 3: Primeiro o sistema tenta buscar o valor da tabela de impostos (TGFDIN), considerando o tipo de imposto igual a 4 (ISS),…](https://ajuda.sankhya.com.br/hc/article_attachments/16337207885079) Primeiro o sistema tenta buscar o valor da tabela de impostos (TGFDIN), considerando o tipo de imposto igual a 4 (ISS), dessa forma verifique:

- Tela 'Serviços' (Configurações » Cadastros » Serviços)
- Aba **"Alíquotas de ISS"**, para a respectiva 'Cidade' certifique-se que o campo **'Cód.Trib.Municipio'** foi configurado:

![Imagem 4: Aba "Alíquotas de ISS" , para a respectiva 'Cidade' certifique-se que o campo 'Cód.Trib.Municipio' foi configurado:](https://ajuda.sankhya.com.br/hc/article_attachments/15071554463255)

![Imagem 5: Caso não existam informações para o item 1, o sistema tentar buscar o valor através das 'Configurações de Serviço por…](https://ajuda.sankhya.com.br/hc/article_attachments/16337207888407) Caso não existam informações para o item 1, o sistema tentar buscar o valor através das 'Configurações de Serviço por Empresa'.

- Tela **"Serviços"** (Caminho de acesso: Configurações » Cadastros » Serviços)
- Aba **"Configurações por Empresa"**, campo **"Cód.Trib.Municipio NFS-e":**

![Imagem 6: Aba "Configurações por Empresa" , campo "Cód.Trib.Municipio NFS-e":](https://ajuda.sankhya.com.br/hc/article_attachments/15071616279447)

![Imagem 7: Por fim, caso não esteja configurado em nenhum dos cenários acima, o sistema verifica o campo da aba "Impostos" :](https://ajuda.sankhya.com.br/hc/article_attachments/16337229331223) Por fim, caso não esteja configurado em nenhum dos cenários acima, o sistema verifica o campo da aba **"Impostos"**:

- Tela **"Serviços"** (Caminho de acesso: Configurações » Cadastros » Serviços)
- Aba **"Impostos"**, campo **'Cód.Trib.Municipio NFS-e'.**

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16337229334295) CAUSA:**

Ocorre normalmente para notas enviadas a prefeitura de Vitória/ES, Porém, pode ocorrer para outras prefeituras que exijam a TAG, 'MunicipioIncidencia' no XML.
