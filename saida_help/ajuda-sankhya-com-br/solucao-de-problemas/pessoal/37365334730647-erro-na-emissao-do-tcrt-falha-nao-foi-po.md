---
id: "37365334730647"
titulo: "Erro na Emissão do TCRT: Falha. Não foi possível gerar o relatório solicitado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37365334730647-Erro-na-Emiss%C3%A3o-do-TCRT-Falha-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-relat%C3%B3rio-solicitado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:21Z"
rotulos: ["Relatórios", "PIS", "Folha", "Configuração Funcionários", "Pessoal+", "Erro", "TRCT", "Emissão do TCRT", "Erro na emissão do TCRT", "TRCT (Termo de Rescisão do Contrato de Trabalho)", "PIS/PASEP"]
---

# Erro na Emissão do TCRT: Falha. Não foi possível gerar o relatório solicitado.

**MENSAGEM:**

Falha. Não foi possível gerar o relatório solicitado.

**Motivo:** Error evaluating expression: Source text:

String format (“%s %s %s %s”, SF(PIS).substring(0,3), SF(PIS).substring(3,8), SF(PIS).substring(8,10), SF(PIS).substring(10,11))

![Imagem 1: String format (“%s %s %s %s”, SF(PIS).substring(0,3), SF(PIS).substring(3,8), SF(PIS).substring(8,10),…](https://ajuda.sankhya.com.br/hc/article_attachments/37365318747415)

##### SITUAÇÃO:

Ao tentar emitir o **TRCT (Termo de Rescisão do Contrato de Trabalho)**, o sistema apresentou um erro que impediu a geração do relatório. A falha está relacionada à validação de expressão e à formatação do campo **PIS**, que não atende aos critérios esperados pelo sistema.

##### SOLUÇÃO:

Para resolver o problema, siga os passos abaixo:

**(1)** Acesse a tela [**''Configuração Funcionários''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios) (Pessoal+ » Cadastros » Configuração Funcionários)

**(2)** Localize o campo **''PIS/PASEP''**.

**(3)** Verifique se o número:

- Possui **11 dígitos**.
- Está preenchido **sem espaços, pontos ou caracteres especiais**.
- Corresponde ao número correto do colaborador.

**(4)** Caso identifique inconsistências:

- Corrija o PIS.
- Salve o cadastro.

**(5)** Após o ajuste, **realize novamente a emissão do TRCT**.

##### CAUSA:

O erro ocorre quando o número do **PIS/PASEP** do colaborador está **incompleto, inválido ou fora do padrão exigido pelo sistema**.

Durante a emissão do **TRCT**, o sistema realiza a quebra e formatação do número do PIS por meio de validações internas (substring). Quando o cadastro apresenta inconsistências, esse processo falha, impedindo a geração do relatório.

Isso pode acontecer quando o **PIS/PASEP** possui quantidade de dígitos inferior ao padrão de **11 dígitos**, está cadastrado com **caracteres inválidos**, como pontos, espaços ou símbolos, ou ainda quando se encontra **nulo, incompleto ou inconsistente** no cadastro do colaborador.
