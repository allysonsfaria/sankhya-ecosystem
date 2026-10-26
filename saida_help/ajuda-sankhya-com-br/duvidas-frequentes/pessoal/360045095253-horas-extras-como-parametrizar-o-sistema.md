---
id: "360045095253"
titulo: "Horas Extras : Como parametrizar o sistema para 50% folha e 50% banco de horas?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045095253-Horas-Extras-Como-parametrizar-o-sistema-para-50-folha-e-50-banco-de-horas"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-27T18:23:22Z"
rotulos: ["#PUBLIFER", "Configuração", "Ponto", "Folha", "Check box em 'Regras para Cálculo' 'Banco de Horas Geral'", "Define divisão de horas extras entre folha e banco", "Exemplo: 50 min = 25 min folha + 25 min banco", "Horas Extras", "Banco de Horas"]
---

# Horas Extras : Como parametrizar o sistema para 50% folha e 50% banco de horas?

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19067562180375) SOLUÇÃO:**

Quando houver necessidade de que as primeiras horas extras realizadas seja considerada metade do valor para o banco e a outra metade para a folha de pagamento, limitando a uma hora por dia no banco, será necessário seguir com a configuração abaixo:

Criado um check box na tela de 'Regras para Cálculo', 'Aba Ponto' >>  sub aba 'Banco de Horas Geral', para que o usuário possa marcá-lo caso necessite dessas configurações:

- **Percentual de lançamento em folha se Extras menor que limite diário BH:**Será configurado o percentual de horas/minutos que irão para movimento se as horas extras diárias forem menores que o valor configurado no campo "Percentual de horas que vão para a folha quando menor que o limite diário do Banco";

Diante dessa marcação, o comportamento do sistema ocorrerá conforme exemplos abaixo:

- **50 minutos** por dia  = 25 minutos paga em folha + 25 minutos banco de horas

- **1:30 horas** por dia  = 45 minutos paga em folha  + 45 minutos banco de horas

- **2 horas** por dia  =  1 paga em folha  + 1 banco de horas

- **3 horas** por dia = 2 paga em folha  + 1 banco de horas

**Importante:**
Nota-se que para os dois últimos exemplos o sistema atualmente já atende a necessidade, através da marcação **'Limite de Horas Extras Diárias para Banco de Horas'**. Dessa forma, a nova marcação deverá estar ligada com essa opção. 

Como comportamento default do sistema, a marcação "Percentual de horas que vão para a folha quando menor que o limite diário do Banco" deverá estar desmarcada.
