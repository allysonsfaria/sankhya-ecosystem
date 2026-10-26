---
id: "43367764153111"
titulo: "Processo Rateio de IBS e CBS na movimentação financeira por parcela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111-Processo-Rateio-de-IBS-e-CBS-na-movimenta%C3%A7%C3%A3o-financeira-por-parcela"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Comece por aqui > Processos do Portal da Reforma Tributária"
atualizado_em: "2026-09-09T18:14:28Z"
rotulos: ["Rateio", "Processo Rateio de IBS e CBS na movimentação financeira por parcela"]
---

# Processo Rateio de IBS e CBS na movimentação financeira por parcela

**Versão mínima:** Sankhya Om 4.36 ou superior · Módulo ERP Core 5.19.0 · Módulo Livros Fiscais 5.44.0
**Módulo:** Livros Fiscais › Cadastros › Portal da Reforma Tributária · **Caminho de acesso:** Menu Principal › Financeiro › Movimentação Financeira

---

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111-Processo-Rateio-de-IBS-e-CBS-na-movimenta%C3%A7%C3%A3o-financeira-por-parcela#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111-Processo-Rateio-de-IBS-e-CBS-na-movimenta%C3%A7%C3%A3o-financeira-por-parcela#antes-de-comecar)
- [Como funciona o rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111-Processo-Rateio-de-IBS-e-CBS-na-movimenta%C3%A7%C3%A3o-financeira-por-parcela#como-funciona)
- [Ajuste de valores com movimento em aberto](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111-Processo-Rateio-de-IBS-e-CBS-na-movimenta%C3%A7%C3%A3o-financeira-por-parcela#ajuste-valores)
- [Como conferir o rateio realizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111-Processo-Rateio-de-IBS-e-CBS-na-movimenta%C3%A7%C3%A3o-financeira-por-parcela#como-conferir)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111-Processo-Rateio-de-IBS-e-CBS-na-movimenta%C3%A7%C3%A3o-financeira-por-parcela#pontos-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111-Processo-Rateio-de-IBS-e-CBS-na-movimenta%C3%A7%C3%A3o-financeira-por-parcela#faq)

## O que é e para que serve

O processo de Rateio de IBS e CBS na movimentação financeira por parcela distribui automaticamente os valores do Imposto sobre Bens e Serviços (IBS) e da Contribuição sobre Bens e Serviços (CBS), calculados no documento fiscal, para cada parcela (título) gerada no módulo **Financeiro** — na mesma proporção do valor de cada parcela em relação ao valor total do documento. Assim, cada título passa a carregar a informação tributária necessária para o futuro repasse ao Split Payment da Reforma Tributária.

O processo não realiza nenhum novo cálculo de tributo: ele apenas desce e divide o valor já apurado no documento fiscal. Também não cobre o envio desses valores a Prestadores de Serviço de Pagamento (PSPs) nem a geração de documentos do tipo DF Agregador — essas etapas dependem de definições regulatórias ainda não publicadas.

## Antes de começar

Para que o rateio seja executado corretamente, atenda aos requisitos abaixo antes de gerar o título financeiro:

- Habilite o cálculo de IBS e CBS no documento fiscal. Para saber mais, acesse [Assistente de Configuração da Tributação integral IBS e CBS (Reforma Tributária)](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479).
- Configure a **TOP (Tipo de Operação)** utilizada na emissão do documento com IBS e CBS habilitados na aba **Reforma Tributária**. Para saber mais, acesse [Guia rápido: como preparar seu sistema para a Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/34971966800151).

**⚠️ Atenção**

O rateio só ocorre corretamente se o valor de IBS e CBS estiver calculado e validado no documento fiscal antes da geração do movimento financeiro. Documentos emitidos sem IBS ou CBS configurados na **TOP** não geram nenhum valor de tributo nas parcelas — esse comportamento é o esperado, sem erro.

## Como funciona o rateio

O rateio é executado automaticamente no momento em que o título financeiro é gerado a partir do documento fiscal. Você não precisa acionar nenhum botão nem configurar nenhum campo adicional — basta que os requisitos acima estejam atendidos.

### Cálculo proporcional por parcela

Para cada parcela gerada, o Sankhya Om calcula a proporção daquela parcela em relação ao valor total do documento e aplica essa mesma proporção ao valor total de IBS e ao valor total de CBS.

Veja um exemplo com um documento fiscal de R$ 1.000,00, com IBS de R$ 100,00 e CBS de R$ 90,00, dividido em duas parcelas de R$ 600,00 e R$ 400,00:

| **Parcela** | **Valor da parcela** | **Proporção** | **IBS rateado** | **CBS rateado** |
| --- | --- | --- | --- | --- |
| 1ª parcela | R$ 600,00 | 60% | R$ 60,00 | R$ 54,00 |
| 2ª parcela | R$ 400,00 | 40% | R$ 40,00 | R$ 36,00 |
| **Total** | **R$ 1.000,00** | **100%** | **R$ 100,00** | **R$ 90,00** |

### Ajuste de sobra de centavos

Quando a divisão proporcional gera valores com casas decimais que, ao serem arredondados, produzem uma diferença de centavos em relação ao total do documento, o Sankhya Om ajusta automaticamente a última parcela para que a soma sempre coincida com o valor total de IBS e CBS do documento. Esse ajuste garante a reconciliação fiscal-financeira sem nenhuma ação manual de sua parte.

### Documentos sem IBS ou CBS

Se o documento fiscal não tiver IBS ou CBS calculados — por exemplo, operações cuja **TOP** não contempla esses tributos — nenhum valor de tributo é gerado nas parcelas. O Sankhya Om não exibe erro: simplesmente não há valor a ratear.

## Ajuste de valores com movimento em aberto

Se o documento fiscal sofrer alteração de valores enquanto o movimento financeiro ainda estiver em aberto (títulos não liquidados), o Sankhya Om recalcula automaticamente o rateio de IBS e CBS em todas as parcelas, mantendo a consistência entre a posição fiscal e a movimentação financeira.

**ℹ️ Nota**

O cancelamento do documento fiscal não exige tratamento especial para o rateio: no Sankhya Om, o cancelamento só é permitido enquanto o movimento financeiro está em aberto, e nesse caso o próprio movimento é excluído — não há registro de parcela a ser recalculado.

## Como conferir o rateio realizado

Após a geração do movimento financeiro, confira os valores de IBS e CBS rateados na tela **Movimentação Financeira**:

1. Acesse **Menu Principal › Financeiro › Movimentação Financeira**.
2. Localize o título gerado a partir do documento fiscal com IBS ou CBS.
3. Abra o título.
4. Confirme os valores de IBS e CBS registrados para aquela parcela.
5. Some os valores de IBS e CBS de todas as parcelas do mesmo documento e compare com o valor de IBS e CBS do documento fiscal de origem.

## Pontos de atenção

- O rateio reflete o valor **Informado** — o IBS e CBS apurado dentro do Sankhya Om a partir do documento fiscal. Esse valor é diferente do tributo **Segregado**, que o Prestador de Serviço de Pagamento (PSP) calculará externamente no momento do pagamento, em etapa futura ainda não implementada.
- A funcionalidade não cobre o DF Agregador, documento que consolida múltiplos DFs sob uma única chave de acesso. A operacionalização desse tipo de documento ainda não foi regulamentada pelo ENCAT/SEFAZ — nenhuma Nota Técnica, leiaute XSD ou especificação técnica foi publicada. Quando a regulamentação for publicada, o escopo será revisado.
- O envio dos valores de IBS e CBS rateados a qualquer PSP não faz parte desta funcionalidade. Essa integração depende de definição dos próprios PSPs sobre como farão a conexão com o Sankhya Om.
- A exigência legal do Split Payment entra em vigor a partir de janeiro de 2027. O uso desta funcionalidade antes dessa data tem caráter preparatório e de validação.

**🚨 Risco operacional**

Não confunda o tributo **Informado**, produzido por este processo dentro do Sankhya Om, com o tributo **Segregado**, que o PSP calculará externamente. Apresentar o valor **Informado** como o valor a ser repassado ao PSP antes de a integração estar definida e implementada pode gerar inconsistências operacionais.

## Perguntas frequentes

### Este processo já envia os valores de IBS e CBS para algum banco ou Pix?

Não. O processo prepara e registra os valores dentro do Sankhya Om. O envio para Prestadores de Serviço de Pagamento é uma etapa futura, que depende de definição dos PSPs sobre como farão a integração.

### O que acontece se você gerar um documento fiscal sem IBS ou CBS e depois habilitar o tributo?

O rateio é executado no momento da geração do título financeiro. Se o documento foi gerado sem IBS ou CBS, nenhum valor de tributo é registrado nas parcelas existentes. Para que o rateio ocorra, reprocesse o documento com a configuração correta de tributos. Consulte o time fiscal antes de qualquer reprocessamento.

### Por que o DF Agregador está fora do escopo?

O conceito do DF Agregador está definido no Manual de Operações do Split Payment (RFB/CGIBS): é o documento que consolida múltiplos DFs sob uma única chave de acesso para uma única transação de pagamento. O que ainda não existe é o modelo de operacionalização — nenhuma Nota Técnica, leiaute XSD ou especificação técnica foi publicada pelo ENCAT/SEFAZ. Sem essa definição regulatória, não há base para especificar o rateio de IBS e CBS nesse cenário.

### A soma das parcelas sempre coincide com o total do documento?

Sim. O Sankhya Om aplica um ajuste automático na última parcela para absorver eventuais diferenças de arredondamento, de forma que a soma das parcelas sempre coincida com o valor total de IBS e CBS do documento fiscal.
