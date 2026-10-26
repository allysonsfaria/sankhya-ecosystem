---
id: "39355771998359"
titulo: "Como corrigir divergências de saldo inicial no Balancete de Verificação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39355771998359-Como-corrigir-diverg%C3%AAncias-de-saldo-inicial-no-Balancete-de-Verifica%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T13:47:43Z"
rotulos: ["Configuração", "Relatórios", "Atualização", "Contabilidade", "Financeiro", "Erro", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Como corrigir divergências de saldo inicial no Balancete de Verificação

Quando o **"Saldo final de um mês"** não corresponde ao **"Saldo inicial do mês seguinte"** no Balancete de Verificação, isso indica uma **"Inconsistência nos saldos contábeis"** que precisa ser corrigida. Este problema pode ocorrer após atualizações do sistema, alterações em lançamentos ou falhas no processamento de saldos.

Este artigo apresenta as **"Melhores práticas"** para identificar e resolver divergências de saldo no Balancete de Verificação, garantindo a **"Integridade das informações contábeis"**.

### Verificações necessárias antes da recomposição

Antes de executar a recomposição de saldos, realize as seguintes verificações para identificar a origem do problema:

**"Análise do Balancete"**: Consulte o relatório **"Balancete de Verificação"** (Contabilidade >> Consultas >> Balancete de Verificação) e verifique se as colunas **"Saldo anterior"** e **"Saldo atual"** do totalizador apresentam divergências. Em um balancete correto, essas colunas devem estar zeradas.

**"Comparação entre períodos"**: Compare o **"Saldo final do mês anterior"** com o **"Saldo inicial do mês atual"**. Esses valores devem ser idênticos. Se houver diferença, identifique em quais contas ela ocorre.

**"Verificação de lançamentos"**: Consulte **"Lançamentos Contábeis"** (Contabilidade >> Arquivos >> Lançamentos Contábeis) e confirme se todos os lotes do período estão **"Fechados"** e se não há lançamentos incompletos ou sem contrapartida.

**"Configuração de impressão"**: Na tela de emissão do Balancete de Verificação, verifique se a opção **"Imprimir saldo anterior zerado"** está desmarcada. Essa configuração pode ocultar saldos iniciais que deveriam ser exibidos.

### Executando a recomposição de saldos

A **"Recomposição de saldos"** recalcula todos os saldos das contas contábeis a partir de uma data específica, corrigindo inconsistências. Siga o passo a passo abaixo:

**(1)** Acesse **"Empresa"** (Contabilidade >> Preferências >> Empresa).

**(2)** Clique no botão **"Outras Opções (...)"** e selecione **"Recompor saldos"**.

**(3)** No campo **"Referência p/ recomposição"**, informe a data do **"Mês início da recomposição"** ao que apresenta problema. Por exemplo, se o erro está em fevereiro, informe **"01/01/20xx"**.

**(4)** O sistema apresentará a mensagem: "A recomposição irá recalcular todo o saldo de contas contábeis da empresa para a referência informada até a referência atual". Confirme a operação.

**(5)** Aguarde o processamento. O tempo pode variar conforme o volume de lançamentos.

**Importante:** Sempre inicie a recomposição pelo mês anterior ao que apresenta o problema, pois o saldo inicial de um mês é construído pelo saldo final do mês anterior.

### Verificando os resultados da recomposição

Após executar a recomposição de saldos, é fundamental verificar se o problema foi resolvido:

**(1)** Acesse **"Balancete de Verificação"** (Contabilidade >> Consultas >> Balancete de Verificação).

**(2)** Gere o balancete do mês que apresentava divergência.

**(3)** Verifique se o saldo inicial agora corresponde ao saldo final do mês anterior.

**(4)** Confirme se as colunas **"Saldo anterior"** e **"Saldo atual"** estão zeradas no totalizador.

**(5)** Repita a verificação para os demais meses do período afetado.

### Considerações sobre o navegador

Se a recomposição de saldos não resolver o problema, verifique qual **"Navegador"** está sendo utilizado para acessar o sistema. O **"Navegador Sankhya"** pode apresentar falhas no processo de recomposição devido ao acúmulo de cache, ocasionando inconsistências nos saldos contábeis.

**Recomendação:** Utilize navegadores como **"Google Chrome"**, **"Mozilla Firefox"** ou **"Microsoft Edge"** para executar a recomposição de saldos. O Navegador Sankhya encontra-se em processo de descontinuação e não recebe mais manutenções.

### Se o problema persistir

Caso a divergência permaneça após a recomposição de saldos, execute as seguintes ações:

**"Recomposição desde o início do exercício"**: Acesse a aba **"Exercício"** em **"Empresa"** (Contabilidade >> Preferências >> Empresa) e verifique o **"Início do período contábil"**. Execute a recomposição a partir dessa data.

**"Análise detalhada de lançamentos"**: Consulte detalhadamente os lançamentos que compõem o saldo das contas com divergência, identificando possíveis lançamentos incorretos ou incompletos.

**"Verificação de fechamento mensal"**: Acesse **"Lotes Contábeis"** (Contabilidade >> Arquivos >> Lotes Contábeis), vá em **"Outras Opções"** e selecione **"Fechamento de mês"**. Certifique-se de que o fechamento foi executado corretamente para o período.

A recomposição de saldos é uma ferramenta essencial para manter a **"Integridade dos dados contábeis"** no sistema, garantindo que os balancetes reflitam corretamente a situação patrimonial da empresa.
