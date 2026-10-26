---
id: "360047545514"
titulo: "Contribuinte de IPI deve apresentar registros E500 e registros filhos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360047545514-Contribuinte-de-IPI-deve-apresentar-registros-E500-e-registros-filhos"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-10-22T19:10:26Z"
rotulos: ["#PUBLIFER", "Configuração", "Fiscal", "IPI", "Impostos", "EFD", "Preferências", "#AGUARDANDOVALIDAÇÃO", "#VALIDADOJUNIOR", "Registros E500 necessários", "Ajustar preferências conforme necessidade", "Verificar configuração de atividade"]
---

# Contribuinte de IPI deve apresentar registros E500 e registros filhos

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18607134629271) MENSAGEM:**

Contribuinte de IPI deve apresentar registros E500 e registros filhos.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18607134637847) CAUSA:**

Quando o EFD está sendo gerado com o Tipo de Atividade 'Industrial ou Equiparada a Industrial', porém a empresa não possui apuração de IPI, ou a empresa realmente trata-se de uma indústria mas não foi configurada corretamente.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18607128125335) SOLUÇÃO:**

O Registro E500 do Sped-Fiscal, tem por objetivo identificar o **período de Apuração do Imposto sobre Produtos Industrializados (IPI).** Dessa forma, será necessário verificar com a Contabilidade, se a empresa deverá ou não gerar o registro E500, e através dessa informação seguir com as análises abaixo:

![Imagem 4: Empresa NÃO deve gerar o Registro E500:](https://ajuda.sankhya.com.br/hc/article_attachments/18607134649239) Empresa NÃO deve gerar o Registro E500:

- Se a empresa não for contribuinte do IPI, na tela de preferências da empresa, aba EFD - Escrituração Fiscal Digital', registro E500 e filhos deverão estar desmarcados para que o sistema não os gere.
- Se a empresa não for contribuinte do IPI, na tela de preferências da empresa, aba EFD - Escrituração Fiscal Digital' no campo **TIPO DE ATIVIDADE** deverá estar definida a opção=> **Outros;**

![Imagem 5: Se a empresa não for contribuinte do IPI, na tela de preferências da empresa, aba EFD - Escrituração Fiscal Digital' no…](https://ajuda.sankhya.com.br/hc/article_attachments/18607128134039)

![Imagem 6: Empresas que devem SIM gerar o Registro E500:](https://ajuda.sankhya.com.br/hc/article_attachments/18607134658583) Empresas que devem SIM gerar o Registro E500:

- Se a empresa for contribuinte do IPI, na tela de preferências da empresa, aba EFD - Escrituração Fiscal Digital', **registro E500 e filhos** deverão estar marcados para que o sistema os gere.
- Se a empresa for contribuinte do IPI, na tela de preferências da empresa, aba EFD - Escrituração Fiscal Digital' no campo TIPO DE ATIVIDADE deverá estar definida a Opção=> **Industrial ou equiparada a indústria;**

![Imagem 7: Se a empresa for contribuinte do IPI, na tela de preferências da empresa, aba EFD - Escrituração Fiscal Digital' no…](https://ajuda.sankhya.com.br/hc/article_attachments/18607134667799)
