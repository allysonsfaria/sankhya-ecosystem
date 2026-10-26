---
id: "44012721120023"
titulo: "[TMS] - Conhecimento de transporte X encontrado, contudo a nota fiscal presente no arquivo de fatura não esta vinculada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012721120023--TMS-Conhecimento-de-transporte-X-encontrado-contudo-a-nota-fiscal-presente-no-arquivo-de-fatura-n%C3%A3o-esta-vinculada"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:36:28Z"
rotulos: ["sync_hc", "lincros", "sync_hash_5458cfe363b4", "lincros_13433357"]
---

# [TMS] - Conhecimento de transporte X encontrado, contudo a nota fiscal presente no arquivo de fatura não esta vinculada

**Menu**: Operacional > Importação > EDI > Importação

**Objetivo**: Como corrigir a mensagem de importação do arquivo EDI: "Conhecimento de transporte 3626755 encontrado, contudo a nota fiscal presente no arquivo de fatura não esta vinculada ao conhecimento"

**Considerações**:

- Possuir o XML da nota fiscal importada, assim como o CT-e;
- Possuir o arquivo EDI de cobrança importado com esta mensagem de erro na importação;

Abaixo segue os procedimentos:

1. Verificar qual o número de série da Nota Fiscal que consta no arquivo EDI;

![Imagem 1: Verificar qual o número de série da Nota Fiscal que consta no arquivo EDI;](https://ajuda.sankhya.com.br/hc/article_attachments/44012707592343)

2. Verificar no Ct-e qual o número de série;

![Imagem 2: 2. Verificar no Ct-e qual o número de série;](https://ajuda.sankhya.com.br/hc/article_attachments/44012707755799)

3. No exemplo acima, o número de série da nota fiscal é '7' e o número de série do CT-e é '1'. Para que a situação seja normalizada, é necessário que o cliente solicite para a transportadora que a mesma emita um nov EDI com o número de série correto e após, importe novamente para o sistema;

**Obs.:**Neste caso, quando o sistema começa a processar o EDI, ele valida tanto a nota fiscal quanto o Ct-e. Se as informações da nota fiscal não baterem no que é enviado no EDI, por exemplo, o sistema não encontra. O mesmo vale para o CT-e.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
