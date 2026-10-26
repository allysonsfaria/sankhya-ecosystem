---
id: "39352171767319"
titulo: "Erro no Cálculo de Avos do 13º Salário para Colaboradores com Licença sem Remuneração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39352171767319-Erro-no-C%C3%A1lculo-de-Avos-do-13%C2%BA-Sal%C3%A1rio-para-Colaboradores-com-Licen%C3%A7a-sem-Remunera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:49Z"
rotulos: ["Configuração", "Afastamento", "Folha de Pagamento", "13º Salário", "Artigo criado KCS", "Sankhya RH - KCS", "Legislação Trabalhista"]
---

# Erro no Cálculo de Avos do 13º Salário para Colaboradores com Licença sem Remuneração

**Mensagem**

O sistema está calculando incorretamente os avos do 13º salário para colaboradores afastados, não descontando os períodos de licença sem remuneração.

**Situação**

Ao processar a folha de pagamento do **"13º salário"**, o sistema não está descontando corretamente os avos dos colaboradores que possuem afastamentos do tipo **"licença sem remuneração"**. O cálculo está considerando períodos em que o funcionário não deveria ter direito ao décimo terceiro, resultando em valores incorretos.

**Solução**

Para corrigir o cálculo, ajuste a configuração dos códigos de afastamento, desativando a flag **"Direito ao Décimo Terceiro"** para os tipos de afastamento que não concedem esse direito. Siga os passos abaixo:

**(1)** Acesse a tela de **"Códigos de Afastamento"** (Pessoal+ » Cadastros » Código de Afastamento).
**(2)** Localize os códigos de afastamento que não concedem direito ao 13º salário, tais como:
• Licença sem remuneração - rais
• Licença sem vencimento
• Licença gestante
• Licença maternidade ou paternidade - rais
• Afastamento temporário para licença gestante
• Aposentadoria por invalidez exceto por acidente de trabalho
• Aposentadoria por invalidez
• Serviço militar

![Imagem 1: Para cada código identificado, desmarque o campo "Direito ao Décimo Terceiro" .](https://ajuda.sankhya.com.br/hc/article_attachments/41399952153111)
**(3)** Para cada código identificado, desmarque o campo **"Direito ao Décimo Terceiro"**.

![Imagem 2: Salve as alterações realizadas. Acesse a tela de "Gerenciador de folhas " (Pessoal+ » Rotinas Folha » Gerenciador de…](https://ajuda.sankhya.com.br/hc/article_attachments/41399988014743)
**(4)** Salve as alterações realizadas.
**(5)** Acesse a tela de **"Gerenciador de folhas "** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas).
**(6)** Recalcule a folha referente ao 13º salário para os funcionários afetados.
**(7)** Verifique se os avos foram calculados corretamente, descontando os períodos de afastamento sem direito ao décimo terceiro.

**Causa**

O erro ocorre porque os códigos de afastamento estavam configurados com a flag **"Direito ao Décimo Terceiro"** ativa. Essa configuração faz com que o sistema considere os períodos de afastamento como tempo de serviço válido para o cálculo, mesmo quando o colaborador não possui esse direito legalmente.

De acordo com a legislação trabalhista brasileira, colaboradores afastados por licença sem remuneração, serviço militar obrigatório e outros tipos específicos de afastamento perdem o direito aos avos correspondentes ao período de afastamento. Portanto, é fundamental que a configuração dos códigos de afastamento reflita corretamente essas regras para garantir o cálculo preciso do 13º salário.
