---
id: "360043062833"
titulo: "Informado NCM inexistente[nItem:nnn] (2015/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043062833-Informado-NCM-inexistente-nItem-nnn-2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:08Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "NCM", "ncm inexistente", "778", "Rejeição [778] - NCM inexistente", "Ajuste código NCM no cadastro do produto", "NCM não existe na tabela MDIC", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Informado NCM inexistente[nItem:nnn] (2015/002)

**MENSAGEM**

[778 - Rejeição]: Informado NCM inexistente [nItem:nnn]

**SITUAÇÃO**

Durante a emissão da nota fiscal eletrônica (NF-e ou NFC-e), ao tentar confirmar ou transmitir o documento, o sistema apresenta a rejeição 778, indicando que o código NCM informado no item da nota não existe ou não está mais válido na tabela oficial da Receita Federal. Esta rejeição bloqueia o processamento e a autorização da nota.

**SOLUÇÃO**

Para corrigir a rejeição 778, siga os passos abaixo:

Identifique o item com NCM incorreto: Caso a NF-e possua múltiplos itens, utilize a tela **"Portal de Vendas"** (Comercial >> Consulta), selecione a nota, clique em **"NF-e"** >> **"Gerar XML da NF-e em arquivo para Conferência"**. Abra o XML em um editor de texto e utilize a busca (Ctrl+F) pelo termo 'nItem' para localizar o item apontado na rejeição.

Consulte a validade do NCM: Acesse o portal oficial da Receita Federal (<https://portalunico.siscomex.gov.br/classif/#/sumario?perfil=publico)> ou utilize os links de consulta fornecidos nas observações abaixo para verificar se o código NCM foi desativado ou substituído.

Atualize o cadastro no sistema: Acesse a tela **"Produtos"** (Configurações >> Cadastros >> Produtos >> Produtos), localize o item identificado, acesse a aba **"Geral"** e altere o campo **"NCM"** pelo código válido encontrado na consulta.

Reenvie a nota: Retorne à tela **"Central de Vendas"** (Comercial >> Central de Vendas), exclua o item antigo da nota e insira-o novamente para que o sistema capture o **"NCM"** atualizado. Realize a transmissão da nota fiscal.

**CAUSA**

A rejeição ocorre quando o código **"NCM"** informado no item da nota não existe na tabela oficial da Receita Federal ou foi desativado ou substituído. A Nomenclatura Comum do Mercosul passa por atualizações periódicas e, quando o cadastro do produto está defasado, a SEFAZ bloqueia a autorização.

**OBSERVAÇÕES:**

[Consulta NCM SEFAZ](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=)

[Tabela TIPI Oficial](http://receita.economia.gov.br/acesso-rapido/legislacao/documentos-e-arquivos/tipi-1.pdf/view)

Tabela NCM Nota Técnica 2016.003 (Vigência 01/04/2022): [Link](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=&AspxAutoDetectCookieSupport=1)
