---
id: "39338396167959"
titulo: "Como incluir informações personalizadas no XML do CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39338396167959-Como-incluir-informa%C3%A7%C3%B5es-personalizadas-no-XML-do-CT-e"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-10-08T14:29:05Z"
rotulos: ["CT-e", "Configuração", "XML", "SEFAZ", "Artigo criado KCS", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# Como incluir informações personalizadas no XML do CT-e

O sistema Sankhya permite incluir informações adicionais no XML do CT-e por meio de configurações e campos específicos disponíveis no lançamento do documento.

#### **(1)**Utilizar o parâmetro QUEINFADCXMLCTE

Uma das formas de incluir informações adicionais no XML do CT-e é utilizar o parâmetro **"Consulta para informação adicional no XML do CTe - QUEINFADCXMLCTE"**. Esse parâmetro permite configurar uma consulta SQL personalizada para incluir informações nas tags `<ObsCont xCampo="">` e `<xTexto>` do XML.

**Passos para configuração:**

**(1)** Acesse as configurações de parâmetros do sistema (Configurações » Avançado » Preferências).

**(2)** Localize o parâmetro **"QUEINFADCXMLCTE"**.

**(3)** Configure uma consulta SQL que retorne as informações desejadas.

 **Exemplo de consulta:**

`SELECT`
`'NUMERO_PEDIDO' AS XCAMPO,`
`PEDIDO.NUMPEDIDO AS XTEXTO`
`FROM TGFCAB`
`JOIN PEDIDO ON TGFCAB.NUNOTA = PEDIDO.NUNOTA`
`WHERE TGFCAB.NUNOTA = :NUNOTA`

Esta consulta irá gerar no XML algo como:

`<ObsCont xCampo="NUMERO_PEDIDO">`
`<xTexto>12345</xTexto>`
`</ObsCont>`

####

#### **(1)**Campos específicos para características adicionais

No lançamento do CT-e, existem campos específicos que geram tags XML personalizadas:

- Os campos **“Característica Adicional do Transporte”** e **“Característica Adicional do Serviço”** geram, respectivamente, as tags `<xCaracAd>` e `<xCaracSer>` no XML, dentro do grupo `Compl`.
- Quando o parâmetro **CTEADDTAGXEMI** estiver habilitado, o nome do usuário emissor do documento será incluído na tag `<xEmi>`.

#### **(1)**Observações importantes

- As alterações nas tags XML devem seguir o padrão estabelecido pela SEFAZ para evitar rejeições.
- Teste a solução gerando um XML para conferência antes de emitir o CT-e oficialmente.
- Para verificar se as informações estão sendo corretamente incluídas, utilize a opção **"Gerar arquivo XML do CT-e para conferência"** disponível no sistema.
- As configurações devem estar em conformidade com os requisitos fiscais vigentes.

Essas configurações permitem incluir no XML dos CT-es as informações internas necessárias, de forma adequada e em conformidade com os requisitos fiscais aplicáveis.
