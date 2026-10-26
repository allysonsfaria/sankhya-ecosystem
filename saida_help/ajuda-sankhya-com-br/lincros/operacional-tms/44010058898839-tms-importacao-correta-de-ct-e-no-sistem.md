---
id: "44010058898839"
titulo: "[TMS] - Importação Correta de CT-e no Sistema TMS: Como Garantir a Inclusão da Chave e XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010058898839--TMS-Importa%C3%A7%C3%A3o-Correta-de-CT-e-no-Sistema-TMS-Como-Garantir-a-Inclus%C3%A3o-da-Chave-e-XML"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:29:20Z"
rotulos: ["sync_hc", "lincros", "lincros_13439322", "sync_hash_c0ad317a849a"]
---

# [TMS] - Importação Correta de CT-e no Sistema TMS: Como Garantir a Inclusão da Chave e XML

## Problema Relatado pelo Cliente:

O cliente informou que os arquivos de CT-e (Conhecimento de Transporte Eletrônico) estão sendo apresentados no sistema TMS sem a chave do CT-e. E também não está sendo possível realizar o download do XML do CT-e.

## Quando este artigo NÃO se aplica

Este passo a passo vale apenas para CT-es que **já existem no TMS** (aparecem em Documentos eletrônicos > CT-es), mas sem chave e sem XML. Se o CT-e não aparece no TMS e também não há nenhuma linha correspondente no log de importação, o arquivo provavelmente não chegou ao sistema — reimportar não resolve a causa. Nesse caso, consulte o artigo "CT-e enviado pela transportadora não aparece no TMS e não há registro no log de importação".

## Passo a Passo para Resolver o Problema:

**1. Verificação do Método de Importação:**

- O primeiro passo é verificar como os CT-es estão sendo importados no sistema. Isso é crucial, pois o processo de importação varia conforme o tipo de arquivo.

**2. Importação via EDI CONEMB:**

- Se os CT-es estão sendo importados via \*\*EDI CONEMB\*\*, neste modelo de importação o CT-e não registra a chave nem mantém o XML no sistema.

**Por quê?** A opção **EDI CONEMB** é projetada para importação de Notas Fiscais de Serviço, que não possuem chave nem XML para download, sendo este o motivo pelo qual essas informações não aparecem.

**3. Importação Correta de CT-es que não são de Serviço:**

- Para CT-es que não são do tipo serviço (ou seja, CT-es de transporte de carga), a importação deve ser feita utilizando o caminho Operacional > Importação > CT-e > Importação.
- Certifique-se de que o arquivo CT-e está sendo importado neste caminho, o que irá registrar a chave do CT-e e manter o XML para futuras consultas e downloads.

**4. Reimportação de CT-e do tipo Normal que não contém chave nem XML:**

- Caso o CT-e tenha sido inicialmente importado via EDI CONEMB, é possível realizar a reimportação do mesmo CT-e utilizando o caminho correto: Operacional > Importação > CT-e > Importação.
- Após a reimportação, o sistema deve exibir corretamente a chave do CT-e e o XML associado.

**5. Validação Final:**

- Após seguir os passos acima, valide se o CT-e agora está com a chave corretamente exibida e o XML disponível para download no sistema.
