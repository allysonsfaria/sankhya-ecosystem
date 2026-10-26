---
id: "43546328357911"
titulo: "Erro PES_E01764 - Não é possível salvar, houve mudança na data de nascimento e já existe um S-2200/S-2300 enviado com sucesso para este colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546328357911-Erro-PES-E01764-N%C3%A3o-%C3%A9-poss%C3%ADvel-salvar-houve-mudan%C3%A7a-na-data-de-nascimento-e-j%C3%A1-existe-um-S-2200-S-2300-enviado-com-sucesso-para-este-colaborador"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-18T11:31:50Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro PES_E01764 - Não é possível salvar, houve mudança na data de nascimento e já existe um S-2200/S-2300 enviado com sucesso para este colaborador

**MENSAGEM**

[PES\_E01764] Não é possível salvar, houve mudança na data de nascimento e já existe um S-2200/S-2300 enviado com sucesso para este colaborador.

**SITUAÇÃO**

A mensagem é apresentada ao tentar alterar a **"Data de Nascimento"** de um colaborador que já possui um evento de admissão (**"S-2200"**) ou de trabalhador sem vínculo (**"S-2300"**) enviado com sucesso ao eSocial. O sistema impede a alteração direta desse dado cadastral após o envio do evento inicial ao governo.

Esse erro ocorre quando você tenta alterar a data de nascimento de um colaborador cujo evento de admissão (S-2200) ou de trabalhador sem vínculo (S-2300) já foi enviado e aceito pelo eSocial. O sistema bloqueia essa alteração para garantir a integridade dos dados, pois a data de nascimento é um dado cadastral fundamental e já foi registrada oficialmente junto ao Governo.

O eSocial não permite que dados-chave do trabalhador (como data de nascimento) sejam alterados diretamente após o envio do evento de admissão. Para corrigir esse tipo de informação, é necessário seguir um procedimento específico de exclusão e reenvio dos eventos.

1. **Verifique se realmente é necessário alterar a data de nascimento**
   - Confirme se a alteração é de fato obrigatória (por exemplo, erro de digitação ou atualização de documento).

**SOLUÇÃO**

**(1)** Acesse a tela de **"Eventos Pendentes"** (Pessoal+ eSocial Eventos Pendentes) e verifique se há eventos posteriores ao **"S-2200"**/**"S-2300"** enviados para o colaborador, como **"S-2205"**, **"S-2206"**, **"S-2220"**, **"S-2230"**, entre outros.

Caso existam outros eventos posteriores, exclua-os primeiro, sempre na ordem do mais recente para o mais antigo.

Eventos periódicos (S-1200, S-1210) não impedem a exclusão, mas se houver folha calculada, pode ser necessário reabrir a competência

**(2)** Exclua todos os eventos posteriores ao **"S-2200"**/**"S-2300"** para o colaborador em questão, sempre iniciando pelo evento mais recente e seguindo a ordem inversa de envio.

**(3)** Após excluir os eventos posteriores, exclua o evento **"S-2200"**/**"S-2300"** do colaborador.

**(4)** Com o evento excluído, retorne ao cadastro do colaborador e realize a alteração da **"Data de Nascimento"**.

**(5)** Após ajustar a data, gere novamente o **"S-2200"**/**"S-2300"** e realize o envio ao eSocial.

**(6)** Por fim, recadastre e envie novamente os eventos posteriores (**"S-2205"**, **"S-2206"**, etc.) conforme a necessidade do histórico do colaborador.

**Reenvie os demais eventos necessários**

- Caso tenha excluído outros eventos (alterações cadastrais, afastamentos, etc.), gere e envie novamente cada um deles, respeitando a ordem cronológica dos fatos.

**Pontos de atenção**

- Não é permitido alterar a data de nascimento diretamente após o envio do S-2200/S-2300.
- Sempre exclua os eventos na ordem inversa (do mais recente para o mais antigo).
- Após corrigir o dado, reenvie todos os eventos necessários para manter o histórico do colaborador atualizado no eSocial.
- Se houver folha calculada para o colaborador, pode ser necessário reabrir a competência para permitir a exclusão dos eventos.

**CAUSA**

A causa do erro é que, após o envio do evento **"S-2200"**/**"S-2300"** ao eSocial, a **"Data de Nascimento"** do colaborador passa a ser uma informação chave para o vínculo trabalhista. Qualquer alteração neste dado exige que o evento de admissão seja excluído e reenviado, pois o eSocial não permite a retificação direta desse campo após o envio inicial. O sistema bloqueia a alteração para garantir a integridade das informações transmitidas ao governo.
