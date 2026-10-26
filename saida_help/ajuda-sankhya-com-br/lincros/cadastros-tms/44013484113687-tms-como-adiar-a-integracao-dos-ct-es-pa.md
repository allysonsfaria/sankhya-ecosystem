---
id: "44013484113687"
titulo: "[TMS] - Como Adiar a Integração dos CT-es para o ERP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013484113687--TMS-Como-Adiar-a-Integra%C3%A7%C3%A3o-dos-CT-es-para-o-ERP"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:58:46Z"
rotulos: ["sync_hc", "lincros", "sync_hash_11fae8768dc3", "lincros_13432387"]
---

# [TMS] - Como Adiar a Integração dos CT-es para o ERP

**1 - Problema Relatado pelo Cliente:**
O cliente relatou a necessidade de adiar/atrasar a integração dos CT-es após a importação dos XML deles no TMS, com o objetivo de evitar problemas com cancelamentos de CT-e realizados pela transportadora após a escrituração no ERP. Pois está havendo muitos casos de CT-es cancelados pela transportadora após já ter sido importado no TMS e integrado no ERP.

## 2 - Passo a Passo para Resolver o Problema:

Se você deseja atrasar a integração/escrituração dos CT-es com o ERP para evitar conflitos de status do CT-e no TMS e ERP, siga estas orientações:

1. ## Entenda a funcionalidade do parâmetro `diasEsperaEscrituracaoCte`:

   - Este parâmetro define um número de dias de espera entre a emissão do CT-e e sua escrituração no sistema.
   - Por exemplo, com o valor definido como **1**, um CT-e emitido no dia 31 só será integrado/escriturado no dia 1º do mês seguinte.
   - É possível configurar dias específicos para cada UF emissora do CT-e.
2. ## Limitação importante:

   - O parâmetro aplica esse atraso **em todos os dias**
   - Isso significa que **todos os CT-es importados no TMS passarão a respeitar esse tempo de espera para só então integrar ao ERP.**
3. ## Como ativar o parâmetro:

   - A ativação e configuração do `diasEsperaEscrituracaoCte` **não é feita diretamente por usuários finais**.
   - Caso deseje utilizar esse recurso, entre em contato com o suporte técnico da Lincros e solicite a ativação do parâmetro com o valor desejado.
4. ## Recomendações adicionais:

   - Antes de solicitar a alteração, avalie com a equipe contábil e de tecnologia os impactos da espera para todos os CT-es.
   - Considere o comportamento operacional do seu processo de integração e escrituração para decidir se o atraso geral é viável.
