---
id: "44013178671383"
titulo: "[TMS] - Importação de CT-e - Erro Unidade não localizada. Possíveis causas: 1. O tomador do frete é Outros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013178671383--TMS-Importa%C3%A7%C3%A3o-de-CT-e-Erro-Unidade-n%C3%A3o-localizada-Poss%C3%ADveis-causas-1-O-tomador-do-frete-%C3%A9-Outros"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T19:50:43Z"
rotulos: ["sync_hc", "lincros", "sync_hash_3e93da5a325a", "lincros_13432841"]
---

# [TMS] - Importação de CT-e - Erro Unidade não localizada. Possíveis causas: 1. O tomador do frete é Outros

**Menu:** Operacional > Importação > CT-e > Importação

**Objetivo:** Entender o motivo desta mensagem ser apresentada ao tentar realizar a importação de um CT-e, também como, entender qual o direcionamento a ser tomado para que a importação seja efetuada com sucesso.

## Considerações:

- Possuir um xml de CT-e no qual está tentando realizar a importação;
- Possuir a tag <TOMA> informada como 4;
- Possuir o parâmetro 'importarCTeTomadorDiferenteEmpresaComMesmoCnpjXml' como 'true' vinculado aos parâmetros da empresa;

Segue abaixo os procedimentos:

Ao tentar realizar a importação de um CT-e com a tag <TOMA> = 4 através do menu Operacional > Importação > CT-e > Importação, e o parâmetro de empresa importarCTeTomadorDiferenteEmpresaComMesmoCnpjXml estiver = true, a seguinte mensagem será apresentada:

![Imagem 1: Ao tentar realizar a importação de um CT-e com a tag <TOMA> = 4 através do menu Operacional > Importação > CT-e >…](https://ajuda.sankhya.com.br/hc/article_attachments/44013178779543)

## Sobre o parâmetro de empresa

![Imagem 2: Sobre o parâmetro de empresa](https://ajuda.sankhya.com.br/hc/article_attachments/44013209529367)

O parâmetro de empresa importarCTeTomadorDiferenteEmpresaComMesmoCnpjXml = true com com que o sistema realize algumas validações;

## Caso a empresa seja um operador logístico:

Verifica se o CNPJ do EMITENTE é equivalente ao de alguma UNIDADE da empresa.

## Caso a empresa não seja operador logístico:

Verifica se o CNPJ do REMETENTE é equivalente ao de alguma UNIDADE da empresa;

ou CNPJ do EXPEDIDOR é equivalente ao de alguma UNIDADE da empresa;

ou CNPJ do RECEBEDOR é equivalente ao de alguma UNIDADE da empresa;

ou CNPJ do DESTINATÁRIO é equivalente ao de alguma UNIDADE da empresa;

Caso nenhum dos fluxos acima não encontre a unidade, é apresentado erro.

## Quando o valor de importarCTeTomadorDiferenteEmpresaComMesmoCnpjXml seja: FALSE:

Verifica se o CNPJ do TOMADOR é equivalente ao de alguma UNIDADE da empresa.

Para que essa mensagem seja corrigida e o CT-e seja importado com sucesso basta realizar a alteração desse parâmetro para 'false' (Somente usuários da Lincros podem realizar alterações nos parâmetros de empresa, portanto, é necessário acionar a nossa equipe de Helpdesk para realizar esse tipo de alteração).

Reprocessar o XML do CT-e novamente e o mesmo deverá importar com sucesso.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
