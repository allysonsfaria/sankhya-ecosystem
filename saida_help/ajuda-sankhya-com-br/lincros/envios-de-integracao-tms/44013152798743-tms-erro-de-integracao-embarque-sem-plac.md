---
id: "44013152798743"
titulo: "[TMS] - Erro de integração \"Embarque sem placa informada\" ao integrar o embarque do TMS ao Tracking"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013152798743--TMS-Erro-de-integra%C3%A7%C3%A3o-Embarque-sem-placa-informada-ao-integrar-o-embarque-do-TMS-ao-Tracking"
trilha: "Lincros > TMS > Envios de integração - TMS"
atualizado_em: "2026-10-05T19:49:38Z"
rotulos: ["sync_hc", "lincros", "lincros_13432891", "sync_hash_13202ba3ec26"]
---

# [TMS] - Erro de integração "Embarque sem placa informada" ao integrar o embarque do TMS ao Tracking

## Resumo do Artigo:

Este artigo orienta sobre a resolução do erro “Embarque sem Placa informada” ao integrar um embarque do TMS com o sistema Tracking via NiFi. A solução envolve validar e informar corretamente a placa do veículo no Pré-Conhecimento, pois o sistema considera essa informação para realizar a integração do embarque ao Tracking.

## 1 - Problema Relatado pelo Cliente:

O cliente reportou falha na integração de Embarques do sistema TMS com o sistema Tracking via NiFi. A mensagem de erro exibida durante o processo de integração foi: "Embarque sem Placa informada"

O erro ocorreu mesmo com a placa informada no embarque, sugerindo que o sistema não reconhecia essa informação durante o processo de integração.

## 2 - Passo a Passo para Resolver o Problema:

Para resolver o erro de integração do embarque do TMS com o sistema Tracking, com a mensagem “Embarque sem Placa informada”, siga os passos abaixo:

## a. Acesse o registro do Embarque no sistema TMS.

   - Na tela Operacional > Cargas > Embarques > acesse o embarque em questão e acesse o Pré-Conhecimento vinculado ao Embarque.

## b. Verifique a presença da placa no Pré-Conhecimento.

   - Confirme se o campo de 'Placa' está preenchido.

## c. Caso a placa não esteja informada no Pré-Conhecimento:

   - Edite o Pré-Conhecimento e insira a placa do veículo.

## d. Salve as alterações no Pré-Conhecimento.

## e. Aguardar o próximo ciclo de integração do NiFi para buscar novamente este embarque.

## f. Valide o sucesso da integração.

   - Confirme que a integração foi concluída sem erros pela mensagem de integração tracking localizada na aba "cadastro" do registro do embarque. Se a mensagem dizer "integrado com sucesso", significa que o embarque foi criado no sistema Tracking.

**Observação importante:** para a integração do embarque do TMS ao Tracking via NiFi, o TMS realiza a validação da placa com base nas informações do 'Pré-Conhecimento' vinculado ao embarque, e não somente a placa informada diretamente no registro de Embarque. Por isso, é essencial que a placa também esteja corretamente preenchida em todos os Pré-Conhecimentos vinculados ao embarque.
