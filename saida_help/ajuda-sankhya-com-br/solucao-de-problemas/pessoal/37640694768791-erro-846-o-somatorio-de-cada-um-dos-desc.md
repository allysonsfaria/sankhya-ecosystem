---
id: "37640694768791"
titulo: "Erro 846 - O somatório de cada um dos descontos de Contribuição Previdenciária (codIncCP = [31, 32, 34, 35]) não pode ser negativo, ou seja, os vencimentos não podem ser superiores aos descontos."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37640694768791-Erro-846-O-somat%C3%B3rio-de-cada-um-dos-descontos-de-Contribui%C3%A7%C3%A3o-Previdenci%C3%A1ria-codIncCP-31-32-34-35-n%C3%A3o-pode-ser-negativo-ou-seja-os-vencimentos-n%C3%A3o-podem-ser-superiores-aos-descontos"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-30T17:03:34Z"
rotulos: ["Impostos", "Folha", "eSocial", "Configuração Funcionários", "Erro", "INSS e IRRF", "Contribuição Previdenciária (codIncCP = [31 32 34 35])", "Evento S-1200", "Somatório das rubricas de desconto", "Somatório das rubricas de vencimentos/adicionais"]
---

# Erro 846 - O somatório de cada um dos descontos de Contribuição Previdenciária (codIncCP = [31, 32, 34, 35]) não pode ser negativo, ou seja, os vencimentos não podem ser superiores aos descontos.

##### MENSAGEM:

##### Erro 846 - O somatório de cada um dos descontos de Contribuição Previdenciária (codIncCP = [31, 32, 34, 35]) não pode ser negativo, ou seja, os vencimentos não podem ser superiores aos descontos.

##### SOLUÇÃO:

##### **(1)** Identifique o colaborador cujo evento foi invalidado e consulte os recibos para verificar quais rubricas foram calculadas na competência.

##### **(2)** Confirme se o evento S-1010 está validado no eSocial e se as incidências das rubricas estão corretas, tanto no sistema quanto no portal do eSocial.

##### **(3)** Caso seja identificada alguma incidência incorreta, ajuste o cadastro da rubrica no S-1010 e reenvie o evento com as correções necessárias.

##### **(4)** Após a validação do S-1010, gere novamente o evento S-1200 e realize o envio ao eSocial.

#####

##### CAUSA:

O erro ocorre porque, no envio do **evento S-1200** do colaborador, o **somatório das rubricas de desconto** com incidência de **INSS e IRRF** ficou **maior** que o **somatório das rubricas de vencimentos/adicionais** com as mesmas incidências.

De acordo com as **regras de validação do leiaute do eSocial**, aplicáveis aos eventos **S-1200, S-2299 e S-2399**, o valor total dos **vencimentos deve ser maior ou igual ao total dos descontos**.

Especificamente, para rubricas que possuam:

- **Incidência em Contribuição Previdenciária (S-1010)** igual a **[31, 32, 34 ou 35]**
- **Incidência em IRRF (S-1010)** igual a **[31, 32, 33 ou 34]**

O somatório das rubricas classificadas como **Vencimento ou Informativa [1,3]** deve ser **maior ou igual** ao somatório das rubricas classificadas como **Desconto ou Informativa Dedutiva [2,4]**, considerando cada código de incidência individualmente.

![Imagem 1: O somatório das rubricas classificadas como Vencimento ou Informativa (1,3) deve ser maior ou igual ao somatório das…](https://ajuda.sankhya.com.br/hc/article_attachments/37647788040471)
