---
id: "39353329300375"
titulo: "Erro no Cálculo de Faltas Não Descontadas em Folha de Pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39353329300375-Erro-no-C%C3%A1lculo-de-Faltas-N%C3%A3o-Descontadas-em-Folha-de-Pagamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-17T13:30:26Z"
rotulos: ["Configuração", "Eventos", "Atualização", "Pessoal", "Folha de Pagamento", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no Cálculo de Faltas Não Descontadas em Folha de Pagamento

**MENSAGEM**

O sistema não está descontando as faltas lançadas na folha de pagamento mensal, mesmo com os registros corretos no sistema.

**SITUAÇÃO**

Ao calcular a **"Folha de Pagamento Mensal"**, o funcionário possui **"Faltas"** lançadas no sistema através da tela **"Faltas"** e **"Lançamento de Movimento"** ou importadas de sistemas de ponto eletrônico. Porém, ao processar o cálculo, o desconto das faltas não é aplicado no pagamento do colaborador, gerando divergências nos valores líquidos e nos reflexos em férias e décimo terceiro salário.

**SOLUÇÃO**

**(1)** Verifique se o evento **"FALTAS"** está ativo no sistema. Acesse a tela **"Eventos"** (Pessoal+ » Rotinas Folha » Faltas) e localize o evento utilizado para cálculo de faltas.

**(2)** Caso o evento esteja inativo, realize a reativação do evento correto e inative o evento incorreto que possa estar sendo utilizado indevidamente.

**(3)** Verifique se a versão do módulo **"Pessoal"** está atualizada. 

**(4)** Após a atualização, acesse a tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento) e realize o reprocessamento da folha de pagamento do funcionário afetado.

**(5)** Se as faltas foram importadas de sistema de ponto eletrônico, verifique se a integração está configurada corretamente e se as faltas estão sendo alimentadas tanto na tela de **"Faltas"** quanto na movimentação da folha.

**(6)** Exclua o cálculo anterior do funcionário e realize um novo cálculo da folha, verificando se o desconto das faltas foi aplicado corretamente.
 

**CAUSA**

O problema pode ocorrer por três causas principais:

**1. Evento de falta inativo:** O evento responsável pelo cálculo das faltas estava inativo no sistema, impedindo que o desconto fosse processado durante o cálculo da folha.

**2. Lançamento incorreto:** Quando o lançamento não foi realizado pela rotina de "Faltas"

**2. Versão desatualizada do módulo:** Versões anteriores à 5.66.5 do módulo Pessoal apresentavam inconsistências no processamento de faltas, especialmente em casos específicos de afastamentos ou integrações com sistemas externos.

**3. Falhas na integração com ponto eletrônico:** Quando as faltas são importadas de sistemas externos, pode haver problemas na alimentação simultânea da tela de faltas e da movimentação de folha, causando divergências nos cálculos de férias e décimo terceiro salário.
