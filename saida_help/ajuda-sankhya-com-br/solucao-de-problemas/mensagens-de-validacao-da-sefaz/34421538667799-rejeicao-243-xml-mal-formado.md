---
id: "34421538667799"
titulo: "Rejeição 243: XML Mal Formado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34421538667799-Rejei%C3%A7%C3%A3o-243-XML-Mal-Formado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-30T19:35:38Z"
rotulos: ["NF-e", "XML", "SEFAZ", "Erro", "Rejeição 243", "codificação do arquivo", "erros de estruturação", "XML Mal Formado", "Documentos Eletrônicos"]
---

# Rejeição 243: XML Mal Formado

**MENSAGEM:**

[243] XML Mal Formado

**SITUAÇÃO:**

A rejeição ocorre ao tentar transmitir uma Nota Fiscal Eletrônica (NF-e) quando o arquivo XML gerado **não segue a estrutura exigida pelo Schema da SEFAZ**.

**SOLUÇÃO:**

Siga o passo a passo para corrigir a rejeição:

**(1)** Valide o arquivo XML antes de enviar: 
Utilize um validador de XML (online ou integrado ao sistema) para verificar se a estrutura está conforme o Schema da SEFAZ.

**(2)** Revise a codificação do arquivo:
Confirme que o XML está salvo em **"UTF-8 sem BOM"**.

**(3)** Evite que certos caracteres especiais estejam em sua forma pura:
Certifique-se de que caracteres como **"&"**, **"<"**, **">"** e **"aspas"** estejam **escapados corretamente, conforme a tabela abaixo:**

| Caractere | Uso no XML | Como deve ser representado no conteúdo |
| --- | --- | --- |
| `&` | Marca início de entidades XML | `&amp;` |
| `<` | Indica abertura de tag | `&lt;` |
| `>` | Indica fechamento de tag | `&gt;` |
| `"` (aspas duplas) | Delimita valor de atributo | `&quot;` |
| `'` (aspas simples) | Também pode delimitar atributo | `&apos;` |

**(4)** Corrija tags mal estruturadas:
Verifique se todas as **tags abertas foram devidamente fechadas** e se estão na **ordem correta**.

**(5)** Utilize um editor de texto ou XML adequado: 
Ferramentas como **"VS Code"**, **"Notepad++"**, **"XML Notepad"** ou sistemas de ERP confiáveis ajudam a detectar erros automaticamente.

Para saber mais como fazer essa detecção automática dos erros, acesse o artigo: [Como identificar caracteres inválidos em um XML?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616473)

**CAUSA:**

A rejeição é causada por **erros de estruturação no arquivo XML**, como tags abertas sem fechamento, caracteres inválidos, espaços em branco indevidos, sequência incorreta de elementos ou codificação errada do arquivo.
