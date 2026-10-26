---
id: "17914376850455"
titulo: "XML não sendo baixado automaticamente no Portal de Importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17914376850455-XML-n%C3%A3o-sendo-baixado-automaticamente-no-Portal-de-Importa%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:52:59Z"
rotulos: ["CT-e", "Configuração", "NF-e", "XML", "Atualização", "Importação", "SEFAZ", "Rotinas", "XML não sendo baixado automaticamente no Portal de Importação", "Gestão de Eventos DFes Recebidos", "Tela Comercial", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# XML não sendo baixado automaticamente no Portal de Importação

**MENSAGEM**

O **"Portal de Importação"** de XML não baixa automaticamente as notas fiscais eletrônicas (NF-e) e conhecimentos de transporte eletrônicos (CT-e). As notas fiscais emitidas contra os CNPJs da empresa não são importadas automaticamente. A consulta manual através do **"Botão Consultar Documentos"** importa os documentos, porém muitas vezes sem o arquivo XML, gerando divergências no portal.

**SITUAÇÃO**

Ao acessar o **"Portal de Importação"** (Comercial >> Rotinas >> Portal de Importação), não são localizados os XMLs importados pelo DFe. Problemas específicos foram identificados após atualizações do sistema. Ao verificar a tela **"Configuração MF-e/DF-e"** (Comercial >> Rotinas>> Configuração MF-e/DF-e), confirma-se que nenhuma nota foi importada automaticamente.

**SOLUÇÃO**

**(1)Verificação de configurações:** Acesse a tela **"Configuração MD-e/DF-e"** (Comercial >> Arquivo >> Manifesto de Destinatários >> Configuração MD-e/DF-e) e verifique se os intervalos de consulta estão configurados corretamente (sugestão: 62 min para NF-e/CT-e e 125 min para Download).
Intervalo Consulta NF-e em minutos: 62
Intervalo Consulta CT-e em minutos: 62
Intervalo Download em minutos: 125

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17914646048919)

**(2)Atualização do sistema:** Realize a atualização do sistema para a versão 4.35b353 (Caso sua versão seja abaixo ou igual a versão do erro) ou superior, onde o problema da O.S. 6704686 foi corrigido. Realize a atualização primeiro em ambiente de teste para validação. Se utiliza banco em nuvem, solicite a atualização à empresa responsável.

**(3)Análise na gestão de eventos:** Acesse a tela **"Gestão de Eventos DFes Recebidos"** (Comercial >> Rotinas >> Gestão de Eventos DFes Recebidos). Filtre pela coluna SCHEMA (ex: resNFe\_v1.01.xsd) para identificar erros específicos. Se necessário, ative o parâmetro **"DFEMODODEBUG"** (Configurações >> Avançado >> Preferências) para análise de log detalhada.

**(4)Correção via banco de dados:** Caso a falha seja estrutural (ex: campos obrigatórios não permitindo nulo em tabelas como TGFIXN ou inconsistência na tabela TGFMDELOG), compare a estrutura da tabela com uma base funcional e realize os ajustes necessários (ex: permissão de nulos nos campos CHAVEACESSO, DHIMPORT, NUMNOTA, TIPO, XML).

**(6)Finalização e alternativas:** Após ajustes via banco, reinicie a Unidade de Dados da tabela e, na tela **"Gestão de Eventos DFes Recebidos"**, selecione os registros com erro e clique no **"Botão Processar"**. Caso o problema persista, tente reiniciar o servidor do sistema, pois os Jobs de importação podem não estar sendo executados automaticamente.

**CAUSA**

- Erros em versões anteriores à 4.35b353 (com destaque para as versões 4.35b347 e 4.35b348) que afetam a integração com MD-e e impedem a execução dos Jobs.
- Inconsistências em tabelas do banco de dados (ex: TGFDFEER, TGFIXN, TGFMDELOG) que bloqueiam o processamento dos eventos.
- Consumo indevido de consultas na SEFAZ devido ao uso simultâneo de outras ferramentas de consulta, gerando conflitos no MD-e.
