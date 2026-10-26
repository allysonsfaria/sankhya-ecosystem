---
id: "15412927675031"
titulo: "XML de resposta do serviço 'Consulta lote RPS' com formato inesperado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15412927675031-XML-de-resposta-do-servi%C3%A7o-Consulta-lote-RPS-com-formato-inesperado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:57:00Z"
rotulos: ["Configuração", "Cidades", "XML", "CORE_E00499", "Prefeituras", "NFS-e", "Problema com Formato Inesperado na Resposta XML do Serviço “Consulta Lote RPS", "Erro"]
---

# XML de resposta do serviço 'Consulta lote RPS' com formato inesperado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16581319635991) MENSAGEM:**

[CORE\_E00499]: XML de resposta do serviço 'Consulta lote RPS' com formato inesperado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16581319639959) SOLUÇÃO:**

Verifique junto à prefeitura, a quantidade máxima de notas suportadas em um lote. Configure no parâmetro **"NFSEMAXNOTALOTE"**  o número que eles orientaram.

No campo **"Qtd. máxima de notas em um lote NFS-e"**, preencha a quantidade máxima de notas (NFS-e) em um único lote; possui a mesma funcionalidade do parâmetro **"Qtd. máxima de notas em um lote NFS-e - NFSEMAXNOTALOTE"**. Caso exista informação no campo Qtd. máxima de notas em um lote NFS-e para alguma cidade, assim como no parâmetro de chave NFSEMAXNOTALOTE, o sistema  irá considerar o campo no Cadastro da cidade em questão.

(2)** Exemplo:**

No parâmetro citado é configurado 50 e no cadastro da cidade de Araxá é configurado 30; para a cidade de Araxá será considerado o valor 30 e, para as demais cidades, o valor 50.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16581350514583) CAUSA:**

Ocorre por não informar a quantidade de notas suportadas em lote de acordo com a prefeitura no parâmetro **"NFSEMAXNOTALOTE".**
