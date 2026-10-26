---
id: "44013486828823"
titulo: "[TMS] - Considerar a Data de Coleta a mesma que a Data de Emissão do CT-e para Cálculo de Previsão de Entrega"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013486828823--TMS-Considerar-a-Data-de-Coleta-a-mesma-que-a-Data-de-Emiss%C3%A3o-do-CT-e-para-C%C3%A1lculo-de-Previs%C3%A3o-de-Entrega"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:59:17Z"
rotulos: ["sync_hc", "lincros", "lincros_13432366", "sync_hash_4427213b75e2"]
---

# [TMS] - Considerar a Data de Coleta a mesma que a Data de Emissão do CT-e para Cálculo de Previsão de Entrega

## 1. Problema Relatado pelo Cliente

O cliente necessita que a **data de coleta** considerada no sistema seja a mesma **data de emissão do CT-e**, desconsiderando outras datas como emissão da NF-e, data de embarque ou data de envio da ordem de coleta.

Esse tipo de configuração é feito por meio de **parâmetros da empresa**, sendo que apenas **analistas de Suporte da Lincros** possuem permissão para realizar esse ajuste no sistema.
Este artigo orienta o cliente sobre quais parâmetros devem ser solicitados ao time de Suporte da Lincros para que o sistema passe a considerar a data de emissão do CT-e como data de coleta, para cálculo da previsão de entrega da transportadora.

---

## 2. Passo a Passo para Resolver o Problema

## Verificar o Parâmetro Atual da Empresa

Acesse o caminho:
**Menu: Cadastros Gerais > Configurações da Empresa > Parâmetros > Empresa**

Na tela de parâmetros, é possível consultar quais configurações estão atualmente aplicadas à empresa em relação à previsão de entrega.

## Solicitar Ajuste ao Time de Suporte

Caso o sistema esteja considerando a data de emissão da NF-e como base para a previsão de entrega, e o embarcador deseje alterar para a **data de emissão do CT-e**, será necessário abrir um chamado para o time de Suporte da Lincros.

No chamado, deve-se solicitar a ativação dos seguintes parâmetros no caminho acima:

- `considerarDataCtePrevisaoEntrega = true`
- `codigoOcorrenciaConfirmacaoColeta` com o código adequado da confirmação de coleta (geralmente é utilizado o código **00**)

## Finalização da Configuração

Após a alteração dos parâmetros e o salvamento das configurações, o sistema irá aplicar a nova lógica de previsão de entrega, considerando a data de emissão do CT-e como **data de coleta**.

---

## 3. Considerações Importantes

- A **previsão de entrega** no sistema pode considerar diferentes datas como ponto de partida: emissão da NF-e, emissão do CT-e, envio da ordem de coleta, entre outras.
- Esse comportamento é controlado por **parâmetros de empresa** e deve ser ajustado com cautela.
- Apenas **usuários Lincros** possuem permissão para realizar alterações nesses parâmetros.
- O ajuste evita divergências nos prazos previstos e garante consistência nas operações logísticas.

Este artigo visa facilitar a compreensão do processo para configurar o ponto de partida para o campo de data de coleta com base na data de emissão do ct-e.
