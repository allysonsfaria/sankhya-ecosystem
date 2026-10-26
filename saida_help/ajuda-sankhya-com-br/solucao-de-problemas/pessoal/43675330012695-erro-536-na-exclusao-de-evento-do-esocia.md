---
id: "43675330012695"
titulo: "Erro 536 na exclusão de evento do eSocial S-2200"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675330012695-Erro-536-na-exclus%C3%A3o-de-evento-do-eSocial-S-2200"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-02T17:27:51Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro 536 na exclusão de evento do eSocial S-2200

**Mensagem**

[536] Informações do empregador, trabalhador e/ou período de apuração incompatíveis.

**Situação**

 O **erro 536** ao tentar **excluir** um evento **S-2200** (Admissão) indica que há **incompatibilidade de informações** ou **eventos dependentes** que impedem a exclusão. Embora o erro 536 seja mais comum no envio de eventos, quando ocorre na exclusão significa que existem outros eventos trabalhistas vinculados ao mesmo contrato que precisam ser removidos primeiro.

> ⚠️ **Importante**: O eSocial exige que a exclusão de eventos siga uma **ordem cronológica inversa** (do mais recente para o mais antigo) para manter a integridade dos dados trabalhistas.

Antes de excluir o S-2200, você precisa verificar quais eventos estão vinculados ao colaborador:

1. Acesse o **portal do eSocial** (gov.br) com certificado digital
2. Consulte o **CPF do colaborador**
3. Verifique todos os eventos enviados para este vínculo
4. Anote os eventos que possuem data **posterior** à admissão

**Solução**

**(1)** Acesse a tela  **Pessoal+ » Rotinas Folha » Central do eSocial** Clique no ícone de **Recibo** (histórico de eventos)

      Identifique todos os eventos posteriores ao S-2200

**Ordem de exclusão recomendada:**

1. **S-2299** (Desligamento) - se houver
2. **S-2230** (Afastamentos) - se houver
3. **S-2220** (ASO/Exames) - se houver
4. **S-2240** (Condições Ambientais) - se houver
5. **S-2206** (Alteração Contratual) - se houver
6. **S-2205** (Alteração Cadastral) - se houver
7. **S-2200** (Admissão) - por último

   **(2)** Caso tenha alterado a data de admissão após o envio do S-2200, ajuste a data para o valor anterior, correspondente ao evento original enviado ao eSocial.

   Antes de tentar excluir o S-2200 novamente, confirme:

   **No cadastro do funcionário:**

   **CPF** está correto e corresponde ao enviado no S-2200

   **Matrícula** está correta

   **Data de Admissão** corresponde ao evento enviado

   **No portal do eSocial:**

   Todos os eventos dependentes foram excluídos com sucesso

   Não há eventos pendentes de processamento

   O vínculo está ativo e corresponde aos dados do sistema

   **(3)** Após ajustar a data, gere novamente o evento de exclusão S-2200 na tela **"Central do eSocial"** (eSocial Central do eSocial).

   **(4)** Envie o evento de exclusão S-2200. O envio será processado corretamente se as informações estiverem compatíveis com o evento original.

**Dica:** Sempre confira se não existem outros eventos trabalhistas enviados para o mesmo vínculo ou contrato (como S-2220, S-2205, S-2206, etc.), pois eles podem impedir a exclusão do S-2200. Caso existam, exclua-os antes de tentar excluir o S-2200.

Antes de tentar excluir o S-2200, confirme:

✅ Todos os eventos posteriores foram excluídos (S-2205, S-2206, S-2220, S-2230, etc.)
✅ A exclusão foi feita na ordem inversa (do mais recente para o mais antigo)
✅ CPF e matrícula do funcionário estão corretos
✅ Não há eventos pendentes de processamento no portal do eSocial
✅ Os dados do sistema correspondem aos dados enviados no S-2200 original
✅ Não há duplicidade de eventos no portal do eSocial

---

## Atenção importante

🚫 **Nunca exclua eventos manualmente no portal do eSocial**

Realizar exclusões diretamente no portal do governo causa **inconsistências** entre o sistema Sankhya e a base do eSocial, impedindo a sincronização correta das informações. Sempre utilize a **Central do eSocial** no sistema para gerar e enviar os eventos de exclusão.

**Causa**

O erro 536 ocorre porque as informações do evento de exclusão S-2200 (como data de admissão, CPF, matrícula, etc.) não coincidem exatamente com as informações do evento original de inclusão S-2200 já enviado ao eSocial. Isso geralmente acontece após alterações cadastrais no sistema, especialmente na data de admissão, ou quando há eventos posteriores enviados para o mesmo vínculo, tornando as informações incompatíveis para a exclusão.
