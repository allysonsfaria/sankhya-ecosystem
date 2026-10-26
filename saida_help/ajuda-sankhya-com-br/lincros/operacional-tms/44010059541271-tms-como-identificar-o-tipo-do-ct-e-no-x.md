---
id: "44010059541271"
titulo: "[TMS] - Como identificar o tipo do CT-e no XML (tag tpCTe) e por que ele foi importado como Normal ou Complementar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010059541271--TMS-Como-identificar-o-tipo-do-CT-e-no-XML-tag-tpCTe-e-por-que-ele-foi-importado-como-Normal-ou-Complementar"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:29:25Z"
rotulos: ["sync_hc", "lincros", "sync_hash_b5b3d6ef112e", "lincros_17269571"]
---

# [TMS] - Como identificar o tipo do CT-e no XML (tag tpCTe) e por que ele foi importado como Normal ou Complementar

**Menu**: Para consultar o CT-e > Documentos eletrônicos > CT-es
Para importar/reimportar o CT-e > Operacional > Importação > CT-e > Importação

**Objetivo**: Explicar como o TMS define o tipo do CT-e (Normal, Complemento de Valores, Anulação ou Substituto) na importação e como conferir esse campo no XML quando o CT-e foi emitido como um tipo, mas foi importado como outro.

**Considerações**:

- Possuir o CT-e importado no TMS e o arquivo XML correspondente;
- O tipo exibido no TMS (aba 'Cadastro' do CT-e, campo 'Tipo') difere do tipo com o qual a transportadora informa ter emitido o documento.

## Como o TMS define o tipo do CT-e

Na importação, o tipo é lido da tag **<tpCTe>**, dentro do bloco **<ide>** do XML. O TMS não interpreta o nome do tipo informado pela transportadora em outros sistemas; ele considera apenas o código dessa tag:

- **0** — CT-e Normal;
- **1** — CT-e de Complemento de Valores (complementar);
- **2** — CT-e de Anulação;
- **3** — CT-e Substituto.

Se a tag trouxer um código desconhecido, a importação apresenta erro.

## Como conferir no XML

1. Acesse Documentos eletrônicos > CT-es e abra o CT-e;
2. Clique em 'Download XML'. Um arquivo zipado será baixado;
3. Extraia o arquivo e abra o XML em um editor de texto ou no navegador;
4. Localize a tag <tpCTe> dentro de <ide> e compare o código com a tabela acima.

**Exemplo**: uma transportadora emite o documento como "Complemento de Valores" no sistema de emissão dela, mas o XML traz <tpCTe>0</tpCTe>. O TMS importa o documento como CT-e Normal, porque é esse o código informado no arquivo.

## O que fazer quando o código está incorreto

A divergência está no documento emitido, não no TMS. A transportadora precisa corrigir o tipo no sistema de emissão e enviar um novo XML com o código correto. Depois, importe o novo arquivo em Operacional > Importação > CT-e > Importação.

## Observações

- CT-e de Complemento de Valores (código 1) exige que o CT-e original ao qual ele se refere já esteja importado no TMS. Veja o artigo "[Pré-conhecimento Complementar sem Normal vinculado: dois erros na importação de CT-e](https://suporte.lincros.com/pt-BR/articles/16796188-tms-pre-conhecimento-complementar-sem-normal-vinculado-dois-erros-na-importacao-de-ct-e)";
- Para CT-e de Anulação (código 2), veja o artigo "[Visualizar erros na Importação de XML de anulação de CT-e](https://suporte.lincros.com/pt-BR/articles/13433363-tms-visualizar-erros-na-importacao-de-xml-de-anulacao-de-ct-e)".

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
