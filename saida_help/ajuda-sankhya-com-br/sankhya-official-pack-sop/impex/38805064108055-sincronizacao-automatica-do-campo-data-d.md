---
id: "38805064108055"
titulo: "Sincronização Automática do campo ''Data de Previsão''"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38805064108055-Sincroniza%C3%A7%C3%A3o-Autom%C3%A1tica-do-campo-Data-de-Previs%C3%A3o"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:01:12Z"
rotulos: ["Configuração", "Atualização", "Importação", "Follow Up", "Pedido de Importação"]
---

# Sincronização Automática do campo ''Data de Previsão''

#### 1. Objetivo

O objetivo da rotina é garantir que o campo **''Data de Previsão''** de entrega permaneça automaticamente sincronizado entre o ''**Pedido de Importação''** e a tela ''**Follow Up''**, assegurando a integridade das informações, evitando divergências operacionais e eliminando retrabalho manual.

###

#### 2. Funcionamento da Sincronização

A sincronização do campo ''Data de Previsão'' ocorre automaticamente após o salvamento da informação no ''Pedido de Importação'' ou no ''Follow Up'', desde que exista vínculo entre os registros. Ao informar e salvar a ''Data de Previsão'' no ''Pedido de Importação'', o sistema **replica automaticamente a informação no** ''Follow Up'' confirmando o status do pedido.

Da mesma forma, ao **alterar e salvar a** ''Data de Previsão'' no ''Follow Up'', **o sistema atualiza automaticamente o Pedido de Importação**.

A **última data salva será considerada válida em ambas as telas**, não sendo permitida divergência entre os registros.

**Para validar o funcionamento**:

1. Informe a Data de Previsão no Pedido e salve;
2. Verifique a replicação no Follow Up;
3. Altere a data no Follow Up e salve;
4. Confirme a atualização automática no Pedido.

#### 3. Regras e Validações

- ##### A atualização ocorre imediatamente após salvar;
- ##### O sistema respeita permissões e regras de edição do usuário;
- Caso o pedido não possa ser atualizado, o sistema apresentará uma mensagem de erro, como **"Pedido já faturado"**.

#### 4. Benefícios da Rotina

- ##### Elimina retrabalho manual;
- ##### Evita divergência de informações;
- ##### Garante maior confiabilidade nos prazos;
- ##### Melhora o controle operacional.
