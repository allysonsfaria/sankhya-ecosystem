---
id: "360044040414"
titulo: "Conferência de Caixa no Fast Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044040414-Confer%C3%AAncia-de-Caixa-no-Fast-Service"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:55:44Z"
rotulos: ["#PUBLIFER", "#revisadojunior", "MANUALRONEI", "O.S1403908", "Conferência", "Configuração", "Fast Service", "Movimentação Financeira", "Preferências", "Financeiro", "Conferência de Caixa", "Acesso baseado em função", "Exige conferência antes de fechar"]
---

# Conferência de Caixa no Fast Service

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18949872888471) SOLUÇÃO:**

A tela será aberta ao solicitar o fechamento do caixa, clicando em "Sair", ou poderá ser acessada pelo menu 'Avançado/Conferência de Caixa':

**Configurações necessárias:**

Se o parâmetro **“Exige conferência antes de fechar? -EXIGECONFCAIXA"** estiver habilitado o sistema exigirá pelo menos uma conferência antes do ‘Fechamento do Caixa’:

Avançado >> Preferências >> Todas Preferências >> Aba 'Miscelânea' >> “Exigir Conferência antes de fechar?”Na tela de conferência, o usuário informa o valor conferido e se houver alguma divergência o sistema lançará um título na 'Movimentação Financeira' para nivelar os valores.

Esse título será gerado com os dados definidos na aba ‘Preferências’ da tela de conferência, onde o usuário informará a Empresa, a TOP de Receita e Despesa, a Natureza, o Centro de Resultado, o Projeto, o Parceiro, o Banco e uma Observação. O título gerado terá ‘Número da Nota’ igual a zero e a ‘Data’ e ‘Hora’ atual:

| **Aba de preferencias oculta**    Se o usuário NÃO for gerente de caixa ou Gerente Financeiro, a ABA será escondida. A ABA "Preferencias da Conferência de Caixa" será apresenta se o usuário for "Gerente Financeiro" ou "Gerente de Caixa" campos nativos do sistema.    Como essas preferencias são gravadas por usuário, temos que considerar que a ABA poderá aparecer no primeiro acesso a tela, mesmo que o usuário não tenha essas marcações, isso é necessário para que façam a primeira definição do usuário, depois de preenchido no primeiro acesso o sistema sempre respeitará marcação citada. |
| --- |

**Importante:**

Esta tela será apresentada com o campo 'Conferência' zerado, obrigando assim a digitação dos valores, antes do fechamento do caixa.

Somente será possível digitar informações no campo 'Conferência' se no 'Tipo de Título' utilizado, o campo "Conferência?" estiver marcado:

Tela 'Tipos de Título' (Jiva W ou G1) >> Aba 'Fast Service':Somente títulos que possuírem essa marcação estarão disponíveis na tela 'Avançado\Conferência de Caixa' do Fast Service.

Incluir no mesmo o parâmetro >

**"Apresentar títulos pendentes na conferência? - APRESTITPENDENT"** - Apresentar tipos de títulos pendentes, este parâmetro irá apresentar títulos que são utilizados no Fast Service que não foram baixados automaticamente nas versões anteriores a esta manutenção.
