---
id: "43675279663127"
titulo: "Erro 536 no envio do evento S-2205 do eSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675279663127-Erro-536-no-envio-do-evento-S-2205-do-eSocial"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-02T17:28:44Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro 536 no envio do evento S-2205 do eSocial

**Mensagem**

536 - Informações de Empregador, trabalhador e/ou período de apuração incompatíveis.

**Situação**

O erro **536** ao enviar o evento **S-2205** (Alteração de Dados Cadastrais) ao eSocial indica que há **incompatibilidade entre as informações do empregador, trabalhador e/ou período de apuração**. Isso significa que o eSocial identificou inconsistências nos dados que estão sendo transmitidos em relação ao que já consta na base de dados do governo.

**Solução**

**(1)**Acesse a tela Pessoal+ » Rotinas Folha » Central do eSocial >**Consulta recibos por funcionários"**  e filtre pelo colaborador e referência do evento.

![Imagem 1: Verifique se existe algum evento "S-2205" ou "S-2206" com data posterior à rescisão ou com informações divergentes do…](https://ajuda.sankhya.com.br/hc/article_attachments/43824398528919)

**(2)**Verifique se existe algum evento **"S-2205"** ou **"S-2206"** com data posterior à rescisão ou com informações divergentes do cadastro original do colaborador.

**(3)**Caso existam eventos inconsistentes, clique com o botão direito sobre o evento e selecione **"Gerar evento como exclusão"** para excluir o evento indevido.

**(4)**Acesse o cadastro do empregado, na aba **"Registro de envio para o eSocial"**Configurações » Cadastros » Pessoal » Configuração Funcionários, clique com o botão direito e selecione **"Preencher data de alteração do S-2205 ou S-2206"**, informando uma data anterior à rescisão, se aplicável.

⚠️ **Importante**: O eSocial exige uma hierarquia cronológica rigorosa. Você não pode enviar um S-2205 com data anterior a eventos já transmitidos.

**(5)**Gere novamente os eventos na **"Central do eSocial"**   Pessoal+ » Rotinas Folha » Central do eSocial e realize o envio do **"S-2205"** com as informações corrigidas.

**(6)**Valide se o evento foi recepcionado com sucesso no portal do eSocial.

**Observação:** Caso o erro persista, revise se as datas de alteração, admissão e rescisão estão corretas e se não há divergências entre os dados enviados e os já registrados no eSocial.

**Causa**

O erro 536 ocorre quando há incompatibilidade entre as informações do empregador, trabalhador ou período de apuração informados no evento S-2205 e os dados já existentes no ambiente do eSocial. Isso pode ser causado por:

- Envio de evento com datas divergentes das já registradas (exemplo: alteração com data posterior à rescisão).
- Alteração de dados cadastrais sem correspondência com o histórico do colaborador no eSocial.
- Existência de eventos duplicados ou em duplicidade para o mesmo período e colaborador.

  ## Checklist de validação

  Antes de reenviar o S-2205, confirme:

  ✅ CPF do funcionário está correto
  ✅ Matrícula corresponde ao vínculo no eSocial
  ✅ Data de alteração é posterior ao último evento enviado
  ✅ Não há eventos duplicados ou rejeitados pendentes
  ✅ CNPJ do empregador está correto
  ✅ Período de apuração está dentro da obrigatoriedade do eSocial
  ✅ Dados cadastrais estão completos e consistentes
