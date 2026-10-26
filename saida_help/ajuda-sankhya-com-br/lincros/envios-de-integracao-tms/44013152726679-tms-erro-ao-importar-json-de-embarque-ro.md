---
id: "44013152726679"
titulo: "[TMS] - Erro ao importar JSON de Embarque (Romaneio) no TMS - transportadora do redespacho igual à do pré-conhecimento normal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013152726679--TMS-Erro-ao-importar-JSON-de-Embarque-Romaneio-no-TMS-transportadora-do-redespacho-igual-%C3%A0-do-pr%C3%A9-conhecimento-normal"
trilha: "Lincros > TMS > Envios de integração - TMS"
atualizado_em: "2026-10-05T19:49:37Z"
rotulos: ["sync_hc", "lincros", "lincros_13432895", "sync_hash_427993496f54"]
---

# [TMS] - Erro ao importar JSON de Embarque (Romaneio) no TMS - transportadora do redespacho igual à do pré-conhecimento normal

## 1 - Problema relatado pelo cliente

Cliente acionou relatando sobre um erro da integração/importação de um arquivo JSON de embarque (romaneio) no TMS. O erro diz: "Conhecimento de redespacho número 109XXX do conhecimento número 109XXX possui a mesma transportadora". Esse erro ocorre na importação do JSON de Embarque quando a transportadora do pré-conhecimento de redespacho é a mesma do pré-conhecimento normal. A solução exige a alteração/correção das transportadoras nos pré-conhecimentos envolvidos, garantindo que cada trecho do transporte (normal e redespacho) utilize transportadoras diferentes.

## 2 - Passo a Passo para Resolver o Problema

Para solucionar o erro apresentado na importação do arquivo JSON de Embarque/Romaneio, siga os passos abaixo:

## a. Identifique os conhecimentos envolvidos:

- A mensagem de erro de integração/importação vai informar o número do pré-conhecimento de redespacho e o número do pré-conhecimento normal.
- Na tela de pré-conhecimentos, em Operacional> Cargas> Pré-conhecimentos, pesquise por eles

## b. Verifique as transportadoras atribuídas:

- Na aba "transporte", confirme se a transportadora vinculada no conhecimento de redespacho é diferente da transportadora do conhecimento do tipo normal.
- A regra de negócio desse processo é validar se a transportadora do pré-conhecimento do tipo redespacho é diferente da transportadora do pré-conhecimento do tipo normal, pois o correto é serem diferentes.

## c. Corrija as transportadoras, se necessário:

- Caso ambos pré-conhecimentos estejam utilizando a mesma transportadora, será necessário alterar uma delas.
- Valide qual transportadora será responsável pela entrega em cada etapa:

- Pré-conhecimento Normal (primeiro trecho/perna do transporte): transportadora responsável pela coleta ou transporte inicial.
- Pré-conhecimento Redespacho (segundo trecho/perna do transporte ou trecho final):transportadora que concluirá a entrega ao destino final.

## d. Atualize os Conhecimentos:

- Após identificar corretamente as transportadoras envolvidas, faça as alterações das transportadoras na aba "transporte" dos respectivos pré-conhecimentos.
- Salve as alterações realizadas.

## e. Refaça a importação do arquivo JSON do Embarque/Romaneio:

- Reenvie o arquivo JSON do Embarque ao TMS
- Com as transportadoras corretas em cada pré-conhecimento, sem serem as mesmas , o processo deve ser concluído com sucesso e o embarque deve ser criado no TMS de acordo com o JSON enviado.
