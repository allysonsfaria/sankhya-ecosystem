---
id: "360043104973"
titulo: "cvc-type.3.1.3: The value 'XXXXXXXXX.XX-XX' of element 'IE' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043104973-cvc-type-3-1-3-The-value-XXXXXXXXX-XX-XX-of-element-IE-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:03Z"
rotulos: ["ERRONF", "#RevisadoGui", "#RevisadoCarmen", "Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "Corrigir IE empresa/parceiro", "Inscrição Estadual inválida", "Consultar Sintegra e ajustar cadastro", "Erro"]
---

# cvc-type.3.1.3: The value 'XXXXXXXXX.XX-XX' of element 'IE' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16484654010519) MENSAGEM:**

cvc-pattern-valid: Value 'XXXXXXXXX.XX-XX' is not facet-valid with respect to pattern '[0-9]{2,14}' for type '#AnonType\_IE'.
cvc-type.3.1.3: The value 'XXXXXXXXX.XX-XX' of element **'IE' is not valid.**

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16484654014999) SOLUÇÃO:**

![Imagem 3: Verifique na mensagem de rejeição retornada, se o valor indicado após o 'the value' , que neste caso foi…](https://ajuda.sankhya.com.br/hc/article_attachments/16484665082263) Verifique na mensagem de rejeição retornada, se o valor indicado após o 'the value' , que neste caso foi 'XXXXXXXXX.XX-XX', se refere ao**IE da Empresa ou do 'Parceiro'**(Considere também parceiro 'Transportadora').

![Imagem 4: Acesse: " Empresas " (Configurações » Cadastros) » Aba Geral » Campo "Inscrição Estadual".](https://ajuda.sankhya.com.br/hc/article_attachments/16484665084311) Acesse: **"[Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913)"** (Configurações » Cadastros) » Aba Geral » Campo **"Inscrição Estadual".**

![Imagem 5: Acesse: " Parceiros " (Configurações » Cadastros) » Aba " Identificação" » Campo "Inscrição Estadual".](https://ajuda.sankhya.com.br/hc/article_attachments/16484665087255) Acesse: **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Configurações » Cadastros) » Aba "**Identificação"** » Campo **"Inscrição Estadual".**

![Imagem 6: De acordo com a Inscrição Estadual "rejeitada", acesse o site do Sintegra e realize a consulta para que essa informação…](https://ajuda.sankhya.com.br/hc/article_attachments/16484654032919) De acordo com a Inscrição Estadual "rejeitada", acesse o site do Sintegra e realize a consulta para que essa informação seja inserida corretamente:

- Acesse o site do SINTEGRA:  <http://www.sintegra.gov.br/>
- Busque pelo Estado do Parceiro ou Empresa:
- Será exibido uma página para consulta usando a CCE (IE), CNPJ ou CPF:
- Clique em Consultar
- Será retornado um quadro com as informações completas, atente-se a informação 'INSCRIÇÃO ESTADUAL'.

![Imagem 7: Ajuste a informação nos cadastros citados (sem informações de hífen, ponto, vírgula ou espaço em branco no início, meio…](https://ajuda.sankhya.com.br/hc/article_attachments/16484665092119) Ajuste a informação nos cadastros citados (sem informações de hífen, ponto, vírgula ou espaço em branco no início, meio ou fim), fature novamente a nota e gere o lote.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16484665095319) OBSERVAÇÃO:**

Caso não localize o campo 'Inscrição Estadual', o mesmo poderá ser inserido através das **"Configurações da tela"**

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16484654041623) CAUSA:**

Ocorre geralmente quando o valor atribuído ao campo IE (**trecho em negrito**) não é valido, pode ser porque foi adicionado hífen, ponto, virgula ou espaçamento no inicio ou meio do I.E(Inscrição Estadual), do cadastro do Emitente, Destinatário ou Transportadora da nota.
