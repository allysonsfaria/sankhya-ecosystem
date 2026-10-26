---
id: "30707310199063"
titulo: "Realizada a configuração para aplicar a Lei da Transparência e as informações não são apresentadas no DANFE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30707310199063-Realizada-a-configura%C3%A7%C3%A3o-para-aplicar-a-Lei-da-Transpar%C3%AAncia-e-as-informa%C3%A7%C3%B5es-n%C3%A3o-s%C3%A3o-apresentadas-no-DANFE"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:34:55Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "Lei da Transparência", "DANFE", "Impostos", "Realizada a configuração para aplicar a Lei da Transparência", "as informações não são apresentadas no DANFE"]
---

# Realizada a configuração para aplicar a Lei da Transparência e as informações não são apresentadas no DANFE

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30707310193431) **SITUAÇÃO:**

Após configurar o sistema para que seja aplicada a lei da transparência ao imprimir o DANFE as informações sobre **Carga Média Tributária** não são impressas.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30707358163479)SOLUÇÃO:**

Para apresentação das informações da Lei da Transparência, as seguintes configurações são necessárias:

**(1)** Cadastro da **TOP**, aba **"NF-e/NFC-e/CF-e"**, campo **"Aplicar Lei da Transparência"** com as opções: Usar do parceiro, Aplicar Sempre, Nunca Aplicar. Caso esteja configurado Usar do Parceiro, o sistema verificará no Cadastro do parceiro;

**(1)** Cadastro do **Parceiro**, aba **"Fiscal",** campo **"Aplicar lei da Transparência"**. Caso a top utilize a configuração do Parceiro, essa configuração é indispensável;

**(1)** Cadastro de **Produto**, aba **"Impostos"** ou no **"Grupo de Produtos"** os campos **"%Carga Media Trib. Nacional"** e **"%carga media trib. importação"**, devem estar configurados com as devidas porcentagens;

**(1)** Classificação do **parceiro**: Consumidor Final.

**(1)** **Parâmetros:**

- **LEI12741FONTE - Fonte do cálculo da Carga Média Tributár**ia >> Deverá ser informado: IBPT ou outra fonte que seja utilizada
- **APLICALEITRANSP - Aplicar a lei da transparência:**
  - Quando **ligado**, para as notas de vendas (TIPMOV = 'V'), vai gerar as informações relativas à carga tributária média (lei da transparência), independente do tipo de cliente ser consumidor, consumidor contribuinte ou produto rural.
  - Quando **desligado**, assume que para as notas de vendas (TIPMOV = 'V') deve gerar (lei da transparência) apenas para cliente consumidor, consumidor contribuinte ou produto rural.

**Observações:**

Se todas as configurações acima estiverem corretas, verifique se na TOP existe um modelo de dados adicionais. Quando há um modelo informado e as cargas médias tributárias não são geradas na tag <infCpl>, e consequentemente não são impressas no DANFE, é preciso tratar no próprio modelo utilizando a variável responsável para buscar estas informações. A variável que trará os dados das cargas médias tributárias é a "**&vlrtributos01**".

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30707358165527)CAUSA:**

Ocorre por falta de alguma das configurações citadas acima, ou por utilizar um modelo de dados adicionais na TOP do lançamento que não contempla a variável **&vlrtributos01**.
